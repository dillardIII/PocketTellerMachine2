Sure, I can help you with that. Here is a simple example of a Python code that implements two basic trading strategies: Mean Reversion and Momentum. These strategies are just for illustrative purposes and should not be used for real trading without proper backtesting and risk management.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Define the instruments to download
tickers = ['AAPL', 'MSFT', 'SPY']

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = '2015-01-01'
end_date = '2020-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
panel_data = pdr.get_data_yahoo(tickers, start_date, end_date)

# Getting just the adjusted closing prices
adj_close = panel_data['Adj Close']

# Calculate the short and long windows for mean reversion strategy
short_window = 5
long_window = 20

# Initialize the signals DataFrame with the signal column
signals = pd.DataFrame(index=adj_close.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = adj_close.rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = adj_close.rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)

# Momentum strategy
# Calculate the returns
returns = adj_close.pct_change()

# Define the number of periods for momentum calculation
momentum_window = 5

# Calculate momentum
signals['momentum'] = returns.rolling(window=momentum_window).mean() 

# Create signals for momentum strategy
signals['signal_momentum'] = 0.0
signals['signal_momentum'][momentum_window:] = np.where(signals['momentum'][momentum_window:] 
                                                        > 0, 1.0, 0.0)

# Generate trading orders for momentum strategy
signals['positions_momentum'] = signals['signal_momentum'].diff()

# Print `signals` for momentum strategy
print(signals)
```

This code implements two simple trading strategies: Mean Reversion and Momentum. The Mean Reversion strategy assumes that the price will revert to its mean over time. It goes long when the price is below its rolling mean and short when it's above. The Momentum strategy assumes that the price will continue in the same direction. It goes long when the momentum is positive and short when it's negative. 

Please note that these strategies are oversimplified and don't take into account transaction costs, slippage, risk management, etc. They are provided for illustrative purposes only and should not be used for real trading without proper backtesting and risk management.