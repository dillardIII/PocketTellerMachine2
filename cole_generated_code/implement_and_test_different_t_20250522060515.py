Sure, I'll provide a simple implementation of two trading strategies: Mean Reversion and Momentum. 

Please note that this is a simplified version and real trading strategies require more complex algorithms, risk management, and data analysis.

```python
import pandas as pd
import numpy as np

# Assuming we have historical stock price data in 'stock_data.csv'
data = pd.read_csv('stock_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Mean Reversion Strategy
def mean_reversion(data, window=30):
    # Calculate the mean of the past 30 days
    mean = data['Close'].rolling(window=window).mean()

    # Buy if the price is 2% less than the mean
    data['Buy_Signal'] = np.where(data['Close'] < mean * 0.98, 1, 0)

    # Sell if the price is 2% more than the mean
    data['Sell_Signal'] = np.where(data['Close'] > mean * 1.02, -1, 0)

    return data

# Momentum Strategy
def momentum(data, window=30):
    # Calculate the difference in price from 30 days ago
    momentum = data['Close'].diff(window)

    # Buy if the momentum is positive
    data['Buy_Signal'] = np.where(momentum > 0, 1, 0)

    # Sell if the momentum is negative
    data['Sell_Signal'] = np.where(momentum < 0, -1, 0)

    return data

# Testing the strategies
mean_reversion_data = mean_reversion(data.copy())
momentum_data = momentum(data.copy())

print(mean_reversion_data.head())
print(momentum_data.head())
```

This code assumes that you have a CSV file named 'stock_data.csv' with historical stock price data. The 'Close' column represents the closing price of the stock.

The Mean Reversion strategy assumes that the price will revert to the mean if it deviates too much. It buys when the price is 2% less than the 30-day mean and sells when the price is 2% more than the 30-day mean.

The Momentum strategy assumes that the price will continue in the same direction. It buys when the price is higher than 30 days ago and sells when the price is lower than 30 days ago.

Remember, these are very simplified strategies and should not be used for real trading without further enhancements.