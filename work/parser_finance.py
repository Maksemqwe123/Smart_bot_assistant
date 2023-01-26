# import yfinance as yf
# import pandas as pd
# import numpy as np
# import seaborn as sna
# import matplotlib.pyplot as plt
#
#
# rm = yf.Ticker('PM')
# # print(rm.info)
#
# hist = rm.history(period='max')
# print(hist)
#
# major_indices = pd.read_html('https://finance.yahoo.com/quote/PM?p=PM&.tsrc=fin-srch')
# print(major_indices)
#
# ticker_list = major_indices
#
# df = yf.download(ticker_list, period='id', start='2020-01-13', end='2022-12-29')
#
# # print(df)
import dateutil.utils
# import yfinance as yf
# ticker = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']
# data= yf.download(ticker,'2016-01-01','2019-08-01')['Adj Close']
# data.head()
# print(data.head())

# import quandl
# aapl = quandl.get("diff", start_date="2020-10-01", end_date="2022-12-29")
# print(aapl)
#
# aapl['PM'] = aapl.Open - aapl.Close
#
# # Delete the new `diff` column
# del aapl['diff']

#
# import pandas as pd
# aapl.to_csv('data/aapl_ohlc.csv')
# df = pd.read_csv('data/aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)

import pandas_datareader as pdr
import datetime
# aapl = pdr.get_data_yahoo('PM',
#                           start=datetime.datetime(2019, 10, 1),
#                           end=datetime.datetime(2021, 1, 1))


# import quandl
# import pandas as pd
# aapl = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")
#
# print(aapl)
#
# major_indices = pd.read_html('https://finance.yahoo.com/quote/PM?p=PM&.tsrc=fin-srch')
# print(major_indices)
#
# print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())
#
# # Inspect the first rows of 2007
# print(aapl.loc['2007'].head())
#
# # Inspect November 2006
# print(aapl.iloc[22:43])
#
# # Inspect the 'Open' and 'Close' values at 2006-11-01 and 2006-12-01
# print(aapl.iloc[[22, 43], [0, 3]])


# import yfinance as yf
#
# stock = yf.Ticker("ABEV3.SA")
# price = stock.info['regularMarketPrice']
# print(price)

#
# import datetime
# import yfinance as yf
# now = datetime.datetime.now().strftime("%Y-%m-%d")
# data = yf.Ticker("ABEV3.SA")
# data = data.history(start="2010-01-01",  end=now)
# print(data)


import yfinance as yf
from db_api.db_test import *
import datetime as dr
from datetime import datetime, date
import pandas_datareader


data_check = []

tickers = ['PM']
for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    data1_close = data['Close'].iloc[-1]
    data1_open = data['Open'].iloc[-1]
    data1_low = data['Low'].iloc[-1]
    data1_high = data['High'].iloc[-1]
    if data1_open > 0 and data1_close > 0 and data1_low > 0 and data1_high > 0:
        data_check.extend((data1_open, data1_close, data1_high, data1_low))
        print('Все переменные положительные')
    else:
        print('произошла ошибка \nзамечено отрицательное значение в датах')

# now = date.today()
# start_year = 2022
# start_mount = 12
# start_day = 3
#
#
# start = date(start_year, start_mount, start_day)
# print(start)
#
# ref = tickers[0]
# print()
#
# df = pandas_datareader.get_data_yahoo(start, now)
#
# new_df = df.copy()
# new_df['year'], new_df['month'], new_df['day'] = df.index.year, df.index.month, df.index.day
# print(df)

import re
import logging
from New_life_db_work.postgresql import DataBase

db = DataBase()

# gyu = 1
# z = []
#
# start = '2023-01-20'
# now = date.today()
# print(type(now))
# data = yf.download(tickers="PM", start=start, interval="1d")
#
# fr = data.reset_index()
# uyj = fr['Date']
#
# yui = '2023-01-19 00:00:00'
#
# for joi in uyj:
#     red = joi
#     z.append(red)
#     print(z)
#
# if gyu == 1:
#     print('cdncndk')
#
# elif gyu == 1:
#     print('cdmcm')
# else:
#     print('mnkdm')
#
# py_logger = logging.getLogger(__name__)
#
# py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
# py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
#
# rt = (py_handler.setFormatter(py_formatter))
#
# py_logger.debug(f"Testing the custom logger for module {__name__}...")
# logging.critical("A DEBUG Message")
# print(logging.debug("A DEBUG Message"))
# print(rt)
#
# logging.basicConfig(level=logging.INFO, filename="parser_finance.py",filemode="w")
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")

