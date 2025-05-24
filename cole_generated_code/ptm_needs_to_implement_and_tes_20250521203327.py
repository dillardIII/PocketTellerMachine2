Sure, here's a simple Python code that can be used to implement and test various trading strategies. For simplicity, let's assume we have two strategies: 'Buy and Hold' and 'Sell and Short'. We will use the pandas library to handle our data and the yfinance library to get the stock data.

```python
import pandas as pd
import yfinance as yf

# Define the trading strategies
def buy_and_hold(data):
    return data['Close'][-1] - data['Close'][0]

def sell_and_short(data):
    return data['Close'][0] - data['Close'][-1]

# Get the stock data
data = yf.download('AAPL', start='2020-01-01', end='2020-12-31')

# Test the strategies
strategies = {'Buy and Hold': buy_and_hold, 'Sell and Short': sell_and_short}
results = {}

for name, strategy in strategies.items():
    profit = strategy(data)
    results[name] = profit

# Print the results
for name, profit in results.items():
    print(f'Strategy: {name}, Profit: {profit}')
```

This code will print the profit for each strategy. The strategy with the highest profit is the most effective one.

Please note that this is a very simplified example. Real trading strategies would be much more complex and would take many more factors into account.