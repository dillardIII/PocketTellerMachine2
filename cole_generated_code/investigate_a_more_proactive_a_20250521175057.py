from ghost_env import INFURA_KEY, VAULT_ADDRESS
One way to mitigate inactive market days is by building an algorithm that will execute trades when certain conditions are met.

The following Python code implements a simple trading algorithm that uses moving averages to decide when to buy or sell. It will only execute a trade if the market is active (i.e. the current price is not equal to the previous day's closing price).

```python
import pandas as pd
import numpy as np
from datetime import datetime
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_algo(symbol):
    # get market data
    end_date = datetime.now()
    start_date = end_date - pd.DateOffset(years=1)
    df = web.get_data_yahoo(symbol, start_date, end_date)

    # calculate moving averages
    df['sma'] = calculate_sma(df['Close'], 14)
    df['ema'] = calculate_ema(df['Close'], 14)

    # create signals (1 for buy, -1 for sell, 0 for hold)
    df['signal'] = np.where(df['ema'] > df['sma'], 1, 0)
    df['signal'] = np.where(df['ema'] < df['sma'], -1, df['signal'])

    # only trades when market is active (avoid inactive market days)
    df['prev_close'] = df['Close'].shift(1)
    df['trade'] = np.where(df['Close'] != df['prev_close'], df['signal'], 0)

    return df

# run the algorithm for a certain stock
trading_df = trading_algo('AAPL')

```

This python code above gets market data for a certain stock (in this case Apple), calculates the 14-day simple moving average (SMA) and the 14-day exponential moving average (EMA) for the closing prices, generates trading signals based on these moving averages (buy if the EMA is above the SMA, sell if the EMA is below the SMA, hold if they're equal), and finally only allow trades when the market is active to avoid days with no wins or losses. 

Keep in mind, this is just a simple trading algorithm and can be greatly improved. Also, it's always a good idea to backtest any trading strategy before using it in a live market.