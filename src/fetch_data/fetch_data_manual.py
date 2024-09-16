# fetch_data_manual.py
import os
from datetime import datetime, timezone
import logging
import pandas as pd
import requests
from tqdm import tqdm

# At the top of your script, add these constants:
CURRENCIES = ['NATIVE', 'USD']
EXCHANGES = ['aggregated', 'binance', 'bitfinex', 'bitflyer', 'bitmex', 'bitstamp', 'bittrex', 'bybit',
             'coinbase', 'coincheck', 'deribit', 'ftx', 'gate.io', 'gemini', 'huobi', 'kraken', 'kucoin',
             'okex', 'poloniex']


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
GLASSNODE_API_KEY = '2ixuRhqosLHPpClDohgjZJsEEyp'
ASSET = 'BTC'
INTERVAL = '24h'
BASE_URL = 'https://api.glassnode.com/v1/metrics'
FOLDER_NAME = 'glassnode_data_btc24h_Sept2024_manual'

# Define the endpoints and their respective metrics with additional parameters
ENDPOINTS = {
    'addresses': [
        {'metric': 'accumulation_balance', 'params': ['c']},
        {'metric': 'supply_balance_less_0001', 'params': ['c']},
        {'metric': 'supply_balance_more_100k', 'params': ['c']},
        {'metric': 'supply_balance_0001_001', 'params': ['c']},
        {'metric': 'supply_balance_001_01', 'params': ['c']},
        {'metric': 'supply_balance_01_1', 'params': ['c']},
        {'metric': 'supply_balance_1_10', 'params': ['c']},
        {'metric': 'supply_balance_10_100', 'params': ['c']},
        {'metric': 'supply_balance_100_1k', 'params': ['c']},
        {'metric': 'supply_balance_10k_100k', 'params': ['c']},
        {'metric': 'supply_balance_1k_10k', 'params': ['c']},
        {'metric': 'accumulation_count', 'params': []},
        {'metric': 'active_count', 'params': []},
    ],
    'blockchain': [
        {'metric': 'utxo_created_value_mean', 'params': ['c']},
        {'metric': 'utxo_created_value_median', 'params': ['c']},
        {'metric': 'utxo_spent_value_mean', 'params': ['c']},
        {'metric': 'utxo_spent_value_median', 'params': ['c']},
        {'metric': 'utxo_created_count', 'params': []},
        {'metric': 'utxo_spent_count', 'params': []},
        {'metric': 'utxo_count', 'params': []},
    ],
    'derivatives': [
        {'metric': 'futures_liquidated_volume_long_sum', 'params': ['c', 'e']},
        {'metric': 'futures_liquidated_volume_short_sum', 'params': ['c', 'e']},
        {'metric': 'futures_open_interest_sum', 'params': ['c', 'e']},
        {'metric': 'futures_volume_daily_sum', 'params': ['c', 'e']},
        {'metric': 'futures_volume_daily_perpetual_sum', 'params': ['c', 'e']},
        {'metric': 'options_volume_daily_sum', 'params': ['c', 'e']},
        {'metric': 'futures_open_interest_perpetual_sum', 'params': ['c', 'e']},
        {'metric': 'futures_funding_rate_perpetual_v2', 'params': ['e']},
        {'metric': 'futures_estimated_leverage_ratio', 'params': ['e']},
        {'metric': 'options_open_interest_sum', 'params': ['c', 'e']},
        {'metric': 'options_open_interest_put_call_ratio', 'params': ['e']},
        {'metric': 'options_volume_put_call_ratio', 'params': ['e']},
    ],
    'distribution': [
        {'metric': 'balance_exchanges_relative_pit', 'params': ['e']},
        {'metric': 'balance_exchanges_pit', 'params': ['c', 'e']},
        {'metric': 'exchange_net_position_change_pit', 'params': ['c', 'e']},
            {'metric': 'balance_exchanges_relative', 'params': ['e']},
            {'metric': 'balance_exchanges', 'params': ['c', 'e']},
            {'metric': 'exchange_net_position_change', 'params': ['c', 'e']},
            {'metric': 'supply_contracts', 'params': ['c']},
            {'metric': 'balance_1pct_holders', 'params': ['c']},
    ],
    'transactions': [
        {'metric': 'transfers_volume_exchanges_net_pit', 'params': ['c', 'e']},
        {'metric': 'transfers_volume_exchanges_net_by_size_pit', 'params': ['c', 'e']},
    ],
    'indicators': [
        {'metric': 'svl_entity_adjusted_24h', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_more_10y', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_1d_1w', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_1m_3m', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_1w_1m', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_1y_2y', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_2y_3y', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_3m_6m', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_3y_5y', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_5y_7y', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_6m_12m', 'params': ['c']},
        {'metric': 'svl_entity_adjusted_7y_10y', 'params': ['c']},
        {'metric': 'svl_1h', 'params': ['c']},
        {'metric': 'svl_more_10y', 'params': ['c']},
        {'metric': 'svl_1d_1w', 'params': ['c']},
        {'metric': 'svl_1h_24h', 'params': ['c']},
        {'metric': 'svl_1m_3m', 'params': ['c']},
        {'metric': 'svl_1w_1m', 'params': ['c']},
        {'metric': 'svl_1y_2y', 'params': ['c']},
        {'metric': 'svl_2y_3y', 'params': ['c']},
        {'metric': 'svl_3m_6m', 'params': ['c']},
        {'metric': 'svl_3y_5y', 'params': ['c']},
        {'metric': 'svl_5y_7y', 'params': ['c']},
        {'metric': 'svl_6m_12m', 'params': ['c']},
        {'metric': 'svl_7y_10y', 'params': ['c']},
    ],
    'lightning': [
        {'metric': 'base_fee_median', 'params': ['c']},
        {'metric': 'network_capacity_sum', 'params': ['c']},
        {'metric': 'channel_size_mean', 'params': ['c']},
        {'metric': 'channel_size_median', 'params': ['c']},
    ],
    'institutions': [
        {'metric': 'btc_us_spot_etf_balances_all', 'params': ['c']},
        {'metric': 'btc_us_spot_etf_balances_latest', 'params': ['c']},
        {'metric': 'btc_us_spot_etf_flows_all', 'params': ['c']},
    ],
    'market': [
        {'metric': 'price_usd_close_pit', 'params': ['c']},
        {'metric': 'spot_buying_volume_sum_pit', 'params': ['c']},
            {'metric': 'price_usd_close', 'params': ['c']},
            {'metric': 'spot_buying_volume_sum', 'params': ['c']},
            {'metric': 'spot_cvd_sum', 'params': ['c']},
            {'metric': 'spot_selling_volume_sum', 'params': ['c']},
            {'metric': 'spot_volume_daily_sum', 'params': ['c']},
            {'metric': 'spot_volume_daily_latest', 'params': ['c']},
            {'metric': 'spot_volume_daily_sum_all', 'params': ['c']},
            {'metric': 'spot_volume_sum_intraday', 'params': ['c']},
    ],
    'mining': [
        {'metric': 'volume_mined_sum_pit', 'params': ['c', 'miner']},
        {'metric': 'revenue_sum_pit', 'params': ['c', 'miner']},
            {'metric': 'volume_mined_sum', 'params': ['c', 'miner']},
            {'metric': 'revenue_sum', 'params': ['c', 'miner']},
            {'metric': 'miners_unspent_supply', 'params': ['c']},
    ],
    'fees': [
        {'metric': 'fees_average_relative_pit', 'params': ['c']},
        {'metric': 'fees_median_relative_pit', 'params': ['c']},
    ],
    # #protocols not for btc
    # 'protocols': [
    #     {'metric': 'lido_deposits_volume_sum', 'params': ['a', 'c']},
    #     {'metric': 'lido_volume_net', 'params': ['a', 'c']},
    #     {'metric': 'lido_total_value_locked', 'params': ['a', 'c']},
    #     {'metric': 'lido_withdrawn_volume_sum', 'params': ['a', 'c']},
    # ],
    'supply': [
        {'metric': 'current_adjusted', 'params': ['c']},
        {'metric': 'burn_rate', 'params': ['c']},
        {'metric': 'burned', 'params': ['c']},
        {'metric': 'current', 'params': ['c']},
        {'metric': 'highly_liquid_sum', 'params': ['c']},
        {'metric': 'illiquid_sum', 'params': ['c']},
        {'metric': 'liquid_illiquid_sum', 'params': ['c']},
        {'metric': 'liquid_sum', 'params': ['c']},
        {'metric': 'lth_sum', 'params': ['c']},
        {'metric': 'lth_loss_sum', 'params': ['c']},
        {'metric': 'lth_profit_sum', 'params': ['c']},
        {'metric': 'minted', 'params': ['c']},
        {'metric': 'probably_lost', 'params': ['c']},
        {'metric': 'provably_lost', 'params': ['c']},
        {'metric': 'revived_more_1y_sum', 'params': ['c']},
        {'metric': 'revived_more_2y_sum', 'params': ['c']},
        {'metric': 'revived_more_3y_sum', 'params': ['c']},
        {'metric': 'revived_more_5y_sum', 'params': ['c']},
        {'metric': 'sth_sum', 'params': ['c']},
        {'metric': 'sth_loss_sum', 'params': ['c']},
        {'metric': 'sth_profit_sum', 'params': ['c']},
        {'metric': 'loss_sum', 'params': ['c']},
        {'metric': 'profit_sum', 'params': ['c']},
        {'metric': 'active_24h', 'params': ['c']},
        {'metric': 'active_more_10y', 'params': ['c']},
        {'metric': 'active_1d_1w', 'params': ['c']},
        {'metric': 'active_1m_3m', 'params': ['c']},
        {'metric': 'active_1w_1m', 'params': ['c']},
        {'metric': 'active_1y_2y', 'params': ['c']},
        {'metric': 'active_2y_3y', 'params': ['c']},
        {'metric': 'active_3m_6m', 'params': ['c']},
        {'metric': 'active_3y_5y', 'params': ['c']},
        {'metric': 'active_5y_7y', 'params': ['c']},
        {'metric': 'active_6m_12m', 'params': ['c']},
        {'metric': 'active_7y_10y', 'params': ['c']},
        {'metric': 'tips', 'params': ['c']},
    ],
    'transactions': [
        {'metric': 'transfers_to_exchanges_count', 'params': ['c', 'e']},
        {'metric': 'transfers_volume_to_exchanges_mean', 'params': ['c', 'e']},
        {'metric': 'transfers_volume_to_exchanges_sum', 'params': ['c', 'e']},
        {'metric': 'transfers_volume_exchanges_net', 'params': ['c', 'e']},
        {'metric': 'transfers_volume_from_exchanges_mean', 'params': ['c', 'e']},
        {'metric': 'transfers_volume_from_exchanges_sum', 'params': ['c', 'e']},
        {'metric': 'transfers_from_exchanges_count', 'params': ['c', 'e']},
        {'metric': 'transfers_volume_within_exchanges_sum', 'params': ['c', 'e']},
    #     {'metric': 'transfers_between_exchanges_count', 'params': ['from_exchange', 'to_exchange']},
    #     {'metric': 'transfers_volume_between_exchanges_sum', 'params': ['c', 'from_exchange', 'to_exchange']},
        {'metric': 'transfers_to_miners_count', 'params': ['miner']},
        {'metric': 'transfers_volume_to_miners_sum', 'params': ['c', 'miner']},
        {'metric': 'transfers_volume_miners_net', 'params': ['c', 'miner']},
        {'metric': 'transfers_volume_from_miners_sum', 'params': ['c', 'miner']},
        {'metric': 'transfers_from_miners_count', 'params': ['miner']},
        {'metric': 'transfers_volume_miners_to_exchanges', 'params': ['c', 'e']},
        {'metric': 'transfers_volume_miners_to_exchanges_all', 'params': ['c', 'e']},
    ]
}


