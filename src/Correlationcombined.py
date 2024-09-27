import pandas as pd
import numpy as np
import requests
from datetime import datetime
from strategy.strategy import Strategy
from strategy.robust import Robust
from strategy.min_max import MinMax
from strategy.z_score import ZScore
from strategy.moving_average import MovingAverage
from strategy.roc import ROC
from strategy.percentile import Percentile
from joblib import Parallel, delayed
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
BASE_PATH_10M = "/Users/stephenlyk/Desktop/Gnproject/glassnode_data_BTC10m"
BASE_PATH_1H = "/Users/stephenlyk/Desktop/Gnproject/glassnode_data_btc1h"
SHORTLIST_PATH_10M = "/Users/stephenlyk/Desktop/Strategy Bank/BTC10m/10Sept2024/all_strategies_results10m.csv"
SHORTLIST_PATH_1H = "/Users/stephenlyk/Desktop/Strategy Bank/BTC1H/10Sept2024/all_strategies_results1h.csv"
ASSET = 'BTC'
GLASSNODE_API_KEY = '2ixuRhqosLHPpClDohgjZJsEEyp'  # Replace with your actual API key

def get_multiplier(interval):
    if interval == '10m':
        return 365 * 24 * 6  # 6 ten-minute intervals per hour
    elif interval == '1h':
        return 365 * 24
    elif interval == '1d':
        return 365
    else:
        raise ValueError(f"Unsupported interval: {interval}")

