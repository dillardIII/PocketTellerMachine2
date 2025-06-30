from ghost_env import INFURA_KEY, VAULT_ADDRESS
Given the high-level nature of your request, below is a simple example of how to monitor trading opportunities using Python. This code isn't designed for live trading, but it should give you an idea of how it can be done.

This script will check if Company_X's moving average over the last 10 days is higher than the moving average over the past 50 days. If so, it might represent a buying opportunity. If the 10-day moving average is less than the 50-day average, it might represent a selling opportunity.

It uses the yfinance library to retrieve stock price data, and pandas to calculate the moving averages. You'll need to replace `Company_X` with the actual symbol of the stock you are interested in.

```python
import yfinance as yf
import pandas as pd

def calculate_moving_average(symbol, period):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1y") # get 1 year history
    return hist['Close'].rolling(window=period).mean()

def check_trading_opportunity(symbol):
    ma_10 = calculate_moving_average(symbol, 10)  #10 day moving average
    ma_50 = calculate_moving_average(symbol, 50)  #50 day moving average

    if ma_10[-1] > ma_50[-1]:  # compare the most recent day's averages
        print(f"Buying opportunity detected for {symbol}")
    elif ma_10[-1] < ma_50[-1]:
        print(f"Selling opportunity detected for {symbol}")

symbol = "Company_X"  
check_trading_opportunity(symbol)
```

Please remember, the strategy used here is a simplification and would not be suitable for actual trading. Professional algorithmic trading systems take into account many more factors, and use much more complex strategies.

CAUTION: Analyze your buy and sell scenarios carefully. Live and auto-trading requires sophisticated error-handling and continuous monitoring to prevent faulty software from causing financial loss.