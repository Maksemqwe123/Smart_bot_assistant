# -*- coding: utf-8 -*-

import yfinance as yf

from creation_files_and_folders import *

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

list_open = []  # list for saving all data open
list_high = []  # list for saving all data high
list_low = []  # list for saving all data low
list_close = []  # list for saving all data close


def main():
    logging.info('Парсинг данных finance запущен')
    for ticker in finance_tickers:  # A cycle for parsing ticker and saving them in the list
        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()

        data_all_open = data['Open'].iloc[-1]
        list_open.append(str(data_all_open))

        data_all_high = data['High'].iloc[-1]
        list_high.append(str(data_all_high))

        data_all_low = data['Low'].iloc[-1]
        list_low.append(str(data_all_low))

        data_all_close = data['Close'].iloc[-1]
        list_close.append(str(data_all_close))

    all_tickers_and_files_path = (list(zip(list_open, list_high, list_low, list_close, files_path_finance)))
    # Creating a variable that combines all the data in list and iterating through all the data by index

    for ticker_and_path in all_tickers_and_files_path:  # A loop for writing data to files and passing the write path to a file
        with open(ticker_and_path[4], 'w') as file:
            writer = csv.writer(file)
            writer.writerow(ticker_and_path[0:4])
        logging.info('Данные с сайта finance записаны в файл')

