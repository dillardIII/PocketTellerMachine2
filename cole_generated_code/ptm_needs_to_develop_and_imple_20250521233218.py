Sure, I can provide a simple example of a Python code for a trading strategy. This strategy will be a basic Moving Average Crossover strategy. It's a very simple strategy where we buy a stock when the short-term moving average crosses above the long-term moving average, and sell when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic strategy and might not be profitable in real trading. It's always recommended to use more complex strategies and consider more factors.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Download historical data as dataframe
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2022-12-31")

# Calculate short-term simple moving average
Short_SMA = df.Close.rolling(window=20).mean()

# Calculate long-term simple moving average
Long_SMA = df.Close.rolling(window=100).mean()

# Create signals based on crossover
df['Buy_Signal'] = np.where(Short_SMA > Long_SMA, 1, 0)
df['Sell_Signal'] = np.where(Short_SMA < Long_SMA, -1, 0)

# Print the dataframe
print(df)
```

This code will print a dataframe where 'Buy_Signal' column will have '1' for the days where we should buy the stock according to the strategy, and 'Sell_Signal' column will have '-1' for the days where we should sell the stock according to the strategy.

Please note that this code requires pandas, pandas_datareader, numpy and yfinance Python libraries. If these are not installed, you can install them using pip:

```bash
pip install pandas pandas_datareader numpy yfinance
```