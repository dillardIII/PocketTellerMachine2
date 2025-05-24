While I can provide you with a starting point for creating a diversified trading strategy in Python, providing an all-encompassing code is not possible due to the complexity and risk associated with trading strategies. Depending on the type of strategies (like momentum, mean-reversion, statistical arbitrage, pairs trading, etc.) the codes can greatly differ. 

However, I can provide you with a rudimentary framework for a python script that calculates simple moving averages (SMA), which could be a very basic part of a trading strategy.

```python
import pandas as pd
import yfinance as yf

def calculate_sma(data, window):
    return data['Close'].rolling(window=window).mean()

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
data = pd.DataFrame(columns=tickers_list)

for ticker in tickers_list:
    data[ticker] = yf.download(ticker, period='1y')['Adj Close']

# Calculate simple moving averages
for ticker in tickers_list:
    # Here we use a 20 day moving average, but this can be adjusted
    data[f'{ticker}_SMA_20'] = calculate_sma(data, 20)

print(data)
```
In the above code, first we get the last 1 year's close price data from Yahoo Finance for a set of stocks (in the provided tickers_list). Then we add a new column for each ticker's 20-day SMA. You can choose different or additional indicators according to your trading strategy.

Please note this is a very basic starting point of a trading strategy. The full strategy could involve much more including but not limited to more indicators, backtesting, forward testing, risk management, portfolio balancing, transaction cost handling etc. 

Consultation with a financial advisor and/or doing substantial self-study about quantitative finance is recommended before creating any live trading strategies.