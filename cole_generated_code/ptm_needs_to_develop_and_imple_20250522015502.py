Sure, I can provide a basic example of a trading strategy using Python. This strategy will be a simple moving average crossover strategy. This strategy is based on the idea that if the short term moving average crosses the long term moving average, it may be a signal of future price movement.

Please note that this is a very basic strategy and in real trading scenario, you would need to consider many other factors like trading fees, slippage, market impact, etc. Also, you would need historical price data to backtest this strategy.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = "AAPL"
data = yf.download(ticker, start="2020-01-01", end="2021-12-31")

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create signals based on crossover
data['signal'] = 0.0
data['signal'][short_sma > long_sma] = 1.0

# Generate trading orders
data['position'] = data['signal'].diff()

# Print data
print(data)
```

In this code:

1. We first download historical data for the desired ticker symbol using `yfinance` library.
2. Then we calculate the short-term and long-term simple moving averages.
3. We create a 'signal' column in our data where we mark 1.0 if the short-term moving average is greater than the long-term moving average.
4. We generate trading orders based on these signals. If the signal changes from 0 to 1, it means we need to buy the stock. If it changes from 1 to 0, it means we need to sell the stock.
5. Finally, we print the data.

This is a very basic strategy and may not be profitable in real trading. In real trading, you would need to consider many other factors and use more sophisticated strategies.