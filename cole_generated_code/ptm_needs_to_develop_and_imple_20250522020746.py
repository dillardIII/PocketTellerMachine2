Sure, I can help you with that. Here's a simple example of a Python trading strategy using a moving average crossover strategy. This strategy buys the stock when the short-term moving average crosses above the long-term moving average, and sells the stock when the short-term moving average crosses below the long-term moving average.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Fetching the data
data = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

# Calculate the short-term moving average
data['Short_SMA'] = data['Close'].rolling(window=20).mean()

# Calculate the long-term moving average
data['Long_SMA'] = data['Close'].rolling(window=100).mean()

# Create a column 'Signal' such that if the Short_SMA is greater than Long_SMA then 1 else 0
data['Signal'] = 0.0  
data['Signal'][data['Short_SMA'] > data['Long_SMA']] = 1.0

# Create a column 'Position' which is the difference of the present and the previous day's 'Signal'
data['Position'] = data['Signal'].diff()

# Print the DataFrame
print(data)

# Create a plot
data[['Close', 'Short_SMA', 'Long_SMA']].plot(grid=True, figsize=(10, 5))

# Plotting the sell signals
plt.plot(data[data['Position'] == -1.0].index, 
         data['Short_SMA'][data['Position'] == -1.0],
         'v', markersize=10, color='r')

# Plotting the buy signals
plt.plot(data[data['Position'] == 1.0].index, 
         data['Short_SMA'][data['Position'] == 1.0],
         '^', markersize=10, color='m')
plt.show()
```

This is a simple trading strategy and may not be profitable in real trading. You should consider other factors such as transaction costs, slippage, risk management, etc. when developing a trading strategy. 

Please replace "AAPL" with the symbol of the stock you want to analyze. The start and end dates can also be modified according to your needs. 

Please note that you will need to install the `pandas_datareader`, `yfinance`, and `matplotlib` libraries to run this code. You can install them using pip:

```bash
pip install pandas_datareader yfinance matplotlib
```