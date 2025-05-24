To develop and implement trading strategies, we can use Python's pandas library for data manipulation and analysis, and yfinance library to download historical market data from Yahoo finance. Here's a simple example of a moving average crossover strategy:

```python
import pandas as pd
import yfinance as yf

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker, start="2020-01-01", end="2021-12-31")

# Calculate the short-term simple moving average
short_sma = ticker_data.Close.rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = ticker_data.Close.rolling(window=100).mean()

# Create a 'signal' (invested or not invested) when short moving average crosses the long moving average
ticker_data['signal'] = 0.0
ticker_data['signal'][short_sma > long_sma] = 1.0

# The difference in these signals will generate actual trading orders
ticker_data['positions'] = ticker_data['signal'].diff()

# Print the DataFrame
print(ticker_data)
```

This script downloads the historical data for Apple Inc. from Yahoo Finance, calculates the short-term (20 days) and long-term (100 days) moving averages, and generates trading signals based on the crossover of these moving averages. A buy signal is generated when the short-term average crosses above the long-term average, and a sell signal is generated when the short-term average crosses below the long-term average.

Please note that this is a very basic trading strategy and may not be profitable. It's recommended to use more sophisticated strategies and risk management techniques in actual trading.