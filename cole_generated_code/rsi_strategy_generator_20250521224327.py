from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple implementation of RSI (Relative Strength Index) strategy generator in Python using the `pandas` and `yfinance` libraries:

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

# Use yfinance while making calls to pandas_datareader
yf.pdr_override()

# Download historical data for required stocks
ticker = "AAPL"
df = pdr.get_data_yahoo(ticker, start="2020-01-01", end="2021-12-31")

def calculate_RSI(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Calculate 14 day RSI
df['RSI'] = calculate_RSI(df['Adj Close'], 14)

# Define the strategy
df['Buy_Signal'] = (df['RSI'] < 30)
df['Sell_Signal'] = (df['RSI'] > 70)

# Print data
print(df)
```

This code calculates the RSI for a given stock (in this case, AAPL) and generates trading signals based on the RSI. The strategy used here is simple: if the RSI is below 30, it's a buy signal, and if it's above 70, it's a sell signal. 

Please note that this is a very basic strategy and might not be profitable in real trading. Always backtest your strategies before using them in live trading.