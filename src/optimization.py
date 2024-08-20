import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.io as pio
from strategy.moving_average import MovingAverage
from strategy.z_score import ZScore
from strategy.rsi import RSI
from strategy.roc import ROC
from strategy.percentile import Percentile
from strategy.min_max import MinMax
from strategy.robust import Robust
from joblib import Parallel, delayed


class Optimization():

    def __init__(self, strategy_name, source_df, window_size_list, threshold_list, target, price='Price', long_short='long', condition='higher'):
        self.strategy_name = strategy_name
        self.source_df = source_df
        self.window_size_list = window_size_list
        self.threshold_list = threshold_list
        self.target = target
        self.price = price
        self.long_short = long_short
        self.condition = condition

        self.results_data_df = pd.DataFrame()

        if self.strategy_name not in globals():
            return

    def _run_strategy(self, window_size, threshold):
        strategy = globals()[self.strategy_name]
        result = strategy(self.source_df, window_size, threshold, target=self.target, price=self.price, long_short=self.long_short, condition=self.condition)
        return result

    def run(self):
        results = Parallel(n_jobs=-3, prefer="processes")(
            delayed(self._run_strategy)(window_size, threshold) for window_size in self.window_size_list for threshold
            in self.threshold_list)

        results_data = []
        for result in results:
            result_data = result.dump_data()
            result_data['Strategy Object'] = result

            results_data.append(result_data)

        self.results_data_df = pd.DataFrame(results_data)
        self.results_data_df = self.results_data_df.sort_values(by='Sharpe', ascending=False)

    def plot_heat_map(self, save_path=None, test_strategy=None, best_window=None, best_threshold=None):
        result_data_pivot = self.results_data_df.pivot(index='Window', columns='Threshold', values='Sharpe')

        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16))

        # Plot heatmap
        sns.heatmap(result_data_pivot, cmap="Greens", annot=True, ax=ax1)
        ax1.set_title(f"{self.strategy_name} {self.long_short.capitalize()} Optimization Heatmap")
        ax1.set_xlabel('Threshold')
        ax1.set_ylabel('Window Size')

        # Get the best strategy using the passed parameters
        best_strategy = self.results_data_df[(self.results_data_df['Window'] == best_window) &
                                             (self.results_data_df['Threshold'] == best_threshold)][
            'Strategy Object'].iloc[0]


        # Plot equity curve using the correct best strategy
        ax2.plot(best_strategy.result_df['Date'], best_strategy.result_df['Cumulative_Profit'], label='Train Strategy',
                 color='blue')
        ax2.plot(best_strategy.result_df['Date'], best_strategy.result_df['Cumulative_Bnh'], label='Train Buy and Hold',
                 color='green')

        if test_strategy is not None:
            ax2.plot(test_strategy.result_df['Date'], test_strategy.result_df['Cumulative_Profit'],
                     label='Test Strategy', color='blue', linestyle='--')
            ax2.plot(test_strategy.result_df['Date'], test_strategy.result_df['Cumulative_Bnh'],
                     label='Test Buy and Hold', color='green', linestyle='--')

        ax2.set_title(
            f"Equity Curve - {self.strategy_name} (Window: {best_strategy.window_size}, Threshold: {best_strategy.threshold:.3f})")
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Cumulative Profit')
        ax2.legend()

        # Add text box with key metrics
        train_metrics = (f"Train - Annual Return: {best_strategy.annual_return * 100:.2f}%, "
                         f"Sharpe: {best_strategy.sharpe:.2f}, MDD: {best_strategy.mdd * 100:.2f}%, "
                         f"Calmar: {best_strategy.calmar:.2f}")
        if test_strategy is not None:
            test_metrics = (f"Test - Annual Return: {test_strategy.annual_return * 100:.2f}%, "
                            f"Sharpe: {test_strategy.sharpe:.2f}, MDD: {test_strategy.mdd * 100:.2f}%, "
                            f"Calmar: {test_strategy.calmar:.2f}")
        else:
            test_metrics = "Test data not available"

        metrics_text = (f"{train_metrics}\n{test_metrics}\n"
                        f"Best Window: {best_strategy.window_size}, Best Threshold: {best_strategy.threshold:.3f}")
        ax2.text(0.02, 0.98, metrics_text, transform=ax2.transAxes, verticalalignment='top',
                 fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)
            plt.close()  # Close the figure to free up memory
        else:
            plt.show()

        print(self.results_data_df.head())

    def get_best(self):
        return self.results_data_df.iloc[0]['Strategy Object']

