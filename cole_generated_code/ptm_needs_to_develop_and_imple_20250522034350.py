Sure, I can provide a simple example of a Python code for a trading strategy. This strategy will be based on moving averages, a common technical indicator used in trading. However, please note that this is a very basic strategy and real-world trading strategies are much more complex and involve many other factors.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = 'AAPL'
df = yf.download(ticker, start='2020-01-01', end='2021-12-31')

# Calculate the short-term simple moving average
short_sma = df['Close'].rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = df['Close'].rolling(window=100).mean()

# Create a column in the DataFrame to hold the trading signals
df['signal'] = 0.0

# Generate trading signals based on the crossover of the short and long SMAs
df['signal'][short_sma > long_sma] = 1.0
df['signal'][short_sma < long_sma] = -1.0

# Calculate the daily returns of the strategy
df['strategy_returns'] = df['signal'].shift() * df['Close'].pct_change()

# Print the DataFrame
print(df)
```

This strategy generates a trading signal whenever the short-term moving average crosses the long-term moving average. If the short-term average is higher, the strategy goes long (buys), and if it's lower, the strategy goes short (sells). The daily returns of the strategy are then calculated based on these signals.

Please note that this is a very simplified trading strategy and is not meant for actual trading. It doesn't take into account transaction costs, slippage, risk management, or other important factors. It's just a basic example to illustrate how a trading strategy could be coded in Python.