from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. This example will use a simple moving average crossover strategy. This strategy buys a stock when the short-term moving average crosses above the long-term moving average, and sells the stock when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic strategy and it doesn't take into account many factors that can influence the stock price. Also, it's recommended to use historical data to backtest the strategy before implementing it.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

# Download historical data for desired stock
ticker = "AAPL"
start_date = datetime(2020,1,1)
end_date = datetime(2021,1,1)
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate short-term simple moving average (SMA)
short_sma = 50
data['ShortSMA'] = data['Close'].rolling(window=short_sma).mean()

# Calculate long-term simple moving average (SMA)
long_sma = 200
data['LongSMA'] = data['Close'].rolling(window=long_sma).mean()

# Create a column 'Signal' such that if ShortSMA > LongSMA then buy else sell
data['Signal'] = 0.0  
data['Signal'][short_sma:] = np.where(data['ShortSMA'][short_sma:] 
                                      > data['LongSMA'][short_sma:], 1.0, 0.0)   

# Generate trading orders
data['Position'] = data['Signal'].diff()

# Print data
print(data)
```

In this code, we first download the historical data for the desired stock using the `yfinance` library. Then, we calculate the short-term and long-term simple moving averages (SMA). We create a new column 'Signal' that is set to 1.0 when the short-term SMA is greater than the long-term SMA (indicating a buy signal), and 0.0 otherwise (indicating a sell signal). Finally, we generate trading orders by taking the difference of the 'Signal' column.

Please install necessary libraries by using pip install command:
```python
pip install pandas numpy yfinance
```