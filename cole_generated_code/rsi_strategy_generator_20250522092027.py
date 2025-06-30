from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple implementation of a Relative Strength Index (RSI) strategy generator in Python using the `pandas` and `yfinance` libraries. This strategy will generate buy signals when the RSI is below 30 (oversold) and sell signals when the RSI is above 70 (overbought).

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Download historical data as dataframe
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

# Calculate the RSI
delta = df['Adj Close'].diff()
up = delta.clip(lower=0)
down = -1*delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up/ema_down

df['RSI'] = 100 - (100/(1 + rs))

# Generate signals
df['Buy_Signal'] = (df['RSI'] < 30)
df['Sell_Signal'] = (df['RSI'] > 70)

print(df)
```

This code will print a dataframe with the historical data for Apple Inc. (AAPL) along with the calculated RSI and the generated buy/sell signals. Please replace "AAPL" with the ticker symbol of the stock you're interested in.

Please note that this is a very simple strategy and may not be profitable in real trading. Always backtest your strategies before using them in live trading.