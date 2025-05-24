Sure, here's a simple Python code that implements a basic momentum trading strategy using pandas library. This strategy buys a stock when its price has been going up for the past 'n' days and sells it when its price has been going down for the past 'n' days.

Please note that this is a simple strategy and may not always lead to wins. It's always recommended to use more sophisticated strategies and consider more factors for real trading.

```python
import pandas as pd
import yfinance as yf

def calculate_momentum(data, lookback_period):
    return data - data.shift(lookback_period)

def implement_strategy(data, lookback_period):
    # Calculate momentum
    data['Momentum'] = calculate_momentum(data['Close'], lookback_period)
    
    # Create signals
    data['Buy_Signal'] = (data['Momentum'] > 0)
    data['Sell_Signal'] = (data['Momentum'] < 0)
    
    return data

def test_strategy(data):
    # Assume we start with no stock and $1000 cash
    stock = 0
    cash = 1000
    
    for i in range(len(data)):
        # If we have a buy signal and we have cash, buy as much as we can
        if data['Buy_Signal'].iloc[i] and cash > 0:
            stock += cash / data['Close'].iloc[i]
            cash = 0
        # If we have a sell signal and we have stock, sell it all
        elif data['Sell_Signal'].iloc[i] and stock > 0:
            cash += stock * data['Close'].iloc[i]
            stock = 0
    
    # Calculate total value
    total_value = cash + stock * data['Close'].iloc[-1]
    
    return total_value

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Implement the strategy with a lookback period of 5 days
data = implement_strategy(data, 5)

# Test the strategy
final_value = test_strategy(data)
print(f'Final value after implementing the strategy: ${final_value:.2f}')
```

This code uses the yfinance library to download historical stock price data, so you need to install this library if you haven't done so (`pip install yfinance`). The code calculates the momentum of the stock price, generates buy/sell signals based on the momentum, and then tests the strategy by simulating buying and selling the stock according to these signals. The final value after implementing the strategy is printed at the end.