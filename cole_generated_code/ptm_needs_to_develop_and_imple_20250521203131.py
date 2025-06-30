from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop a trading strategy, we need to define a set of rules to guide our trading decisions. Here is a very simple Python code for a trading strategy using moving averages. 

This strategy will buy when the short-term moving average crosses above the long-term moving average, and sell when the short-term moving average crosses below the long-term moving average. 

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker,'2020-01-01','2021-12-31')

# Calculate short-term and long-term moving averages
short_window = 40
long_window = 100

signals = pd.DataFrame(index=ticker_data.index)
signals['signal'] = 0.0

# Short moving average
signals['short_mavg'] = ticker_data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Long moving average
signals['long_mavg'] = ticker_data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

print(signals)
```

This code uses Yahoo Finance to download historical data, calculates the short-term and long-term moving averages, and generates trading signals based on these moving averages. 

Please note that this is a very basic trading strategy and may not be profitable in real trading. It's always recommended to backtest any strategy before live trading. Also, this strategy does not take into account trading fees or slippage. 

You would need to install the `yfinance` package to download the data from Yahoo Finance. You can install it using `pip install yfinance`.