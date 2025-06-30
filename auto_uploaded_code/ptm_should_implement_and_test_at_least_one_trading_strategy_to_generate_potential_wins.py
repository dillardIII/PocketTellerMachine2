from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple implementation of a moving average crossover strategy using Python and the pandas library. This strategy generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average.

```python
import pandas as pd
import yfinance as yf

# Download historical data for required stocks
data = yf.download('AAPL','2016-01-01','2021-12-31')

# Calculate short-term simple moving average
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Create a column 'Signal' such that if 20-day SMA is greater than 50-day SMA then Signal is 1 else 0
data['Signal'] = 0.0  
data['Signal'][data['SMA_20'] > data['SMA_50']] = 1.0

# Create a column 'Position' which is a day-to-day difference of the 'Signal' column
data['Position'] = data['Signal'].diff()

# Print data
print(data)

# Now, when Position column is 1 then it means a buy signal and when Position column is -1 then it means a sell signal.
```

Please note that this is a very basic trading strategy and real-world strategies involve much more factors and complexity. Also, this strategy does not take into account trading fees or slippage. 

You should also be aware that past performance is not indicative of future results, and you should not rely on this strategy to make real trading decisions without consulting a financial advisor or conducting your own research.