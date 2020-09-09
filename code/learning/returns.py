import yfinance as yf
import pandas as pd
import numpy as np
import quandl

API_KEY = '8ohVvwCgmzgRpFeza8FD'
quandl.ApiConfig.api_key = API_KEY

# Download APPL Stock price 
df = yf.download('AAPL', start='1999-12-31', end='2010-12-31', progress=False)
df.rename(columns = {'Adj Close': 'adj_close'},inplace=True)
df = df.loc[:,['adj_close']]

# 
'''
    Calculate the simple return:
    
    Percent Change/Simple Return = (CurrentValue-PrevValue)/CurrentValue
'''
df['simple_rtn'] = df.adj_close.pct_change()

'''
    Calculate the log return:
    
    Log Return = ln(CurrentValue/PrevValue)
'''
df['log_rtn'] = np.log(df.adj_close/df.adj_close.shift(1))

# print(df.head(5))

# Download Consumer Price Index from Quandl
df_cpi = quandl.get(dataset='RATEINF/CPI_USA', start_date='1999-12-31',  end_date='2010-12-31')
df_cpi.rename(columns= {'Value' : 'cpi'}, inplace=True)

df_dates = pd.DataFrame(index=pd.date_range(start='1999-12-31',  end='2010-12-31'))

print(df_dates.asfreq('M').head(20))



# print('Reached here successfully')
