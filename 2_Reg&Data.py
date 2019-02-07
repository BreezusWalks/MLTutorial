import os
import pandas as pd
import quandl

api_key = open('api_key.txt', 'r').read()
pd.set_option("display.max_columns", 100)

df = quandl.get('WIKI/GOOGL', authtoken=api_key)
# df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
print(df.tail())