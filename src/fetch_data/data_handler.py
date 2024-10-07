# data_handler.py
import pandas as pd
import requests
from datetime import datetime
import logging
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DataHandler:
    def __init__(self, api_key, asset, interval, FOLDER_NAME):
        self.api_key = api_key
        self.asset = asset
        self.interval = interval
        self.successful_metrics = []
        self.failed_metrics = []
        self.data_folder = FOLDER_NAME
        os.makedirs(self.data_folder, exist_ok=True)
        self.miner_list = ["aggregated", "other", "1THash&58COIN", "AntPool", "ArkPool", "BinancePool", "BitFury",
                           "BitMinter", "Bixin", "BTC.com", "BTC.TOP", "DPool", "F2Pool", "FoundryUSAPool", "Genesis",
                           "HuobiPool", "KuCoinPool", "Lubian.com", "LuxorTech", "MaraPool", "NovaBlock", "OKExPool",
                           "Patoshi", "PegaPool", "Poolin", "SBICrypto", "SigmaPool", "SlushPool", "SpiderPool",
                           "TerraPool", "UKRPool", "Ultimus", "ViaBTC"]

    def fetch_glassnode_metrics(self):
        url = "https://api.glassnode.com/v2/metrics/endpoints"
        params = {'api_key': self.api_key}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            metrics = [item['path'] for item in data if isinstance(item, dict) and 'path' in item]
            return sorted(set(metrics))
        else:
            logging.error(f"Error fetching metrics list: {response.status_code}")
            logging.error(f"Response content: {response.text}")
            return []

    def fetch_glassnode_data(self, metric, start_timestamp, end_timestamp, miner=None):
        if metric.startswith('/v1/metrics/'):
            metric = metric[len('/v1/metrics/'):]

        url = f"https://api.glassnode.com/v1/metrics/{metric}"

        params = {
            'a': self.asset,
            's': start_timestamp,
            'u': end_timestamp,
            'i': self.interval,
            'api_key': self.api_key
        }

        if miner:
            params['miner'] = miner

        try:
            response = requests.get(url, params=params)
            logging.info(f"Request URL: {response.url}")
            logging.info(f"Response status: {response.status_code}")
            logging.info(f"Response text: {response.text[:100]}...")  # Log first 100 characters

            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"Error fetching data for {metric} (Miner: {miner}): {response.status_code}")
                logging.error(f"Response content: {response.text}")
                return None
        except Exception as e:
            logging.error(f"Exception occurred while fetching data for {metric} (Miner: {miner}): {str(e)}")
            return None

    def prepare_specific_data(self, start_date, end_date, metric):
        start_timestamp = int(datetime.combine(start_date, datetime.min.time()).timestamp())
        end_timestamp = int(datetime.combine(end_date, datetime.min.time()).timestamp())

        # First, try fetching without miner parameter
        data = self.fetch_glassnode_data(metric, start_timestamp, end_timestamp)

        if data is not None:
            df = pd.DataFrame(data)
            if 't' in df.columns and 'v' in df.columns:
                df['Date'] = pd.to_datetime(df['t'], unit='s')
                df = df.rename(columns={'v': metric})
                df = df[['Date', metric]].sort_values('Date')
                return df
            else:
                logging.warning(f"Unexpected data format for metric {metric}. Columns: {df.columns}")
                return None

        # If data is None, check if it's due to missing miner parameter
        error_response = self.fetch_glassnode_data(metric, start_timestamp, end_timestamp, "aggregated")
        if error_response is None or "missing miner param" not in str(error_response).lower():
            return None

        # If miner parameter is required, fetch for each miner
        miner_data = {}
        for miner in self.miner_list:
            data = self.fetch_glassnode_data(metric, start_timestamp, end_timestamp, miner)
            if data:
                df = pd.DataFrame(data)
                if 't' in df.columns and 'v' in df.columns:
                    df['Date'] = pd.to_datetime(df['t'], unit='s')
                    df = df.rename(columns={'v': metric})
                    df = df[['Date', metric]].sort_values('Date')
                    miner_data[miner] = df
                else:
                    logging.warning(f"Unexpected data format for metric {metric}, miner {miner}. Columns: {df.columns}")

        return miner_data if miner_data else None