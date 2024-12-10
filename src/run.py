#!/usr/bin/env python
import os
import numpy as np
import pandas as pd
from strategy.z_score import ZScore
from strategy.moving_average import MovingAverage
from strategy.rsi import RSI
from strategy.roc import ROC
from strategy.percentile import Percentile
from strategy.min_max import MinMax
from strategy.robust import Robust
from strategy.divergence import Divergence
from strategy.LogTransform import LogTransform
from strategy.ModifiedZscore import ModifiedZScore
from strategy.DecimalScaling import DecimalScaling
from optimization import Optimization
import requests
import time
from tqdm import tqdm
import multiprocessing
import warnings
import logging
from concurrent.futures import ProcessPoolExecutor, as_completed
import psutil
import resource
import gc
from memory_profiler import profile
from config import GLASSNODE_API_KEY

# Suppress warnings and configure logging
warnings.filterwarnings('ignore', category=pd.errors.SettingWithCopyWarning)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configure pandas display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# User Configuration
COMMISSION = 0.0005
ASSET = 'ETH'
INTERVAL = '1h'
WINDOW_SIZE_PERCENT = 0.10
NUM_WINDOW_SIZES = 40
FACTOR_DIRECTORY = '/Users/stephenlyk/Desktop/Gnproject/src/fetch_data/glassnode_data_Dec2024_single'
SHIFT = 2

# Resource Management Configuration
MAX_MEMORY_PERCENT = 85
MAX_CPU_PERCENT = 95
BATCH_SIZE = 100
CHUNK_SIZE = 50
COOL_DOWN_PERIOD = 60
ERROR_COOL_DOWN = 30

# Strategy Configuration
strategy_classes = {
    'MovingAverage': MovingAverage,
    'ZScore': ZScore,
    'RSI': RSI,
    'ROC': ROC,
    'Percentile': Percentile,
    'MinMax': MinMax,
    'Robust': Robust,
    'Divergence': Divergence,
    'LogTransform': LogTransform,
    'ModifiedZScore': ModifiedZScore,
    'DecimalScaling': DecimalScaling,
}


def set_process_limits():
    """Set process resource limits"""
    try:
        total_ram = psutil.virtual_memory().total
        memory_limit = int(total_ram * 0.75)
        resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit))
        logger.info(f"Process memory limit set to {memory_limit / (1024 ** 3):.2f} GB")
    except Exception as e:
        logger.warning(f"Failed to set process limits: {str(e)}")


def monitor_process():
    """Monitor current process resource usage"""
    process = psutil.Process()
    return {
        'cpu_percent': process.cpu_percent(),
        'memory_percent': process.memory_percent(),
        'memory_info': process.memory_info()
    }


def timeit(func):
    """Decorator to measure function execution time"""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Function {func.__name__} took {end_time - start_time:.2f} seconds")
        return result

    return wrapper


