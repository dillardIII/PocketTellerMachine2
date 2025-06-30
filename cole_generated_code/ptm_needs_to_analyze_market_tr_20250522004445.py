from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that uses the yfinance library to get the stock data and pandas to analyze it. This code will identify the stocks with the highest percentage increase for the day.

Please note that this is a very basic example and real-world trading algorithms are much more complex and take into account many other factors.

```python
import yfinance as yf
import pandas as pd

# Define the list of stocks we are interested in
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']

# Get the data for the last day
data = yf.download(stocks, period='1d')

# Calculate the percentage change
data['Change'] = (data['Close'] - data['Open']) / data['Open'] * 100

# Sort by the change and get the top 5 stocks
top_stocks = data.sort_values('Change', ascending=False).head(5)

print(top_stocks)
```

This script will download the latest daily data for the specified stocks, calculate the percentage change from the opening price to the closing price, and then print out the top 5 stocks with the highest percentage increase.

Please note that you need to install yfinance and pandas libraries to run this script. You can install them using pip:

```bash
pip install yfinance pandas
```