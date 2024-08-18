import numpy as np
import pandas as pd
import plotly.express as px
from  strategy.moving_average import MovingAverage
from strategy.strategy import Strategy

class RSI(Strategy):

    def __init__(self, source_df, window_size, threshold, target='Price', price='Price', long_short="long", condition="higher"):
        super().__init__(source_df, window_size, threshold, target=target, price=price, long_short=long_short, condition=condition)
        self.result_df = self._rsi_strategy(source_df.copy(), window_size, threshold, target, long_short, condition)
        self.annual_return = Strategy.annual_return(self.result_df)
        self.mdds = Strategy.return_mdds(self.result_df['Cumulative_Profit'])
        self.mdd = self.mdds[self.mdds.last_valid_index()]
        self.calmar = self.annual_return/abs(self.mdd)
        self.sharpe = Strategy.get_sharpe(self.result_df)


    def _rsi_strategy(self, df, window_size, threshold, target, long_short, condition):
        df['delta'] = df[target].diff()

        df['gain'] = df['delta'].apply(lambda x: x if x > 0 else 0)
        df['loss'] = df['delta'].apply(lambda x: -x if x < 0 else 0)

        df['avg_gain'] = df['gain'].rolling(window=window_size, min_periods=1).mean()
        df['avg_loss'] = df['loss'].rolling(window=window_size, min_periods=1).mean()

        df['rs'] = df['avg_gain'] / df['avg_loss']
        df['RSI'] = 1 - (1 / (1 + df['rs']))

        self._add_position(df, "RSI", "bounded", threshold, long_short, condition)


        return df


    def plot_graph(self):
        print(self.sharpe)
        fig = px.line(self.result_df, x='Date', y='Cumulative_Profit')
        fig.show()
