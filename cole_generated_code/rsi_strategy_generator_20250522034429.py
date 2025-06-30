from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code that generates an RSI strategy using the `pandas` and `yfinance` libraries.

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Download historical data as dataframe
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

# Calculate the RSI
delta = df['Close'].diff()
up = delta.clip(lower=0)
down = -1*delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up/ema_down

df['RSI'] = 100 - (100/(1 + rs))

# Create a function to signal when to buy and sell an asset
def generate_signals(df):
    buy_signal = []
    sell_signal = []
    for i in range(len(df['RSI'])):
        if df['RSI'][i] < 30:  # Oversold condition
            buy_signal.append(df['Close'][i])
            sell_signal.append(np.nan)
        elif df['RSI'][i] > 70:  # Overbought condition
            sell_signal.append(df['Close'][i])
            buy_signal.append(np.nan)
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)
            
    return buy_signal, sell_signal

# Generate signals
df['Buy_Signal_Price'], df['Sell_Signal_Price'] = generate_signals(df)

print(df)
```

This script downloads historical price data for Apple Inc. (AAPL), calculates the RSI, and generates buy and sell signals based on the RSI. The buy signal is generated when the RSI falls below 30 (oversold condition), and the sell signal is generated when the RSI rises above 70 (overbought condition). The signals are then added to the dataframe.