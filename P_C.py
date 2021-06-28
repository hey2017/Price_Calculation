# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 20:04:34 2021

@author: motta
"""


import pandas as pd
import yahoo_finance as yf
#from yahoofinancials import YahooFinancials

# install the datareader: pip install pandas_datareader
import pandas_datareader as pdr
import datetime
tickers = ['msft', 'aapl', 'TSLA', 'GOOG', 'amzn', 'fb']
df = pdr.DataReader(tickers, data_source='yahoo', start='2015-01-01', end='2021-06-25')
df_close = pdr.DataReader(tickers, data_source='yahoo', start='2015-01-01', end='2021-06-25')['Close']


# Export dataframe to a xlsx file
df.to_excel('Stock_price.xlsx')
df_close.to_excel('Stock_price_close.xlsx')


#df2 = pd.read_csv("Stock_price_close.xlsx")

print(df.head(),"\n")
print("\n the data column information:\n",df.info())
print("\n columns count, mean, std, min, 25%, 50%, 75%, and max:\n",df.describe())


import matplotlib.pyplot as pyplot
data2 = df_close
data2 = data2.rename(columns={'msft':'Microsoft', 'aapl':'Apple', 'TSLA':'Tesla', 'GOOG':'Google', 'amzn':'Amazon', 'fb':'Facebook'})


import seaborn as sns
import matplotlib.pyplot as plt

#correlation matrix for many features
correlations = data2.corr().round(2)

print('The correlation matrix\n',correlations)

ax = sns.heatmap(correlations,annot = True)

plt.setp(ax.get_xticklabels(), rotation=20, ha="right",
         rotation_mode="anchor")
plt.title('Correlation matrix')
