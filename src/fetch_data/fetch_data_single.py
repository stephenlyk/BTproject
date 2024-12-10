import os
from datetime import datetime, timezone
import logging
import pandas as pd
import requests
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from functools import partial

CURRENCIES = ['NATIVE', 'USD']
EXCHANGES = ['aggregated', 'binance', 'bitfinex', 'bitflyer', 'bitmex', 'bitstamp', 'bittrex', 'bybit',
             'coinbase', 'coincheck', 'deribit', 'ftx', 'gate.io', 'gemini', 'huobi', 'kraken', 'kucoin',
             'okex', 'poloniex']

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

GLASSNODE_API_KEY = '2ixuRhqosLHPpClDohgjZJsEEyp'
ASSET = 'BTC'
INTERVAL = '24h'
BASE_URL = 'https://api.glassnode.com/v1/metrics'
FOLDER_NAME = 'glassnode_data_Dec2024_24h'

ENDPOINTS = {
    'supply': [
        {'metric': 'lth_sth_profit_loss_relative', 'is_breakdown': True},
        {'metric': 'realized_profit_loss_lth_sth_to_exchanges_relative', 'is_breakdown': True},
        {'metric': 'transfers_volume_entity_adjusted_from_lth_sth_profit_loss_relative', 'is_breakdown': True},
        {'metric': 'svab_entity_adjusted', 'is_breakdown': True},
    ],

    'breakdowns': [
        {'metric': 'realized_loss_by_lth_sth', 'is_breakdown': True},
        {'metric': 'realized_loss_by_pnl', 'is_breakdown': True},
        {'metric': 'realized_loss_by_wallet_size', 'is_breakdown': True},
        {'metric': 'realized_loss_by_age', 'is_breakdown': True},
        {'metric': 'realized_profit_by_pnl', 'is_breakdown': True},
        {'metric': 'realized_profit_by_wallet_size', 'is_breakdown': True},
        {'metric': 'realized_profit_by_age', 'is_breakdown': True},
        {'metric': 'realized_profit_by_lth_sth', 'is_breakdown': True},
        {'metric': 'sopr_by_age', 'is_breakdown': True},
        {'metric': 'sopr_by_pnl', 'is_breakdown': True},
        {'metric': 'sopr_by_wallet_size', 'is_breakdown': True},
        {'metric': 'sopr_by_lth_sth', 'is_breakdown': True},
        {'metric': 'spent_volume_sum_by_age', 'is_breakdown': True},
        {'metric': 'spent_volume_sum_by_pnl', 'is_breakdown': True},
        {'metric': 'spent_volume_sum_by_wallet_size', 'is_breakdown': True},
        {'metric': 'spent_volume_sum_by_lth_sth', 'is_breakdown': True},
        {'metric': 'spent_volume_profit_sum_by_age', 'is_breakdown': True},
        {'metric': 'spent_volume_profit_sum_by_wallet_size', 'is_breakdown': True},
        {'metric': 'spent_volume_profit_sum_by_lth_sth', 'is_breakdown': True},
        {'metric': 'spent_volume_loss_sum_by_age', 'is_breakdown': True},
        {'metric': 'spent_volume_loss_sum_by_wallet_size', 'is_breakdown': True},
        {'metric': 'spent_volume_loss_sum_by_lth_sth', 'is_breakdown': True},
        {'metric': 'supply_by_age', 'is_breakdown': True},
        {'metric': 'supply_by_wallet_size', 'is_breakdown': True},
        {'metric': 'marketcap_usd_by_age', 'is_breakdown': True},
        {'metric': 'marketcap_usd_by_wallet_size', 'is_breakdown': True},
        {'metric': 'marketcap_realized_usd_by_age', 'is_breakdown': True},
        {'metric': 'marketcap_realized_usd_by_wallet_size', 'is_breakdown': True},
        {'metric': 'mvrv_by_age', 'is_breakdown': True},
        {'metric': 'mvrv_by_wallet_size', 'is_breakdown': True},
        {'metric': 'price_realized_usd_by_age', 'is_breakdown': True},
        {'metric': 'price_realized_usd_by_wallet_size', 'is_breakdown': True},
    ],
}


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


