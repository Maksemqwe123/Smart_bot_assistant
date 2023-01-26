import os
import csv

from datetime import datetime

data_price = datetime.now()
only_date = data_price.date()

files_path_finance = []  # List for saving paths to a folder
files_path_binance = []

finance_tickers = ['BTC-USD', 'MSFT', 'PM', 'TXN']  # tickers for parsing

binance_tickers = ['BTC_BUSD', 'MATIC_BUSD', 'XRP_BUSD', 'ETH_BUSD']


for ticker_name in finance_tickers:  # Loop to create files and folders
    if not os.path.isdir(f"C:/Data/finance/{ticker_name}/"):
        os.mkdir(f"C:/Data/finance/{ticker_name}/")  # Creating a folder if it does not exist
    with open(f"C:/Data/finance/{ticker_name}/{only_date}.csv", "w") as file:
        files_path_finance.append(file.name)  # Creating a file if it does not exist

for ticker_name in binance_tickers:  # Loop to create files and folders
    if not os.path.isdir(f"C:/Data/binance/{ticker_name}/"):
        os.mkdir(f"C:/Data/binance/{ticker_name}/")  # Creating a folder if it does not exist
    with open(f"C:/Data/binance/{ticker_name}/{only_date}.csv", "w") as file:
        files_path_binance.append(file.name)
