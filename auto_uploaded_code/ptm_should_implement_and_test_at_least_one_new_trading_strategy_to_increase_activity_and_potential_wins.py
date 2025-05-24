Here's a simple Python code to implement a Moving Average Crossover strategy. This strategy is one of the most commonly used strategies in trading. It uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. Conversely, when the short moving average crosses below the long moving average, it's a signal to sell.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Download historical data as dataframe
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

# Calculate short-term simple moving average
Short_SMA = pd.DataFrame()
Short_SMA['Close Price'] = df['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
Long_SMA = pd.DataFrame()
Long_SMA['Close Price'] = df['Close'].rolling(window=100).mean()

# Create a new dataframe to store all data
data = pd.DataFrame()
data['AAPL'] = df['Close']
data['Short_SMA'] = Short_SMA['Close Price']
data['Long_SMA'] = Long_SMA['Close Price']

# Create signals
signals = pd.DataFrame(index=data.index)
signals['signal'] = 0.0
signals['short_mavg'] = data['Short_SMA']
signals['long_mavg'] = data['Long_SMA']

# Generate trading signals (1 for buy, -1 for sell)
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, -1.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print data
print(data)
print(signals)
```

Please note that this is a very basic trading strategy and in real-world trading, you would need to consider transaction costs, slippage, risk management, etc. Also, the performance of this strategy hasn't been tested in this code. You would need to backtest this strategy using historical data to see how it would have performed in the past before using it for actual trading.