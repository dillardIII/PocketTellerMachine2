Sure, here is a simple Python code using pandas and yfinance libraries to implement and test two different trading strategies: Moving Average Crossover and Buy and Hold. 

Please note that this is a very basic implementation and real trading strategies should consider more factors and be tested more thoroughly.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
data = yf.download(tickers_list,'2015-1-1')['Adj Close']

# Print first 5 rows of the data
print(data.head())

# Implementing Moving Average Crossover strategy
def MAC(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = data.rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = data.rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Implementing Buy and Hold strategy
def buy_and_hold(data):
    signals = pd.DataFrame(index=data.index)
    signals['Buy'] = 0.0
    signals['Sell'] = 0.0

    # Buy on the first day and hold
    signals['Buy'][0] = 1

    return signals

# Testing the strategies
for ticker in tickers_list:
    print(f"Testing for {ticker}")
    data_ticker = data[ticker]
    
    # Moving Average Crossover
    signals = MAC(data_ticker, 20, 100)
    print(signals)

    # Buy and Hold
    signals = buy_and_hold(data_ticker)
    print(signals)
```

This code fetches the adjusted close prices for a list of tickers using the yfinance library. Then it tests two strategies: Moving Average Crossover and Buy and Hold. The Moving Average Crossover strategy generates a buy signal when the short moving average crosses above the long moving average, and a sell signal when the short moving average crosses below the long moving average. The Buy and Hold strategy simply buys on the first day and holds the position.