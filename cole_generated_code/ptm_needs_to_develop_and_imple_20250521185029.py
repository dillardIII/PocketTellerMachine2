Here's a simple example of a Python code that could be used to develop a trading strategy. This strategy is based on moving averages, a common indicator in technical analysis.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)

    # Create a column 'Signal' such that if the short window SMA is greater than long window SMA then buy else sell
    data['Signal'] = 0.0  
    data['Signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)   

    # Create a column 'Position' which is the difference of the 'Signal' column. This column actually tells when to buy or sell stock
    data['Position'] = data['Signal'].diff()

def get_data(symbol, start_date, end_date):
    df = web.DataReader(symbol, 'yahoo', start_date, end_date)
    return df

# Define the symbol and time frame
symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'

# Get the data
data = get_data(symbol, start_date, end_date)

# Define the short and long window
short_window = 40
long_window = 100

# Apply the trading strategy
trading_strategy(data, short_window, long_window)

print(data)
```
This script fetches historical stock data, calculates simple moving averages over a short and long window, and generates trading signals based on these averages. 

Please note that this is a simple trading strategy and may not be profitable in real trading. Always backtest any strategy before live trading. Also, this script does not include any risk management or portfolio optimization techniques.