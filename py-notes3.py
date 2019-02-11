import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use ('ggplot')

df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

#Creatting a new column
df['100ma'] = df['Adj Close'].rolling(window=100).mean

#input modifitying the dataframe, instead of redefinitng the dataframe (Can also fill na with o etc.)
df.dropna(inplace=True)

print(df.head())

#plotting wiht matplotlib, usually with 1 sub plot
#name = plt.subplot2grid((rows,column), (starting point), rowspan = %n, colspan = %n, if sharing axis with the first plot)
ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 1, colspan =1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan =1, sharex = ax1)

#reference the index, in this case date annd plotting the parameters
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax1.plot(df.index, df['Volume'])

plt.show()
