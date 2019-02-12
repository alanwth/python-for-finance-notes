import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates as mdates
import pandas as pd
pandas_datareader.data as web
style.use('ggplot')

df = pd.read._csv('tsla.csv', parse_dates = True, index_col = 0)
#df['100ma'] = df['Adj Close'].rolling(windows = 100, min_periods = 0).mean()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace = True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
#print(df_ohlc.head())
