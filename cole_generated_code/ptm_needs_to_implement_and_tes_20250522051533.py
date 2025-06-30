from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple Python code to simulate a basic trading strategy. Here, we'll use a simple moving average crossover strategy. We'll use the `pandas_datareader` library to fetch historical stock price data and `pandas` to manipulate the data.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex and might require more sophisticated tools and techniques.

```python
import pandas as pd
import pandas_datareader as web

# Fetch historical data
df = web.get_data_yahoo('AAPL', start='2020-01-01', end='2021-12-31')

# Calculate short-term and long-term moving averages
short_window = 20
long_window = 100
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0
signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   
signals['positions'] = signals['signal'].diff()

# Print signals
print(signals)
```

In this code, we first fetch the historical data for Apple Inc. (AAPL) from Yahoo Finance. We then calculate the short-term (20 days) and long-term (100 days) moving averages of the closing prices. 

A buy signal is generated when the short-term moving average crosses above the long-term moving average, and a sell signal is generated when the short-term moving average crosses below the long-term moving average.

Please make sure to install necessary libraries by using pip:
```bash
pip install pandas pandas_datareader numpy
```

Remember, this is a very simple strategy and might not be profitable in real trading. Always backtest your strategies before live trading.