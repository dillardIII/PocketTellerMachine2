Sure, I can provide a simple example of a trading strategy using Python. In this example, we will use a simple moving average crossover strategy. This strategy buys when the short-term moving average crosses above the long-term moving average, and sells when the short-term moving average crosses below the long-term moving average.

Please note that this is a very simple strategy and is not guaranteed to be profitable. It is just an example to illustrate how a trading strategy could be implemented in Python.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

# Download historical data for required stocks
ticker = "AAPL"
tickerData = yf.Ticker(ticker)
data = tickerData.history(period='1d', start='2010-1-1', end=datetime.now().strftime('%Y-%m-%d'))

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create a 'signal' (invested or not invested) when short is above long
data['signal'] = np.where(short_sma > long_sma, 1.0, 0.0)

# Calculate daily returns
data['daily_return'] = data['Close'].pct_change()

# Calculate strategy returns
data['strategy_returns'] = data['signal'].shift() * data['daily_return']

# Calculate cumulative returns
data['cumulative_strategy_returns'] = (1 + data['strategy_returns']).cumprod()

# Print the DataFrame
print(data)
```

This code downloads historical data for a specific stock (in this case, Apple), calculates the short-term and long-term simple moving averages, generates a trading signal based on the crossover of these averages, and then calculates the returns of this strategy.

Please note that you will need to install the `yfinance`, `pandas`, and `numpy` libraries to run this code. You can do this using pip:

```bash
pip install yfinance pandas numpy
```

Also, please remember that this is a very basic strategy and should not be used for actual trading without further refinement and testing.