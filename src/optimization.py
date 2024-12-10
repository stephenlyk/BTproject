import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.io as pio
from joblib import Parallel, delayed
import matplotlib.patches as patches


class Optimization():
    def __init__(self, strategy_class, train_df, test_df, window_size_list, threshold_list, target, price='Price',
                 long_short='long', condition='higher'):
        self.strategy_class = strategy_class
        self.train_df = train_df
        self.test_df = test_df
        self.window_size_list = window_size_list
        self.threshold_list = threshold_list
        self.target = target
        self.price = price
        self.long_short = long_short
        self.condition = condition

        self.train_results_data_df = pd.DataFrame()
        self.test_results_data_df = pd.DataFrame()

    def _run_strategy(self, window_size, threshold):
        train_result = self.strategy_class(self.train_df, window_size, threshold, target=self.target, price=self.price,
                                           long_short=self.long_short, condition=self.condition)
        test_result = self.strategy_class(self.test_df, window_size, threshold, target=self.target, price=self.price,
                                          long_short=self.long_short, condition=self.condition)
        return train_result, test_result

    def run(self):
        results = Parallel(n_jobs=-3, prefer="processes")(
            delayed(self._run_strategy)(window_size, threshold) for window_size in self.window_size_list for threshold
            in self.threshold_list)

        train_results_data = []
        test_results_data = []
        for train_result, test_result in results:
            train_data = train_result.dump_data()
            train_data['Strategy Object'] = train_result
            train_results_data.append(train_data)

            test_data = test_result.dump_data()
            test_data['Strategy Object'] = test_result
            test_results_data.append(test_data)

        self.train_results_data_df = pd.DataFrame(train_results_data)
        self.train_results_data_df = self.train_results_data_df.sort_values(by='Sharpe', ascending=False)

        self.test_results_data_df = pd.DataFrame(test_results_data)
        self.test_results_data_df = self.test_results_data_df.sort_values(by='Sharpe', ascending=False)

    def plot_heat_map(self, save_path=None, best_window=None, best_threshold=None):
        train_result_data_pivot = self.train_results_data_df.pivot(index='Window', columns='Threshold', values='Sharpe')
        test_result_data_pivot = self.test_results_data_df.pivot(index='Window', columns='Threshold', values='Sharpe')

        # Create a figure with three subplots
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(24, 8))

        # Function to plot heatmap and highlight max value
        def plot_heatmap_with_highlight(data, ax, title):
            sns.heatmap(data, cmap="Greens", annot=True, ax=ax)
            ax.set_title(title)
            ax.set_xlabel('Threshold')
            ax.set_ylabel('Window Size')

            # Find the position of the maximum value
            max_idx = data.values.argmax()
            max_row, max_col = np.unravel_index(max_idx, data.shape)

            # Create a rectangle patch to highlight the max value
            rect = patches.Rectangle((max_col, max_row), 1, 1, fill=False, edgecolor='red', lw=2)
            ax.add_patch(rect)

        # Plot train heatmap
        plot_heatmap_with_highlight(train_result_data_pivot, ax1,
                                    f"{self.strategy_class.__name__} {self.long_short.capitalize()} Train Optimization Heatmap")

        # Plot test heatmap
        plot_heatmap_with_highlight(test_result_data_pivot, ax2,
                                    f"{self.strategy_class.__name__} {self.long_short.capitalize()} Test Optimization Heatmap")

        # Get the best strategy
        best_train_strategy = self.train_results_data_df[(self.train_results_data_df['Window'] == best_window) &
                                                         (self.train_results_data_df['Threshold'] == best_threshold)][
            'Strategy Object'].iloc[0]

        best_test_strategy = self.test_results_data_df[(self.test_results_data_df['Window'] == best_window) &
                                                       (self.test_results_data_df['Threshold'] == best_threshold)][
            'Strategy Object'].iloc[0]

        # Plot equity curves
        ax3.plot(best_train_strategy.result_df['Date'], best_train_strategy.result_df['Cumulative_Profit'],
                 label='Train Strategy',
                 color='blue')
        ax3.plot(best_train_strategy.result_df['Date'], best_train_strategy.result_df['Cumulative_Bnh'],
                 label='Train Buy and Hold',
                 color='green')
        ax3.plot(best_test_strategy.result_df['Date'], best_test_strategy.result_df['Cumulative_Profit'],
                 label='Test Strategy',
                 color='blue', linestyle='--')
        ax3.plot(best_test_strategy.result_df['Date'], best_test_strategy.result_df['Cumulative_Bnh'],
                 label='Test Buy and Hold',
                 color='green', linestyle='--')

        ax3.set_title(
            f"Equity Curve - {self.strategy_class.__name__} (Window: {best_window}, Threshold: {best_threshold:.3f})")
        ax3.set_xlabel('Date')
        ax3.set_ylabel('Cumulative Profit')
        ax3.legend()

        # Add text box with key metrics
        train_metrics = (f"Train - Annual Return: {best_train_strategy.annual_return * 100:.2f}%, "
                         f"Sharpe: {best_train_strategy.sharpe:.2f}, MDD: {best_train_strategy.mdd * 100:.2f}%, "
                         f"Calmar: {best_train_strategy.calmar:.2f}")

        test_metrics = (f"Test - Annual Return: {best_test_strategy.annual_return * 100:.2f}%, "
                        f"Sharpe: {best_test_strategy.sharpe:.2f}, MDD: {best_test_strategy.mdd * 100:.2f}%, "
                        f"Calmar: {best_test_strategy.calmar:.2f}")

        metrics_text = (f"{train_metrics}\n{test_metrics}\n"
                        f"Best Window: {best_window}, Best Threshold: {best_threshold:.3f}")
        ax3.text(0.02, 0.98, metrics_text, transform=ax3.transAxes, verticalalignment='top',
                 fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)
            plt.close()  # Close the figure to free up memory
        else:
            plt.show()

        print(self.train_results_data_df.head())

    def get_best(self):
        return self.train_results_data_df.iloc[0]['Strategy Object']
