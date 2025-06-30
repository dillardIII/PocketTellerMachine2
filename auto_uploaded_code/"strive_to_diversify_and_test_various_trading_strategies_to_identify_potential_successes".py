from ghost_env import INFURA_KEY, VAULT_ADDRESS
To achieve the task, we needs some libraries like pandas, numpy, matplotlib, and yfinance (to fetch stock price data) to be installed. For modeling, we use statsmodels and pyfolio for performance analysis.

The following demonstrates two simple strategies: Moving Average Crossover and Mean Reversion.

Here are the Python scripts to simulate these trading strategies:

```python
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from pyfolio import create_simple_tear_sheet
from statsmodels.tsa.stattools import adfuller

# Create the functions to implement the strategies
def moving_average_crossover(ticker, short_window, long_window):
    data = yf.download(ticker, start="2022-01-01", end="2022-12-31")
    data['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    data['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    data['signal'] = np.where(data['short_mavg'] > data['long_mavg'], 1.0, 0.0)
    data['positions'] = data['signal'].diff()
    create_simple_tear_sheet(data['Close'].pct_change().dropna(), live_start_date='2022-06-01')
    return data

def mean_reversion(ticker):
    data = yf.download(ticker, start="2022-01-01", end="2022-12-31")
    adf_result = adfuller(data['Close'].dropna())
    print(f'ADF Statistic: {adf_result[0]}')
    print(f'p-value: {adf_result[1]}')
    if adf_result[1] < 0.05:
        print('The series is stationary')
    else:
        print('The series is not stationary')
    data['z_score'] = (data['Close'] - data['Close'].rolling(window=20).mean()) / data['Close'].rolling(window=20).std()
    data['signal'] = np.where(data['z_score'] < -1, 1, 0)
    data['signal'] = np.where(data['z_score'] > 1, -1, data['signal'])
    data['positions'] = data['signal'].diff()
    create_simple_tear_sheet(data['Close'].pct_change().dropna(), live_start_date='2022-06-01')
    return data

# Run strategies and plot
apple_mac = moving_average_crossover('AAPL', 50, 200)
plt.figure(figsize=(20,10))
plt.plot(apple_mac.index, apple_mac['Close'], label='AAPL')
plt.plot(apple_mac.index, apple_mac['short_mavg'], label='50 day moving average')
plt.plot(apple_mac.index, apple_mac['long_mavg'], label='200 day moving average')
plt.show()

apple_mr = mean_reversion('AAPL')
plt.figure(figsize=(20,10))
plt.plot(apple_mr.index, apple_mr['Close'], label='AAPL')
plt.plot(apple_mr.index, apple_mr['z_score'], label='Z_score')
plt.show()
```

Please note that these are just simple examples. Real-life trading strategy development involves a lot more complexity and considerations, including trade execution, transaction costs, risk management, etc. Also, past performance does not guarantee future results. Therefore, more complicated strategies and due diligence is needed in actual trading.