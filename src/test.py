import pandas as pd
import numpy as np
from strategy.percentile import Percentile
from optimization import Optimization
import sys


def load_single_file(filename):
    try:
        print(f"Attempting to load file: {filename}")
        df = pd.read_csv(filename)
        print("File loaded successfully")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{filename}' is empty.")
        return None
    except Exception as e:
        print(f"Error loading file '{filename}': {str(e)}")
        return None


def calculate_window_sizes(data_length):
    return [int(data_length * i) for i in [0.1, 0.2, 0.3, 0.4, 0.5]]


def split_data(df):
    split_point = int(len(df) * 0.8)
    return df[:split_point], df[split_point:]


def preprocess_data(df):
    # Rename the '/v1/metrics/indicators/asol_sth' column to 'Value'
    df = df.rename(columns={'/v1/metrics/indicators/asol_sth': 'Value'})

    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort by date
    df = df.sort_values('Date')

    # Create a dummy 'Price' column (you may want to replace this with actual price data if available)
    df['Price'] = np.arange(len(df))

    return df


def pilot_run(filename, price_factor_df):
    print(f"Starting pilot run with file: {filename}")

    # Preprocess the data
    price_factor_df = preprocess_data(price_factor_df)

    print(f"Data shape: {price_factor_df.shape}")
    print(f"Columns: {price_factor_df.columns}")
    print("All column names:")
    for col in price_factor_df.columns:
        print(f"  - {col}")
    print(f"First few rows:\n{price_factor_df.head()}")

    train_df, test_df = split_data(price_factor_df)
    print(f"Train data shape: {train_df.shape}")
    print(f"Test data shape: {test_df.shape}")

    data_length = len(train_df)
    window_size_list = calculate_window_sizes(data_length)
    print(f"Window sizes: {window_size_list}")

    strategy = "Percentile"
    threshold_params = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    long_short = "short"
    condition = "higher"

    print(f"Running optimization for strategy: {strategy}")
    try:
        train_optimization = Optimization(strategy, train_df, window_size_list, threshold_params,
                                          target="Value", price='Price',
                                          long_short=long_short, condition=condition)
        print("Starting optimization process...")
        train_optimization.run()
        print("Optimization complete. Getting best strategy...")
        best_strategy = train_optimization.get_best()

        if best_strategy is None:
            print("No valid strategy found.")
        else:
            print(f"Best strategy found:")
            print(f"Type of best_strategy: {type(best_strategy)}")
            print("Attributes and methods of best_strategy:")
            for attr in dir(best_strategy):
                if not attr.startswith("__"):
                    print(f"  - {attr}")

            # Try to access some common attributes or methods
            try:
                print(f"Strategy parameters: {best_strategy.get_params()}")
            except AttributeError:
                print("get_params() method not found")

            try:
                print(f"Strategy performance: {best_strategy.performance}")
            except AttributeError:
                print("performance attribute not found")

            # If you have access to the Percentile class definition, you can add more specific checks here

            print("Testing best strategy on test data...")
            # We'll need to adjust this part based on what we learn about the Percentile object
            test_strategy = Percentile(test_df, **best_strategy.get_params())
            print(f"Test performance: {test_strategy.performance}")
    except Exception as e:
        print(f"An error occurred during optimization: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("Script started")
    filename = "/Users/stephenlyk/Desktop/Gnproject/glassnode_data_eth1h/_v1_metrics_indicators_asol_sth.csv"

    try:
        # Load the file
        df = load_single_file(filename)
        if df is not None:
            pilot_run(filename, df)
        else:
            print("Failed to load the file. Exiting.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

    print("Script finished")