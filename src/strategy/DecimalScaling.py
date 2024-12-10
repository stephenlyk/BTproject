import numpy as np
import pandas as pd
import plotly.express as px
from strategy.strategy import Strategy
import logging

logger = logging.getLogger(__name__)


class DecimalScaling(Strategy):
    def __init__(self, source_df, window_size, threshold, target='Price', price='Price', long_short="long",
                 condition="higher"):
        super().__init__(source_df, window_size, threshold, target=target, price=price, long_short=long_short,
                         condition=condition)
        self.result_df = self._decimal_scaling_strategy(source_df.copy(), window_size, threshold, target, long_short,
                                                        condition)
        self.annual_return = Strategy.annual_return(self.result_df)
        self.mdds = Strategy.return_mdds(self.result_df['Cumulative_Profit'])
        self.mdd = self.mdds[self.mdds.last_valid_index()]
        self.calmar = self.annual_return / abs(self.mdd)
        self.sharpe = Strategy.get_sharpe(self.result_df)

    @staticmethod
    def get_scaling_factor(x):
        """Vectorized way to get number of digits"""
        return np.floor(np.log10(np.abs(x)) + 1)

    def _decimal_scaling_strategy(self, df, window_size, threshold, target, long_short, condition):
        # Handle zero/negative values
        eps = 1e-10
        abs_values = np.abs(df[target]) + eps

        # Calculate scaling factors using vectorized operations
        scaling_factors = self.get_scaling_factor(
            abs_values.rolling(window=window_size, min_periods=1).max()
        )

        # Apply decimal scaling using vectorized operations
        df['Decimal_Scaled'] = df[target] / (10 ** scaling_factors)

        self._add_position(df, "Decimal_Scaled", "bounded", threshold, long_short, condition)
        return df