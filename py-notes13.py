'''This tutorial is about Quantopian and how to backtest the algorithm'''

#context is a python dictionary and it contains information about the portfolio
def initialize(context):
    context.appl = sid(24) #sid is used beacuse tickers could be used by serval companies

def handle_data(context, data): #data is your collection of information
    hist = data.history(context.appl, 'price', 50, '1d') #stock id, parameters of interest, bar count, frequency
    log.info(hist.head())

    #simple moving average
    sma_50 = hist.mean()
    sma_20 = hist[-20:].mean()
