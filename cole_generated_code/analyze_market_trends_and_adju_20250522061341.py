Analyzing market trends and adjusting trading strategies is a complex task that involves a lot of data analysis and potentially machine learning algorithms. Here is a basic example of how you might start to approach this task using Python, pandas for data manipulation, and yfinance to download stock price data.

```python
import pandas as pd
import yfinance as yf

def calculate_trends(data):
    # Calculate moving averages
    data['MA10'] = data['Close'].rolling(window=10).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()
    
    # Create a "signals" column
    data['Buy_Signal'] = (data['MA10'] > data['MA50'])
    data['Sell_Signal'] = (data['MA10'] < data['MA50'])
    
    return data

def adjust_strategy(data):
    buy_signals = data[data['Buy_Signal']]
    sell_signals = data[data['Sell_Signal']]
    
    # For simplicity, let's just say we'll buy/sell 1 share each time
    money = 0
    shares = 0
    
    for _, row in buy_signals.iterrows():
        shares += 1
        money -= row['Close']
    
    for _, row in sell_signals.iterrows():
        shares -= 1
        money += row['Close']
        
    return money, shares

# Download historical market data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Calculate trends
data = calculate_trends(data)

# Adjust strategy based on trends
money, shares = adjust_strategy(data)

print(f'Final money: ${money}, Final shares: {shares}')
```

This is a very basic strategy and doesn't take into account many factors that you would want to consider in a real trading strategy, such as transaction costs, the time value of money, risk, diversification, etc. For a more sophisticated analysis, you might want to look into machine learning or other predictive modeling techniques.