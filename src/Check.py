import pandas as pd
import numpy as np
import requests
from optimization import Optimization
import os
from strategy.z_score import ZScore
from strategy.robust import Robust
from strategy.roc import ROC
from strategy.min_max import MinMax
from strategy.moving_average import MovingAverage
from strategy.percentile import Percentile
from strategy.rsi import RSI
from strategy.divergence import Divergence
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from config import GLASSNODE_API_KEY

# Standard User Input Section
COMMISSION = 0.0005  # 7 basis points, change as needed
WINDOW_SIZE_PERCENT = 0.1  # 10%
NUM_WINDOW_SIZES = 40
TRAIN_RATIO = 0.7  # 70%
GLASSNODE_API_KEY = GLASSNODE_API_KEY
ASSET = 'BTC'
INTERVAL = '1h'

# File and Strategy
FILE_PATH = "/Users/stephenlyk/Desktop/Strategy Bank/ETH/17Aug2024/book3.csv"
STRATEGY_NAME = "ZScore"
LONG_SHORT = "long"
CONDITION = "lower"

# Strategy-specific threshold parameters
STRATEGY_PARAMS = {
    'ZScore': {'threshold_list': np.round(np.linspace(-3, 3, 20), 3)},
    'MovingAverage': {'threshold_list': np.round(np.linspace(-0.1, 0.1, 20), 3)},
    'RSI': {'threshold_list': np.round(np.linspace(0.2, 0.8, 32), 3)},
    'ROC': {'threshold_list': np.round(np.linspace(-0.1, 0.1, 20), 3)},
    'MinMax': {'threshold_list': np.round(np.linspace(0.1, 0.9, 20), 3)},
    'Robust': {'threshold_list': np.round(np.linspace(0, 2, 20), 3)},
    'Percentile': {'threshold_list': np.round(np.linspace(0.1, 0.9, 20), 3)},
    'Divergence': {'threshold_list': np.round(np.linspace(-3, 3, 20), 3)}  # Add this line
}

