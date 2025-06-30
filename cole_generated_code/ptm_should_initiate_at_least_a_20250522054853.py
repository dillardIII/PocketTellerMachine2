from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a basic example of how you might set up a Python script to initiate trades and evaluate the effectiveness of your current strategies. This example uses the `yfinance` library to get stock data, and `pandas` for data manipulation.

Please note that this is a simplified example and real trading involves more complexities. This script also assumes that you have a function `evaluate_strategy()` that takes a DataFrame of trades and returns some evaluation of the strategy's effectiveness.

```python
import yfinance as yf
import pandas as pd

# Define the stocks we're interested in
stocks = ['AAPL', 'MSFT', 'GOOGL']

# Define the DataFrame to store our trades
trades = pd.DataFrame(columns=['stock', 'buy_price', 'sell_price', 'profit'])

# Loop over each stock
for stock in stocks:
    # Get the stock data
    data = yf.download(stock, start='2021-01-01', end='2021-12-31')
    
    # Assume we have a function `should_buy()` that tells us when to buy based on the data
    if should_buy(data):
        # Buy the stock at the current price
        buy_price = data['Close'][-1]
        
        # Assume we have a function `should_sell()` that tells us when to sell based on the data
        if should_sell(data):
            # Sell the stock at the current price
            sell_price = data['Close'][-1]
            
            # Calculate the profit
            profit = sell_price - buy_price
            
            # Record the trade
            trades = trades.append({'stock': stock, 'buy_price': buy_price, 'sell_price': sell_price, 'profit': profit}, ignore_index=True)

# Evaluate the effectiveness of the strategy
effectiveness = evaluate_strategy(trades)

print(f'The effectiveness of the current strategy is: {effectiveness}')
```

Please replace `should_buy()`, `should_sell()`, and `evaluate_strategy()` with your actual trading strategy and evaluation functions.