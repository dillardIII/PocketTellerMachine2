from ghost_env import INFURA_KEY, VAULT_ADDRESS
Your request is quite broad and developing a trading strategy involves a lot of factors. However, I can provide you with a simple example of a Python code that uses a basic trading strategy. This strategy is called Moving Average Crossover. It's a simple strategy that buys when the short term moving average crosses above the long term moving average and sells when the short term moving average crosses below the long term moving average.

This code uses the `pandas_datareader` library to fetch historical stock price data from Yahoo Finance and `pandas` to calculate the moving averages.

```python
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

# Define the stock to be analyzed
stock = 'AAPL'

# Define the period for which we want historical data
start_date = datetime(2020, 1, 1)
end_date = datetime.now()

# Fetch the data
df = pdr.get_data_yahoo(stock, start_date, end_date)

# Calculate the short term moving average
short_rolling = df['Close'].rolling(window=20).mean()

# Calculate the long term moving average
long_rolling = df['Close'].rolling(window=100).mean()

# Create a signal when the short term moving average crosses the long term moving average
df['signal'] = 0.0
df['signal'][short_rolling > long_rolling] = 1.0

# Create trading orders based on the signal
df['positions'] = df['signal'].diff()

# Print the DataFrame
print(df)
```

This code generates a DataFrame with the stock's historical price data, two moving averages, a signal column that is 1.0 when the short term moving average is above the long term moving average and 0.0 otherwise, and a positions column that indicates when to buy (1.0) and when to sell (-1.0).

Please note that this is a very basic trading strategy and is unlikely to be profitable without further refinement and risk management. Also, the `pandas_datareader` library may not work if Yahoo Finance changes their website or if the library is not maintained.