def fetch_glassnode_data(interval):
    url = f"https://api.glassnode.com/v1/metrics/market/price_usd_close"
    params = {
        'a': ASSET,
        'i': interval,
        'api_key': GLASSNODE_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.columns = ['Date', 'Price']
        df['Date'] = pd.to_datetime(df['Date'], unit='s')
        df.set_index('Date', inplace=True)
        return df
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def get_strategy_class(strategy_name):
    strategy_map = {
        'Robust': Robust,
        'MinMax': MinMax,
        'ZScore': ZScore,
        'MovingAverage': MovingAverage,
        'ROC': ROC,
        'Percentile': Percentile
    }
    return strategy_map.get(strategy_name, Strategy)

def process_metric(row, btc_price_df, base_path):
    metric_file = row['Metric']
    if pd.isna(metric_file) or metric_file.strip() == '':
        print(f"Skipping row with empty metric file: {row}")
        return None

    if not metric_file.startswith(base_path):
        metric_file = os.path.join(base_path, os.path.basename(metric_file))

    print(f"Attempting to read file: {metric_file}")

    metric_name = os.path.basename(metric_file).split('.')[0]

    try:
        metric_df = pd.read_csv(metric_file)
        metric_df.columns = ['Date', 'Value']
        metric_df['Date'] = pd.to_datetime(metric_df['Date'])
        metric_df.set_index('Date', inplace=True)
        metric_df['Value'] = metric_df['Value'].shift(2)
        metric_df = metric_df.dropna()

        merged_df = metric_df.join(btc_price_df, how='inner')

        StrategyClass = get_strategy_class(row['Strategy'])

        strategy = StrategyClass(
            source_df=merged_df,
            window_size=int(row['Best Window']),
            threshold=row['Best Threshold'],
            target='Value',
            price='Price',
            long_short=row['Long_Short'],
            condition=row['Condition'].lower()
        )

        result_df = strategy.result_df

        return pd.Series(result_df['Profit'], name=f"{metric_name}_{row['Strategy']}_{row['Long_Short']}_{row['Condition']}")

    except FileNotFoundError:
        print(f"File not found: {metric_file}")
        return None
    except Exception as e:
        print(f"Error processing {metric_file}: {str(e)}")
        return None


def process_resolution(shortlist_path, base_path, interval):
    shortlist_df = pd.read_csv(shortlist_path)
    btc_price_df = fetch_glassnode_data(interval)

    results = Parallel(n_jobs=-1)(
        delayed(process_metric)(row, btc_price_df, base_path) for _, row in shortlist_df.iterrows())
    all_profits_df = pd.concat([r for r in results if r is not None], axis=1)

    return all_profits_df, btc_price_df


def resample_and_align_data(df_10m, df_1h):
    # Ensure the index is datetime
    df_10m.index = pd.to_datetime(df_10m.index)
    df_1h.index = pd.to_datetime(df_1h.index)

    # Resample 1h data to 10m
    df_1h_resampled = df_1h.resample('10T').ffill()

    # Adjust the 1h profits for 10m scale
    df_1h_resampled = df_1h_resampled / 6  # Divide by 6 as there are 6 10-minute periods in an hour

    # Align the resampled 1h data with 10m data
    aligned_df = pd.concat([df_10m, df_1h_resampled], axis=1)

    # Forward fill any missing values
    aligned_df = aligned_df.fillna(method='ffill')

    return aligned_df


def main():
    # Process 10-minute resolution
    all_profits_10m, btc_price_10m = process_resolution(SHORTLIST_PATH_10M, BASE_PATH_10M, '10m')

    # Process 1-hour resolution
    all_profits_1h, btc_price_1h = process_resolution(SHORTLIST_PATH_1H, BASE_PATH_1H, '1h')

    # Resample and align the data
    combined_profits = resample_and_align_data(all_profits_10m, all_profits_1h)

    # Calculate combined strategy profit
    combined_profits['Combined_Profit'] = combined_profits.mean(axis=1)
    combined_profits['Cumulative_Profit'] = combined_profits['Combined_Profit'].cumsum()

    # Use 10m BTC price for Buy and Hold comparison
    combined_profits['BnH_Returns'] = btc_price_10m['Price'].pct_change()
    combined_profits['BnH_Cumulative'] = combined_profits['BnH_Returns'].cumsum()

    # Calculate performance metrics
    multiplier = get_multiplier('10m')  # Use 10m multiplier for annualization
    annual_return = combined_profits['Combined_Profit'].mean() * multiplier * 100
    sharpe_ratio = combined_profits['Combined_Profit'].mean() / combined_profits['Combined_Profit'].std() * np.sqrt(
        multiplier)
    max_drawdown = (combined_profits['Cumulative_Profit'] - combined_profits['Cumulative_Profit'].cummax()).min() * 100
    calmar_ratio = annual_return / abs(max_drawdown)

    bnh_annual_return = combined_profits['BnH_Returns'].mean() * multiplier * 100
    bnh_sharpe_ratio = combined_profits['BnH_Returns'].mean() / combined_profits['BnH_Returns'].std() * np.sqrt(
        multiplier)
    bnh_max_drawdown = (combined_profits['BnH_Cumulative'] - combined_profits['BnH_Cumulative'].cummax()).min() * 100
    bnh_calmar_ratio = bnh_annual_return / abs(bnh_max_drawdown)

    # Create equity curve plot
    plt.figure(figsize=(12, 8))
    plt.plot(combined_profits.index, combined_profits['Cumulative_Profit'] * 100, label='Combined Strategy')
    plt.plot(combined_profits.index, combined_profits['BnH_Cumulative'] * 100, label='Buy and Hold')
    plt.title('Equity Curve of Combined Strategy (10m and 1h) vs Buy and Hold')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Profit (%)')
    plt.legend()

    # Add performance metrics to the plot
    metrics_text = (
        f'Combined Strategy:\n'
        f'Annual Return: {annual_return:.2f}%\n'
        f'Sharpe Ratio: {sharpe_ratio:.2f}\n'
        f'Max Drawdown: {max_drawdown:.2f}%\n'
        f'Calmar Ratio: {calmar_ratio:.2f}\n\n'
        f'Buy and Hold:\n'
        f'Annual Return: {bnh_annual_return:.2f}%\n'
        f'Sharpe Ratio: {bnh_sharpe_ratio:.2f}\n'
        f'Max Drawdown: {bnh_max_drawdown:.2f}%\n'
        f'Calmar Ratio: {bnh_calmar_ratio:.2f}'
    )
    plt.text(0.02, 0.98, metrics_text, transform=plt.gca().transAxes, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8), fontsize=8)

    plt.tight_layout()
    plt.savefig('equity_curve_combined_10m_1h.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("\nEquity curve with Buy and Hold saved as 'equity_curve_combined_10m_1h.png'")

    # Save all profits to a CSV file
    output_file = 'all_metrics_profits_combined.csv'
    combined_profits.to_csv(output_file)
    print(f"\nAll metrics profits saved to {output_file}")

    # Calculate correlation matrix
    correlation_matrix = combined_profits.drop(
        ['Combined_Profit', 'Cumulative_Profit', 'BnH_Cumulative', 'BnH_Returns'], axis=1).corr()

    # Save the correlation matrix to a CSV file
    correlation_matrix.to_csv('correlation_matrix_combined.csv')
    print("\nCorrelation matrix saved to 'correlation_matrix_combined.csv'")

    # Create a heatmap of the correlation matrix with values
    plt.figure(figsize=(30, 24))  # Large figure size for better readability

    # Create heatmap
    sns.heatmap(correlation_matrix,
                annot=True,  # Show the correlation values
                fmt=".2f",  # Format to 2 decimal places
                cmap='coolwarm',
                vmin=-1,
                vmax=1,
                center=0,
                square=True,  # Make each cell square-shaped
                linewidths=.5,  # Add lines between cells
                cbar_kws={"shrink": .8})

    # Rotate x-axis labels
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)

    # Set title and adjust layout
    plt.title('Correlation Heatmap of Strategy Profits (Combined 10m and 1h)', fontsize=20)
    plt.tight_layout()

    # Save the figure
    plt.savefig('correlation_heatmap_full_combined.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("\nFull correlation heatmap with values saved as 'correlation_heatmap_full_combined.png'")


if __name__ == "__main__":
    main()