To develop a trading strategy, we can use the concept of moving averages, a common strategy used in trading. This strategy can be implemented using Python with the help of the pandas library. Here is a simple example of a trading strategy using moving averages:

```python
import pandas as pd
import pandas_datareader as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the start and end dates
start_date = '01-01-2020'
end_date = '31-12-2020'

# Get the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term/simple moving average over a 20 day period
df['SMA_20'] = df['Adj Close'].rolling(window=20).mean()

# Calculate the long-term/simple moving average over a 100 day period
df['SMA_100'] = df['Adj Close'].rolling(window=100).mean()

# Create a function to signal when to buy and sell an asset/stock
def implement_strategy(data):
    buy_list = []
    sell_list = []
    flag = False

    for i in range(len(data)):
        if data['SMA_20'][i] > data['SMA_100'][i]:
            if flag != True:
                buy_list.append(data['Adj Close'][i])
                sell_list.append(np.nan)
                flag = True
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        elif data['SMA_20'][i] < data['SMA_100'][i]:
            if flag != False:
                sell_list.append(data['Adj Close'][i])
                buy_list.append(np.nan)
                flag = False
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)

    return (buy_list, sell_list)

# Implement the strategy
df['Buy_Signal_Price'], df['Sell_Signal_Price'] = implement_strategy(df)

# Print the DataFrame
print(df)
```

This code will print a DataFrame with the stock's adjusted close price, the 20-day simple moving average, the 100-day simple moving average, and the buy and sell signal prices. The buy and sell signals are based on when the 20-day simple moving average crosses the 100-day simple moving average.

Please note that this is a very basic trading strategy and should not be used for actual trading without further enhancements and testing. It's always recommended to consult with a financial advisor before making any trading decisions.