class StrategyChecker:
    def __init__(self, file_path, strategy_name, long_short, condition):
        self.file_path = file_path
        self.strategy_name = strategy_name
        self.strategy_class = globals()[strategy_name]
        self.long_short = long_short
        self.condition = condition
        self.commission = COMMISSION
        self.btc_price_df = self.fetch_glassnode_data()
        self.df = self.read_and_prepare_data()
        self.train_df, self.test_df = self.split_data()
        self.window_size_list = self.calculate_window_sizes()
        self.threshold_list = STRATEGY_PARAMS[self.strategy_name]['threshold_list']
        self.metric_name = os.path.splitext(os.path.basename(self.file_path))[0]
        self.result_folder = "result"
        self.metric_folder = os.path.join(self.result_folder, self.metric_name)
        self.ensure_folders_exist()

    def ensure_folders_exist(self):
        if not os.path.exists(self.result_folder):
            os.makedirs(self.result_folder)
            print(f"Created folder: {self.result_folder}")
        if not os.path.exists(self.metric_folder):
            os.makedirs(self.metric_folder)
            print(f"Created folder: {self.metric_folder}")

    def fetch_glassnode_data(self):
        url = f"https://api.glassnode.com/v1/metrics/market/price_usd_close"
        params = {
            'a': ASSET,
            'i': INTERVAL,
            'api_key': GLASSNODE_API_KEY
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

    def read_and_prepare_data(self):
        df = pd.read_csv(self.file_path)
        df.columns = ['Date', 'Value']
        df['Date'] = pd.to_datetime(df['Date'])
        df['Value'] = df['Value'].shift(1)
        merged_df = pd.merge(self.btc_price_df, df, on='Date', how='inner')
        merged_df = merged_df.sort_values('Date').dropna()
        return merged_df

    def split_data(self):
        train_size = int(len(self.df) * TRAIN_RATIO)
        return self.df.iloc[:train_size], self.df.iloc[train_size:]

    def calculate_window_sizes(self):
        data_length = len(self.train_df)
        max_window = int(data_length * WINDOW_SIZE_PERCENT)
        min_window = 2
        return np.linspace(min_window, max_window, NUM_WINDOW_SIZES, dtype=int)

    def optimize_strategy(self):
        optimization = Optimization(self.strategy_class, self.train_df, self.test_df, self.window_size_list,
                                    self.threshold_list,
                                    target='Value', price='Price', long_short=self.long_short,
                                    condition=self.condition)
        optimization.run()
        best_strategy = optimization.get_best()
        return optimization, best_strategy.window_size, best_strategy.threshold

    def calculate_metrics(self, strategy_obj):
        return strategy_obj.sharpe, strategy_obj.mdd, strategy_obj.calmar

    def prepare_detailed_df(self, strategy_obj):
        df = strategy_obj.result_df.copy()
        df['Daily_PnL'] = df['Profit']
        df['BTC_Returns'] = df['Price'].pct_change()
        df['Long_Short'] = self.long_short
        df['Condition'] = self.condition

        columns = ['Date', 'Value', 'Price', 'Position', 'Long_Short', 'Condition', 'Daily_PnL', 'Cumulative_Profit',
                   'BTC_Returns']

        strategy_score_columns = {
            'ZScore': 'Z_Score',
            'MinMax': 'Rolling_MinMax_Scaled',
            'Robust': 'Robust_Scaled',
            'ROC': 'ROC',
            'MovingAverage': 'MA_Score',
            'Percentile': 'Percentile_Score',
            'RSI': 'RSI_Score',
            'Divergence': 'Divergence'  # Add this line
        }

        score_column = strategy_score_columns.get(self.strategy_name)

        if score_column and score_column in df.columns:
            columns.insert(3, score_column)

        return df[columns]

    def calculate_beta(self, df):
        cov_matrix = np.cov(df['Daily_PnL'].fillna(0), df['BTC_Returns'].fillna(0))
        beta = cov_matrix[0, 1] / np.var(df['BTC_Returns'].fillna(0))
        return beta

    def calculate_num_trades(self, df):
        # Calculate the number of trades by counting position changes
        return (df['Position'].diff() != 0).sum()

    def plot_optimization_heatmap(self, optimization, best_window, best_threshold):
        heatmap_filename = os.path.join(self.metric_folder,
                                        f'{self.strategy_name}_{self.long_short}_{self.condition}_heatmap_and_equity.png')
        try:
            # Remove duplicate entries from the results_data_df
            optimization.train_results_data_df = optimization.train_results_data_df.groupby(
                ['Window', 'Threshold']).first().reset_index()
            optimization.test_results_data_df = optimization.test_results_data_df.groupby(
                ['Window', 'Threshold']).first().reset_index()

            # Use the plot_heat_map method from the Optimization class
            optimization.plot_heat_map(save_path=heatmap_filename, best_window=best_window,
                                       best_threshold=best_threshold)

            print(f"Heatmap and equity curve saved as {heatmap_filename}")
        except Exception as e:
            logging.error(
                f"Error generating heatmap for {self.strategy_name}, {self.long_short}, {self.condition}: {str(e)}")

    def _plot_single_heatmap(self, data, position_type, filename):
        pivot_data = data.pivot_table(index='Window', columns='Threshold', values='Sharpe', aggfunc='mean')
        plt.figure(figsize=(12, 8))
        sns.heatmap(pivot_data, cmap="Greens", annot=True)
        plt.title(f"{self.strategy_name} {position_type} Optimization Heatmap")
        plt.xlabel('Threshold')
        plt.ylabel('Window Size')
        plt.savefig(filename)
        plt.close()

    def save_detailed_results(self, train_df, test_df):
        train_filename = os.path.join(self.metric_folder,
                                      f'{self.strategy_name}_{self.long_short}_{self.condition}_train_detailed.csv')
        test_filename = os.path.join(self.metric_folder,
                                     f'{self.strategy_name}_{self.long_short}_{self.condition}_test_detailed.csv')
        train_df.to_csv(train_filename, index=False)
        test_df.to_csv(test_filename, index=False)
        print(f"Detailed train results saved as {train_filename}")
        print(f"Detailed test results saved as {test_filename}")

    def save_summary_results(self, results):
        summary_filename = os.path.join(self.metric_folder,
                                        f'{self.strategy_name}_{self.long_short}_{self.condition}_summary.csv')
        pd.DataFrame([results]).to_csv(summary_filename, index=False)
        print(f"Summary results saved as {summary_filename}")

    def run(self):
        try:
            print(f"Running strategy: {self.strategy_name}")
            print(f"File being processed: {self.file_path}")

            logging.info(f"Running strategy: {self.strategy_name}, {self.long_short}, {self.condition}")

            optimization, best_window, best_threshold = self.optimize_strategy()

            strategy_class = globals()[self.strategy_name]

            train_strategy = strategy_class(self.train_df, best_window, best_threshold, target='Value', price='Price',
                                            long_short=self.long_short, condition=self.condition)
            test_strategy = strategy_class(self.test_df, best_window, best_threshold, target='Value', price='Price',
                                           long_short=self.long_short, condition=self.condition)

            # Plot and save the heatmap and equity curves
            try:
                self.plot_optimization_heatmap(optimization, best_window, best_threshold)
                logging.info(
                    f"Successfully generated heatmap for {self.strategy_name}, {self.long_short}, {self.condition}")
            except Exception as e:
                logging.error(
                    f"Error generating heatmap for {self.strategy_name}, {self.long_short}, {self.condition}: {str(e)}")

            train_sharpe, train_mdd, train_calmar = self.calculate_metrics(train_strategy)
            test_sharpe, test_mdd, test_calmar = self.calculate_metrics(test_strategy)

            # Prepare detailed dataframes
            train_df_detailed = self.prepare_detailed_df(train_strategy)
            test_df_detailed = self.prepare_detailed_df(test_strategy)

            # Save detailed results
            self.save_detailed_results(train_df_detailed, test_df_detailed)

            # Calculate beta
            train_beta = self.calculate_beta(train_df_detailed)
            test_beta = self.calculate_beta(test_df_detailed)

            # Calculate number of trades
            train_num_trades = self.calculate_num_trades(train_df_detailed)
            test_num_trades = self.calculate_num_trades(test_df_detailed)

            # Prepare results
            results = {
                'Metric': self.file_path,
                'Strategy': self.strategy_name,
                'Long_Short': self.long_short,
                'Condition': self.condition,
                'Best Window': best_window,
                'Best Threshold': best_threshold,
                'Train Annual Return': train_strategy.annual_return,
                'Test Annual Return': test_strategy.annual_return,
                'Train Sharpe': train_sharpe,
                'Test Sharpe': test_sharpe,
                'Train MDD': train_mdd,
                'Test MDD': test_mdd,
                'Train Calmar': train_calmar,
                'Test Calmar': test_calmar,
                'Train Beta': train_beta,
                'Test Beta': test_beta,
                'Train Num Trades': train_num_trades,
                'Test Num Trades': test_num_trades
            }

            # Save summary results
            self.save_summary_results(results)

            logging.info(f"Successfully processed: {self.strategy_name}, {self.long_short}, {self.condition}")
            return results

        except Exception as e:
            logging.error(f"Error in StrategyChecker.run for {self.strategy_name}, {self.long_short}, {self.condition}: {str(e)}")
            return None


def run_single_strategy(file_path, strategy_name, long_short, condition):
    checker = StrategyChecker(file_path, strategy_name, long_short, condition)
    return checker.run()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 4:
        file_path = sys.argv[1]
        strategy_name = sys.argv[2]
        long_short = sys.argv[3]
        condition = sys.argv[4]
        run_single_strategy(file_path, strategy_name, long_short, condition)
    else:
        print("Usage: python Check.py <file_path> <strategy_name> <long_short> <condition>")