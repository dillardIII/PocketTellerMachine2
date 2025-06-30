from ghost_env import INFURA_KEY, VAULT_ADDRESS
Developing and implementing varied strategies require a lot of understanding of the market and various other factors. However, I can show you a very basic idea of how one could isolate various strategies in Python code.

Two simple strategies could be:
1. Moving average strategy: This is a very common investment strategy for trading, involving two averages, if short time average cross long time average from below, it is a buy signal and reverse is a sell signal.
2. Buy and hold strategy: This is a passive investment strategy where you invest in a diverse portfolio and hold onto these investments over a long duration.

In Python, we can use a dedicated library for finance called 'pandas_datareader' which allows us to get stock market data straight into our python environment for our manipulation.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web

# Setting the stock we are interested in
stock = 'AAPL'

# Setting start and end dates for stock data
start_date = '01-01-2010'
end_date = '01-01-2021'

# Importing the stock data
data = web.DataReader(stock, 'yahoo', start_date, end_date)

# Moving Average Strategy
data['short_average'] = data['Close'].rolling(window=20).mean()
data['long_average'] = data['Close'].rolling(window=100).mean()

data[['Close','short_average','long_average']].plot(figsize=(10,5))
plt.grid(True)
plt.title(stock + ' Moving Averages')
plt.axis('tight')
plt.ylabel('Price')

#Buy And Hold Strategy
initial_investment = 10000
shares = initial_investment/data['Close'][0]
hold_portfolio_value = shares * data['Close']

hold_portfolio_value.plot(label='Buy and Hold Strategy', figsize=(10,5))
plt.title(stock + ' Buy and Hold Strategy')
plt.grid(True)
plt.ylabel('Portfolio Value')
plt.legend()

plt.show()
```

This code shows simple implementation is quite simple. Always look for other strategies based on your risk level and various other parameters in actual trading.