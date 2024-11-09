# fetch_selected_data.py
import os
from datetime import datetime, timezone
from data_handler import DataHandler
import logging
from tqdm import tqdm
import pandas as pd
import requests
from difflib import get_close_matches

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
GLASSNODE_API_KEY = '2ixuRhqosLHPpClDohgjZJsEEyp'
ASSET = 'BTC'
INTERVAL = '1h'
FOLDER_NAME = 'glassnode_data_btc1h_Oct2024_selected'


def get_all_available_metrics():
    """Fetch all available metrics from Glassnode API."""
    url = "https://api.glassnode.com/v2/metrics/endpoints"
    params = {'api_key': GLASSNODE_API_KEY}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        metrics = [item['path'] for item in data if isinstance(item, dict) and 'path' in item]
        return sorted(set(metrics))
    except requests.RequestException as e:
        logging.error(f"Error fetching metrics list: {str(e)}")
        return []


def clean_metric_name(metric):
    """Clean metric name for comparison."""
    return metric.lower().replace('/', '_').replace('.', '_').replace('-', '_')


def find_matching_metric(target_metric, available_metrics):
    """Find the matching metric from available metrics using fuzzy matching."""
    # Extract the relevant part from the filepath
    if '/' in target_metric:
        target_metric = target_metric.split('/')[-1]

    # Clean up the target metric
    target_metric = clean_metric_name(target_metric)

    # Create a list of cleaned available metrics for comparison
    cleaned_available = [(clean_metric_name(m.split('/')[-1]), m) for m in available_metrics]

    # Try exact match first
    for cleaned, original in cleaned_available:
        if cleaned == target_metric:
            return original

    # Try fuzzy matching if no exact match found
    matches = get_close_matches(target_metric, [cleaned for cleaned, _ in cleaned_available], n=1, cutoff=0.6)
    if matches:
        for cleaned, original in cleaned_available:
            if cleaned == matches[0]:
                return original

    return None


def extract_metric_from_filepath(filepath):
    """Extract the metric name from the filepath in the CSV."""
    filename = filepath.split('/')[-1]

    # Remove common prefixes and file extension
    if filename.startswith('_v1_metrics_'):
        metric = filename.replace('_v1_metrics_', '').rsplit('.', 1)[0]
    elif filename.startswith('lightning_'):
        metric = '_'.join(filename.split('_')[:2])
    elif filename.startswith('supply_'):
        metric = '_'.join(filename.split('_')[:3])
    else:
        metric = filename.rsplit('.', 1)[0]

    return metric


def fetch_selected_data(start_date, end_date, metrics_file):
    # Get all available metrics from Glassnode
    available_metrics = get_all_available_metrics()
    logging.info(f"Found {len(available_metrics)} available metrics from Glassnode")

    # Read the metrics from the CSV file
    df = pd.read_csv(metrics_file)

    # Create mapping for selected metrics
    selected_metrics = []
    for filepath in df['Metric']:
        target_metric = extract_metric_from_filepath(filepath)
        matched_metric = find_matching_metric(target_metric, available_metrics)

        if matched_metric:
            selected_metrics.append(matched_metric)
            logging.info(f"Matched '{target_metric}' to '{matched_metric}'")
        else:
            logging.warning(f"Could not find matching metric for '{target_metric}'")

    logging.info(f"Found {len(selected_metrics)} matching metrics to fetch")

    # Convert to UTC timestamp
    start_timestamp = int(datetime(start_date.year, start_date.month, start_date.day,
                                   tzinfo=timezone.utc).timestamp())
    end_timestamp = int(end_date.timestamp())

    data_handler = DataHandler(GLASSNODE_API_KEY, ASSET, INTERVAL, FOLDER_NAME)

    for metric in tqdm(selected_metrics, desc="Fetching selected metrics"):
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
    metrics_file = '/Users/stephenlyk/Desktop/Strategy Bank/BTC1H/28Oct2024/Final_list.csv' # Make sure this file is in the same directory
    fetch_selected_data(start_date, end_date, metrics_file)