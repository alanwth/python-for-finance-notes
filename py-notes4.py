import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
#new libraries
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use ('ggplot')

df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)
#df['100ma'] = df['Adj Close'].rolling(window=100).mean

#resampling the data
df_ohlc = df['Adj CLose].resample('10D').ohlc()
df_volume = df['Vloume'].resample('10D").sum()

#reseting the date
df_ohlc.reset_index(inplace = True)

#Converting the date to mdates
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#plotting wiht matplotlib, usually with 1 sub plot
#name = plt.subplot2grid((rows,column), (starting point), rowspan = %n, colspan = %n, if sharing axis with the first plot)
ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 1, colspan =1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan =1, sharex = ax1)
#convert the mdates to normal dates
ax1.xaxis_date()

#Chaning the default colour to green up red down
candlestick_ohlc(ax1, df_ohlc.values, width = 2, colorup = 'g')
ax2.fill_between (df_volume.index.map(mdates.dates.date2num), df_volume.values, 0)
                                  
plt.show()
