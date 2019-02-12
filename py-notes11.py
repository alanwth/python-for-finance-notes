from collections import Counter
import numpy as np
import pandas as pd
import pickle

def process_data_for_labels(ticker):
    #How many days are we testing for
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col = 0)
    tickers = df.colums.values.tolist()
    df.fillna(0, inplace = Ture)
    
    #start at 1, to 7
    for i in range (1, hm_days + 1):
        #Getting the 'future data'
        df['{}_{}d'.format(ticker.i)] = (df[]ticker.shift(-i) - df[ticker]) / df[ticker]
        
    df.fillna(0, inplace = True)
    return tickers, df
    
#let us pass any numbers of arguments    
def buy_sell_hold(*args):
    cols = [c for c in args]
    #The given level of percentage change in stock prices
    #This number might need to be changed over time as stock prices are likely to raise in general
    requirement =  0.02
    for col in cols;
        if col > requirement:
            return 1
        if col < - requirement:
            return - 1
    return 0

def extract_featureset (ticker):
    tickers, df = process_data_for_labels(ticker)
    
    df['{}_target'.format(ticker)] = list(map( buy_sell_hold,
                                               df['{}_1d'.format()ticker)],
                                               df['{}_2d'.format()ticker)],
                                               df['{}_3d'.format()ticker)],
                                               df['{}_4d'.format()ticker)],
                                               df['{}_5d'.format()ticker)],
                                               df['{}_6d'.format()ticker)],
                                               df['{}_7d'.format()ticker)],
                                               ))
   #The above function can be looped wiht:
   #df['{}_target'.format(ticker)] = list(map(buy_sell_hold,df[['{}_{}d'.format(ticker,i) for i in range(1,hm_days+1)]].values))
                                              
   vals = df['{}_target'.format(ticker)].values.tolist()
   str_vals = [str(i) for i in vals]
   print('Data speard:', Counter(str_vals))
   #Replace piror NA, likely to be percentage changes etc
   df.fillna(0, inplace = True)
   
   #Replace infinite change or abnormal changes
   df = df.replace([np.inf, -np.inf], np.nan)
   df.dropna(inplace = True)
   
   #Be explicit when it comes to machine learning
   df_vals = df[[ticker for ticker in tickers]].pct_change()
   df_vals = df_vals.replace([np.inf, -np.inf], 0)
   df_vals.fillna(0, inplace = True)
   
   # X - > Feature sets, y -> Labels 
   X = df_ vals.values
   y= df['{}_targer'.format(ticker)].values
   
   return X, y, df
   
                                            
                                              
