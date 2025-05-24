Sure, I can provide a simple example of a Python code for a basic trading strategy. This strategy will be a simple moving average crossover strategy. In this strategy, we buy when the short-term moving average crosses above the long-term moving average, and sell when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic strategy and might not be profitable in real trading. It's just an example to show how to implement a trading strategy in Python.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = "AAPL"
data = yf.download(ticker, start="2020-01-01", end="2022-12-31")

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

This code will print a dataframe where a 1 in the 'position' column indicates a buy order and a -1 indicates a sell order.

You would need to install yfinance package to download the stock data. You can install it using pip:

```bash
pip install yfinance
```

Remember, this is a very basic strategy and in real trading you would need to consider transaction costs, risk management, portfolio optimization and many other factors.