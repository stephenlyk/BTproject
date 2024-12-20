import pandas as pd
import numpy as np
import requests
from datetime import datetime
from strategy.strategy import Strategy
from strategy.robust import Robust
from strategy.rsi import RSI
from strategy.min_max import MinMax
from strategy.z_score import ZScore
from strategy.moving_average import MovingAverage
from strategy.roc import ROC
from strategy.percentile import Percentile
from strategy.divergence import Divergence
from strategy.LogTransform import LogTransform
from strategy.ModifiedZscore import ModifiedZScore
from strategy.DecimalScaling import DecimalScaling
from joblib import Parallel, delayed
import os
import seaborn as sns
import matplotlib.pyplot as plt


BASE_PATH = '/Users/stephenlyk/Desktop/Gnproject/src/fetch_data/glassnode_data_btc10m_Dec2024'
shortlist_path = '/Users/stephenlyk/Desktop/Strategy Bank/BTC10m/2Dec2024/all_strategies_results_6.csv'
ASSET = 'BTC'
INTERVAL = '10m'
GLASSNODE_API_KEY = '2ixuRhqosLHPpClDohgjZJsEEyp'  # Replace with your actual API key
SHIFT = 5

# Function to determine multiplier based on INTERVAL
def get_multiplier(interval):
    if interval == '10m':
        return 365 * 24 * 6  # 6 ten-minute intervals per hour
    elif interval == '1h':
        return 365 * 24
    elif interval == '24h':
        return 365
    else:
        raise ValueError(f"Unsupported interval: {interval}")

# Get multiplier based on INTERVAL
MULTIPLIER = get_multiplier(INTERVAL)

def fetch_glassnode_data():
    url = f"https://api.glassnode.com/v1/metrics/market/price_usd_close"
    params = {
        'a': ASSET,
        'i': INTERVAL,
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
        'Percentile': Percentile,
        'Divergence': Divergence,
        'RSI': RSI,
        'LogTransform': LogTransform,
        'ModifiedZScore': ModifiedZScore,
        'DecimalScaling': DecimalScaling,
    }
    return strategy_map.get(strategy_name, Strategy)


def process_metric(row, btc_price_df):
    metric_file = row['Metric']
    if pd.isna(metric_file) or metric_file.strip() == '':
        print(f"Skipping row with empty metric file: {row}")
        return None

    if not metric_file.startswith(BASE_PATH):
        metric_file = os.path.join(BASE_PATH, os.path.basename(metric_file))

    print(f"Attempting to read file: {metric_file}")

    metric_name = os.path.basename(metric_file).split('.')[0]

    try:
        metric_df = pd.read_csv(metric_file)
        metric_df.columns = ['Date', 'Value']
        metric_df['Date'] = pd.to_datetime(metric_df['Date'])
        metric_df.set_index('Date', inplace=True)
        metric_df['Value'] = metric_df['Value'].shift(SHIFT)
        metric_df = metric_df.dropna()

        merged_df = metric_df.join(btc_price_df, how='inner')

        StrategyClass = get_strategy_class(row['Strategy'])

        # Check if 'Best Window' and 'Best Threshold' are valid
        if pd.isna(row['Best Window']) or pd.isna(row['Best Threshold']):
            print(f"Skipping invalid window or threshold for {metric_name}")
            return None

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

        # Create a unique key for this combination
        unique_key = f"{metric_name}_{row['Strategy']}_{row['Long_Short']}_{row['Condition']}_{int(row['Best Window'])}_{row['Best Threshold']}"

        return pd.Series(result_df['Profit'], name=unique_key)

    except FileNotFoundError:
        print(f"File not found: {metric_file}")
        return None
    except Exception as e:
        print(f"Error processing {metric_file}: {str(e)}")
        return None

# Read the Shortlist CSV
shortlist_df = pd.read_csv(shortlist_path)

# Fetch BTC price data
btc_price_df = fetch_glassnode_data()

# Process all metrics in parallel
results = Parallel(n_jobs=-1)(delayed(process_metric)(row, btc_price_df) for _, row in shortlist_df.iterrows())

# Combine all results into a single dataframe
all_profits_df = pd.concat([result for result in results if result is not None], axis=1)

# Calculate equally weighted combined strate gy
all_profits_df['Combined_Profit'] = all_profits_df.mean(axis=1)

# Calculate cumulative profit arithmetically for the combined strategy
all_profits_df['Cumulative_Profit'] = all_profits_df['Combined_Profit'].cumsum()

# Calculate Buy and Hold returns and cumulative returns
all_profits_df['BnH_Returns'] = btc_price_df['Price'].pct_change()
all_profits_df['BnH_Cumulative'] = all_profits_df['BnH_Returns'].cumsum()

# Calculate performance metrics
annual_return = all_profits_df['Combined_Profit'].mean() * MULTIPLIER * 100  # Convert to percentage
sharpe_ratio = all_profits_df['Combined_Profit'].mean() / all_profits_df['Combined_Profit'].std() * np.sqrt(MULTIPLIER)
max_drawdown = (all_profits_df['Cumulative_Profit'] - all_profits_df['Cumulative_Profit'].cummax()).min() * 100
calmar_ratio = annual_return / abs(max_drawdown)

# Calculate BnH metrics
bnh_annual_return = all_profits_df['BnH_Returns'].mean() * MULTIPLIER * 100
bnh_sharpe_ratio = all_profits_df['BnH_Returns'].mean() / all_profits_df['BnH_Returns'].std() * np.sqrt(MULTIPLIER)
bnh_max_drawdown = (all_profits_df['BnH_Cumulative'] - all_profits_df['BnH_Cumulative'].cummax()).min() * 100
bnh_calmar_ratio = bnh_annual_return / abs(bnh_max_drawdown)

# Create equity curve plot
plt.figure(figsize=(12, 8))
plt.plot(all_profits_df.index, all_profits_df['Cumulative_Profit'] * 100, label='Combined Strategy')
plt.plot(all_profits_df.index, all_profits_df['BnH_Cumulative'] * 100, label='Buy and Hold')
plt.title('Equity Curve of Combined Strategy vs Buy and Hold')
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
plt.savefig('equity_curve_with_bnh.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nEquity curve with Buy and Hold saved as 'equity_curve_with_bnh.png'")

# Save all profits to a CSV file
output_file = 'all_metrics_profits.csv'
all_profits_df.to_csv(output_file)
print(f"\nAll metrics profits saved to {output_file}")

# Calculate correlation matrix
correlation_matrix = all_profits_df.corr()

# Save the correlation matrix to a CSV file
correlation_matrix.to_csv('correlation_matrix.csv')
print("\nCorrelation matrix saved to 'correlation_matrix.csv'")

# Create a heatmap of the correlation matrix with values
plt.figure(figsize=(30, 24))  # Large figure size for better readability

# Create heatmap
sns.heatmap(correlation_matrix,
            annot=True,  # Show the correlation values
            fmt=".2f",   # Format to 2 decimal places
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
plt.title('Correlation Heatmap of Strategy Profits', fontsize=20)
plt.tight_layout()

# Save the figure
plt.savefig('correlation_heatmap_full.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nFull correlation heatmap with values saved as 'correlation_heatmap_full.png'")