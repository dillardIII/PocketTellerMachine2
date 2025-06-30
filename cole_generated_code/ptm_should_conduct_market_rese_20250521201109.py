from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python script that uses the `yfinance` library to download stock data and `pandas` to analyze it. This script identifies stocks with the highest percentage increase over the last 5 days.

Please note that this is a very basic form of market analysis and should not be used for actual trading decisions without further enhancements.

```python
import yfinance as yf
import pandas as pd

# Define the list of stocks we are interested in
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']

# Download historical market data
data = yf.download(stocks, start="2022-01-01", end="2022-12-31")

# Calculate the percentage change over the last 5 days
data['5 Day % Change'] = (data['Adj Close'].shift(-5) - data['Adj Close']) / data['Adj Close'] * 100

# Identify the stocks with the highest percentage increase
top_stocks = data['5 Day % Change'].idxmax()

print(top_stocks)
```

This code will print out the stock symbol of the stock with the highest percentage increase over the last 5 days.

Please note that you need to install the `yfinance` and `pandas` libraries if you haven't done so already. You can install them using pip:

```bash
pip install yfinance pandas
```

Also, you need to replace the `start` and `end` parameters with the actual dates for your market research.