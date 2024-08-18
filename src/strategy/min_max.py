import numpy as np
import pandas as pd
import plotly.express as px
from  strategy.moving_average import MovingAverage
from strategy.strategy import Strategy


class MinMax(Strategy):

    def __init__(self, source_df, window_size, threshold, target='Price', price='Price', long_short="long", condition="higher"):
        super().__init__(source_df, window_size, threshold, target=target, price=price, long_short=long_short, condition=condition)
        self.result_df = self._min_max_strategy(source_df.copy(), window_size, threshold, target, long_short, condition)
        self.annual_return = Strategy.annual_return(self.result_df)
        self.mdds = Strategy.return_mdds(self.result_df['Cumulative_Profit'])
        self.mdd = self.mdds[self.mdds.last_valid_index()]
        self.calmar = self.annual_return/abs(self.mdd)
        self.sharpe = Strategy.get_sharpe(self.result_df)


    def _min_max_strategy(self, df, window_size, threshold, target, long_short, condition):
        df['rolling_min'] = df[target].rolling(window=window_size).min()
        df['rolling_max'] = df[target].rolling(window=window_size).max()

        df['Rolling_MinMax_Scaled'] = (df[target] - df['rolling_min']) / (df['rolling_max'] - df['rolling_min'])

        self._add_position(df, "Rolling_MinMax_Scaled", "bounded", threshold, long_short, condition)

        return df

    def plot_graph(self):
        print(self.sharpe)
        fig = px.line(self.result_df, x='Date', y='Cumulative_Profit')
        fig.show()
