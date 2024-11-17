# fetch_data_santiment.py
import os
from datetime import datetime, timezone
import san
import pandas as pd
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SANTIMENT_API_KEY = 'dlpuyo2zmkqrwtq3_yb7sjowvpd3nt334'
ASSET = 'bitcoin'
FOLDER_NAME = 'santiment_data_btc_1h_Nov2024'

san.ApiConfig.api_key = SANTIMENT_API_KEY


def fetch_and_save_data(start_date, end_date):
    os.makedirs(FOLDER_NAME, exist_ok=True)

    # Fetch all available metrics
    available_metrics = san.available_metrics_for_slug(ASSET)
    logging.info(f"Total metrics available: {len(available_metrics)}")

    for metric in tqdm(available_metrics, desc="Fetching and saving data"):
        try:
            df = san.get(
                f"{metric}/{ASSET}",
                from_date=start_date,
                to_date=end_date,
                interval="60m"
            )

            if df is None or df.empty:
                logging.warning(f"No data available for metric: {metric}")
                continue

            # Convert the index to date string format 'YYYY-MM-DD'
            df.index = df.index.strftime('%Y-%m-%d %H:%M:%S')

            # Rename the column to match the metric name
            df.columns = [metric]

            # Reset the index to make the date a column
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'Date'}, inplace=True)

            csv_filename = os.path.join(FOLDER_NAME, f"{metric.replace('/', '_')}.csv")
            df.to_csv(csv_filename, index=False)
            logging.info(f"Saved data for {metric} to {csv_filename}")

        except Exception as e:
            logging.error(f"Error fetching data for metric {metric}: {str(e)}")


if __name__ == "__main__":
    start_date = "2020-01-01T00:00:00Z"
    end_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    fetch_and_save_data(start_date, end_date)