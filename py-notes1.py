#libraries
#pandas
#pandas-datareader
#matplotlib
#beautifulsoup4
#scikit-learn / sklearn

#Importing libraries
importa datetime as dt
import matplotlib.pyplot as plt
from matpolotlib import style
import pandas as pd
import pandas_datareader.data as web

#import a plot style of choice
style.use('ggplot')

#start and end dates
start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

#dataframe = web.datareader ('ticker', 'where from', start date, end date) 
df = web.DataReader ('TSLA', yahoo', start, end)
#printing the top first rows of data, df.head(n)/df.tail(n)
print (df.head())
