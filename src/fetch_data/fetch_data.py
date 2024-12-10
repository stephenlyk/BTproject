import os
from datetime import datetime, timezone
from data_handler import DataHandler
import logging
from tqdm import tqdm
import pandas as pd
from multiprocessing import Pool, cpu_count
from functools import partial

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
GLASSNODE_API_KEY = '2ixuRhqosLHPpClDohgjZJsEEyp'
ASSET = 'BTC'
INTERVAL = '24h'
FOLDER_NAME = 'glassnode_data_btc24h_Dec2024'
MAX_WORKERS = cpu_count() - 1

def process_metric(metric, data_handler, start_timestamp, end_timestamp):
    """Process a single metric"""
    try:
        data = data_handler.prepare_specific_data(start_timestamp, end_timestamp, metric)

        if data is None:
            logging.warning(f"No data available for metric: {metric}.")
            return

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

    except Exception as e:
        logging.error(f"Error processing metric {metric}: {str(e)}")

def process_metrics_chunk(metrics_chunk, data_handler, start_timestamp, end_timestamp):
    """Process a chunk of metrics"""
    for metric in metrics_chunk:
        process_metric(metric, data_handler, start_timestamp, end_timestamp)

def fetch_and_save_data(start_date, end_date):
    # Convert to UTC timestamp with time components
    start_timestamp = int(datetime(start_date.year, start_date.month, start_date.day,
                                 tzinfo=timezone.utc).timestamp())
    end_timestamp = int(end_date.timestamp())

    data_handler = DataHandler(GLASSNODE_API_KEY, ASSET, INTERVAL, FOLDER_NAME)

    # Fetch all available metrics
    all_metrics = data_handler.fetch_glassnode_metrics()
    logging.info(f"Total metrics available: {len(all_metrics)}")

    # Calculate chunk size and split metrics into chunks
    chunk_size = max(1, len(all_metrics) // MAX_WORKERS)
    metrics_chunks = [all_metrics[i:i + chunk_size]
                     for i in range(0, len(all_metrics), chunk_size)]

    # Create partial function with fixed parameters
    process_chunk = partial(process_metrics_chunk,
                          data_handler=data_handler,
                          start_timestamp=start_timestamp,
                          end_timestamp=end_timestamp)

    # Use multiprocessing to process chunks in parallel
    with Pool(processes=MAX_WORKERS) as pool:
        list(tqdm(
            pool.imap(process_chunk, metrics_chunks),
            total=len(metrics_chunks),
            desc="Processing metric chunks"
        ))

if __name__ == "__main__":
    start_date = datetime(2020, 1, 1, tzinfo=timezone.utc).date()
    end_date = datetime.now(timezone.utc)
    fetch_and_save_data(start_date, end_date)