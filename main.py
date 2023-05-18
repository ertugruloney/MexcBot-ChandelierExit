
import ccxt
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import os
import math
import numpy as np
import pandas as pd
import datetime
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
US_BUSINESS_DAY = CustomBusinessDay(calendar=USFederalHolidayCalendar())
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import itertools
import matplotlib.dates as mpl_dates
import yfinance as yf
from finta import TA
import requests



exchange = ccxt.mexc({
    'apiKey': '',
    'secret': ''
})
# Define the symbol and timeframe
symbol = 'KAS/USDT'
timeframe = '15m'



def calculate_tis(df, atr_period):
    #  Calculate ATR
    atr = TA.ATR(df, period=atr_period)
    
    #  Calculate chandelier exits
    chandelier_info = TA.CHANDELIER(df, short_period=atr_period, long_period=atr_period, k=3)

    #  Add to price dataframe
    df = pd.concat([df, atr, chandelier_info], axis=1, ignore_index=False)

    return df
def calculate_signals(df):
    a=df['close'].shift(1)
    #  Long position
    df['enter_long'] = np.where((df['close'] > df['Short.']) & (df['close'].shift(1) <= df['Short.'].shift(1)), 1, 0)
    df['exit_long'] = np.where((df['close'] < df['Long.']) & (df['close'].shift(1) >= df['Long.'].shift(1)), 1, 0) 
    
    #  Short position
    df['enter_short'] = np.where((df['close'] < df['Long.']) & (df['close'].shift(1) >= df['Long.'].shift(1)), 1, 0)
    df['exit_short'] = np.where((df['close'] > df['Short.']) & (df['close'].shift(1) <= df['Short.'].shift(1)), 1, 0)
    return df
def calculate_tis(df, atr_period):
    #  Calculate ATR
    atr = TA.ATR(df, period=atr_period)
    
    #  Calculate chandelier exits
    chandelier_info = TA.CHANDELIER(df, short_period=atr_period, long_period=atr_period, k=1.5)
    #  Add to price dataframe
    df = pd.concat([df, atr, chandelier_info], axis=1, ignore_index=False)
    return df

try:
    while True:
        print('bot başladı')
        # Fetch candlestick data
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
        
        # Convert the data to a Pandas dataframe
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        # Set the timestamp as the index
        df.set_index('timestamp', inplace=True)
        atr_period =1
        start_investment = 100
        df = df.tail(400)
        df.reset_index(inplace=True)
        df = calculate_tis(df, atr_period)
        df = calculate_signals(df)
        df=df.values.tolist()
        balance1= exchange.fetch_balance()["free"]
        asd=2
        try:
            balance1= exchange.fetch_balance()["free"]
            balance2= exchange.fetch_balance()["free"]['USDT']
            if float(balance1)>=float(balance2):
                signal=1
            else:
                signal=0
        except:
            signal=0
        
        
        if signal==0 and df[-1][9]==1:
            
            balance= exchange.fetch_balance()["free"]['USDT']-6
            price = exchange.fetch_ticker("KAS/USDT")['last']
            amount =float(balance/price)
            # add timeInForce to params
            params = { 'timInForce': 'IOC' }
            order = exchange.create_order('KAS/USDT','limit','buy', amount, price, params)
            print(order)
            signal=1
        if signal==1 and df[-1][10]==1:
            balance= exchange.fetch_balance()["free"]['KAS']
            price = exchange.fetch_ticker("KAS/USDT")['last']
            amount =float(balance)
            # add timeInForce to params
            params = { 'timInForce': 'IOC' }
            order = exchange.create_order('KAS/USDT','limit','sell', amount, price, params)
            print(order)
except:
    pass