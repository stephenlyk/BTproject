# fetch_data.py
import os
from datetime import datetime, timezone
from data_handler import DataHandler
import logging
from tqdm import tqdm
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
GLASSNODE_API_KEY = '2ixuRhqosLHPpClDohgjZJsEEyp'
ASSET = 'BTC'
INTERVAL = '1h'
FOLDER_NAME = 'glassnode_data_btc1h_Nov2024'


def fetch_and_save_data(start_date, end_date):
    # Convert to UTC timestamp with time components
    start_timestamp = int(datetime(start_date.year, start_date.month, start_date.day,
                                   tzinfo=timezone.utc).timestamp())
    end_timestamp = int(end_date.timestamp())

    data_handler = DataHandler(GLASSNODE_API_KEY, ASSET, INTERVAL, FOLDER_NAME)

    # Fetch all available metrics
    all_metrics = data_handler.fetch_glassnode_metrics()
    logging.info(f"Total metrics available: {len(all_metrics)}")

    for metric in tqdm(all_metrics, desc="Fetching and saving data"):
        data = data_handler.prepare_specific_data(start_timestamp, end_timestamp, metric)

        if data is None:
            logging.warning(f"No data available for metric: {metric}.")
            continue

        if isinstance(data, pd.DataFrame):
            # Non-miner specific data
            csv_filename = os.path.join(data_handler.data_folder, f"{metric.replace('/', '_')}.csv")
            data.to_csv(csv_filename, index=False)
            logging.info(f"Saved data for {metric} to {csv_filename}")
        elif isinstance(data, dict):
            # Miner-specific data
            for miner, df in data.items():
                if df is None or df.empty:
                    logging.warning(f"No data available for metric: {metric}, miner: {miner}.")
                    continue

                csv_filename = os.path.join(data_handler.data_folder, f"{metric.replace('/', '_')}_{miner}.csv")
                df.to_csv(csv_filename, index=False)
                logging.info(f"Saved data for {metric} (Miner: {miner}) to {csv_filename}")


if __name__ == "__main__":
    start_date = datetime(2020, 1, 1, tzinfo=timezone.utc).date()
    end_date = datetime.now(timezone.utc)
    fetch_and_save_data(start_date, end_date)