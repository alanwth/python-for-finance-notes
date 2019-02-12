#import datetime as dt
#import matplotlib.pyplot as plt
#from matplotlib import style
#from matplotlib.finance import candlestick_ohlc
#from matplotlib.dates as mdates
#import pandas as pd
#pandas_datareader.data as web
#style.use('ggplot')

#df = pd.read._csv('tsla.csv', parse_dates = True, index_col = 0)
##df['100ma'] = df['Adj Close'].rolling(windows = 100, min_periods = 0).mean()

#df_ohlc = df['Adj Close'].resample('10D').ohlc()
#df_volume = df['Volume'].resample('10D').sum()

#df_ohlc.reset_index(inplace = True)

#df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
##print(df_ohlc.head())



#Extracting data from web tables
import bs4 as bs
#serialised any python objects, save any object, in this case the wikipedia list of S&P500 list
import pickle
import requests

def save_sp500_tickers():
  resp = requests.get(https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
  soup = bs.BeautifulSoup(resp.text, "lxml")
  table = soup.find('table', {'class':'wikitable sortable;})
  tickers = []
  for row in table.findAll('tr') [1:]:
     ticker = row.findAll('td') [0].text
     tickers.append(ticker)
                             
  with open("sp500tickers.pickle", "wb") as f:
  
 print(tickers)
                             
 return tickers
                              
save_sp500_tickers()