# Combined exchange list for all metrics
EXCHANGES = [
    'aggregated', 'binance', 'bitfinex', 'bitflyer', 'bitmex', 'bitstamp', 'bittrex', 'bybit',
    'coinbase', 'coincheck', 'deribit', 'ftx', 'gate.io', 'gemini', 'huobi', 'kraken', 'kucoin',
    'okex', 'poloniex'
]


def fetch_miner_list(metric):
    url = f"{BASE_URL}/mining/{metric}/miners"
    params = {
        'a': ASSET,
        'api_key': GLASSNODE_API_KEY
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        miners = response.json().get(ASSET, [])
        logging.info(f"Fetched miner list for {metric}: {miners}")
        return miners
    except requests.RequestException as e:
        logging.error(f"Error fetching miner list for {metric}: {e}")
        return None

def fetch_exchange_list(metric):
    url = f"{BASE_URL}/transactions/{metric}/flows"
    params = {
        'a': ASSET,
        'api_key': GLASSNODE_API_KEY
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching exchange list for {metric}: {e}")
        return None

def fetch_glassnode_data(endpoint, metric, start_timestamp, end_timestamp, params):
    url = f"{BASE_URL}/{endpoint}/{metric}"
    params = {
        'a': ASSET,
        's': start_timestamp,
        'u': end_timestamp,
        'i': INTERVAL,
        'api_key': GLASSNODE_API_KEY,
        **params
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching data for {endpoint}/{metric}: {e}")
        return None

def fetch_exchange_list(metric):
    url = f"{BASE_URL}/transactions/{metric}/flows"
    params = {
        'a': ASSET,
        'api_key': GLASSNODE_API_KEY
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get(ASSET, [])
    except requests.RequestException as e:
        logging.error(f"Error fetching exchange list for {metric}: {e}")
        return None

def fetch_miner_list(metric):
    url = f"{BASE_URL}/mining/{metric}/miners"
    params = {
        'a': ASSET,
        'api_key': GLASSNODE_API_KEY
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        miners = response.json().get(ASSET, [])
        logging.info(f"Fetched miner list for {metric}: {miners}")
        return miners
    except requests.RequestException as e:
        logging.error(f"Error fetching miner list for {metric}: {e}")
        return None


def fetch_and_save_data(start_date, end_date):
    start_timestamp = int(datetime.combine(start_date, datetime.min.time()).replace(tzinfo=timezone.utc).timestamp())
    end_timestamp = int(end_date.timestamp())

    data_folder = FOLDER_NAME
    os.makedirs(data_folder, exist_ok=True)

    for endpoint, metrics in tqdm(ENDPOINTS.items(), desc="Fetching endpoints"):
        for metric_info in tqdm(metrics, desc=f"Fetching metrics for {endpoint}", leave=False):
            metric = metric_info['metric']
            params = metric_info['params']

            base_params = {
                'a': ASSET,
                's': start_timestamp,
                'u': end_timestamp,
                'i': INTERVAL,
                'api_key': GLASSNODE_API_KEY,
            }

            param_combinations = [{}]
            if 'c' in params:
                param_combinations = [{'c': curr} for curr in CURRENCIES]
            if 'e' in params:
                param_combinations = [dict(p, e=exch) for p in param_combinations for exch in EXCHANGES]
            if 'm' in params:
                miners = fetch_miner_list(metric)
                if miners:
                    param_combinations = [dict(p, m=miner) for p in param_combinations for miner in miners]

            for param_combo in param_combinations:
                request_params = {**base_params, **param_combo}

                data = fetch_glassnode_data(endpoint, metric, start_timestamp, end_timestamp, request_params)

                if data:
                    df = pd.DataFrame(data)
                    if 't' in df.columns and 'v' in df.columns:
                        df['Date'] = pd.to_datetime(df['t'], unit='s')
                        df = df.rename(columns={'v': metric})
                        df = df[['Date', metric]].set_index('Date').sort_index()

                        filename_parts = [endpoint, metric, ASSET]
                        for key, value in param_combo.items():
                            filename_parts.append(f"{key}_{value}")

                        csv_filename = os.path.join(data_folder, "_".join(filename_parts) + ".csv")

                        df.to_csv(csv_filename)
                        logging.info(f"Saved data for {endpoint}/{metric} to {csv_filename}")
                    else:
                        logging.warning(f"Unexpected data format for {endpoint}/{metric}. Skipping.")
                else:
                    logging.warning(f"No data available for {endpoint}/{metric} ({request_params})")

if __name__ == "__main__":
    start_date = datetime(2020, 1, 1, tzinfo=timezone.utc).date()
    end_date = datetime.now(timezone.utc)
    fetch_and_save_data(start_date, end_date)