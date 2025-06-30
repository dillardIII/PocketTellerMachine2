from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help you with that. However, writing a trading strategy involves a lot of factors. It requires knowledge about financial markets, trading rules, and risk management. 

Here is a simple example of a Python code that implements a basic moving average crossover strategy using pandas. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it means the price is increasing and it's time to buy. Conversely, when the short moving average crosses below the long moving average, it means the price is decreasing and it's time to sell.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker,'2020-1-1','2020-12-31')

# Calculate short-term simple moving average
short_sma= ticker_data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma= ticker_data['Close'].rolling(window=100).mean()

# Create signals based on crossover
ticker_data['signal'] = 0.0
ticker_data['signal'][short_sma > long_sma] = 1.0

# Generate trading orders
ticker_data['position'] = ticker_data['signal'].diff()

# Print data
print(ticker_data)
```

Please note that this is a very basic trading strategy and may not be profitable in real trading. It's just an example to show how to implement a trading strategy in Python. 

In real-world trading, you would need to consider transaction costs, risk management, portfolio optimization, and many other factors. It's also important to backtest your strategy on historical data before you start trading.