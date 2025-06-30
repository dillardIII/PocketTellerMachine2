from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. This strategy is based on a simple Moving Average Crossover, which is one of the most popular trading strategies. 

In this strategy, we will use two moving averages: a fast one (short term) and a slow one (long term). When the fast moving average crosses above the slow moving average, it indicates a bullish signal, and we should buy. Conversely, when the fast moving average crosses below the slow moving average, it indicates a bearish signal, and we should sell.

Please note that this is a very basic strategy and in real-world trading, you would need to consider many other factors such as transaction costs, slippage, risk management, etc.

Here is a simple implementation using Python and pandas:

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for required stocks
data = yf.download('AAPL','2016-01-01','2021-12-31')

# Calculate the short term and long term moving averages
data['short_mavg'] = data['Close'].rolling(window=20).mean()
data['long_mavg'] = data['Close'].rolling(window=100).mean()

# Create a 'signal' (invested or not invested) when the short moving average crosses the long moving average
data['signal'] = np.where(data['short_mavg'] > data['long_mavg'], 1.0, 0.0)

# Generate trading orders
data['positions'] = data['signal'].diff()

# Print the DataFrame
print(data)
```

In this code, we first download the historical data for Apple stock using the `yfinance` library. Then we calculate the short-term (20 days) and long-term (100 days) moving averages of the closing prices. We generate a trading signal whenever the short moving average crosses the long moving average. Finally, we generate trading orders based on these signals.

Please note that you need to install the `yfinance` library to download the stock data from Yahoo Finance. You can install it using pip:

```bash
pip install yfinance
```

Also, this is a very basic strategy and may not be profitable in real trading. You should always backtest your strategies before live trading.