Sure, I can provide you with a simple example of a trading strategy using Python. This strategy is called a Moving Average Crossover, which is one of the most common systematic trading strategies. This strategy is not a recommendation for real trading, it's just an example.

In this strategy, we will use two moving averages: one will be faster and the other slower. When the faster moving average crosses above the slower one, it may be a good time to buy. Conversely, when the faster moving average crosses below the slower one, it may be a good time to sell.

We will use the `pandas` library for data manipulation and the `yfinance` library to download the stock data.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(stock, start='2000-01-01', end='2020-12-31'):
    data = yf.download(stock, start, end)
    return pd.DataFrame(data)

# Calculate moving averages
def calculate_MA(data, short_window, long_window):
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

# Download Apple Inc. data
data = download_data('AAPL')

# Calculate moving averages and generate signals
signals = calculate_MA(data, 50, 200)

# Print signals
print(signals)
```

In this code, we first download the historical data for the desired ticker symbol (in this case, 'AAPL' for Apple Inc.). We then calculate the short and long moving averages and generate trading signals based on these. When the short moving average is greater than the long moving average, we generate a buy signal (1.0), and when it's less, we generate a sell signal (0.0). The 'positions' column shows the change in signals from the previous day, indicating when to place a trade.