#!/usr/bin/env python
import os
import numpy as np
import pandas as pd
from src.strategy.divergence import Divergence
from optimization import Optimization
import requests
import time
from tqdm import tqdm
import multiprocessing
import warnings
import logging
from joblib import Parallel, delayed
from config import GLASSNODE_API_KEY

warnings.filterwarnings('ignore', category=pd.errors.SettingWithCopyWarning)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# User Input Section
COMMISSION = 0.0007
GLASSNODE_API_KEY = GLASSNODE_API_KEY
ASSET = 'BTC'
INTERVAL = '1h'
WINDOW_SIZE_PERCENT = 0.10
NUM_WINDOW_SIZES = 40

FACTOR_DIRECTORY = '/Users/stephenlyk/Desktop/Gnproject/src/fetch_data/glassnode_data_btc_1hSept2024'

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Function {func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result
    return wrapper

def fetch_glassnode_data(asset, interval, api_key):
    url = f"https://api.glassnode.com/v1/metrics/market/price_usd_close"
    params = {
        'a': asset,
        'i': interval,
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.columns = ['Date', 'Price']
        df['Date'] = pd.to_datetime(df['Date'], unit='s')
        return df
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def read_glassnode_csv(file_path):
    df = pd.read_csv(file_path)
    df.columns = ['Date', 'Value']
    df['Date'] = pd.to_datetime(df['Date'])
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    df['Value'] = df['Value'].shift(2)  # Add this line to shift the data
    df = df.dropna()
    return df

def calculate_window_sizes(data_length):
    max_window = int(data_length * WINDOW_SIZE_PERCENT)
    min_window = 2
    return np.linspace(min_window, max_window, NUM_WINDOW_SIZES, dtype=int)

def split_data(df, train_ratio=0.7):
    train_size = int(len(df) * train_ratio)
    train_df = df.iloc[:train_size]
    test_df = df.iloc[train_size:]
    return train_df, test_df

@timeit
def run_optimization():
    asset_price_df = fetch_glassnode_data(ASSET, INTERVAL, GLASSNODE_API_KEY)

    price_factor_dict = {}
    for filename in tqdm(os.listdir(FACTOR_DIRECTORY), desc="Reading CSV files"):
        if filename.endswith('.csv'):
            file_path = os.path.join(FACTOR_DIRECTORY, filename)
            df = read_glassnode_csv(file_path)
            merged_df = pd.merge(asset_price_df, df, how='inner', on='Date')
            merged_df = merged_df.sort_values('Date')
            merged_df = merged_df.ffill()
            if not merged_df.empty:
                price_factor_dict[filename] = merged_df
            else:
                logger.warning(f"Skipping empty DataFrame for {filename}")

    threshold_params = np.round(np.linspace(-3, 3, 20), 3)
    long_short_params = ['long', 'short', 'both']
    condition_params = ['lower', 'higher']

    running_list = []
    for filename in price_factor_dict:
        for long_short in long_short_params:
            for condition in condition_params:
                test = {
                    'Metric': filename,
                    'Strategy': 'Divergence',
                    'Strategy Type': long_short,
                    'Condition': condition
                }
                running_list.append(test)

    total_combinations = len(running_list)
    logger.info(f"Total combinations to process: {total_combinations}")

    def running_single_strategy(run):
        try:
            filename = run['Metric']
            price_factor_df = price_factor_dict[filename].copy()
            price_factor_df = price_factor_df.rename(columns={'Value': run['Metric']})

            if price_factor_df.empty:
                logger.warning(f"Empty DataFrame for {filename}. Skipping.")
                return None

            train_df, test_df = split_data(price_factor_df)

            if train_df.empty or test_df.empty:
                logger.warning(f"Empty train or test DataFrame for {filename}. Skipping.")
                return None

            data_length = len(train_df)
            window_size_list = calculate_window_sizes(data_length)

            train_optimization = Optimization('Divergence', train_df, window_size_list, threshold_params,
                                              target=run['Metric'], price='Price', long_short=run['Strategy Type'],
                                              condition=run['Condition'])
            train_optimization.run()
            best_strategy = train_optimization.get_best()

            if best_strategy is None:
                logger.warning(f"No best strategy found for {run}")
                return None

            # Run on test data with best parameters
            test_strategy = Divergence(test_df, best_strategy.window_size, best_strategy.threshold,
                                       target=run['Metric'], price='Price', long_short=run['Strategy Type'],
                                       condition=run['Condition'])

            result = {
                'Train Sharpe': best_strategy.sharpe,
                'Test Sharpe': test_strategy.sharpe,
                'Best Window': best_strategy.window_size,
                'Best Threshold': best_strategy.threshold
            }
            return run | result
        except Exception as e:
            logger.error(f"Error in running_single_strategy for {run}: {str(e)}")
            return None

    num_cores = multiprocessing.cpu_count() - 2  # Leave one core free
    parallel_results = Parallel(n_jobs=num_cores)(
        delayed(running_single_strategy)(run) for run in tqdm(running_list, total=total_combinations, desc="Processing strategies")
    )

    results_list = []
    for result in parallel_results:
        if result is not None:
            results_list.append(result)

    return results_list

if __name__ == "__main__":
    try:
        results_list = run_optimization()

        if results_list:
            valid_results = [result for result in results_list if result is not None]
            if valid_results:
                results_df = pd.DataFrame(valid_results)
                results_df.to_csv(f"{ASSET.lower()}_divergence_factor_test_final.csv", index=False)
                logger.info('Optimization completed and final results saved')
                logger.info(results_df)
            else:
                logger.warning('No valid results were generated')
        else:
            logger.warning('No results were generated')

    except Exception as e:
        logger.error(f"An error occurred during optimization: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())

    logger.info('Run completed')