def process_metric(endpoint_metric_tuple, start_timestamp, end_timestamp, data_folder):
    endpoint, metric_info = endpoint_metric_tuple
    metric = metric_info['metric']
    is_breakdown = metric_info.get('is_breakdown', False)

    try:
        base_params = {}  # Empty base params since no additional parameters needed
        data = fetch_glassnode_data(endpoint, metric, start_timestamp, end_timestamp, base_params)

        if data:
            if is_breakdown and isinstance(data[0], dict):
                # Handle breakdown metrics with multiple columns
                df = pd.DataFrame(data)

                # Convert timestamp to datetime
                if 't' in df.columns:
                    df['timestamp'] = pd.to_datetime(df['t'], unit='s')
                    df = df.drop('t', axis=1)

                    # If 'o' column exists and contains dictionaries, expand it
                    if 'o' in df.columns and isinstance(df['o'].iloc[0], dict):
                        df_expanded = pd.json_normalize(df['o'])
                        df = pd.concat([df[['timestamp']], df_expanded], axis=1)

                    df = df.set_index('timestamp').sort_index()

                    # Split into separate CSV files, one for each metric
                    for column in df.columns:
                        # Create a new dataframe with just timestamp and the current column
                        df_single = df[[column]].copy()
                        df_single.reset_index(inplace=True)  # Make timestamp a regular column

                        # Create filename
                        filename_parts = [endpoint, metric, ASSET, column]
                        csv_filename = os.path.join(data_folder, "_".join(filename_parts) + ".csv")

                        # Save to CSV
                        df_single.columns = ['timestamp', 'value']  # Rename columns to standard names
                        df_single.to_csv(csv_filename, index=False)
                        logging.info(f"Saved data for {endpoint}/{metric}/{column} to {csv_filename}")
            else:
                # Handle regular metrics with two columns
                df = pd.DataFrame(data)
                if 't' in df.columns and 'v' in df.columns:
                    df['timestamp'] = pd.to_datetime(df['t'], unit='s')
                    df = df.rename(columns={'v': 'value'})
                    df = df[['timestamp', 'value']]

                    filename_parts = [endpoint, metric, ASSET]
                    csv_filename = os.path.join(data_folder, "_".join(filename_parts) + ".csv")

                    df.to_csv(csv_filename, index=False)
                    logging.info(f"Saved data for {endpoint}/{metric} to {csv_filename}")

        else:
            logging.warning(f"No data available for {endpoint}/{metric}")

    except Exception as e:
        logging.error(f"Error processing {endpoint}/{metric}: {str(e)}")


def fetch_and_save_data(start_date, end_date):
    start_timestamp = int(datetime.combine(start_date, datetime.min.time()).replace(tzinfo=timezone.utc).timestamp())
    end_timestamp = int(end_date.timestamp())

    data_folder = FOLDER_NAME
    os.makedirs(data_folder, exist_ok=True)

    all_metrics = []
    for endpoint, metrics in ENDPOINTS.items():
        for metric_info in metrics:
            all_metrics.append((endpoint, metric_info))

    num_processes = max(1, cpu_count() - 1)

    process_metric_partial = partial(
        process_metric,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        data_folder=data_folder
    )

    with Pool(processes=num_processes) as pool:
        list(tqdm(
            pool.imap(process_metric_partial, all_metrics),
            total=len(all_metrics),
            desc="Processing metrics"
        ))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'glassnode_fetch_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
            logging.StreamHandler()
        ]
    )

    start_date = datetime(2020, 1, 1, tzinfo=timezone.utc).date()
    end_date = datetime.now(timezone.utc)
    fetch_and_save_data(start_date, end_date)