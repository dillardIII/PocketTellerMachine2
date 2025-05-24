Sure, here is a simple Python code implementing a basic trading strategy using Moving Average Crossover. This strategy increases the number of trades by buying when the short-term average crosses above the long-term average and selling when the short-term average crosses below the long-term average.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

# Define the stock to be traded
stock = 'AAPL'

# Load the data
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

# Calculate the short-term and long-term moving averages
df['ShortMA'] = df['Close'].rolling(window=20).mean()
df['LongMA'] = df['Close'].rolling(window=100).mean()

# Create a column 'Signal' such that if the short-term MA is greater than long-term MA then buy else sell
df['Signal'] = np.where(df['ShortMA'] > df['LongMA'], 1, 0)

# Create a column 'Position' which is the difference of the 'Signal' column and its previous value
df['Position'] = df['Signal'].diff()

# Print the dataframe
print(df)

# The 'Position' column indicates the trading signals. A value of 1 means buy and a value of -1 means sell.
```

This is a simple and basic strategy. In real trading, you would need to consider transaction costs, risk management, and other factors. Also, you should use more sophisticated strategies and machine learning models to predict the price and make trading decisions.

Please note that this code requires the `pandas`, `numpy`, and `pandas_datareader` libraries. You can install them using pip:

```shell
pip install pandas numpy pandas_datareader
```

Also, this code uses Yahoo Finance to get the stock data. If you want to use another data source, you would need to modify the code accordingly.