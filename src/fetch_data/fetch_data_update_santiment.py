# fetch_selected_santiment.py
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
FOLDER_NAME = 'santiment_data_btc_1h_Oct2024_selected'

san.ApiConfig.api_key = SANTIMENT_API_KEY

def extract_metric_name(filepath):
    """Extract the metric name from the filepath in the CSV."""
    # Get the filename part
    filename = filepath.split('/')[-1]
    # Remove the .csv extension
    metric_name = filename.rsplit('.', 1)[0]
    return metric_name

def get_available_metrics():
    """Get all available metrics for the asset."""
    try:
        available_metrics = san.available_metrics_for_slug(ASSET)
        return available_metrics
    except Exception as e:
        logging.error(f"Error fetching available metrics: {str(e)}")
        return []

def fetch_selected_data(start_date, end_date, metrics_file):
    """Fetch selected metrics from Santiment."""
    os.makedirs(FOLDER_NAME, exist_ok=True)

    # Get all available metrics
    available_metrics = get_available_metrics()
    logging.info(f"Total available metrics from Santiment: {len(available_metrics)}")

    # Read the metrics from the CSV file
    df = pd.read_csv(metrics_file)
    selected_metrics = []

    # Extract metric names from file paths
    for filepath in df['Metric']:
        metric_name = extract_metric_name(filepath)
        # Check if metric exists in available metrics
        if metric_name in available_metrics:
            selected_metrics.append(metric_name)
            logging.info(f"Found matching metric: {metric_name}")
        else:
            logging.warning(f"Metric not available: {metric_name}")

    logging.info(f"Found {len(selected_metrics)} metrics to fetch")

    # Fetch data for each metric
    for metric in tqdm(selected_metrics, desc="Fetching selected metrics"):
        try:
            # Fetch data from Santiment
            df = san.get(
                f"{metric}/{ASSET}",
                from_date=start_date,
                to_date=end_date,
                interval="60m"
            )

            if df is None or df.empty:
                logging.warning(f"No data available for metric: {metric}")
                continue

            # Format the dataframe
            df.index = df.index.strftime('%Y-%m-%d %H:%M:%S')
            df.columns = [metric]
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'Date'}, inplace=True)

            # Save to CSV
            csv_filename = os.path.join(FOLDER_NAME, f"{metric}.csv")
            df.to_csv(csv_filename, index=False)
            logging.info(f"Saved data for {metric} to {csv_filename}")

        except Exception as e:
            logging.error(f"Error fetching data for metric {metric}: {str(e)}")
            continue

def main():
    # Set up date range
    start_date = "2020-01-01T00:00:00Z"
    end_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    metrics_file = '/Users/stephenlyk/Desktop/Strategy Bank/BTC1H/28Oct2024/Book12.csv'  # Make sure this file is in the same directory

    try:
        fetch_selected_data(start_date, end_date, metrics_file)
    except Exception as e:
        logging.error(f"An error occurred during execution: {str(e)}")
    finally:
        logging.info("Script execution completed")

if __name__ == "__main__":
    main()