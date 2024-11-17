import os
from datetime import datetime, timezone, timedelta
import san
import pandas as pd
from tqdm import tqdm
import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set the API key
SANTIMENT_API_KEY = 'dlpuyo2zmkqrwtq3_yb7sjowvpd3nt334'
san.ApiConfig.api_key = SANTIMENT_API_KEY


def extract_metrics_from_csv(csv_path: str) -> list:
    """Extract metric names from the CSV file."""
    df = pd.read_csv(csv_path)
    metrics = []
    for path in df['Metric']:
        metric = os.path.basename(path).replace('.csv', '')
        metric = metric.replace('_change_30d', '')
        metrics.append(metric)
    return metrics


def check_specific_metrics_freshness(metrics: list,
                                     asset: str = 'bitcoin',
                                     lookback_hours: int = 48) -> Dict[str, Optional[dict]]:
    """
    Check the latest available timestamp for specified Santiment metrics.
    """
    current_utc = datetime.now(timezone.utc)
    start_date = (current_utc - timedelta(hours=lookback_hours)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end_date = current_utc.strftime("%Y-%m-%dT%H:%M:%SZ")

    metric_freshness = {}

    print(f"\nChecking data freshness:")
    print(f"Current UTC: {current_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"Looking back {lookback_hours} hours")
    print("-" * 80)

    for metric in tqdm(metrics, desc="Checking metric freshness"):
        try:
            df = san.get(
                f"{metric}/{asset}",
                from_date=start_date,
                to_date=end_date,
                interval="60m"
            )

            if df is not None and not df.empty:
                latest_timestamp = df.index[-1]
                time_lag = current_utc - latest_timestamp
                update_frequency = pd.Series(df.index).diff().median()

                metric_freshness[metric] = {
                    'latest_timestamp': latest_timestamp,
                    'lag_hours': time_lag.total_seconds() / 3600,
                    'lag_minutes': time_lag.total_seconds() / 60,
                    'update_frequency_hours': update_frequency.total_seconds() / 3600,
                    'data_points': len(df)
                }
            else:
                metric_freshness[metric] = None

        except Exception as e:
            logging.error(f"Error checking {metric}: {str(e)}")
            metric_freshness[metric] = {
                'status': 'Error',
                'message': str(e)
            }

    return metric_freshness


def print_detailed_metric_summary(metric_freshness: Dict[str, dict]) -> None:
    """
    Print a detailed summary of metric freshness with lag times and update frequencies.
    """
    print("\nDetailed Metric Freshness Summary:")
    print("=" * 100)
    print(f"{'Metric':<40} {'Latest Data':<25} {'Lag Time':<15} {'Update Freq':<15} {'Points'}")
    print("-" * 100)

    # Sort metrics by lag time
    available_metrics = []
    error_metrics = []

    for metric, info in metric_freshness.items():
        if info is None:
            error_metrics.append((metric, "No data available"))
        elif 'status' in info:
            error_metrics.append((metric, info['message']))
        else:
            available_metrics.append((metric, info))

    # Print available metrics sorted by lag time
    for metric, info in sorted(available_metrics, key=lambda x: x[1]['lag_minutes']):
        latest = info['latest_timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        lag_hours = info['lag_hours']

        if lag_hours >= 1:
            lag_str = f"{lag_hours:.1f}h"
        else:
            lag_str = f"{info['lag_minutes']:.1f}m"

        update_freq = f"{info['update_frequency_hours']:.1f}h"
        points = info['data_points']

        print(f"{metric:<40} {latest:<25} {lag_str:<15} {update_freq:<15} {points}")

    # Print metrics with errors
    if error_metrics:
        print("\nMetrics with Errors:")
        print("-" * 80)
        for metric, error in error_metrics:
            print(f"- {metric}: {error}")


if __name__ == "__main__":
    # Path to your CSV file
    csv_path = '/Users/stephenlyk/Desktop/Strategy Bank/BTC1H/28Oct2024/all_strategies_results.csv'

    # Extract metrics from CSV
    metrics = extract_metrics_from_csv(csv_path)

    # Check freshness of specific metrics
    metric_freshness = check_specific_metrics_freshness(metrics)
    print_detailed_metric_summary(metric_freshness)