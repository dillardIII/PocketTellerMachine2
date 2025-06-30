from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. This example will use a simple moving average crossover strategy. We will use the `pandas` library for data manipulation and the `yfinance` library to download stock price data from Yahoo Finance.

Please install necessary libraries by running the following commands in your terminal:
```
pip install pandas
pip install yfinance
```

Here is the Python code:

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = "AAPL"
ticker_data = yf.download(ticker, start="2020-01-01", end="2022-12-31")

# Calculate moving averages
short_window = 20
long_window = 100

signals = pd.DataFrame(index=ticker_data.index)
signals['signal'] = 0.0

# Short moving average
signals['short_mavg'] = ticker_data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Long moving average
signals['long_mavg'] = ticker_data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

This script downloads the historical price data for the specified ticker symbol, calculates short and long moving averages, and generates trading signals based on these moving averages. A buy signal is generated when the short moving average crosses above the long moving average, and a sell signal is generated when the short moving average crosses below the long moving average.

Please note that this is a very basic trading strategy and is not recommended for actual trading without further enhancements and risk management.