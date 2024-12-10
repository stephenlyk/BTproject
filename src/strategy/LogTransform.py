import numpy as np
import pandas as pd
import plotly.express as px
from strategy.strategy import Strategy
import logging

logger = logging.getLogger(__name__)


class LogTransform(Strategy):
    def __init__(self, source_df, window_size, threshold, target='Price', price='Price', long_short="long",
                 condition="higher"):
        super().__init__(source_df, window_size, threshold, target=target, price=price, long_short=long_short,
                         condition=condition)
        self.result_df = self._log_transform_strategy(source_df.copy(), window_size, threshold, target, long_short,
                                                      condition)
        self.annual_return = Strategy.annual_return(self.result_df)
        self.mdds = Strategy.return_mdds(self.result_df['Cumulative_Profit'])
        self.mdd = self.mdds[self.mdds.last_valid_index()]
        self.calmar = self.annual_return / abs(self.mdd)
        self.sharpe = Strategy.get_sharpe(self.result_df)

    def _log_transform_strategy(self, df, window_size, threshold, target, long_short, condition):
        df['Log_Transform'] = np.log1p(df[target])
        df['Log_MA'] = df['Log_Transform'].rolling(window=window_size).mean()
        df['Log_Signal'] = (df['Log_Transform'] - df['Log_MA']) / df['Log_Transform'].rolling(window=window_size).std()

        self._add_position(df, "Log_Signal", "diff", threshold, long_short, condition)
        return df