def fetch_glassnode_data(asset, interval, api_key):
    """Fetch price data from Glassnode API"""
    url = f"https://api.glassnode.com/v1/metrics/market/price_usd_close"
    params = {
        'a': asset,
        'i': interval,
        'api_key': api_key
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            df.columns = ['Date', 'Price']
            df['Date'] = pd.to_datetime(df['Date'], unit='s')
            df['Price'] = df['Price'].astype('float32')  # Memory optimization
            return df
        else:
            raise Exception(f"API request failed: {response.status_code}")
    except Exception as e:
        logger.error(f"Failed to fetch Glassnode data: {str(e)}")
        raise


def read_glassnode_csv(file_path):
    """Read and preprocess Glassnode CSV data"""
    try:
        df = pd.read_csv(file_path)
        df.columns = ['Date', 'Value']
        df['Date'] = pd.to_datetime(df['Date'])
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce').astype('float32')
        df['Value'] = df['Value'].shift(SHIFT)
        return df.dropna()
    except Exception as e:
        logger.error(f"Error reading CSV {file_path}: {str(e)}")
        raise


def calculate_window_sizes(data_length):
    """Calculate window sizes for strategy optimization"""
    max_window = int(data_length * WINDOW_SIZE_PERCENT)
    min_window = 2
    return np.linspace(min_window, max_window, NUM_WINDOW_SIZES, dtype=int)


def split_data(df, train_ratio=0.7):
    """Split data into training and testing sets"""
    train_size = int(len(df) * train_ratio)
    return df.iloc[:train_size], df.iloc[train_size:]


def process_data_chunk(chunk_files, asset_price_df, batch_start):
    """Process a chunk of data files"""
    price_factor_dict = {}
    for filename in tqdm(chunk_files, desc=f"Processing batch {batch_start}"):
        try:
            file_path = os.path.join(FACTOR_DIRECTORY, filename)
            df = read_glassnode_csv(file_path)

            merged_df = pd.merge(
                asset_price_df[['Date', 'Price']],
                df[['Date', 'Value']],
                how='inner',
                on='Date'
            ).sort_values('Date')

            if not merged_df.empty:
                price_factor_dict[filename] = merged_df

            # Resource monitoring
            if len(price_factor_dict) % 10 == 0:
                stats = monitor_process()
                if stats['memory_percent'] > MAX_MEMORY_PERCENT:
                    logger.warning("High memory usage detected, cleaning up...")
                    gc.collect()

        except Exception as e:
            logger.error(f"Error processing {filename}: {str(e)}")
            continue

    return price_factor_dict


def running_single_strategy(run_params):
    """Execute a single strategy optimization"""
    try:
        filename = run_params['Metric']
        price_factor_df = run_params['price_factor_dict'][filename].copy()
        price_factor_df = price_factor_df.rename(columns={'Value': run_params['Metric']})

        if price_factor_df.empty:
            return None

        train_df, test_df = split_data(price_factor_df)
        if train_df.empty or test_df.empty:
            return None

        window_size_list = calculate_window_sizes(len(train_df))
        StrategyClass = strategy_classes[run_params['Strategy']]

        try:
            train_optimization = Optimization(
                StrategyClass, train_df, test_df, window_size_list,
                run_params['threshold_params'],
                target=run_params['Metric'],
                price='Price',
                long_short=run_params['Strategy Type'],
                condition=run_params['Condition']
            )

            train_optimization.run()
            best_strategy = train_optimization.get_best()

            test_strategy = StrategyClass(
                test_df,
                best_strategy.window_size,
                best_strategy.threshold,
                target=run_params['Metric'],
                price='Price',
                long_short=run_params['Strategy Type'],
                condition=run_params['Condition']
            )

            return {
                'Metric': run_params['Metric'],
                'Strategy': run_params['Strategy'],
                'Strategy Type': run_params['Strategy Type'],
                'Condition': run_params['Condition'],
                'Train Sharpe': best_strategy.sharpe,
                'Test Sharpe': test_strategy.sharpe,
                'Best Window': best_strategy.window_size,
                'Best Threshold': best_strategy.threshold
            }

        except Exception as e:
            logger.error(f"Strategy execution error: {str(e)}")
            return None

    except Exception as e:
        logger.error(f"Error in running_single_strategy: {str(e)}")
        return None


def process_single_strategy(params):
    """Process a single strategy with proper error handling"""
    try:
        filename = params['Metric']
        price_factor_df = params['price_factor_dict'][filename].copy()
        price_factor_df = price_factor_df.rename(columns={'Value': params['Metric']})

        if price_factor_df.empty:
            return None

        train_df, test_df = split_data(price_factor_df)
        if train_df.empty or test_df.empty:
            return None

        window_size_list = calculate_window_sizes(len(train_df))
        StrategyClass = strategy_classes[params['Strategy']]
        threshold_list = params['threshold_params']

        best_result = None
        best_sharpe = float('-inf')

        for window_size in window_size_list:
            for threshold in threshold_list:
                try:
                    train_strategy = StrategyClass(
                        train_df, window_size, threshold,
                        target=params['Metric'],
                        price='Price',
                        long_short=params['Strategy Type'],
                        condition=params['Condition']
                    )

                    if train_strategy.sharpe > best_sharpe:
                        best_sharpe = train_strategy.sharpe
                        best_result = {
                            'Metric': params['Metric'],
                            'Strategy': params['Strategy'],
                            'Strategy Type': params['Strategy Type'],
                            'Condition': params['Condition'],
                            'Best Window': window_size,  # Changed from 'Window'
                            'Best Threshold': threshold,  # Changed from 'Threshold'
                            'Train Sharpe': train_strategy.sharpe,
                            'Test Sharpe': None
                        }
                except Exception as e:
                    continue

        if best_result:
            # Calculate test performance for best parameters
            test_strategy = StrategyClass(
                test_df,
                best_result['Best Window'],  # Changed from 'Window'
                best_result['Best Threshold'],  # Changed from 'Threshold'
                target=params['Metric'],
                price='Price',
                long_short=params['Strategy Type'],
                condition=params['Condition']
            )
            best_result['Test Sharpe'] = test_strategy.sharpe

        return best_result

    except Exception as e:
        logger.error(f"Error in process_single_strategy: {str(e)}")
        return None


def run_parallel_optimization(strategy_combinations, num_workers=None):
    """Run optimization in parallel with better error handling"""
    if num_workers is None:
        num_workers = max(1, multiprocessing.cpu_count() - 2)

    chunk_size = max(1, len(strategy_combinations) // (num_workers * 4))
    results = []

    with multiprocessing.Pool(num_workers) as pool:
        try:
            with tqdm(total=len(strategy_combinations), desc="Processing strategies") as pbar:
                for result in pool.imap_unordered(process_single_strategy,
                                                  strategy_combinations,
                                                  chunksize=chunk_size):
                    if result:
                        results.append(result)
                    pbar.update(1)

        except Exception as e:
            logger.error(f"Error in parallel processing: {str(e)}")
            pool.terminate()
        finally:
            pool.close()
            pool.join()

    return results


def calculate_calmar_ratio(annual_return, mdd):
    """Safely calculate Calmar ratio"""
    try:
        if abs(mdd) < 1e-10:  # Effectively zero
            return float('inf') if annual_return > 0 else float('-inf') if annual_return < 0 else 0.0
        return annual_return / abs(mdd)
    except Exception:
        return 0.0


@timeit
def run_optimization(batch_size=BATCH_SIZE, start_index=0):
    """Main optimization function"""
    try:
        asset_price_df = fetch_glassnode_data(ASSET, INTERVAL, GLASSNODE_API_KEY)
        all_files = [f for f in os.listdir(FACTOR_DIRECTORY) if f.endswith('.csv')]
        batch_end = min(start_index + batch_size, len(all_files))
        current_batch_files = all_files[start_index:batch_end]

        logger.info(f"Processing files {start_index} to {batch_end} of {len(all_files)}")

        # Process data
        price_factor_dict = {}
        for filename in tqdm(current_batch_files, desc="Reading data files"):
            try:
                file_path = os.path.join(FACTOR_DIRECTORY, filename)
                df = read_glassnode_csv(file_path)
                merged_df = pd.merge(
                    asset_price_df[['Date', 'Price']],
                    df[['Date', 'Value']],
                    how='inner',
                    on='Date'
                )
                if not merged_df.empty:
                    price_factor_dict[filename] = merged_df
            except Exception as e:
                logger.error(f"Error processing {filename}: {str(e)}")

        # Define parameter ranges
        threshold_params = {
            'ZScore': np.round(np.linspace(-3, 3, 20), 3),
            'MovingAverage': np.round(np.linspace(-0.1, 0.1, 20), 3),
            'RSI': np.round(np.linspace(0.2, 0.8, 10), 3),
            'ROC': np.round(np.linspace(-0.1, 0.1, 20), 3),
            'MinMax': np.round(np.linspace(0.1, 0.9, 20), 3),
            'Robust': np.round(np.linspace(0, 2, 20), 3),
            'Percentile': np.round(np.linspace(0.1, 0.9, 20), 3),
            'Divergence': np.round(np.linspace(-3, 3, 20), 3),
            'LogTransform': np.round(np.linspace(-3, 3, 20), 3),
            'ModifiedZScore': np.round(np.linspace(-3, 3, 20), 3),
            'DecimalScaling': np.round(np.linspace(0.1, 0.9, 20), 3),
            'AdaptiveNorm': np.round(np.linspace(-3, 3, 20), 3),
            'MomentumNorm': np.round(np.linspace(-3, 3, 20), 3),
            'RangeVolNorm': np.round(np.linspace(-3, 3, 20), 3),
            'EntropyNorm': np.round(np.linspace(-3, 3, 20), 3),
        }

        # Generate strategy combinations
        strategy_combinations = []
        for filename in price_factor_dict:
            for strategy in strategy_classes:
                # for long_short in ['long', 'short', 'both']:
                for long_short in ['both']:
                    for condition in ['lower', 'higher']:
                        strategy_combinations.append({
                            'Metric': filename,
                            'Strategy': strategy,
                            'Strategy Type': long_short,
                            'Condition': condition,
                            'price_factor_dict': price_factor_dict,
                            'threshold_params': threshold_params[strategy]
                        })

        # Run parallel optimization
        results = run_parallel_optimization(strategy_combinations)

        # Save results to CSV
        if results:
            df = pd.DataFrame(results)
            df.to_csv(f"{ASSET.lower()}_factor_test_batch_{start_index}.csv", index=False)

        return results, batch_end < len(all_files), batch_end

    except Exception as e:
        logger.error(f"Error in run_optimization: {str(e)}")
        return [], False, start_index


if __name__ == "__main__":
    try:
        batch_size = BATCH_SIZE
        current_index = 0
        has_more = True
        all_results = []

        while has_more:
            logger.info(f"Starting batch at index {current_index}")

            results_list, has_more, next_index = run_optimization(
                batch_size=batch_size,
                start_index=current_index
            )

            if results_list:
                all_results.extend(results_list)
                pd.DataFrame(all_results).to_csv(
                    f"{ASSET.lower()}_factor_test_final.csv",
                    index=False
                )
                logger.info(f'Batch {current_index} completed and saved')

            current_index = next_index
            gc.collect()
            time.sleep(5)

    except Exception as e:
        logger.error(f"An error occurred during optimization: {str(e)}")

    logger.info('Run completed')