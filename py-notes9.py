#In machine learning, everthing becomes features and labels
#the features define somethinf and the label is basically the target in our case

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
    
process_data_for_labels('XOM')
