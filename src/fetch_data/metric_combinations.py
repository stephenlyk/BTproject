METRIC_COMBINATIONS = [
            {
                'name': '001_market_value_efficiency',
                'metric1': 'market/marketcap_usd',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Market cap to transfer volume ratio - indicates if market value is supported by transaction activity'
            },
            {
                'name': '002_network_load_cost',
                'metric1': 'transactions/count',
                'metric2': 'fees/volume_sum',
                'operation': 'divide',
                'description': 'Transaction count to fee ratio - measures cost efficiency of network usage'
            },
            {
                'name': '003_mining_revenue_efficiency',
                'metric1': 'mining/revenue_sum',
                'metric2': 'mining/hash_rate_mean',
                'operation': 'divide',
                'description': 'Revenue per hash rate - indicates mining profitability'
            },
            {
                'name': '004_active_market_participation',
                'metric1': 'addresses/active_count',
                'metric2': 'addresses/new_non_zero_count',
                'operation': 'divide',
                'description': 'Active to new address ratio - measures network growth quality'
            },
            {
                'name': '005_realized_price_deviation',
                'metric1': 'market/price_usd_close',
                'metric2': 'market/price_realized_usd',
                'operation': 'divide',
                'description': 'Market price to realized price ratio - indicates market value vs accumulated cost basis'
            },
            {
                'name': '006_exchange_flow_pressure',
                'metric1': 'transactions/transfers_volume_to_exchanges_sum',
                'metric2': 'transactions/transfers_volume_from_exchanges_sum',
                'operation': 'divide',
                'description': 'Exchange inflow to outflow ratio - measures net exchange pressure'
            },
            {
                'name': '007_hash_difficulty_equilibrium',
                'metric1': 'mining/hash_rate_mean',
                'metric2': 'mining/difficulty_latest',
                'operation': 'divide',
                'description': 'Hash rate to difficulty ratio - indicates mining competition balance'
            },
            {
                'name': '008_fee_market_stress',
                'metric1': 'fees/volume_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Fee to transaction volume ratio - measures network congestion cost'
            },
            {
                'name': '009_network_value_density',
                'metric1': 'market/marketcap_usd',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Market cap per active address - measures value density of network usage'
            },
            {
                'name': '010_miner_sell_pressure',
                'metric1': 'mining/volume_mined',
                'metric2': 'transactions/transfers_volume_miners_to_exchanges',
                'operation': 'divide',
                'description': 'Mined volume to exchange transfer ratio - indicates miner selling pressure'
            },
            {
                'name': '011_transaction_efficiency',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Average transaction value - measures transaction efficiency'
            },
            {
                'name': '012_network_usage_cost',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'fees/volume_mean',
                'operation': 'divide',
                'description': 'Transaction volume to average fee ratio - indicates transaction cost efficiency'
            },
            {
                'name': '013_exchange_balance_impact',
                'metric1': 'distribution/balance_exchanges',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Exchange balance to market cap ratio - measures potential sell-side liquidity'
            },
            {
                'name': '014_mining_profitability_pressure',
                'metric1': 'mining/revenue_sum',
                'metric2': 'mining/difficulty_latest',
                'operation': 'divide',
                'description': 'Mining revenue to difficulty ratio - indicates mining profitability pressure'
            },
            {
                'name': '015_network_growth_quality',
                'metric1': 'addresses/new_non_zero_count',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'New addresses to price volatility ratio - measures organic growth'
            },
            {
                'name': '016_realized_market_momentum',
                'metric1': 'market/marketcap_realized_usd',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'divide',
                'description': 'Realized cap to drawdown ratio - indicates holder conviction'
            },
            {
                'name': '017_exchange_flow_impact',
                'metric1': 'transactions/transfers_volume_exchanges_net',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Net exchange flow impact on volatility'
            },
            {
                'name': '018_mining_revenue_efficiency',
                'metric1': 'mining/revenue_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Mining revenue to network volume ratio - measures mining revenue efficiency'
            },
            {
                'name': '019_network_value_quality',
                'metric1': 'market/marketcap_usd',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Market cap per transaction - measures value density of network activity'
            },
            {
                'name': '020_holder_conviction_strength',
                'metric1': 'supply/illiquid_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Illiquid supply response to market drawdowns'
            },
            {
                'name': '021_market_realized_spread',
                'metric1': 'market/price_usd_close',
                'metric2': 'market/price_realized_usd',
                'operation': 'divide',
                'description': 'Market to realized price spread - indicates market sentiment'
            },
            {
                'name': '022_network_congestion_cost',
                'metric1': 'fees/volume_mean',
                'metric2': 'transactions/count',
                'operation': 'multiply',
                'description': 'Average fee impact on transaction activity'
            },
            {
                'name': '023_miner_revenue_stability',
                'metric1': 'mining/revenue_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Mining revenue stability relative to price volatility'
            },
            {
                'name': '024_exchange_liquidity_ratio',
                'metric1': 'distribution/balance_exchanges',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Exchange balance to liquid supply ratio - measures available liquidity'
            },
            {
                'name': '025_network_value_density',
                'metric1': 'market/marketcap_usd',
                'metric2': 'transactions/transfer_volume_mean',
                'operation': 'divide',
                'description': 'Market cap to average transaction value ratio'
            },
            {
                'name': '026_mining_difficulty_pressure',
                'metric1': 'mining/difficulty_latest',
                'metric2': 'mining/revenue_sum',
                'operation': 'divide',
                'description': 'Difficulty to revenue ratio - indicates mining pressure'
            },
            {
                'name': '027_transaction_value_efficiency',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Volume per active address - measures transaction value efficiency'
            },
            {
                'name': '028_market_momentum_strength',
                'metric1': 'market/price_usd_close',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'divide',
                'description': 'Price to drawdown ratio - indicates market momentum'
            },
            {
                'name': '029_network_adoption_quality',
                'metric1': 'addresses/new_non_zero_count',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'New addresses to price ratio - measures price-driven adoption'
            },
            {
                'name': '030_holder_distribution_balance',
                'metric1': 'supply/illiquid_sum',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Illiquid to liquid supply ratio - indicates holder distribution'
            },
            {
                'name': '031_mining_hashrate_efficiency',
                'metric1': 'mining/hash_rate_mean',
                'metric2': 'mining/volume_mined',
                'operation': 'divide',
                'description': 'Hash rate to mined volume ratio - measures mining efficiency'
            },
            {
                'name': '032_fee_market_equilibrium',
                'metric1': 'fees/volume_mean',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Average fee to price ratio - indicates fee market balance'
            },
            {
                'name': '033_exchange_flow_momentum',
                'metric1': 'transactions/transfers_volume_to_exchanges_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Exchange inflow response to market drawdowns'
            },
            {
                'name': '034_network_usage_density',
                'metric1': 'transactions/count',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Transactions per active address - measures network usage density'
            },
            {
                'name': '035_market_liquidity_ratio',
                'metric1': 'market/marketcap_usd',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Market cap to liquid supply ratio - indicates market liquidity'
            },
            {
                'name': '036_mining_profitability_index',
                'metric1': 'mining/revenue_sum',
                'metric2': 'mining/volume_mined',
                'operation': 'divide',
                'description': 'Revenue per mined volume - indicates mining profitability'
            },
            {
                'name': '037_transaction_cost_ratio',
                'metric1': 'fees/volume_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Fee volume to price ratio - measures transaction costs'
            },
            {
                'name': '038_network_value_circulation',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Transaction volume to market cap ratio - measures value circulation'
            },
            {
                'name': '039_exchange_balance_pressure',
                'metric1': 'distribution/balance_exchanges',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Exchange balance response to market drawdowns'
            },
            {
                'name': '040_mining_difficulty_adjustment',
                'metric1': 'mining/difficulty_latest',
                'metric2': 'mining/hash_rate_mean',
                'operation': 'divide',
                'description': 'Difficulty to hash rate ratio - indicates mining adjustment pressure'
            },
            {
                'name': '041_holder_activity_ratio',
                'metric1': 'addresses/active_count',
                'metric2': 'supply/illiquid_sum',
                'operation': 'divide',
                'description': 'Active addresses to illiquid supply ratio - measures holder activity'
            },
            {
                'name': '042_market_momentum_quality',
                'metric1': 'market/price_usd_close',
                'metric2': 'transactions/transfer_volume_mean',
                'operation': 'divide',
                'description': 'Price to average transaction value ratio - indicates price support'
            },
            {
                'name': '043_network_growth_momentum',
                'metric1': 'addresses/new_non_zero_count',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'New addresses to transaction count ratio - measures network growth'
            },
            {
                'name': '044_exchange_flow_efficiency',
                'metric1': 'transactions/transfers_volume_exchanges_net',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Net exchange flow to market cap ratio - measures flow impact'
            },
            {
                'name': '045_mining_revenue_distribution',
                'metric1': 'mining/revenue_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Mining revenue to network volume ratio - indicates revenue distribution'
            },
            {
                'name': '046_fee_market_pressure',
                'metric1': 'fees/volume_mean',
                'metric2': 'transactions/transfer_volume_mean',
                'operation': 'divide',
                'description': 'Average fee to transaction value ratio - measures fee pressure'
            },
            {
                'name': '047_holder_distribution_change',
                'metric1': 'supply/illiquid_change',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Illiquid supply change response to market drawdowns'
            },
            {
                'name': '048_market_realized_momentum',
                'metric1': 'market/marketcap_usd',
                'metric2': 'market/marketcap_realized_usd',
                'operation': 'divide',
                'description': 'Market cap to realized cap ratio - indicates market momentum'
            },
            {
                'name': '049_network_congestion_index',
                'metric1': 'fees/volume_sum',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Fee volume per transaction - measures network congestion'
            },
            {
                'name': '050_exchange_liquidity_pressure',
                'metric1': 'distribution/balance_exchanges',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Exchange balance to network volume ratio - indicates liquidity pressure'
            },
            {
                'name': '051_miner_sell_efficiency',
                'metric1': 'mining/volume_mined',
                'metric2': 'mining/revenue_sum',
                'operation': 'divide',
                'description': 'Mined volume to revenue ratio - indicates mining efficiency'
            },
            {
                'name': '052_transaction_value_density',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'transactions/size_sum',
                'operation': 'divide',
                'description': 'Transaction volume to size ratio - measures value density'
            },
            {
                'name': '053_network_usage_impact',
                'metric1': 'addresses/active_count',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Active addresses to volatility ratio - measures usage stability'
            },
            {
                'name': '054_market_supply_ratio',
                'metric1': 'market/marketcap_usd',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Market cap to current supply ratio - indicates price per coin'
            },
            {
                'name': '055_exchange_activity_ratio',
                'metric1': 'transactions/transfers_between_exchanges_count',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Inter-exchange to total transaction ratio - measures exchange activity'
            },
            {
                'name': '056_mining_difficulty_impact',
                'metric1': 'mining/difficulty_latest',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Difficulty to price ratio - indicates mining adjustment to price'
            },
            {
                'name': '057_fee_revenue_ratio',
                'metric1': 'fees/volume_sum',
                'metric2': 'mining/revenue_sum',
                'operation': 'divide',
                'description': 'Fee volume to mining revenue ratio - measures fee contribution'
            },
            {
                'name': '058_holder_balance_distribution',
                'metric1': 'supply/illiquid_sum',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Illiquid to total supply ratio - measures holder distribution'
            },
            {
                'name': '059_network_value_support',
                'metric1': 'market/marketcap_usd',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Market cap to network volume ratio - indicates value support'
            },
            {
                'name': '060_exchange_volume_impact',
                'metric1': 'transactions/transfers_volume_between_exchanges_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Inter-exchange volume to market cap ratio'
            },
            {
                'name': '061_mining_profit_margin',
                'metric1': 'mining/revenue_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Mining revenue to price ratio - indicates mining profitability'
            },
            {
                'name': '062_transaction_size_efficiency',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'transactions/size_mean',
                'operation': 'divide',
                'description': 'Volume to average transaction size ratio'
            },
            {
                'name': '063_network_adoption_momentum',
                'metric1': 'addresses/new_non_zero_count',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'New to active address ratio - measures adoption momentum'
            },
            {
                'name': '064_market_liquidity_stress',
                'metric1': 'supply/liquid_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Liquid supply response to market drawdowns'
            },
            {
                'name': '065_exchange_balance_momentum',
                'metric1': 'distribution/balance_exchanges',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Exchange balance impact on volatility'
            },
            {
                'name': '066_mining_network_share',
                'metric1': 'mining/revenue_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Mining revenue to network volume ratio'
            },
            {
                'name': '067_fee_transaction_ratio',
                'metric1': 'fees/volume_mean',
                'metric2': 'transactions/transfer_volume_mean',
                'operation': 'divide',
                'description': 'Average fee to transaction value ratio'
            },
            {
                'name': '068_holder_activity_impact',
                'metric1': 'addresses/active_count',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Active address response to market drawdowns'
            },
            {
                'name': '069_market_network_ratio',
                'metric1': 'market/marketcap_usd',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Market cap to transaction count ratio'
            },
            {
                'name': '070_exchange_flow_balance',
                'metric1': 'transactions/transfers_volume_to_exchanges_sum',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Exchange inflow to liquid supply ratio'
            },
            {
                'name': '071_mining_cost_efficiency',
                'metric1': 'mining/revenue_sum',
                'metric2': 'mining/difficulty_latest',
                'operation': 'divide',
                'description': 'Mining revenue to difficulty ratio'
            },
            {
                'name': '072_transaction_cost_impact',
                'metric1': 'fees/volume_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Fee volume response to market drawdowns'
            },
            {
                'name': '073_network_usage_value',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Volume per active address'
            },
            {
                'name': '074_market_momentum_indicator',
                'metric1': 'market/price_usd_close',
                'metric2': 'market/price_realized_usd',
                'operation': 'divide',
                'description': 'Market to realized price ratio momentum'
            },
            {
                'name': '075_exchange_dominance_ratio',
                'metric1': 'distribution/balance_exchanges',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Exchange balance to total supply ratio'
            },
            {
                'name': '076_mining_volume_efficiency',
                'metric1': 'mining/volume_mined',
                'metric2': 'mining/hash_rate_mean',
                'operation': 'divide',
                'description': 'Mined volume to hash rate ratio'
            },
            {
                'name': '077_fee_value_ratio',
                'metric1': 'fees/volume_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Fee volume to market cap ratio'
            },
            {
                'name': '078_holder_supply_ratio',
                'metric1': 'supply/illiquid_sum',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Illiquid to liquid supply distribution'
            },
            {
                'name': '079_network_value_indicator',
                'metric1': 'market/marketcap_usd',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Value per active address'
            },
            {
                'name': '080_exchange_activity_impact',
                'metric1': 'transactions/transfers_between_exchanges_count',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Exchange activity impact on volatility'
            },
            {
                'name': '081_mining_revenue_distribution',
                'metric1': 'mining/revenue_sum',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Mining revenue per coin'
            },
            {
                'name': '082_transaction_value_momentum',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Transaction volume response to drawdowns'
            },
            {
                'name': '083_network_growth_efficiency',
                'metric1': 'addresses/new_non_zero_count',
                'metric2': 'fees/volume_mean',
                'operation': 'divide',
                'description': 'Network growth to fee cost ratio'
            },
            {
                'name': '084_market_supply_momentum',
                'metric1': 'market/marketcap_usd',
                'metric2': 'supply/illiquid_change',
                'operation': 'multiply',
                'description': 'Market value response to supply changes'
            },
            {
                'name': '085_exchange_liquidity_flow',
                'metric1': 'transactions/transfers_volume_exchanges_net',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Net exchange flow to liquid supply ratio'
            },
            {
                'name': '086_mining_difficulty_stress',
                'metric1': 'mining/difficulty_latest',
                'metric2': 'mining/revenue_sum',
                'operation': 'divide',
                'description': 'Mining difficulty to revenue stress'
            },
            {
                'name': '087_fee_market_activity',
                'metric1': 'fees/volume_sum',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Fee volume per active address'
            },
            {
                'name': '088_holder_balance_impact',
                'metric1': 'supply/illiquid_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Illiquid supply impact on volatility'
            },
            {
                'name': '089_network_transaction_efficiency',
                'metric1': 'transactions/count',
                'metric2': 'transactions/size_mean',
                'operation': 'divide',
                'description': 'Transaction count to average size ratio'
            },
            {
                'name': '090_market_activity_ratio',
                'metric1': 'market/marketcap_usd',
                'metric2': 'transactions/size_sum',
                'operation': 'divide',
                'description': 'Market cap to transaction size ratio'
            },
            {
                'name': '091_exchange_volume_efficiency',
                'metric1': 'transactions/transfers_volume_between_exchanges_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Inter-exchange to total volume ratio'
            },
            {
                'name': '092_mining_hash_efficiency',
                'metric1': 'mining/hash_rate_mean',
                'metric2': 'mining/volume_mined',
                'operation': 'divide',
                'description': 'Hash rate to mined volume efficiency'
            },
            {
                'name': '093_fee_volume_impact',
                'metric1': 'fees/volume_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Fee volume impact on volatility'
            },
            {
                'name': '094_holder_distribution_momentum',
                'metric1': 'supply/illiquid_change',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Supply distribution change impact'
            },
            {
                'name': '095_network_value_momentum',
                'metric1': 'market/marketcap_usd',
                'metric2': 'transactions/transfer_volume_mean',
                'operation': 'divide',
                'description': 'Market value to transaction value momentum'
            },
            {
                'name': '096_exchange_balance_efficiency',
                'metric1': 'distribution/balance_exchanges',
                'metric2': 'transactions/transfers_volume_exchanges_net',
                'operation': 'divide',
                'description': 'Exchange balance to net flow efficiency'
            },
            {
                'name': '097_mining_market_ratio',
                'metric1': 'mining/revenue_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Mining revenue to market cap ratio'
            },
            {
                'name': '098_transaction_network_ratio',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Volume per transaction ratio'
            },
            {
                'name': '099_network_adoption_cost',
                'metric1': 'addresses/new_non_zero_count',
                'metric2': 'fees/volume_sum',
                'operation': 'divide',
                'description': 'Network adoption to fee cost ratio'
            },
            {
                'name': '100_market_realized_efficiency',
                'metric1': 'market/marketcap_realized_usd',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'divide',
                'description': 'Realized cap response to market drawdowns'
            },
            {
                'name': '101_derivatives_market_depth',
                'metric1': 'derivatives/futures_open_interest_sum',
                'metric2': 'market/spot_volume_daily_sum',
                'operation': 'divide',
                'description': 'Futures open interest to spot volume ratio - measures derivatives market depth'
            },
            {
                'name': '102_options_market_sentiment',
                'metric1': 'derivatives/options_volume_put_call_ratio',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Put-call ratio response to volatility - indicates market sentiment'
            },
            {
                'name': '103_futures_leverage_risk',
                'metric1': 'derivatives/futures_liquidated_volume_long_sum',
                'metric2': 'derivatives/futures_open_interest_sum',
                'operation': 'divide',
                'description': 'Liquidation to open interest ratio - measures leverage risk'
            },
            {
                'name': '104_perpetual_funding_stress',
                'metric1': 'derivatives/futures_funding_rate_perpetual',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Funding rate response to volatility - indicates market stress'
            },
            {
                'name': '105_futures_basis_pressure',
                'metric1': 'derivatives/futures_volume_daily_sum',
                'metric2': 'derivatives/futures_open_interest_sum',
                'operation': 'divide',
                'description': 'Futures volume to open interest ratio - measures trading pressure'
            },
            {
                'name': '106_options_market_depth',
                'metric1': 'derivatives/options_volume_daily_sum',
                'metric2': 'market/spot_volume_daily_sum',
                'operation': 'divide',
                'description': 'Options to spot volume ratio - indicates derivatives market depth'
            },
            {
                'name': '107_futures_dominance_ratio',
                'metric1': 'derivatives/futures_volume_daily_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Futures to on-chain volume ratio - measures derivatives dominance'
            },
            {
                'name': '108_liquidation_impact_ratio',
                'metric1': 'derivatives/futures_liquidated_volume_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Liquidation volume impact on market drawdowns'
            },
            {
                'name': '109_perpetual_volume_dominance',
                'metric1': 'derivatives/futures_volume_daily_perpetual_sum',
                'metric2': 'derivatives/futures_volume_daily_sum',
                'operation': 'divide',
                'description': 'Perpetual to total futures volume ratio'
            },
            {
                'name': '110_options_risk_premium',
                'metric1': 'derivatives/options_volume_put_call_ratio',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Put-call ratio response to market drawdowns'
            },
            {
                'name': '111_institutional_flow_impact',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Large transaction impact on volatility'
            },
            {
                'name': '112_whale_balance_ratio',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Top holder balance to total supply ratio'
            },
            {
                'name': '113_exchange_whale_activity',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'transactions/transfers_volume_to_exchanges_sum',
                'operation': 'divide',
                'description': 'Large exchange transfers to total exchange inflow ratio'
            },
            {
                'name': '114_institutional_holding_pressure',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Large holder response to market drawdowns'
            },
            {
                'name': '115_whale_transaction_impact',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Large transaction to total volume ratio'
            },
            {
                'name': '116_supply_shock_ratio',
                'metric1': 'supply/illiquid_sum',
                'metric2': 'distribution/balance_exchanges',
                'operation': 'divide',
                'description': 'Illiquid supply to exchange balance ratio'
            },
            {
                'name': '117_miner_outflow_ratio',
                'metric1': 'transactions/transfers_volume_miners_to_exchanges',
                'metric2': 'mining/volume_mined',
                'operation': 'divide',
                'description': 'Miner exchange transfers to mined volume ratio'
            },
            {
                'name': '118_stablecoin_supply_ratio',
                'metric1': 'transactions/transfer_volume_sum',
                'metric2': 'market/marketcap_realized_usd',
                'operation': 'divide',
                'description': 'Network volume to realized cap ratio'
            },
            {
                'name': '119_exchange_concentration_risk',
                'metric1': 'distribution/balance_exchanges',
                'metric2': 'supply/illiquid_sum',
                'operation': 'divide',
                'description': 'Exchange balance to illiquid supply ratio'
            },
            {
                'name': '120_institutional_accumulation',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Large transaction volume to price ratio'
            },
            {
                'name': '121_utxo_profit_pressure',
                'metric1': 'blockchain/utxo_profit_count',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Profitable UTXO response to market drawdowns'
            },
            {
                'name': '122_realized_cap_momentum',
                'metric1': 'market/marketcap_realized_usd',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Realized to market cap ratio momentum'
            },
            {
                'name': '123_lightning_network_growth',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Lightning capacity to on-chain volume ratio'
            },
            {
                'name': '124_mempool_congestion',
                'metric1': 'mempool/fees_sum',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Mempool fees to transaction count ratio'
            },
            {
                'name': '125_utxo_spending_pattern',
                'metric1': 'blockchain/utxo_spent_value_sum',
                'metric2': 'blockchain/utxo_created_value_sum',
                'operation': 'divide',
                'description': 'UTXO spending to creation ratio'
            },
            {
                'name': '126_lightning_adoption_rate',
                'metric1': 'lightning/nodes_count',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Lightning nodes to active addresses ratio - measures L2 adoption'
            },
            {
                'name': '127_utxo_age_momentum',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/utxo_spent_value_mean',
                'operation': 'divide',
                'description': 'UTXO creation to average spending ratio'
            },
            {
                'name': '128_mempool_value_density',
                'metric1': 'mempool/txs_value_sum',
                'metric2': 'mempool/txs_count_sum',
                'operation': 'divide',
                'description': 'Average value per mempool transaction'
            },
            {
                'name': '129_futures_leverage_density',
                'metric1': 'derivatives/futures_open_interest_sum',
                'metric2': 'derivatives/futures_volume_daily_sum',
                'operation': 'divide',
                'description': 'Open interest to daily volume ratio'
            },
            {
                'name': '130_options_market_leverage',
                'metric1': 'derivatives/options_open_interest_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Options open interest to market cap ratio'
            },
            {
                'name': '131_realized_loss_stress',
                'metric1': 'indicators/realized_loss',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Realized loss response to market drawdowns'
            },
            {
                'name': '132_sopr_momentum',
                'metric1': 'indicators/sopr',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'SOPR to volatility ratio - profit-taking momentum'
            },
            {
                'name': '133_exchange_efficacy',
                'metric1': 'transactions/transfers_volume_between_exchanges_sum',
                'metric2': 'distribution/balance_exchanges',
                'operation': 'divide',
                'description': 'Inter-exchange volume to total exchange balance'
            },
            {
                'name': '134_lightning_channel_efficiency',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/channels_count',
                'operation': 'divide',
                'description': 'Average lightning channel capacity'
            },
            {
                'name': '135_futures_basis_impact',
                'metric1': 'derivatives/futures_volume_daily_perpetual_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Perpetual volume impact on volatility'
            },
            {
                'name': '136_realized_cap_efficiency',
                'metric1': 'market/marketcap_realized_usd',
                'metric2': 'indicators/realized_loss',
                'operation': 'divide',
                'description': 'Realized cap to realized loss ratio'
            },
            {
                'name': '137_mempool_fee_pressure',
                'metric1': 'mempool/fees_median_relative',
                'metric2': 'transactions/count',
                'operation': 'multiply',
                'description': 'Median fee pressure on transaction activity'
            },
            {
                'name': '138_utxo_value_density',
                'metric1': 'blockchain/utxo_created_value_mean',
                'metric2': 'blockchain/utxo_count',
                'operation': 'divide',
                'description': 'Average value per UTXO'
            },
            {
                'name': '139_options_risk_ratio',
                'metric1': 'derivatives/options_volume_put_call_ratio',
                'metric2': 'market/mvrv',
                'operation': 'multiply',
                'description': 'Put-call ratio response to market value'
            },
            {
                'name': '140_lightning_network_density',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/nodes_count',
                'operation': 'divide',
                'description': 'Average capacity per lightning node'
            },
            {
                'name': '141_futures_funding_impact',
                'metric1': 'derivatives/futures_funding_rate_perpetual',
                'metric2': 'derivatives/futures_open_interest_sum',
                'operation': 'multiply',
                'description': 'Funding rate impact on open interest'
            },
            {
                'name': '142_realized_profit_momentum',
                'metric1': 'indicators/realized_profit',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Realized profit to volatility ratio'
            },
            {
                'name': '143_mempool_size_pressure',
                'metric1': 'mempool/txs_size_sum',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Mempool to block size ratio'
            },
            {
                'name': '144_options_market_pressure',
                'metric1': 'derivatives/options_volume_daily_sum',
                'metric2': 'derivatives/futures_volume_daily_sum',
                'operation': 'divide',
                'description': 'Options to futures volume ratio'
            },
            {
                'name': '145_utxo_creation_momentum',
                'metric1': 'blockchain/utxo_created_count',
                'metric2': 'blockchain/utxo_spent_count',
                'operation': 'divide',
                'description': 'UTXO creation to spending ratio'
            },
            {
                'name': '146_lightning_fee_efficiency',
                'metric1': 'lightning/base_fee_median',
                'metric2': 'fees/volume_mean',
                'operation': 'divide',
                'description': 'Lightning to on-chain fee ratio'
            },
            {
                'name': '147_futures_volume_impact',
                'metric1': 'derivatives/futures_volume_buy_sum',
                'metric2': 'derivatives/futures_volume_sell_sum',
                'operation': 'divide',
                'description': 'Buy to sell volume ratio in futures'
            },
            {
                'name': '148_realized_value_stress',
                'metric1': 'market/price_realized_usd',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Realized price response to drawdowns'
            },
            {
                'name': '149_mempool_congestion_impact',
                'metric1': 'mempool/fees_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'multiply',
                'description': 'Mempool fee impact on volatility'
            },
            {
                'name': '150_options_leverage_risk',
                'metric1': 'derivatives/options_open_interest_sum',
                'metric2': 'derivatives/options_volume_daily_sum',
                'operation': 'divide',
                'description': 'Options open interest to volume ratio'
            },
            {
                'name': '151_lightning_node_efficiency',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/node_connectivity',
                'operation': 'divide',
                'description': 'Network capacity to connectivity ratio'
            },
            {
                'name': '152_futures_liquidation_risk',
                'metric1': 'derivatives/futures_liquidated_volume_long_sum',
                'metric2': 'derivatives/futures_liquidated_volume_short_sum',
                'operation': 'divide',
                'description': 'Long to short liquidation ratio'
            },
            {
                'name': '153_utxo_profit_momentum',
                'metric1': 'blockchain/utxo_profit_count',
                'metric2': 'blockchain/utxo_loss_count',
                'operation': 'divide',
                'description': 'Profitable to unprofitable UTXO ratio'
            },
            {
                'name': '154_mempool_value_efficiency',
                'metric1': 'mempool/txs_value_sum',
                'metric2': 'mempool/fees_sum',
                'operation': 'divide',
                'description': 'Transaction value to fee ratio in mempool'
            },
            {
                'name': '155_options_market_balance',
                'metric1': 'derivatives/options_volume_daily_sum',
                'metric2': 'market/spot_volume_daily_sum',
                'operation': 'divide',
                'description': 'Options to spot volume ratio'
            },
            {
                'name': '156_realized_profit_efficiency',
                'metric1': 'indicators/realized_profit',
                'metric2': 'indicators/realized_loss',
                'operation': 'divide',
                'description': 'Realized profit to loss ratio'
            },
            {
                'name': '157_lightning_channel_distribution',
                'metric1': 'lightning/channels_count',
                'metric2': 'lightning/nodes_count',
                'operation': 'divide',
                'description': 'Average channels per node'
            },
            {
                'name': '158_futures_market_stress',
                'metric1': 'derivatives/futures_liquidated_volume_sum',
                'metric2': 'derivatives/futures_volume_daily_sum',
                'operation': 'divide',
                'description': 'Liquidation to trading volume ratio'
            },
            {
                'name': '159_utxo_spending_efficiency',
                'metric1': 'blockchain/utxo_spent_value_mean',
                'metric2': 'blockchain/utxo_created_value_mean',
                'operation': 'divide',
                'description': 'Spent to created UTXO value ratio'
            },
            {
                'name': '160_mempool_transaction_pressure',
                'metric1': 'mempool/txs_count_sum',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Mempool to confirmed transaction ratio'
            },
            {
                'name': '161_options_risk_sentiment',
                'metric1': 'derivatives/options_volume_put_call_ratio',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Put-call ratio response to drawdowns'
            },
            {
                'name': '162_lightning_capacity_growth',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Lightning capacity to market cap ratio'
            },
            {
                'name': '163_futures_basis_efficiency',
                'metric1': 'derivatives/futures_volume_daily_sum',
                'metric2': 'market/spot_volume_daily_sum',
                'operation': 'divide',
                'description': 'Futures to spot volume efficiency'
            },
            {
                'name': '164_utxo_age_distribution',
                'metric1': 'blockchain/utxo_created_count',
                'metric2': 'blockchain/utxo_count',
                'operation': 'divide',
                'description': 'New to total UTXO ratio'
            },
            {
                'name': '165_mempool_fee_efficiency',
                'metric1': 'mempool/fees_median_relative',
                'metric2': 'fees/volume_mean',
                'operation': 'divide',
                'description': 'Mempool to confirmed fee ratio'
            },
            {
                'name': '166_realized_cap_momentum',
                'metric1': 'market/marketcap_realized_usd',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Realized cap response to volatility'
            },
            {
                'name': '167_lightning_network_growth',
                'metric1': 'lightning/nodes_count',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Node growth relative to volatility'
            },
            {
                'name': '168_futures_leverage_impact',
                'metric1': 'derivatives/futures_open_interest_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Open interest response to drawdowns'
            },
            {
                'name': '169_utxo_value_momentum',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'UTXO creation value to volatility ratio'
            },
            {
                'name': '170_mempool_size_efficiency',
                'metric1': 'mempool/txs_size_sum',
                'metric2': 'transactions/size_sum',
                'operation': 'divide',
                'description': 'Mempool to confirmed transaction size ratio'
            },
            {
                'name': '171_options_market_momentum',
                'metric1': 'derivatives/options_volume_daily_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Options volume response to volatility'
            },
            {
                'name': '172_lightning_fee_pressure',
                'metric1': 'lightning/fee_rate_median',
                'metric2': 'lightning/channel_size_mean',
                'operation': 'divide',
                'description': 'Lightning fee to channel size ratio'
            },
            {
                'name': '173_futures_market_momentum',
                'metric1': 'derivatives/futures_volume_perpetual_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Perpetual volume response to drawdowns'
            },
            {
                'name': '174_utxo_efficiency_ratio',
                'metric1': 'blockchain/utxo_spent_value_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'UTXO spending to transaction volume ratio'
            },
            {
                'name': '175_mempool_value_momentum',
                'metric1': 'mempool/txs_value_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Mempool value response to volatility'
            },
            {
                'name': '176_options_leverage_momentum',
                'metric1': 'derivatives/options_open_interest_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Options open interest response to drawdowns'
            },
            {
                'name': '177_lightning_network_efficiency',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/fee_rate_median',
                'operation': 'divide',
                'description': 'Network capacity to fee rate ratio'
            },
            {
                'name': '178_futures_funding_efficiency',
                'metric1': 'derivatives/futures_funding_rate_perpetual',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Funding rate to volatility ratio'
            },
            {
                'name': '179_utxo_creation_pressure',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'UTXO creation value to block size ratio'
            },
            {
                'name': '180_mempool_congestion_ratio',
                'metric1': 'mempool/txs_count_sum',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Mempool transactions to block count ratio'
            },
            {
                'name': '181_options_market_efficiency',
                'metric1': 'derivatives/options_volume_daily_sum',
                'metric2': 'derivatives/options_open_interest_sum',
                'operation': 'divide',
                'description': 'Options volume to open interest ratio'
            },
            {
                'name': '182_lightning_connectivity_efficiency',
                'metric1': 'lightning/node_connectivity',
                'metric2': 'lightning/channels_count',
                'operation': 'divide',
                'description': 'Node connectivity to channel count ratio'
            },
            {
                'name': '183_futures_volume_efficiency',
                'metric1': 'derivatives/futures_volume_buy_perpetual_sum',
                'metric2': 'derivatives/futures_volume_sell_perpetual_sum',
                'operation': 'divide',
                'description': 'Perpetual buy to sell volume ratio'
            },
            {
                'name': '184_utxo_profit_efficiency',
                'metric1': 'blockchain/utxo_profit_count',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Profitable UTXO response to volatility'
            },
            {
                'name': '185_mempool_fee_momentum',
                'metric1': 'mempool/fees_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Mempool fee response to drawdowns'
            },
            {
                'name': '186_options_risk_efficiency',
                'metric1': 'derivatives/options_volume_put_call_ratio',
                'metric2': 'derivatives/futures_liquidated_volume_sum',
                'operation': 'multiply',
                'description': 'Options risk to futures liquidation ratio'
            },
            {
                'name': '187_lightning_capacity_efficiency',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Lightning to on-chain capacity ratio'
            },
            {
                'name': '188_futures_risk_ratio',
                'metric1': 'derivatives/futures_liquidated_volume_sum',
                'metric2': 'market/spot_volume_daily_sum',
                'operation': 'divide',
                'description': 'Futures liquidation to spot volume ratio'
            },
            {
                'name': '189_utxo_age_efficiency',
                'metric1': 'blockchain/utxo_spent_count',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'UTXO spending to transaction count ratio'
            },
            {
                'name': '190_mempool_size_momentum',
                'metric1': 'mempool/txs_size_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Mempool size response to volatility'
            },
            {
                'name': '191_options_market_strength',
                'metric1': 'derivatives/options_open_interest_sum',
                'metric2': 'derivatives/futures_open_interest_sum',
                'operation': 'divide',
                'description': 'Options to futures open interest ratio'
            },
            {
                'name': '192_lightning_growth_efficiency',
                'metric1': 'lightning/nodes_count',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Lightning adoption to network activity ratio'
            },
            {
                'name': '193_futures_basis_momentum',
                'metric1': 'derivatives/futures_volume_daily_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Futures volume response to drawdowns'
            },
            {
                'name': '194_utxo_value_distribution',
                'metric1': 'blockchain/utxo_created_value_mean',
                'metric2': 'blockchain/utxo_spent_value_mean',
                'operation': 'divide',
                'description': 'Created to spent UTXO value ratio'
            },
            {
                'name': '195_mempool_efficiency_ratio',
                'metric1': 'mempool/txs_value_sum',
                'metric2': 'mempool/txs_size_sum',
                'operation': 'divide',
                'description': 'Mempool value to size efficiency'
            },
            {
                'name': '196_options_volume_impact',
                'metric1': 'derivatives/options_volume_daily_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Options volume response to drawdowns'
            },
            {
                'name': '197_lightning_channel_momentum',
                'metric1': 'lightning/channels_count',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'Channel growth response to volatility'
            },
            {
                'name': '198_futures_leverage_distribution',
                'metric1': 'derivatives/futures_open_interest_sum',
                'metric2': 'derivatives/futures_liquidated_volume_sum',
                'operation': 'divide',
                'description': 'Open interest to liquidation volume ratio'
            },
            {
                'name': '199_utxo_spending_momentum',
                'metric1': 'blockchain/utxo_spent_value_sum',
                'metric2': 'market/price_volatility_1_month',
                'operation': 'divide',
                'description': 'UTXO spending response to volatility'
            },
            {
                'name': '200_mempool_transaction_momentum',
                'metric1': 'mempool/txs_count_sum',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Mempool transaction response to drawdowns'
            },
            {
                'name': '201_price_momentum_quality',
                'metric1': 'market/price_usd_close',
                'metric2': 'market/price_usd_ohlc_close',
                'operation': 'divide',
                'description': 'Price momentum quality - measures closing price consistency'
            },
            {
                'name': '202_block_value_density',
                'metric1': 'blockchain/block_volume_sum',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Value density per block - indicates transaction efficiency'
            },
            {
                'name': '203_fee_urgency_ratio',
                'metric1': 'fees/fee_ratio_multiple',
                'metric2': 'fees/gas_price_median',
                'operation': 'divide',
                'description': 'Fee urgency indicator - measures transaction priority levels'
            },
            {
                'name': '204_market_depth_impact',
                'metric1': 'market/price_usd_close',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Price to market cap ratio - indicates market depth'
            },
            {
                'name': '205_block_interval_efficiency',
                'metric1': 'blockchain/block_interval_mean',
                'metric2': 'mining/difficulty_latest',
                'operation': 'divide',
                'description': 'Block timing efficiency relative to difficulty'
            },
            {
                'name': '206_realized_momentum_strength',
                'metric1': 'market/price_realized_usd',
                'metric2': 'market/mvrv_ratio',
                'operation': 'multiply',
                'description': 'Realized price momentum relative to market value'
            },
            {
                'name': '207_mining_revenue_impact',
                'metric1': 'mining/revenue_from_fees',
                'metric2': 'mining/revenue_sum',
                'operation': 'divide',
                'description': 'Fee contribution to mining revenue'
            },
            {
                'name': '208_exchange_flow_strength',
                'metric1': 'distribution/exchange_net_position_change',
                'metric2': 'market/price_usd_close',
                'operation': 'multiply',
                'description': 'Exchange flow impact on price'
            },
            {
                'name': '209_hashrate_efficiency_ratio',
                'metric1': 'mining/hash_rate_mean',
                'metric2': 'mining/difficulty_latest',
                'operation': 'divide',
                'description': 'Mining efficiency relative to network difficulty'
            },
            {
                'name': '210_supply_activity_ratio',
                'metric1': 'supply/active_24h',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Active supply participation rate'
            },
            {
                'name': '211_fee_value_density',
                'metric1': 'fees/volume_mean',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Fee density per block size'
            },
            {
                'name': '212_market_liquidity_flow',
                'metric1': 'market/marketcap_realized_usd',
                'metric2': 'distribution/balance_exchanges_all',
                'operation': 'divide',
                'description': 'Market liquidity relative to exchange holdings'
            },
            {
                'name': '213_mining_difficulty_impact',
                'metric1': 'mining/difficulty_latest',
                'metric2': 'mining/revenue_from_fees',
                'operation': 'divide',
                'description': 'Difficulty impact on fee revenue'
            },
            {
                'name': '214_exchange_concentration',
                'metric1': 'distribution/balance_exchanges_all',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Exchange balance concentration'
            },
            {
                'name': '215_block_efficiency_ratio',
                'metric1': 'blockchain/block_volume_sum',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Block processing efficiency'
            },
            {
                'name': '216_market_value_efficiency',
                'metric1': 'market/mvrv_ratio',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'divide',
                'description': 'Market value efficiency during drawdowns'
            },
            {
                'name': '217_mining_profitability_stress',
                'metric1': 'mining/revenue_sum',
                'metric2': 'mining/difficulty_latest',
                'operation': 'divide',
                'description': 'Mining profitability under difficulty pressure'
            },
            {
                'name': '218_supply_distribution_health',
                'metric1': 'supply/profit_relative',
                'metric2': 'supply/active_24h',
                'operation': 'divide',
                'description': 'Profitable supply activation rate'
            },
            {
                'name': '219_fee_market_equilibrium',
                'metric1': 'fees/fee_ratio_multiple',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'multiply',
                'description': 'Fee market balance relative to block timing'
            },
            {
                'name': '220_exchange_volume_impact',
                'metric1': 'distribution/exchange_net_position_change',
                'metric2': 'market/marketcap_realized_usd',
                'operation': 'divide',
                'description': 'Exchange flow impact on realized value'
            },
            {
                'name': '221_hashrate_reward_efficiency',
                'metric1': 'mining/hash_rate_mean',
                'metric2': 'mining/revenue_sum',
                'operation': 'divide',
                'description': 'Mining efficiency per revenue unit'
            },
            {
                'name': '222_market_depth_ratio',
                'metric1': 'market/price_usd_close',
                'metric2': 'distribution/balance_exchanges_all',
                'operation': 'divide',
                'description': 'Price to exchange liquidity ratio'
            },
            {
                'name': '223_block_size_utilization',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Block space utilization efficiency'
            },
            {
                'name': '224_supply_profit_momentum',
                'metric1': 'supply/profit_relative',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'divide',
                'description': 'Supply profitability during market stress'
            },
            {
                'name': '225_mining_revenue_stability',
                'metric1': 'mining/revenue_sum',
                'metric2': 'mining/revenue_from_fees',
                'operation': 'divide',
                'description': 'Mining revenue composition stability'
            },
            {
                'name': '226_exchange_balance_pressure',
                'metric1': 'distribution/exchange_net_position_change',
                'metric2': 'supply/active_24h',
                'operation': 'divide',
                'description': 'Exchange flow relative to active supply'
            },
            {
                'name': '227_fee_velocity_ratio',
                'metric1': 'fees/volume_mean',
                'metric2': 'fees/fee_ratio_multiple',
                'operation': 'multiply',
                'description': 'Fee market velocity indicator'
            },
            {
                'name': '228_market_realized_spread',
                'metric1': 'market/price_usd_close',
                'metric2': 'market/price_realized_usd',
                'operation': 'divide',
                'description': 'Market to realized price spread'
            },
            {
                'name': '229_block_reward_efficiency',
                'metric1': 'mining/revenue_sum',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'multiply',
                'description': 'Block reward efficiency metric'
            },
            {
                'name': '230_supply_activation_ratio',
                'metric1': 'supply/active_24h',
                'metric2': 'supply/profit_relative',
                'operation': 'divide',
                'description': 'Supply activation relative to profitability'
            },
            {
                'name': '231_exchange_liquidity_ratio',
                'metric1': 'distribution/balance_exchanges_all',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Exchange liquidity to market value ratio'
            },
            {
                'name': '232_mining_efficiency_score',
                'metric1': 'mining/hash_rate_mean',
                'metric2': 'mining/revenue_from_fees',
                'operation': 'divide',
                'description': 'Mining efficiency relative to fee revenue'
            },
            {
                'name': '233_market_stress_indicator',
                'metric1': 'market/price_drawdown_relative',
                'metric2': 'market/mvrv_ratio',
                'operation': 'multiply',
                'description': 'Market stress relative to value ratio'
            },
            {
                'name': '234_block_space_demand',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'fees/volume_mean',
                'operation': 'multiply',
                'description': 'Block space demand pressure'
            },
            {
                'name': '235_supply_distribution_metric',
                'metric1': 'supply/profit_relative',
                'metric2': 'distribution/balance_exchanges_all',
                'operation': 'divide',
                'description': 'Supply distribution relative to exchange balance'
            },
            {
                'name': '236_fee_market_pressure',
                'metric1': 'fees/fee_ratio_multiple',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Fee market pressure during drawdowns'
            },
            {
                'name': '237_hashrate_difficulty_balance',
                'metric1': 'mining/hash_rate_mean',
                'metric2': 'mining/difficulty_latest',
                'operation': 'divide',
                'description': 'Mining power to difficulty balance'
            },
            {
                'name': '238_market_liquidity_score',
                'metric1': 'market/marketcap_realized_usd',
                'metric2': 'supply/active_24h',
                'operation': 'divide',
                'description': 'Market liquidity relative to active supply'
            },
            {
                'name': '239_block_efficiency_metric',
                'metric1': 'blockchain/block_volume_sum',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Block efficiency in value transfer'
            },
            {
                'name': '240_exchange_flow_momentum',
                'metric1': 'distribution/exchange_net_position_change',
                'metric2': 'market/mvrv_ratio',
                'operation': 'multiply',
                'description': 'Exchange flow impact on market value'
            },
            {
                'name': '241_mining_revenue_ratio',
                'metric1': 'mining/revenue_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Mining revenue to market value ratio'
            },
            {
                'name': '242_supply_velocity_metric',
                'metric1': 'supply/active_24h',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'divide',
                'description': 'Supply velocity during market stress'
            },
            {
                'name': '243_fee_equilibrium_ratio',
                'metric1': 'fees/volume_mean',
                'metric2': 'mining/revenue_from_fees',
                'operation': 'divide',
                'description': 'Fee market equilibrium indicator'
            },
            {
                'name': '244_market_depth_indicator',
                'metric1': 'market/price_usd_close',
                'metric2': 'distribution/exchange_net_position_change',
                'operation': 'divide',
                'description': 'Market depth relative to exchange flows'
            },
            {
                'name': '245_block_creation_efficiency',
                'metric1': 'blockchain/block_interval_mean',
                'metric2': 'mining/hash_rate_mean',
                'operation': 'divide',
                'description': 'Block creation efficiency metric'
            },
            {
                'name': '246_supply_profit_ratio',
                'metric1': 'supply/profit_relative',
                'metric2': 'market/mvrv_ratio',
                'operation': 'divide',
                'description': 'Supply profitability to market value ratio'
            },
            {
                'name': '247_exchange_balance_momentum',
                'metric1': 'distribution/balance_exchanges_all',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'multiply',
                'description': 'Exchange balance impact during drawdowns'
            },
            {
                'name': '248_mining_difficulty_stress',
                'metric1': 'mining/difficulty_latest',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Mining difficulty relative to price'
            },
            {
                'name': '249_market_efficiency_ratio',
                'metric1': 'market/marketcap_realized_usd',
                'metric2': 'market/price_drawdown_relative',
                'operation': 'divide',
                'description': 'Market efficiency during drawdowns'
            },
            {
                'name': '250_block_value_ratio',
                'metric1': 'blockchain/block_volume_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Block value to market cap ratio'
            },
            {
                'name': '251_active_wallet_momentum',
                'metric1': 'addresses/active_count',
                'metric2': 'addresses/sending_count',
                'operation': 'divide',
                'description': 'Active to sending address ratio - network activity quality'
            },
            {
                'name': '252_transaction_size_efficiency',
                'metric1': 'blockchain/block_height',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Block height to size ratio - blockchain efficiency'
            },
            {
                'name': '253_network_usage_density',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'multiply',
                'description': 'Block production density'
            },
            {
                'name': '254_address_balance_distribution',
                'metric1': 'addresses/min_point_zero_1_count',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Small holder to active address ratio'
            },
            {
                'name': '255_blockchain_growth_rate',
                'metric1': 'blockchain/block_height',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Blockchain growth efficiency'
            },
            {
                'name': '256_network_adoption_rate',
                'metric1': 'addresses/new_non_zero_count',
                'metric2': 'addresses/sending_count',
                'operation': 'divide',
                'description': 'New address adoption rate'
            },
            {
                'name': '257_block_time_consistency',
                'metric1': 'blockchain/block_interval_mean',
                'metric2': 'blockchain/block_interval_median',
                'operation': 'divide',
                'description': 'Block timing consistency ratio'
            },
            {
                'name': '258_active_supply_ratio',
                'metric1': 'supply/active_more_1y_percent',
                'metric2': 'supply/active_24h',
                'operation': 'divide',
                'description': 'Long-term to active supply ratio'
            },
            {
                'name': '259_transaction_confirmation_efficiency',
                'metric1': 'blockchain/block_count',
                'metric2': 'mempool/transactions_count',
                'operation': 'divide',
                'description': 'Transaction confirmation efficiency'
            },
            {
                'name': '260_address_activity_concentration',
                'metric1': 'addresses/sending_count',
                'metric2': 'addresses/receiving_count',
                'operation': 'divide',
                'description': 'Sending to receiving address ratio'
            },
            {
                'name': '261_network_load_distribution',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'mempool/size_bytes',
                'operation': 'divide',
                'description': 'Network load distribution efficiency'
            },
            {
                'name': '262_utxo_creation_rate',
                'metric1': 'blockchain/utxo_created_count',
                'metric2': 'blockchain/utxo_spent_count',
                'operation': 'divide',
                'description': 'UTXO creation to spending ratio'
            },
            {
                'name': '263_address_balance_momentum',
                'metric1': 'addresses/min_1_count',
                'metric2': 'addresses/non_zero_count',
                'operation': 'divide',
                'description': 'Significant holder ratio trend'
            },
            {
                'name': '264_network_congestion_indicator',
                'metric1': 'mempool/transactions_count',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'multiply',
                'description': 'Network congestion level'
            },
            {
                'name': '265_blockchain_utilization_rate',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_weight_mean',
                'operation': 'divide',
                'description': 'Block space utilization efficiency'
            },
            {
                'name': '266_active_address_velocity',
                'metric1': 'addresses/active_count',
                'metric2': 'addresses/new_non_zero_count',
                'operation': 'divide',
                'description': 'Address activation velocity'
            },
            {
                'name': '267_transaction_processing_efficiency',
                'metric1': 'blockchain/block_count',
                'metric2': 'mempool/size_bytes',
                'operation': 'divide',
                'description': 'Transaction processing efficiency'
            },
            {
                'name': '268_utxo_age_distribution',
                'metric1': 'blockchain/utxo_created_value_mean',
                'metric2': 'blockchain/utxo_spent_value_mean',
                'operation': 'divide',
                'description': 'UTXO age distribution pattern'
            },
            {
                'name': '269_network_health_indicator',
                'metric1': 'blockchain/block_height',
                'metric2': 'mempool/transactions_count',
                'operation': 'divide',
                'description': 'Overall network health metric'
            },
            {
                'name': '270_address_distribution_quality',
                'metric1': 'addresses/min_1_count',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Address distribution quality'
            },
            {
                'name': '271_block_space_efficiency',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Block space usage efficiency'
            },
            {
                'name': '272_network_participation_rate',
                'metric1': 'addresses/active_count',
                'metric2': 'addresses/non_zero_count',
                'operation': 'divide',
                'description': 'Network participation rate'
            },
            {
                'name': '273_mempool_clearance_rate',
                'metric1': 'mempool/transactions_count',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Mempool clearance efficiency'
            },
            {
                'name': '274_utxo_value_distribution',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/utxo_created_count',
                'operation': 'divide',
                'description': 'Average UTXO value creation'
            },
            {
                'name': '275_blockchain_growth_efficiency',
                'metric1': 'blockchain/block_height',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Blockchain growth efficiency'
            },
            {
                'name': '276_active_address_distribution',
                'metric1': 'addresses/sending_count',
                'metric2': 'addresses/non_zero_count',
                'operation': 'divide',
                'description': 'Active address distribution'
            },
            {
                'name': '277_network_load_balance',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_weight_mean',
                'operation': 'divide',
                'description': 'Network load balance indicator'
            },
            {
                'name': '278_transaction_validation_rate',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Transaction validation efficiency'
            },
            {
                'name': '279_utxo_spending_pattern',
                'metric1': 'blockchain/utxo_spent_value_sum',
                'metric2': 'blockchain/utxo_spent_count',
                'operation': 'divide',
                'description': 'Average UTXO spending pattern'
            },
            {
                'name': '280_address_activity_pattern',
                'metric1': 'addresses/active_count',
                'metric2': 'addresses/min_point_zero_1_count',
                'operation': 'divide',
                'description': 'Address activity distribution'
            },
            {
                'name': '281_blockchain_capacity_utilization',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'mempool/size_bytes',
                'operation': 'divide',
                'description': 'Blockchain capacity usage'
            },
            {
                'name': '282_network_density_metric',
                'metric1': 'addresses/active_count',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Network usage density'
            },
            {
                'name': '283_mempool_growth_rate',
                'metric1': 'mempool/size_bytes',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Mempool growth dynamics'
            },
            {
                'name': '284_utxo_efficiency_ratio',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/utxo_spent_value_sum',
                'operation': 'divide',
                'description': 'UTXO creation efficiency'
            },
            {
                'name': '285_block_propagation_efficiency',
                'metric1': 'blockchain/block_interval_mean',
                'metric2': 'blockchain/block_interval_median',
                'operation': 'divide',
                'description': 'Block propagation efficiency'
            },
            {
                'name': '286_address_balance_activity',
                'metric1': 'addresses/min_1_count',
                'metric2': 'addresses/sending_count',
                'operation': 'divide',
                'description': 'Address balance activity ratio'
            },
            {
                'name': '287_network_stress_indicator',
                'metric1': 'mempool/transactions_count',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Network stress level'
            },
            {
                'name': '288_blockchain_efficiency_score',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_weight_mean',
                'operation': 'divide',
                'description': 'Blockchain efficiency metric'
            },
            {
                'name': '289_utxo_lifecycle_pattern',
                'metric1': 'blockchain/utxo_created_count',
                'metric2': 'blockchain/utxo_created_value_mean',
                'operation': 'divide',
                'description': 'UTXO lifecycle efficiency'
            },
            {
                'name': '290_address_utilization_ratio',
                'metric1': 'addresses/active_count',
                'metric2': 'addresses/min_1_count',
                'operation': 'divide',
                'description': 'Address utilization efficiency'
            },
            {
                'name': '291_network_confirmation_rate',
                'metric1': 'blockchain/block_count',
                'metric2': 'mempool/size_bytes',
                'operation': 'divide',
                'description': 'Transaction confirmation rate'
            },
            {
                'name': '292_blockchain_growth_pattern',
                'metric1': 'blockchain/block_height',
                'metric2': 'blockchain/block_weight_mean',
                'operation': 'divide',
                'description': 'Blockchain growth pattern'
            },
            {
                'name': '293_mempool_efficiency_ratio',
                'metric1': 'mempool/transactions_count',
                'metric2': 'mempool/size_bytes',
                'operation': 'divide',
                'description': 'Mempool processing efficiency'
            },
            {
                'name': '294_utxo_distribution_metric',
                'metric1': 'blockchain/utxo_created_value_mean',
                'metric2': 'blockchain/utxo_created_count',
                'operation': 'divide',
                'description': 'UTXO value distribution'
            },
            {
                'name': '295_network_usage_pattern',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Network usage efficiency'
            },
            {
                'name': '296_address_activity_efficiency',
                'metric1': 'addresses/sending_count',
                'metric2': 'addresses/min_point_zero_1_count',
                'operation': 'divide',
                'description': 'Address activity efficiency'
            },
            {
                'name': '297_blockchain_load_distribution',
                'metric1': 'blockchain/block_weight_mean',
                'metric2': 'mempool/size_bytes',
                'operation': 'divide',
                'description': 'Blockchain load distribution'
            },
            {
                'name': '298_utxo_turnover_rate',
                'metric1': 'blockchain/utxo_spent_count',
                'metric2': 'blockchain/utxo_created_count',
                'operation': 'divide',
                'description': 'UTXO turnover efficiency'
            },
            {
                'name': '299_network_capacity_metric',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Network capacity utilization'
            },
            {
                'name': '300_address_growth_quality',
                'metric1': 'addresses/new_non_zero_count',
                'metric2': 'addresses/min_1_count',
                'operation': 'divide',
                'description': 'Address growth quality metric'
            },
            {
                'name': '301_futures_open_dominance',
                'metric1': 'derivatives/futures_open_interest_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Futures open interest relative to market cap'
            },
            {
                'name': '302_options_risk_ratio',
                'metric1': 'derivatives/options_volume_puts_sum',
                'metric2': 'derivatives/options_volume_calls_sum',
                'operation': 'divide',
                'description': 'Put-call volume ratio indicator'
            },
            {
                'name': '303_perpetual_funding_pressure',
                'metric1': 'derivatives/futures_funding_rate_perpetual',
                'metric2': 'market/price_usd_close',
                'operation': 'multiply',
                'description': 'Perpetual funding rate impact'
            },
            {
                'name': '304_futures_leverage_density',
                'metric1': 'derivatives/futures_liquidated_volume_sum',
                'metric2': 'derivatives/futures_open_interest_sum',
                'operation': 'divide',
                'description': 'Leverage density in futures market'
            },
            {
                'name': '305_options_market_depth',
                'metric1': 'derivatives/options_open_interest_sum',
                'metric2': 'derivatives/options_volume_sum',
                'operation': 'divide',
                'description': 'Options market depth indicator'
            },
            {
                'name': '306_futures_basis_spread',
                'metric1': 'derivatives/futures_basis_3m',
                'metric2': 'derivatives/futures_basis_6m',
                'operation': 'divide',
                'description': 'Futures term structure spread'
            },
            {
                'name': '307_derivatives_volume_ratio',
                'metric1': 'derivatives/volume_sum',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Derivatives to spot volume ratio'
            },
            {
                'name': '308_perpetual_dominance_ratio',
                'metric1': 'derivatives/futures_volume_perpetual_sum',
                'metric2': 'derivatives/futures_volume_sum',
                'operation': 'divide',
                'description': 'Perpetual futures market dominance'
            },
            {
                'name': '309_options_strike_distribution',
                'metric1': 'derivatives/options_atm_implied_vol_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Options strike price distribution'
            },
            {
                'name': '310_futures_risk_premium',
                'metric1': 'derivatives/futures_basis_3m',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Futures risk premium indicator'
            },
            {
                'name': '311_leverage_liquidation_risk',
                'metric1': 'derivatives/futures_liquidated_volume_long_sum',
                'metric2': 'derivatives/futures_liquidated_volume_short_sum',
                'operation': 'divide',
                'description': 'Long-short liquidation ratio'
            },
            {
                'name': '312_options_market_sentiment',
                'metric1': 'derivatives/options_volume_puts_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Options market sentiment indicator'
            },
            {
                'name': '313_futures_market_efficiency',
                'metric1': 'derivatives/futures_volume_sum',
                'metric2': 'derivatives/futures_open_interest_sum',
                'operation': 'divide',
                'description': 'Futures market turnover efficiency'
            },
            {
                'name': '314_perpetual_basis_impact',
                'metric1': 'derivatives/futures_basis_perpetual',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Perpetual basis impact on price'
            },
            {
                'name': '315_options_leverage_ratio',
                'metric1': 'derivatives/options_open_interest_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Options leverage relative to market cap'
            },
            {
                'name': '316_futures_volume_impact',
                'metric1': 'derivatives/futures_volume_buy_sum',
                'metric2': 'derivatives/futures_volume_sell_sum',
                'operation': 'divide',
                'description': 'Futures buy-sell volume impact'
            },
            {
                'name': '317_derivatives_risk_metric',
                'metric1': 'derivatives/futures_liquidated_volume_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'multiply',
                'description': 'Derivatives risk impact on price'
            },
            {
                'name': '318_options_expiry_pressure',
                'metric1': 'derivatives/options_volume_sum',
                'metric2': 'derivatives/options_open_interest_sum',
                'operation': 'divide',
                'description': 'Options expiry pressure indicator'
            },
            {
                'name': '319_futures_funding_efficiency',
                'metric1': 'derivatives/futures_funding_rate_perpetual',
                'metric2': 'derivatives/futures_basis_perpetual',
                'operation': 'divide',
                'description': 'Funding rate efficiency metric'
            },
            {
                'name': '320_leverage_concentration_risk',
                'metric1': 'derivatives/futures_open_interest_sum',
                'metric2': 'derivatives/futures_volume_sum',
                'operation': 'divide',
                'description': 'Leverage concentration indicator'
            },
            {
                'name': '321_options_delta_exposure',
                'metric1': 'derivatives/options_volume_calls_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Options delta exposure ratio'
            },
            {
                'name': '322_futures_term_structure',
                'metric1': 'derivatives/futures_basis_6m',
                'metric2': 'derivatives/futures_basis_perpetual',
                'operation': 'divide',
                'description': 'Futures term structure indicator'
            },
            {
                'name': '323_perpetual_market_depth',
                'metric1': 'derivatives/futures_volume_perpetual_sum',
                'metric2': 'derivatives/futures_open_interest_sum',
                'operation': 'divide',
                'description': 'Perpetual market depth ratio'
            },
            {
                'name': '324_options_market_coverage',
                'metric1': 'derivatives/options_volume_sum',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Options market coverage ratio'
            },
            {
                'name': '325_futures_liquidation_impact',
                'metric1': 'derivatives/futures_liquidated_volume_sum',
                'metric2': 'derivatives/futures_volume_sum',
                'operation': 'divide',
                'description': 'Futures liquidation impact ratio'
            },
            {
                'name': '326_derivatives_market_stress',
                'metric1': 'derivatives/futures_liquidated_volume_sum',
                'metric2': 'derivatives/options_volume_puts_sum',
                'operation': 'multiply',
                'description': 'Derivatives market stress indicator'
            },
            {
                'name': '327_options_gamma_exposure',
                'metric1': 'derivatives/options_volume_calls_sum',
                'metric2': 'derivatives/options_volume_puts_sum',
                'operation': 'divide',
                'description': 'Options gamma exposure ratio'
            },
            {
                'name': '328_futures_basis_efficiency',
                'metric1': 'derivatives/futures_basis_3m',
                'metric2': 'derivatives/futures_volume_sum',
                'operation': 'divide',
                'description': 'Futures basis efficiency metric'
            },
            {
                'name': '329_perpetual_funding_impact',
                'metric1': 'derivatives/futures_funding_rate_perpetual',
                'metric2': 'derivatives/futures_volume_perpetual_sum',
                'operation': 'multiply',
                'description': 'Perpetual funding impact indicator'
            },
            {
                'name': '330_options_market_liquidity',
                'metric1': 'derivatives/options_volume_sum',
                'metric2': 'derivatives/options_open_interest_sum',
                'operation': 'divide',
                'description': 'Options market liquidity ratio'
            },
            {
                'name': '331_futures_market_depth',
                'metric1': 'derivatives/futures_open_interest_sum',
                'metric2': 'derivatives/volume_sum',
                'operation': 'divide',
                'description': 'Futures market depth indicator'
            },
            {
                'name': '332_derivatives_leverage_ratio',
                'metric1': 'derivatives/futures_open_interest_sum',
                'metric2': 'derivatives/options_open_interest_sum',
                'operation': 'divide',
                'description': 'Derivatives leverage comparison'
            },
            {
                'name': '333_options_risk_reversal',
                'metric1': 'derivatives/options_volume_calls_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Options risk reversal indicator'
            },
            {
                'name': '334_futures_volume_efficiency',
                'metric1': 'derivatives/futures_volume_buy_sum',
                'metric2': 'derivatives/futures_open_interest_sum',
                'operation': 'divide',
                'description': 'Futures volume efficiency ratio'
            },
            {
                'name': '335_perpetual_market_stress',
                'metric1': 'derivatives/futures_liquidated_volume_sum',
                'metric2': 'derivatives/futures_funding_rate_perpetual',
                'operation': 'multiply',
                'description': 'Perpetual market stress indicator'
            },
            {
                'name': '336_options_market_balance',
                'metric1': 'derivatives/options_volume_puts_sum',
                'metric2': 'derivatives/options_open_interest_sum',
                'operation': 'divide',
                'description': 'Options market balance ratio'
            },
            {
                'name': '337_futures_risk_indicator',
                'metric1': 'derivatives/futures_liquidated_volume_long_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Futures market risk indicator'
            },
            {
                'name': '338_derivatives_volume_impact',
                'metric1': 'derivatives/volume_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Derivatives volume price impact'
            },
            {
                'name': '339_options_strike_efficiency',
                'metric1': 'derivatives/options_volume_calls_sum',
                'metric2': 'derivatives/options_volume_sum',
                'operation': 'divide',
                'description': 'Options strike efficiency ratio'
            },
            {
                'name': '340_futures_basis_impact',
                'metric1': 'derivatives/futures_basis_3m',
                'metric2': 'derivatives/futures_volume_sum',
                'operation': 'multiply',
                'description': 'Futures basis market impact'
            },
            {
                'name': '341_perpetual_efficiency_ratio',
                'metric1': 'derivatives/futures_volume_perpetual_sum',
                'metric2': 'derivatives/futures_liquidated_volume_sum',
                'operation': 'divide',
                'description': 'Perpetual market efficiency ratio'
            },
            {
                'name': '342_options_market_risk',
                'metric1': 'derivatives/options_volume_puts_sum',
                'metric2': 'derivatives/options_volume_sum',
                'operation': 'divide',
                'description': 'Options market risk indicator'
            },
            {
                'name': '343_futures_market_sentiment',
                'metric1': 'derivatives/futures_basis_3m',
                'metric2': 'derivatives/futures_basis_perpetual',
                'operation': 'divide',
                'description': 'Futures market sentiment indicator'
            },
            {
                'name': '344_derivatives_risk_ratio',
                'metric1': 'derivatives/futures_liquidated_volume_sum',
                'metric2': 'derivatives/volume_sum',
                'operation': 'divide',
                'description': 'Derivatives risk exposure ratio'
            },
            {
                'name': '345_options_leverage_impact',
                'metric1': 'derivatives/options_open_interest_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Options leverage price impact'
            },
            {
                'name': '346_futures_efficiency_metric',
                'metric1': 'derivatives/futures_volume_sum',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Futures market efficiency metric'
            },
            {
                'name': '347_perpetual_risk_indicator',
                'metric1': 'derivatives/futures_funding_rate_perpetual',
                'metric2': 'derivatives/futures_liquidated_volume_sum',
                'operation': 'multiply',
                'description': 'Perpetual market risk indicator'
            },
            {
                'name': '348_options_market_efficiency',
                'metric1': 'derivatives/options_volume_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Options market efficiency ratio'
            },
            {
                'name': '349_futures_market_balance',
                'metric1': 'derivatives/futures_volume_buy_sum',
                'metric2': 'derivatives/futures_basis_3m',
                'operation': 'divide',
                'description': 'Futures market balance indicator'
            },
            {
                'name': '350_derivatives_market_depth',
                'metric1': 'derivatives/volume_sum',
                'metric2': 'derivatives/futures_open_interest_sum',
                'operation': 'divide',
                'description': 'Overall derivatives market depth'
            },
            {
                'name': '351_utxo_value_density',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/utxo_count',
                'operation': 'divide',
                'description': 'Average value per UTXO in circulation'
            },
            {
                'name': '352_block_chain_growth',
                'metric1': 'blockchain/block_height',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Blockchain growth efficiency ratio'
            },
            {
                'name': '353_utxo_profit_ratio',
                'metric1': 'blockchain/utxo_profit_count',
                'metric2': 'blockchain/utxo_loss_count',
                'operation': 'divide',
                'description': 'Ratio of profitable to unprofitable UTXOs'
            },
            {
                'name': '354_block_weight_efficiency',
                'metric1': 'blockchain/block_weight_mean',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Block weight utilization efficiency'
            },
            {
                'name': '355_utxo_creation_momentum',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/utxo_spent_value_sum',
                'operation': 'divide',
                'description': 'UTXO creation vs spending momentum'
            },
            {
                'name': '356_blockchain_size_growth',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Blockchain size growth rate'
            },
            {
                'name': '357_utxo_age_indicator',
                'metric1': 'blockchain/utxo_spent_value_mean',
                'metric2': 'blockchain/utxo_created_value_mean',
                'operation': 'divide',
                'description': 'UTXO age distribution indicator'
            },
            {
                'name': '358_block_space_utilization',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_weight_mean',
                'operation': 'divide',
                'description': 'Block space utilization ratio'
            },
            {
                'name': '359_utxo_spending_efficiency',
                'metric1': 'blockchain/utxo_spent_count',
                'metric2': 'blockchain/utxo_created_count',
                'operation': 'divide',
                'description': 'UTXO spending efficiency ratio'
            },
            {
                'name': '360_blockchain_validation_rate',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Block validation rate'
            },
            {
                'name': '361_utxo_volume_ratio',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'UTXO volume to block size ratio'
            },
            {
                'name': '362_block_propagation_metric',
                'metric1': 'blockchain/block_interval_mean',
                'metric2': 'blockchain/block_interval_median',
                'operation': 'divide',
                'description': 'Block propagation efficiency'
            },
            {
                'name': '363_utxo_lifecycle_metric',
                'metric1': 'blockchain/utxo_spent_value_sum',
                'metric2': 'blockchain/utxo_profit_count',
                'operation': 'divide',
                'description': 'UTXO lifecycle efficiency'
            },
            {
                'name': '364_blockchain_density_ratio',
                'metric1': 'blockchain/block_weight_mean',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Blockchain density indicator'
            },
            {
                'name': '365_utxo_profit_momentum',
                'metric1': 'blockchain/utxo_profit_count',
                'metric2': 'blockchain/utxo_created_count',
                'operation': 'divide',
                'description': 'UTXO profit creation ratio'
            },
            {
                'name': '366_block_efficiency_score',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Block efficiency scoring metric'
            },
            {
                'name': '367_utxo_distribution_pattern',
                'metric1': 'blockchain/utxo_created_value_mean',
                'metric2': 'blockchain/utxo_loss_count',
                'operation': 'divide',
                'description': 'UTXO value distribution pattern'
            },
            {
                'name': '368_blockchain_growth_momentum',
                'metric1': 'blockchain/block_height',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Blockchain growth momentum'
            },
            {
                'name': '369_utxo_turnover_efficiency',
                'metric1': 'blockchain/utxo_spent_count',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'UTXO turnover per block'
            },
            {
                'name': '370_block_size_momentum',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_interval_median',
                'operation': 'divide',
                'description': 'Block size growth momentum'
            },
            {
                'name': '371_utxo_value_momentum',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/utxo_loss_count',
                'operation': 'divide',
                'description': 'UTXO value creation momentum'
            },
            {
                'name': '372_blockchain_efficiency_ratio',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_weight_mean',
                'operation': 'divide',
                'description': 'Blockchain processing efficiency'
            },
            {
                'name': '373_utxo_creation_efficiency',
                'metric1': 'blockchain/utxo_created_count',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'UTXO creation rate efficiency'
            },
            {
                'name': '374_block_validation_efficiency',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Block validation efficiency'
            },
            {
                'name': '375_utxo_spending_pattern',
                'metric1': 'blockchain/utxo_spent_value_mean',
                'metric2': 'blockchain/utxo_count',
                'operation': 'divide',
                'description': 'UTXO spending pattern indicator'
            },
            {
                'name': '376_blockchain_utilization_score',
                'metric1': 'blockchain/block_weight_mean',
                'metric2': 'blockchain/block_interval_median',
                'operation': 'divide',
                'description': 'Blockchain utilization scoring'
            },
            {
                'name': '377_utxo_age_distribution',
                'metric1': 'blockchain/utxo_created_value_mean',
                'metric2': 'blockchain/utxo_spent_value_mean',
                'operation': 'divide',
                'description': 'UTXO age distribution pattern'
            },
            {
                'name': '378_block_space_efficiency',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_height',
                'operation': 'divide',
                'description': 'Block space usage efficiency'
            },
            {
                'name': '379_utxo_profit_distribution',
                'metric1': 'blockchain/utxo_profit_count',
                'metric2': 'blockchain/utxo_count',
                'operation': 'divide',
                'description': 'UTXO profit distribution ratio'
            },
            {
                'name': '380_blockchain_growth_rate',
                'metric1': 'blockchain/block_height',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Blockchain growth rate indicator'
            },
            {
                'name': '381_utxo_efficiency_score',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/utxo_spent_count',
                'operation': 'divide',
                'description': 'UTXO efficiency scoring'
            },
            {
                'name': '382_block_timing_efficiency',
                'metric1': 'blockchain/block_interval_mean',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Block timing efficiency ratio'
            },
            {
                'name': '383_utxo_volume_efficiency',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'UTXO volume creation efficiency'
            },
            {
                'name': '384_blockchain_density_score',
                'metric1': 'blockchain/block_weight_mean',
                'metric2': 'blockchain/block_height',
                'operation': 'divide',
                'description': 'Blockchain density scoring'
            },
            {
                'name': '385_utxo_loss_ratio',
                'metric1': 'blockchain/utxo_loss_count',
                'metric2': 'blockchain/utxo_count',
                'operation': 'divide',
                'description': 'UTXO loss distribution ratio'
            },
            {
                'name': '386_block_propagation_rate',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_interval_median',
                'operation': 'divide',
                'description': 'Block propagation rate'
            },
            {
                'name': '387_utxo_creation_pattern',
                'metric1': 'blockchain/utxo_created_count',
                'metric2': 'blockchain/utxo_profit_count',
                'operation': 'divide',
                'description': 'UTXO creation pattern indicator'
            },
            {
                'name': '388_blockchain_load_metric',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_weight_mean',
                'operation': 'divide',
                'description': 'Blockchain load measurement'
            },
            {
                'name': '389_utxo_spending_momentum',
                'metric1': 'blockchain/utxo_spent_value_sum',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'UTXO spending momentum'
            },
            {
                'name': '390_block_efficiency_indicator',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_height',
                'operation': 'divide',
                'description': 'Block processing efficiency indicator'
            },
            {
                'name': '391_utxo_value_efficiency',
                'metric1': 'blockchain/utxo_created_value_mean',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'UTXO value creation efficiency'
            },
            {
                'name': '392_blockchain_processing_rate',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'Blockchain processing rate'
            },
            {
                'name': '393_utxo_distribution_efficiency',
                'metric1': 'blockchain/utxo_created_value_sum',
                'metric2': 'blockchain/utxo_spent_value_sum',
                'operation': 'divide',
                'description': 'UTXO distribution efficiency'
            },
            {
                'name': '394_block_weight_utilization',
                'metric1': 'blockchain/block_weight_mean',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Block weight utilization ratio'
            },
            {
                'name': '395_utxo_lifecycle_ratio',
                'metric1': 'blockchain/utxo_spent_count',
                'metric2': 'blockchain/utxo_profit_count',
                'operation': 'divide',
                'description': 'UTXO lifecycle efficiency ratio'
            },
            {
                'name': '396_blockchain_growth_efficiency',
                'metric1': 'blockchain/block_height',
                'metric2': 'blockchain/block_weight_mean',
                'operation': 'divide',
                'description': 'Blockchain growth efficiency'
            },
            {
                'name': '397_utxo_profit_efficiency',
                'metric1': 'blockchain/utxo_profit_count',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'UTXO profit generation efficiency'
            },
            {
                'name': '398_block_space_momentum',
                'metric1': 'blockchain/block_size_mean',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Block space growth momentum'
            },
            {
                'name': '399_utxo_creation_rate',
                'metric1': 'blockchain/utxo_created_count',
                'metric2': 'blockchain/block_interval_mean',
                'operation': 'divide',
                'description': 'UTXO creation rate'
            },
            {
                'name': '400_blockchain_efficiency_score',
                'metric1': 'blockchain/block_count',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Overall blockchain efficiency score'
            },
            {
                'name': '401_whale_balance_impact',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Whale balance market impact ratio'
            },
            {
                'name': '402_institutional_flow_strength',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Institutional flow strength indicator'
            },
            {
                'name': '403_exchange_whale_ratio',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'transactions/transfers_volume_exchanges_net',
                'operation': 'divide',
                'description': 'Exchange whale activity ratio'
            },
            {
                'name': '404_whale_accumulation_trend',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Whale accumulation trend indicator'
            },
            {
                'name': '405_institutional_holding_ratio',
                'metric1': 'distribution/balance_10pct_holders',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Institutional holding ratio'
            },
            {
                'name': '406_whale_transaction_impact',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Whale transaction market impact'
            },
            {
                'name': '407_exchange_concentration_risk',
                'metric1': 'distribution/exchange_net_position_change',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Exchange concentration risk indicator'
            },
            {
                'name': '408_whale_supply_ratio',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'supply/active_24h',
                'operation': 'divide',
                'description': 'Whale supply activity ratio'
            },
            {
                'name': '409_institutional_flow_impact',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Institutional flow price impact'
            },
            {
                'name': '410_whale_movement_efficiency',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Whale movement efficiency ratio'
            },
            {
                'name': '411_exchange_whale_pressure',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'distribution/balance_exchanges_all',
                'operation': 'divide',
                'description': 'Exchange whale pressure indicator'
            },
            {
                'name': '412_institutional_balance_momentum',
                'metric1': 'distribution/balance_10pct_holders',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Institutional balance momentum'
            },
            {
                'name': '413_whale_liquidity_ratio',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Whale liquidity ratio'
            },
            {
                'name': '414_exchange_flow_concentration',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'transactions/transfers_volume_to_exchanges_sum',
                'operation': 'divide',
                'description': 'Exchange flow concentration'
            },
            {
                'name': '415_institutional_activity_impact',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/marketcap_realized_usd',
                'operation': 'divide',
                'description': 'Institutional activity impact'
            },
            {
                'name': '416_whale_distribution_metric',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'distribution/balance_exchanges_all',
                'operation': 'divide',
                'description': 'Whale distribution metric'
            },
            {
                'name': '417_exchange_large_flow_ratio',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Large exchange flow ratio'
            },
            {
                'name': '418_institutional_holding_impact',
                'metric1': 'distribution/balance_10pct_holders',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Institutional holding impact'
            },
            {
                'name': '419_whale_market_influence',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Whale market influence ratio'
            },
            {
                'name': '420_exchange_whale_efficiency',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Exchange whale efficiency'
            },
            {
                'name': '421_institutional_flow_ratio',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'transactions/transfers_volume_exchanges_net',
                'operation': 'divide',
                'description': 'Institutional flow ratio'
            },
            {
                'name': '422_whale_accumulation_efficiency',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'market/price_realized_usd',
                'operation': 'divide',
                'description': 'Whale accumulation efficiency'
            },
            {
                'name': '423_exchange_institutional_impact',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'market/marketcap_realized_usd',
                'operation': 'divide',
                'description': 'Exchange institutional impact'
            },
            {
                'name': '424_whale_holding_pressure',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Whale holding pressure'
            },
            {
                'name': '425_institutional_exchange_ratio',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'distribution/balance_exchanges_all',
                'operation': 'divide',
                'description': 'Institutional exchange ratio'
            },
            {
                'name': '426_whale_transaction_efficiency',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Whale transaction efficiency'
            },
            {
                'name': '427_exchange_concentration_metric',
                'metric1': 'distribution/exchange_net_position_change',
                'metric2': 'transactions/transfers_volume_large_exchanges_sum',
                'operation': 'divide',
                'description': 'Exchange concentration metric'
            },
            {
                'name': '428_institutional_supply_impact',
                'metric1': 'distribution/balance_10pct_holders',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Institutional supply impact'
            },
            {
                'name': '429_whale_market_momentum',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/price_realized_usd',
                'operation': 'divide',
                'description': 'Whale market momentum'
            },
            {
                'name': '430_exchange_whale_momentum',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Exchange whale momentum'
            },
            {
                'name': '431_institutional_activity_ratio',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Institutional activity ratio'
            },
            {
                'name': '432_whale_exchange_impact',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'distribution/exchange_net_position_change',
                'operation': 'divide',
                'description': 'Whale exchange impact'
            },
            {
                'name': '433_institutional_market_depth',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Institutional market depth'
            },
            {
                'name': '434_whale_liquidity_impact',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Whale liquidity impact'
            },
            {
                'name': '435_exchange_institutional_flow',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'transactions/transfers_volume_exchanges_net',
                'operation': 'divide',
                'description': 'Exchange institutional flow'
            },
            {
                'name': '436_institutional_holding_efficiency',
                'metric1': 'distribution/balance_10pct_holders',
                'metric2': 'market/price_realized_usd',
                'operation': 'divide',
                'description': 'Institutional holding efficiency'
            },
            {
                'name': '437_whale_activity_impact',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/marketcap_realized_usd',
                'operation': 'divide',
                'description': 'Whale activity impact'
            },
            {
                'name': '438_exchange_whale_distribution',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'distribution/balance_exchanges_all',
                'operation': 'divide',
                'description': 'Exchange whale distribution'
            },
            {
                'name': '439_institutional_momentum_ratio',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Institutional momentum ratio'
            },
            {
                'name': '440_whale_market_efficiency',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Whale market efficiency'
            },
            {
                'name': '441_exchange_large_transaction_impact',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Exchange large transaction impact'
            },
            {
                'name': '442_institutional_supply_ratio',
                'metric1': 'distribution/balance_10pct_holders',
                'metric2': 'supply/active_24h',
                'operation': 'divide',
                'description': 'Institutional supply ratio'
            },
            {
                'name': '443_whale_flow_efficiency',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'transactions/transfers_volume_exchanges_net',
                'operation': 'divide',
                'description': 'Whale flow efficiency'
            },
            {
                'name': '444_exchange_institutional_momentum',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'market/price_realized_usd',
                'operation': 'divide',
                'description': 'Exchange institutional momentum'
            },
            {
                'name': '445_institutional_market_impact',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Institutional market impact'
            },
            {
                'name': '446_whale_exchange_efficiency',
                'metric1': 'distribution/balance_1pct_holders',
                'metric2': 'distribution/balance_exchanges_all',
                'operation': 'divide',
                'description': 'Whale exchange efficiency'
            },
            {
                'name': '447_exchange_large_flow_impact',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Exchange large flow impact'
            },
            {
                'name': '448_institutional_liquidity_ratio',
                'metric1': 'distribution/balance_10pct_holders',
                'metric2': 'supply/liquid_sum',
                'operation': 'divide',
                'description': 'Institutional liquidity ratio'
            },
            {
                'name': '449_whale_market_activity',
                'metric1': 'transactions/transfers_volume_large_sum',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Whale market activity ratio'
            },
            {
                'name': '450_institutional_exchange_efficiency',
                'metric1': 'transactions/transfers_volume_large_exchanges_sum',
                'metric2': 'transactions/transfers_volume_to_exchanges_sum',
                'operation': 'divide',
                'description': 'Institutional exchange efficiency'
            },
            {
                'name': '451_lightning_network_growth',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Lightning Network growth relative to market cap'
            },
            {
                'name': '452_layer2_adoption_rate',
                'metric1': 'lightning/nodes_count',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Layer 2 adoption rate indicator'
            },
            {
                'name': '453_lightning_capacity_efficiency',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/channels_count',
                'operation': 'divide',
                'description': 'Average capacity per channel'
            },
            {
                'name': '454_network_channel_density',
                'metric1': 'lightning/channels_count',
                'metric2': 'lightning/nodes_count',
                'operation': 'divide',
                'description': 'Channels per node ratio'
            },
            {
                'name': '455_lightning_fee_efficiency',
                'metric1': 'lightning/fee_rate_median',
                'metric2': 'fees/volume_mean',
                'operation': 'divide',
                'description': 'Lightning to on-chain fee efficiency'
            },
            {
                'name': '456_layer2_scaling_metric',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Layer 2 scaling efficiency'
            },
            {
                'name': '457_lightning_node_stability',
                'metric1': 'lightning/nodes_count',
                'metric2': 'lightning/node_connectivity_mean',
                'operation': 'divide',
                'description': 'Node stability indicator'
            },
            {
                'name': '458_channel_efficiency_ratio',
                'metric1': 'lightning/channels_count',
                'metric2': 'lightning/channel_size_mean',
                'operation': 'divide',
                'description': 'Channel efficiency metric'
            },
            {
                'name': '459_lightning_network_depth',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/nodes_count',
                'operation': 'divide',
                'description': 'Network depth per node'
            },
            {
                'name': '460_layer2_usage_density',
                'metric1': 'lightning/channels_count',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Layer 2 usage density'
            },
            {
                'name': '461_lightning_growth_momentum',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Lightning growth momentum'
            },
            {
                'name': '462_channel_creation_efficiency',
                'metric1': 'lightning/channels_count',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Channel creation rate'
            },
            {
                'name': '463_lightning_node_distribution',
                'metric1': 'lightning/nodes_count',
                'metric2': 'addresses/active_count',
                'operation': 'divide',
                'description': 'Node distribution ratio'
            },
            {
                'name': '464_layer2_capacity_utilization',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/channel_size_mean',
                'operation': 'divide',
                'description': 'Capacity utilization efficiency'
            },
            {
                'name': '465_lightning_fee_impact',
                'metric1': 'lightning/fee_rate_median',
                'metric2': 'lightning/channel_size_mean',
                'operation': 'divide',
                'description': 'Fee impact on channel size'
            },
            {
                'name': '466_network_connectivity_ratio',
                'metric1': 'lightning/node_connectivity_mean',
                'metric2': 'lightning/nodes_count',
                'operation': 'divide',
                'description': 'Network connectivity efficiency'
            },
            {
                'name': '467_lightning_scaling_efficiency',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Lightning scaling efficiency'
            },
            {
                'name': '468_channel_size_distribution',
                'metric1': 'lightning/channel_size_mean',
                'metric2': 'lightning/channel_size_median',
                'operation': 'divide',
                'description': 'Channel size distribution pattern'
            },
            {
                'name': '469_layer2_adoption_momentum',
                'metric1': 'lightning/nodes_count',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Layer 2 adoption momentum'
            },
            {
                'name': '470_lightning_network_efficiency',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/fee_rate_median',
                'operation': 'divide',
                'description': 'Network efficiency ratio'
            },
            {
                'name': '471_channel_growth_rate',
                'metric1': 'lightning/channels_count',
                'metric2': 'lightning/network_capacity_sum',
                'operation': 'divide',
                'description': 'Channel growth efficiency'
            },
            {
                'name': '472_lightning_node_efficiency',
                'metric1': 'lightning/nodes_count',
                'metric2': 'lightning/fee_rate_median',
                'operation': 'divide',
                'description': 'Node efficiency metric'
            },
            {
                'name': '473_layer2_capacity_growth',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'supply/current',
                'operation': 'divide',
                'description': 'Layer 2 capacity growth ratio'
            },
            {
                'name': '474_lightning_fee_distribution',
                'metric1': 'lightning/fee_rate_median',
                'metric2': 'lightning/channels_count',
                'operation': 'divide',
                'description': 'Fee distribution per channel'
            },
            {
                'name': '475_network_stability_metric',
                'metric1': 'lightning/nodes_count',
                'metric2': 'lightning/channel_size_mean',
                'operation': 'divide',
                'description': 'Network stability indicator'
            },
            {
                'name': '476_lightning_market_impact',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'market/marketcap_realized_usd',
                'operation': 'divide',
                'description': 'Lightning market impact ratio'
            },
            {
                'name': '477_channel_efficiency_score',
                'metric1': 'lightning/channels_count',
                'metric2': 'lightning/node_connectivity_mean',
                'operation': 'divide',
                'description': 'Channel efficiency score'
            },
            {
                'name': '478_layer2_network_density',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/nodes_count',
                'operation': 'divide',
                'description': 'Layer 2 network density'
            },
            {
                'name': '479_lightning_adoption_rate',
                'metric1': 'lightning/nodes_count',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Lightning adoption rate'
            },
            {
                'name': '480_channel_size_efficiency',
                'metric1': 'lightning/channel_size_mean',
                'metric2': 'lightning/fee_rate_median',
                'operation': 'divide',
                'description': 'Channel size efficiency'
            },
            {
                'name': '481_lightning_node_growth',
                'metric1': 'lightning/nodes_count',
                'metric2': 'blockchain/block_count',
                'operation': 'divide',
                'description': 'Lightning node growth rate'
            },
            {
                'name': '482_layer2_fee_efficiency',
                'metric1': 'lightning/fee_rate_median',
                'metric2': 'lightning/network_capacity_sum',
                'operation': 'divide',
                'description': 'Layer 2 fee efficiency'
            },
            {
                'name': '483_lightning_capacity_distribution',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/channel_size_median',
                'operation': 'divide',
                'description': 'Capacity distribution pattern'
            },
            {
                'name': '484_network_growth_efficiency',
                'metric1': 'lightning/nodes_count',
                'metric2': 'lightning/network_capacity_sum',
                'operation': 'divide',
                'description': 'Network growth efficiency'
            },
            {
                'name': '485_lightning_channel_impact',
                'metric1': 'lightning/channels_count',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Channel impact on price'
            },
            {
                'name': '486_layer2_scaling_ratio',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'transactions/count',
                'operation': 'divide',
                'description': 'Layer 2 scaling ratio'
            },
            {
                'name': '487_lightning_efficiency_score',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/node_connectivity_mean',
                'operation': 'divide',
                'description': 'Lightning efficiency score'
            },
            {
                'name': '488_channel_utilization_ratio',
                'metric1': 'lightning/channel_size_mean',
                'metric2': 'lightning/network_capacity_sum',
                'operation': 'divide',
                'description': 'Channel utilization ratio'
            },
            {
                'name': '489_layer2_node_efficiency',
                'metric1': 'lightning/nodes_count',
                'metric2': 'lightning/channel_size_mean',
                'operation': 'divide',
                'description': 'Layer 2 node efficiency'
            },
            {
                'name': '490_lightning_network_momentum',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'market/price_realized_usd',
                'operation': 'divide',
                'description': 'Lightning network momentum'
            },
            {
                'name': '491_channel_growth_momentum',
                'metric1': 'lightning/channels_count',
                'metric2': 'lightning/nodes_count',
                'operation': 'divide',
                'description': 'Channel growth momentum'
            },
            {
                'name': '492_lightning_market_depth',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'market/volume_sum',
                'operation': 'divide',
                'description': 'Lightning market depth'
            },
            {
                'name': '493_layer2_efficiency_metric',
                'metric1': 'lightning/channel_size_mean',
                'metric2': 'lightning/fee_rate_median',
                'operation': 'divide',
                'description': 'Layer 2 efficiency metric'
            },
            {
                'name': '494_lightning_node_impact',
                'metric1': 'lightning/nodes_count',
                'metric2': 'market/marketcap_usd',
                'operation': 'divide',
                'description': 'Lightning node market impact'
            },
            {
                'name': '495_channel_stability_indicator',
                'metric1': 'lightning/channels_count',
                'metric2': 'lightning/fee_rate_median',
                'operation': 'divide',
                'description': 'Channel stability indicator'
            },
            {
                'name': '496_layer2_growth_momentum',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'blockchain/block_size_mean',
                'operation': 'divide',
                'description': 'Layer 2 growth momentum'
            },
            {
                'name': '497_lightning_capacity_momentum',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'lightning/nodes_count',
                'operation': 'divide',
                'description': 'Lightning capacity momentum'
            },
            {
                'name': '498_network_fee_efficiency',
                'metric1': 'lightning/fee_rate_median',
                'metric2': 'lightning/channel_size_median',
                'operation': 'divide',
                'description': 'Network fee efficiency'
            },
            {
                'name': '499_layer2_market_impact',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'market/price_usd_close',
                'operation': 'divide',
                'description': 'Layer 2 market impact'
            },
            {
                'name': '500_lightning_scaling_score',
                'metric1': 'lightning/network_capacity_sum',
                'metric2': 'transactions/transfer_volume_sum',
                'operation': 'divide',
                'description': 'Lightning scaling score'
            }
        ]
