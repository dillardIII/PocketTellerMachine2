from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code implementing a basic moving average crossover strategy using pandas library. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it means the price is increasing and it's a good time to buy. Conversely, when the short moving average crosses below the long moving average, it means the price is decreasing and it's a good time to sell.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker, start="2020-01-01", end=datetime.today().strftime('%Y-%m-%d'))

# Calculate short-term simple moving average
short_sma= 20
ticker_data['Short_SMA'] = ticker_data['Close'].rolling(window=short_sma).mean()

# Calculate long-term simple moving average
long_sma = 50
ticker_data['Long_SMA'] = ticker_data['Close'].rolling(window=long_sma).mean()

# Create a column 'Signal' such that if Short_SMA > Long_SMA then buy else sell
ticker_data['Signal'] = 0.0  
ticker_data['Signal'][short_sma:] = np.where(ticker_data['Short_SMA'][short_sma:] 
                                            > ticker_data['Long_SMA'][short_sma:], 1.0, 0.0)   

# Generate trading orders
ticker_data['Position'] = ticker_data['Signal'].diff()

# Print the DataFrame
print(ticker_data)
```

This is a very simple trading strategy and may not be profitable in real trading. You should consider other factors like trading fees, slippage, and market impact. Also, you should use more sophisticated strategies and machine learning models to predict the market movement.

Please install the necessary libraries by running `pip install pandas yfinance numpy` before running the script.

Also, please note that this script is for educational purposes only and should not be used for real trading without proper backtesting and strategy optimization.