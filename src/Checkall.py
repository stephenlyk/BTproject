# Checkall.py
import os
import pandas as pd
import logging
from joblib import Parallel, delayed
from Check import run_single_strategy

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_PATH = "/Users/stephenlyk/Desktop/Gnproject/glassnode_data_eth1hv/"
STRATEGY_PATH = "/Users/stephenlyk/Desktop/Gnproject/src/eth_factor_test_final.csv"


def process_strategy(row):
    try:
        file_path = os.path.join(BASE_PATH, row['Metric'])
        strategy_name = row['Strategy']
        long_short = row['Strategy Type']
        condition = row['Condition']

        logging.info(f"Processing strategy: {strategy_name}, {long_short}, {condition} with file: {file_path}")

        # Run the strategy
        result = run_single_strategy(file_path, strategy_name, long_short, condition)

        if result is None:
            logging.warning(f"No results for strategy {strategy_name}, {long_short}, {condition}")
            return None

        # Combine the results with the original input parameters
        result.update({
            'Original Train Sharpe': row['Train Sharpe'],
            'Original Test Sharpe': row['Test Sharpe'],
            'Original Best Window': row['Best Window'],
            'Original Best Threshold': row['Best Threshold']
        })

        logging.info(f"Successfully processed: {strategy_name}, {long_short}, {condition}")
        return result

    except Exception as e:
        logging.error(f"Error processing strategy {strategy_name}, {long_short}, {condition}: {str(e)}")
        return None

def main():
    try:
        # Read the strategy list
        strat_list = pd.read_csv(STRATEGY_PATH)

        # Use joblib to parallelize the processing
        num_cores = os.cpu_count() - 1  # Leave one core free
        results = Parallel(n_jobs=num_cores)(
            delayed(process_strategy)(row) for _, row in strat_list.iterrows()
        )

        # Filter out None results and combine into a DataFrame
        results = [r for r in results if r is not None]
        if results:
            combined_results = pd.DataFrame(results)

            # Remove duplicates based on Metric, Strategy, Long_Short, and Condition
            combined_results = combined_results.drop_duplicates(
                subset=['Metric', 'Strategy', 'Long_Short', 'Condition'])

            # Reorder columns to have original parameters first
            columns_order = ['Metric', 'Strategy', 'Long_Short', 'Condition',
                             'Original Best Window', 'Original Best Threshold',
                             'Original Train Sharpe', 'Original Test Sharpe',
                             'Best Window', 'Best Threshold', 'Train Sharpe', 'Test Sharpe',
                             'Train Annual Return', 'Test Annual Return',
                             'Train MDD', 'Test MDD', 'Train Calmar', 'Test Calmar',
                             'Train Beta', 'Test Beta', 'Train Num Trades', 'Test Num Trades']

            # Ensure all columns exist, if not, fill with NaN
            for col in columns_order:
                if col not in combined_results.columns:
                    combined_results[col] = pd.np.nan

            # Reorder the columns
            combined_results = combined_results[columns_order]

            # Save the combined results
            combined_results.to_csv('all_strategies_results.csv', index=False)
            print("All strategies have been processed. Results saved to 'all_strategies_results.csv'")
        else:
            print("No valid results were produced. Please check the logs for errors.")

    except Exception as e:
        print(f"An error occurred in the main function: {str(e)}")
        logging.error(f"Main function error: {str(e)}")


if __name__ == "__main__":
    main()