import numpy as np
import pandas as pd
import plotly.express as px
from strategy.strategy import Strategy
import logging

logger = logging.getLogger(__name__)


class ModifiedZScore(Strategy):
    def __init__(self, source_df, window_size, threshold, target='Price', price='Price', long_short="long",
                 condition="higher"):
        super().__init__(source_df, window_size, threshold, target=target, price=price, long_short=long_short,
                         condition=condition)
        self.result_df = self._modified_zscore_strategy(source_df.copy(), window_size, threshold, target, long_short,
                                                        condition)
        self.annual_return = Strategy.annual_return(self.result_df)
        self.mdds = Strategy.return_mdds(self.result_df['Cumulative_Profit'])
        self.mdd = self.mdds[self.mdds.last_valid_index()]
        self.calmar = self.annual_return / abs(self.mdd)
        self.sharpe = Strategy.get_sharpe(self.result_df)

    @staticmethod
    def rolling_mad(series, window):
        """Optimized rolling MAD calculation"""
        # Calculate the rolling median
        rolling_median = series.rolling(window=window).median()

        # Calculate absolute deviations
        abs_dev = np.abs(series - rolling_median)

        # Calculate MAD
        mad = abs_dev.rolling(window=window).median()
        return mad

    def _modified_zscore_strategy(self, df, window_size, threshold, target, long_short, condition):
        # Vectorized operations instead of rolling apply
        df['Rolling_Median'] = df[target].rolling(window=window_size, min_periods=1).median()
        df['Rolling_MAD'] = self.rolling_mad(df[target], window_size)

        # Add small constant to avoid division by zero
        eps = 1e-10
        df['Modified_ZScore'] = 0.6745 * (df[target] - df['Rolling_Median']) / (df['Rolling_MAD'] + eps)

        self._add_position(df, "Modified_ZScore", "diff", threshold, long_short, condition)
        return df