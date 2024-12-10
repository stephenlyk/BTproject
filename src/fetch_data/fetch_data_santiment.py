import os
from datetime import datetime, timezone, timedelta
import san
import pandas as pd
from tqdm import tqdm
import logging
from multiprocessing import Pool, cpu_count
from functools import partial

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SANTIMENT_API_KEY = 'dlpuyo2zmkqrwtq3_yb7sjowvpd3nt334'
ASSET = 'bitcoin'
FOLDER_NAME = 'santiment_data_btc_1h_Dec2024'
MAX_WORKERS = cpu_count() - 1

san.ApiConfig.api_key = SANTIMENT_API_KEY


def verify_hourly_data(df):
    """Verify if the data is actually hourly"""
    if df is None or df.empty or len(df) < 2:
        return False

    # Convert index to datetime if it's not already
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    # Calculate time differences
    time_diffs = df.index.to_series().diff()

    # Allow for some small deviation (e.g., 59-61 minutes)
    is_hourly = time_diffs.median().total_seconds() >= 3540 and time_diffs.median().total_seconds() <= 3660

    return is_hourly


def process_metric(metric, start_date, end_date):
    """Process a single metric"""
    try:
        # Try fetching 24 hours of data first to test if hourly granularity is supported
        test_end = datetime.now(timezone.utc)
        test_start = test_end - timedelta(days=1)

        df_test = san.get(
            f"{metric}/{ASSET}",
            from_date=test_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            to_date=test_end.strftime("%Y-%m-%dT%H:%M:%SZ"),
            interval="1h"
        )

        if df_test is None or df_test.empty:
            logging.warning(f"No data available for metric: {metric}")
            return

        if not verify_hourly_data(df_test):
            logging.info(f"Skipping metric {metric} - does not support hourly resolution")
            return

        # If hourly data is supported, fetch the full date range
        df = san.get(
            f"{metric}/{ASSET}",
            from_date=start_date,
            to_date=end_date,
            interval="1h"
        )

        if df is None or df.empty:
            logging.warning(f"No data available for metric: {metric}")
            return

        # Convert the index to date string format
        df.index = df.index.strftime('%Y-%m-%d %H:%M:%S')

        # Rename the column to match the metric name
        df.columns = [metric]

        # Reset the index to make the date a column
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'Date'}, inplace=True)

        csv_filename = os.path.join(FOLDER_NAME, f"{metric.replace('/', '_')}.csv")
        df.to_csv(csv_filename, index=False)
        logging.info(f"Saved hourly data for {metric} to {csv_filename}")

    except Exception as e:
        logging.error(f"Error processing metric {metric}: {str(e)}")


def process_metrics_chunk(metrics_chunk, start_date, end_date):
    """Process a chunk of metrics"""
    for metric in metrics_chunk:
        process_metric(metric, start_date, end_date)


def fetch_and_save_data(start_date, end_date):
    """Fetch and save data using multiprocessing"""
    os.makedirs(FOLDER_NAME, exist_ok=True)

    # Fetch all available metrics
    available_metrics = san.available_metrics_for_slug(ASSET)
    logging.info(f"Total metrics available: {len(available_metrics)}")

    # Calculate chunk size and split metrics into chunks
    chunk_size = max(1, len(available_metrics) // MAX_WORKERS)
    metrics_chunks = [available_metrics[i:i + chunk_size]
                      for i in range(0, len(available_metrics), chunk_size)]

    # Create partial function with fixed dates
    process_chunk = partial(process_metrics_chunk, start_date=start_date, end_date=end_date)

    # Use multiprocessing to process chunks in parallel
    with Pool(processes=MAX_WORKERS) as pool:
        list(tqdm(
            pool.imap(process_chunk, metrics_chunks),
            total=len(metrics_chunks),
            desc="Processing metric chunks"
        ))


if __name__ == "__main__":
    start_date = "2020-01-01T00:00:00Z"
    end_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fetch_and_save_data(start_date, end_date)