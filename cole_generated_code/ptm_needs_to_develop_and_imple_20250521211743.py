from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple Python code that uses a simple moving average crossover strategy. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it means that recent prices are getting higher than the average of the past prices, which is a buy signal. Conversely, when the short moving average crosses below the long moving average, it is a sell signal.

Please note that this is a very basic strategy and actual trading strategies can be much more complex involving multiple factors and indicators.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker, start='2020-01-01', end=datetime.today().strftime('%Y-%m-%d'))

# Calculate short-term simple moving average
short_sma = 50
ticker_data['Short_SMA'] = ticker_data['Close'].rolling(window=short_sma).mean()

# Calculate long-term simple moving average
long_sma = 200
ticker_data['Long_SMA'] = ticker_data['Close'].rolling(window=long_sma).mean()

# Create a column to hold the buy/sell signals
ticker_data['Buy_Signal'] = np.where(ticker_data['Short_SMA'] > ticker_data['Long_SMA'], 1, 0)
ticker_data['Sell_Signal'] = np.where(ticker_data['Short_SMA'] < ticker_data['Long_SMA'], -1, 0)

# Print data
print(ticker_data)
```

This script downloads the historical data for a specific stock (Apple Inc. in this case), calculates the short-term and long-term simple moving averages, and generates buy/sell signals based on the crossover of these moving averages.

Please note that you need to have the `pandas`, `numpy`, `yfinance`, and `datetime` libraries installed in your Python environment to run this script. You can install them using pip:

```
pip install pandas numpy yfinance
```

Also, remember that this is a very simplistic strategy and might not work well in real trading. Always backtest your strategies before using them in live trading.