import yfinance as yf
import pandas as pd
import numpy as np

# Download APPL Stock price 
df = yf.download('AAPL', start='1999-12-11', end='2010-12-31', progress=False)
df.head(10)


# print('Reached here successfully')
