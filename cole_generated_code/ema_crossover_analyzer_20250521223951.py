from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help you with that. Here's a simple implementation of an EMA Crossover Analyzer using Python and pandas library. 

This code will calculate the short-term (9-day) and long-term (21-day) Exponential Moving Average (EMA) of a stock's prices. A "Buy" signal is generated when the short-term EMA crosses above the long-term EMA, and a "Sell" signal is generated when the short-term EMA crosses below the long-term EMA.

```python
import pandas as pd
import pandas_datareader as pdr
import datetime as dt

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
data = pdr.get_data_yahoo(tickers_list, start=dt.datetime.today()-dt.timedelta(365), end=dt.datetime.today())['Close']

def EMA_Crossover(data, short_period, long_period):
    # Calculate short-term EMA
    ShortEMA = data.ewm(span=short_period, adjust=False).mean()
    # Calculate long-term EMA
    LongEMA = data.ewm(span=long_period, adjust=False).mean()
    # Create signals
    data['Buy_Signal'] = ShortEMA > LongEMA
    data['Sell_Signal'] = ShortEMA < LongEMA
    return data

# Apply EMA Crossover strategy
for ticker in tickers_list:
    data[ticker] = EMA_Crossover(data[ticker], 9, 21)

# Print data
print(data)
```

This code will print the stock prices along with the "Buy_Signal" and "Sell_Signal" columns. If the "Buy_Signal" is True, it means that the short-term EMA has crossed above the long-term EMA, indicating a good time to buy. If the "Sell_Signal" is True, it means that the short-term EMA has crossed below the long-term EMA, indicating a good time to sell.

Please note that this is a very basic implementation of the EMA Crossover strategy. In a real-world scenario, you would need to consider other factors such as trading fees, slippage, and the risk of overfitting.