Sure, I can provide a simple example of a trading strategy using Python. This strategy will be based on moving averages, which is a common trading strategy. We will use the pandas library to handle our data and calculate the moving averages.

Please note that this is a very basic strategy and real-world trading involves much more complexity and risk.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2021-12-31')

# Calculate short-term and long-term moving averages
short_term_avg = data['Close'].rolling(window=20).mean()
long_term_avg = data['Close'].rolling(window=100).mean()

# Create signals
data['Buy_Signal'] = (short_term_avg > long_term_avg)
data['Sell_Signal'] = (short_term_avg < long_term_avg)

# Print data
print(data)

# Implement the trading strategy
def implement_strategy(data):
    cash = 10000  # Initial investment
    stock = 0
    for i in range(len(data)):
        # Buy if there is a buy signal and we have cash
        if data['Buy_Signal'].iloc[i] and cash > 0:
            stock = cash / data['Close'].iloc[i]
            cash = 0
        # Sell if there is a sell signal and we have stock
        elif data['Sell_Signal'].iloc[i] and stock > 0:
            cash = stock * data['Close'].iloc[i]
            stock = 0
    return cash

# Calculate final portfolio value
final_portfolio_value = implement_strategy(data)
print('Final portfolio value: ', final_portfolio_value)
```

This code first downloads historical data for a specific ticker symbol. Then it calculates short-term and long-term moving averages of the closing prices. A buy signal is generated when the short-term average is higher than the long-term average, and a sell signal is generated when the short-term average is lower than the long-term average. The trading strategy is then implemented: we start with a certain amount of cash, buy when there is a buy signal and we have cash, and sell when there is a sell signal and we have stock. The final portfolio value is then calculated.

Please note that this is a very basic trading strategy and does not take into account transaction costs, slippage, risk management, etc. It's important to thoroughly backtest any trading strategy before live trading.