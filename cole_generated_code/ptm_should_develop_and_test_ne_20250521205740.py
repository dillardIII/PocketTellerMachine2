In order to develop and test new trading strategies, we need to have a dataset of historical trading data. We also need to define what a "winning" trade is. For the sake of this example, let's assume that a winning trade is one where the sell price is higher than the buy price.

Here is a simplified example of how to develop and test a trading strategy using Python. We will use the pandas library to handle our data and the yfinance library to download historical stock price data.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2020-12-31')

# Define a simple trading strategy: buy when the price is lower than the 10-day moving average, sell when it's higher
data['MA10'] = data['Close'].rolling(10).mean()
data['Buy_Signal'] = (data['Close'] < data['MA10'])
data['Sell_Signal'] = (data['Close'] > data['MA10'])

# Assume we buy/sell at the next day's open price
data['Buy_Price'] = data['Open'].shift(-1)[data['Buy_Signal']]
data['Sell_Price'] = data['Open'].shift(-1)[data['Sell_Signal']]

# Calculate the profit/loss
data['Profit'] = data['Sell_Price'] - data['Buy_Price']

# Sum up the profit/loss to get the total profit/loss for this strategy
total_profit = data['Profit'].sum()

print(f'Total profit from this strategy: {total_profit}')
```

This is a very simple strategy and in reality, you would want to consider more factors, such as transaction costs. Also, this strategy does not consider the amount of capital you have and assumes you can always buy/sell when the signal is given. You would also want to split your data into a training set and a test set, and use the training set to develop the strategy and the test set to evaluate its performance.