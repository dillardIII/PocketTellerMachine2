Sure, I can help you with that. Here's a simple example of how you might implement multiple trading strategies in Python using the `yfinance` library to get stock data. In this example, we'll implement two strategies: a moving average crossover strategy and a mean reversion strategy.

```python
import pandas as pd
import yfinance as yf

# Download historical data for required stocks
data = yf.download('AAPL','2016-01-01','2021-12-31')

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window).mean()
    return ema

# Moving Average Crossover Strategy
def moving_average_crossover(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short simple moving average
    signals['short_mavg'] = calculate_sma(data['Close'], short_window)
    # Long simple moving average
    signals['long_mavg'] = calculate_sma(data['Close'], long_window)

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

    # Calculate the mean for the past window days
    signals['mean'] = calculate_sma(data['Close'], window)
    # Calculate the standard deviation for the past window days
    signals['std'] = data['Close'].rolling(window=window).std()

    # Create signals
    signals['signal'] = np.where(data['Close'] < (signals['mean'] - 1.5 * signals['std']), 1.0, 0.0)
    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Apply strategies
moving_average_signals = moving_average_crossover(data, 20, 100)
mean_reversion_signals = mean_reversion(data, 20)

print(moving_average_signals)
print(mean_reversion_signals)
```

Please note that this is a very basic example and real trading strategies would need to be much more complex and consider many more factors. Also, this code does not include any sort of backtesting or performance measurement, which would be crucial in a real trading system.