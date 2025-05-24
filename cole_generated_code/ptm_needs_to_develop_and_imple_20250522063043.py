To develop and implement a variety of trading strategies, we can use Python libraries such as pandas for data manipulation, yfinance to download stock price data, and numpy for numerical computations. Here's an example of two simple trading strategies: Moving Average Crossover and Mean Reversion.

Please note that this is a simplified example and real trading strategies would require much more complex algorithms, risk management, and careful consideration of transaction costs.

```python
import pandas as pd
import yfinance as yf
import numpy as np

# Download historical data for desired ticker
ticker = "AAPL"
ticker_data = yf.download(ticker, start="2020-01-01", end="2021-12-31")

# Moving Average Crossover Strategy
def moving_average_crossover(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   
    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Mean Reversion Strategy
def mean_reversion(data, window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Calculate mean and standard deviation
    signals['mean'] = data['Close'].rolling(window=window, min_periods=1, center=False).mean()
    signals['std'] = data['Close'].rolling(window=window, min_periods=1, center=False).std()

    # Create signals
    signals['signal'] = np.where(data['Close'] < (signals['mean'] - 1.5*signals['std']), 1.0, 0.0)
    signals['signal'] = np.where(data['Close'] > (signals['mean'] + 1.5*signals['std']), -1.0, signals['signal'])

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Apply strategies
mac_signals = moving_average_crossover(ticker_data, 20, 100)
mr_signals = mean_reversion(ticker_data, 20)

print(mac_signals)
print(mr_signals)
```

In the above code, the Moving Average Crossover strategy generates a buy signal when the short moving average crosses above the long moving average, and a sell signal when the short moving average crosses below the long moving average.

The Mean Reversion strategy generates a buy signal when the price falls 1.5 standard deviations below the mean, and a sell signal when the price rises 1.5 standard deviations above the mean.