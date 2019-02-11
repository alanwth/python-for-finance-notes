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
#exporting data to csv
df.to_csv('tsla.csv')

#To read a csv and to convert date to an date-time index
  #df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)
#Printig muiltiple parameters
  #print(df[['Open', 'High']].head)
 
#plotting the graph of the csv
 #df.plot()
 #or df['Adj close'].plot to show adjusted close
 #plt.show()
 
