In order to develop a trading strategy, we need to define some rules or conditions under which we will buy or sell the stocks. Here is a simple Python code for a trading strategy using moving average crossover. This strategy is based on two moving averages, a "fast" moving average (short term) and a "slow" moving average (long term). When the fast moving average crosses above the slow moving average, it's a signal to buy. When the fast moving average crosses below the slow moving average, it's a signal to sell.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for required stocks
ticker = "AAPL"
tickerData = yf.Ticker(ticker)
data = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate the short term simple moving average
short_sma = data.rolling(window=20).mean()

# Calculate the long term simple moving average
long_sma = data.rolling(window=100).mean()

# Create a column in the data dataframe to hold the trading signals
data['signal'] = 0.0

# Generate trading signals based on the crossover of the short and long moving averages
data['signal'][short_sma > long_sma] = 1.0
data['signal'][short_sma < long_sma] = -1.0

# Calculate the daily returns
data['daily_return'] = data['Close'].pct_change()

# Calculate the strategy returns
data['strategy_returns'] = data['daily_return'] * data['signal'].shift()

# Print the first few rows of the data dataframe
print(data.head())
```

This is a very basic trading strategy and may not be profitable in real-world trading. It's important to backtest any strategy before using it in live trading. Also, this strategy does not take into account transaction costs or slippage. 

Please note that this code requires the yfinance and pandas libraries. If these are not installed, you can install them using pip:

```bash
pip install yfinance pandas
```