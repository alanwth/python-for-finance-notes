#Extracting data from web tables
import bs4 as bs
imprt datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import os
import pandas as pd
import pandas_datareader.data as web
#serialised any python objects, save any object, in this case the wikipedia list of S&P500 list
import pickle
import requests

stylr.use(ggplot)

def save_sp500_tickers():
  resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
  soup = bs.BeautifulSoup(resp.text, "lxml")
  table = soup.find('table', {'class':'wikitable sortable;})
  tickers = []
  for row in table.findAll('tr') [1:]:
     ticker = row.findAll('td') [0].text
     tickers.append(ticker)
                             
  with open("sp500tickers.pickle", "wb") as f:
  
 print(tickers)
                             
 return tickers
 
#save_sp500_tickers()

#Build on the previous function
def get_data_from_yahoo(reload_sp500=False)
  if reload_sp500:
    tickers = save_sp500_tickers()
  else:
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
        
  if not os.path.exists('stock_dfs'):
      os.akedirs('stock_dfs')
      
  start = dt.datetime(2000,1,1)
  end = dt.datetime(2016,12,31)
  
  for ticker in tickers:
      print(ticker)
      if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
          df = web.Datareader(ticker, 'yahoo', start, end)
          df.to_csv('stock_dfs/{}.csv'.format(ticker))
      else:
          print('Already have ()'. format(ticker))
          
def compile_data():
    with open("sp500tickers.pickle", "rb") as f;
        tickers = pickle.load(f)
        
    main_df = pd.DataFrame()
    
    #To count where we are in the process
    for count,ticker in enumerate(tickers)
        df = pd.read_csv('stock_df/{}.csv'.format(ticker))
        df.set_index('Date', inpace = True)
        
        df.rename(colums = ('Adj Close', ticker), inplace = True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 11, inplace = True)
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how = 'outer')
        
        #print the count for every 10 stocks Adj Close data
        if count % 10 == 0:
            print(count)
                              
    print(main_df.head())
    main_df.to_csv('sp500_joined_closes')
    
def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    #df['AAPL'].plot()
    #plt.show()
    df_corr = df.corr()
    #shows the correlation between the stocks
    print(df_corr.head())
    
    #Gives inner value, a numpy array of the column and row
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    #Red (Negative), Yellow (Netural), Green (Positive)
    heatmap = ax.pcolor(data, camp = plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    # arraging ticks in a half mark
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor = False)
    ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor = False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    
    #data.shape shouldn't matter in this case as the column and the rows the same
    column_labels = df_corr.colums
    row_labels = df_corr.index
    
    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation = 90)
    #set limit of -1 to 1, but won't be needed for coverience
    heatmap.set_clim(-1,1)
    
visualize_data()
    
    
      
            
