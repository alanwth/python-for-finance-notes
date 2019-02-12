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
    requirement =  0.02
    for col in cols;
        if col > requirment:
            return 1
        if col < - requirement:
            return - 1
    return 0
    
    
