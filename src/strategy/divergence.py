import numpy as np
import pandas as pd
import plotly.express as px
from strategy.strategy import Strategy

class Divergence(Strategy):

    def __init__(self, source_df, window_size, threshold, target='Price', price='Price', long_short="long", condition="higher"):
        super().__init__(source_df, window_size, threshold, target=target, price=price, long_short=long_short, condition=condition)
        self.result_df = self._divergence_strategy(source_df.copy(), window_size, threshold, target, price, long_short, condition)
        self.annual_return = Strategy.annual_return(self.result_df)
        self.mdds = Strategy.return_mdds(self.result_df['Cumulative_Profit'])
        self.mdd = self.mdds[self.mdds.last_valid_index()]
        self.calmar = self.annual_return/abs(self.mdd)
        self.sharpe = Strategy.get_sharpe(self.result_df)

    def _divergence_strategy(self, df, window_size, threshold, target, price, long_short, condition):
        # Calculate Z-scores for both price and target
        df['Price_MA'] = Strategy.return_moving_average(df, price, window_size)
        df['Price_SD'] = Strategy.return_moving_average_sd(df, price, window_size)
        df['Price_Z_Score'] = (df[price] - df['Price_MA']) / df['Price_SD']

        df['Target_MA'] = Strategy.return_moving_average(df, target, window_size)
        df['Target_SD'] = Strategy.return_moving_average_sd(df, target, window_size)
        df['Target_Z_Score'] = (df[target] - df['Target_MA']) / df['Target_SD']

        # Calculate divergence
        df['Divergence'] = df['Price_Z_Score'] - df['Target_Z_Score']

        self._add_position(df, "Divergence", "diff", threshold, long_short, condition)
        return df