Sure, here's a simple example of how you might start to analyze past trades using Python. This example assumes you have a CSV file of past trades with columns for 'Date', 'Symbol', 'Buy/Sell', 'Quantity', and 'Price'. We'll use pandas for data manipulation and matplotlib for visualization.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the past trades data from a CSV file
trades = pd.read_csv('past_trades.csv')

# Convert the 'Date' column to datetime format
trades['Date'] = pd.to_datetime(trades['Date'])

# Sort the trades by date
trades = trades.sort_values('Date')

# Calculate the total value of each trade
trades['Value'] = trades['Quantity'] * trades['Price']

# Group by 'Date' and 'Buy/Sell' and calculate the sum of 'Value'
grouped = trades.groupby(['Date', 'Buy/Sell'])['Value'].sum().unstack()

# Plot the daily total value of buys and sells
grouped.plot(kind='line')
plt.title('Daily Total Value of Buys and Sells')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
```

This will give you a line chart showing the total value of buys and sells for each day. This is a very basic analysis and there are many other ways you could analyze the data depending on what you're interested in. For example, you could look at the most frequently traded symbols, the average trade size, the distribution of trades over time, etc.