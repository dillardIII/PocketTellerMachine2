from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of how you might implement different trading strategies in Python. For this example, I'll use the `yfinance` library to fetch stock data, and `pandas` to handle the data. 

Please note that this is a very simplified example and actual trading strategies would require much more complex algorithms and risk management techniques.

```python
import yfinance as yf
import pandas as pd

# Define the stocks to trade
stocks = ['AAPL', 'MSFT', 'GOOGL']

# Fetch the stock data
data = yf.download(stocks, start='2020-01-01', end='2020-12-31')

# Calculate the moving averages for different strategies
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Define a simple trading strategy: Buy when the 20-day moving average is above the 50-day moving average
data['Buy_Signal'] = (data['SMA_20'] > data['SMA_50'])

# Print the data
print(data)
```

This script fetches the closing prices for Apple, Microsoft, and Google for the year 2020. It then calculates the 20-day and 50-day simple moving averages (SMA) for these stocks. The trading strategy is to buy the stock when the 20-day SMA is above the 50-day SMA.

Please remember that this is a very basic example and does not take into account many factors that would be important in a real trading strategy, such as transaction costs, risk management, diversification, etc.