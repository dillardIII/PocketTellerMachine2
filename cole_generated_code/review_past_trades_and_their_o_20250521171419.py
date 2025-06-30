from ghost_env import INFURA_KEY, VAULT_ADDRESS
To complete the task, we need a dataset containing data about past trades. As the dataset is not specified here, we'll assume that we have a dataset with the fields: 'TradeID', 'Asset', 'BuyPrice', 'SellPrice', 'TradeDate'.

A simplified version of Python code could be written as this:

```python
import pandas as pd
from datetime import datetime

def calculate_profit(row):
    return (row['SellPrice'] - row['BuyPrice']) / row['BuyPrice']

# Load data from CSV file
df = pd.read_csv('past_trades.csv')

# Convert TradeDate to datetime
df['TradeDate'] = pd.to_datetime(df['TradeDate'])

# Sort by TradeDate
df = df.sort_values('TradeDate')

# Calculate profit for each trade
df['Profit'] = df.apply(calculate_profit, axis=1)

# Calculate average profit
average_profit = df['Profit'].mean()

# Lets create 2 new dataframes: wins (profitable trades) and losses (not profitable trades)
wins = df[df['Profit'] > 0]
losses = df[df['Profit'] <= 0]

# Calculate the win and loss percent over all trades
win_percent = (len(wins) / len(df)) * 100
loss_percent = (len(losses) / len(df)) * 100

print(f'Average profit: {average_profit * 100}%')
print(f'Win percent: {win_percent}%')
print(f'Loss percent: {loss_percent}%')
```

This is pretty basic and would need to be adapted to suit your specific needs. This sample code calculates profit of each trade, calculates the mean profit, determines the percentage of winning and losing trades. 

Please replace 'past_trades.csv' with the real CSV file path that represents historical trades.

Also, replace 'BuyPrice', 'SellPrice', 'Asset', 'TradeID' and 'TradeDate' with the real fields present in the dataset.

Remember to review and run this code in a safe and secure environment.