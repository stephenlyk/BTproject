import pandas as pd
import os
from itertools import product

# Define paths
DATA_DIR = '/Users/stephenlyk/Desktop/Gnproject/src/fetch_data/glassnode_data_btc24h_Sept2024'
OUTPUT_DIR = '/Users/stephenlyk/Desktop/Gnproject/combined_factorcheck'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


def read_csv(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    df.columns = ['Value']  # Rename the second column to 'Value'
    return df


def is_open_interest_file(filename):
    return 'open_interest' in filename.lower()


def is_market_cap_file(filename):
    return 'marketcap_usd' in filename.lower()


def calculate_combined_factor(oi_df, mcap_df):
    common_index = oi_df.index.intersection(mcap_df.index)
    oi_values = oi_df.loc[common_index, 'Value']
    mcap_values = mcap_df.loc[common_index, 'Value']
    return oi_values / mcap_values


def main():
    csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]

    oi_files = [f for f in csv_files if is_open_interest_file(f)]
    mcap_files = [f for f in csv_files if is_market_cap_file(f)]

    for oi_file, mcap_file in product(oi_files, mcap_files):
        try:
            oi_df = read_csv(os.path.join(DATA_DIR, oi_file))
            mcap_df = read_csv(os.path.join(DATA_DIR, mcap_file))

            combined_factor = calculate_combined_factor(oi_df, mcap_df)

            output_filename = f"{os.path.splitext(oi_file)[0]}_divided_by_{os.path.splitext(mcap_file)[0]}.csv"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            combined_factor.to_frame(name='Value').to_csv(output_path)
            print(f"Saved combined factor: {output_filename}")
        except Exception as e:
            print(f"Error processing {oi_file} and {mcap_file}: {str(e)}")


if __name__ == "__main__":
    main()