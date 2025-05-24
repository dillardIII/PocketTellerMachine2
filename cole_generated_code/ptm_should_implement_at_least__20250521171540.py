Here is a simple example of a Python code of a trading strategy using moving averages. Please note that this is a simplified version and a real trading strategy would require more sophisticated and rigorous methods. 

```python
# Import necessary libraries
import pandas as pd
from pandas_datareader import data as web

# Define function for calculating moving averages
def calculate_moving_average(data, window):
    return data['Adj Close'].rolling(window=window).mean()

# Trading strategy function
def trading_strategy(data):
    # Calculate short-term moving average
    short_moving_avg = calculate_moving_average(data, 20)

    # Calculate long-term moving average
    long_moving_avg = calculate_moving_average(data, 50)

    # Create signal when short-term moving average crosses above long-term
    data['Buy_Signal'] = (short_moving_avg > long_moving_avg)

    # Create signal when short-term moving average crosses below long-term
    data['Sell_Signal'] = (short_moving_avg < long_moving_avg)

    return data

# Specify the stock symbol and date range
symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'

# Retrieve the data from Yahoo Finance
data = web.DataReader(symbol, 'yahoo', start_date, end_date)

# Apply the strategy
data = trading_strategy(data)

print(data)
```
This code implement a simple trading strategy based on moving averages. It creates a 'Buy_Signal' when the short-term moving average crosses above the long-term moving average, and a 'Sell_Signal' when the short-term moving average crosses below the long-term moving average. It uses Yahoo Finance to retrieve the stock data. We applied the strategy on Apple's stock (AAPL) but you can replace the symbol with any other stock you are interested in. The date range is also adjustable.