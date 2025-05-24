Here is a simple Python code that uses the `yfinance` library to download stock data and initiate a trade based on a simple strategy. This code is for demonstration purposes only and does not guarantee any profits. It's always recommended to use a well-tested strategy for real trading.

```python
import yfinance as yf
from datetime import datetime, timedelta

# Define the stock to trade
stock_symbol = 'AAPL'

# Download historical data as dataframe
data = yf.download(stock_symbol, start=datetime.now() - timedelta(days=30), end=datetime.now())

# Calculate moving averages
data['MA10'] = data['Close'].rolling(window=10).mean()
data['MA20'] = data['Close'].rolling(window=20).mean()

# Define a simple strategy: Buy if MA10 > MA20, else sell
data['Buy_Signal'] = (data['MA10'] > data['MA20']).astype(int).diff()

# Print the dataframe
print(data)

# Initiate a trade based on the strategy
for i in range(len(data)):
    if data['Buy_Signal'].iloc[i] == 1.0:
        print(f"Buy {stock_symbol} at ${data['Close'].iloc[i]} on {data.index[i]}")
    elif data['Buy_Signal'].iloc[i] == -1.0:
        print(f"Sell {stock_symbol} at ${data['Close'].iloc[i]} on {data.index[i]}")
```

This script first downloads the past 30 days of data for the specified stock symbol. It then calculates 10-day and 20-day moving averages of the closing prices. A buy signal is generated when the 10-day moving average crosses above the 20-day moving average, and a sell signal is generated when the 10-day moving average crosses below the 20-day moving average. The script then initiates trades based on these signals.

Please note that you need to install `yfinance` library to run this code. You can install it using pip:

```
pip install yfinance
```

Also, this is a very simple strategy and might not be profitable in real trading. Always backtest your strategies before using them in live trading.