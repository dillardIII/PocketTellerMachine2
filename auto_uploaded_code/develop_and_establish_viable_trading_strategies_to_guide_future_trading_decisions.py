from ghost_env import INFURA_KEY, VAULT_ADDRESS
Creating a viable trading strategy involves using financial analysis techniques to analyze market behavior such as price directions and volume. Some of the most common strategies include technical analysis, quantitative trading, and algorithmic trading. Given that creating such a strategy requires domain knowledge and can be very complex, here's a simplified version using a moving average crossover strategy.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# fetch historical market data
data = yf.download('AAPL', start='2020-01-01', end='2021-12-31')

# create 30 days short term simple moving average
data['SMA_30'] = data['Close'].rolling(window=30).mean()

# create 100 days long term simple moving average
data['SMA_100'] = data['Close'].rolling(window=100).mean()

# create a function to signal when to buy and when to sell stock
def create_signal(data):
    buy_signal = []
    sell_signal = []
    flag = -1

    for i in range(len(data)):
        if data['SMA_30'][i] > data['SMA_100'][i]:
            if flag != 1:
                buy_signal.append(data['Close'][i])
                sell_signal.append(np.nan)
                flag = 1
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)
                
        elif data['SMA_30'][i] < data['SMA_100'][i]:
            if flag != 0:
                sell_signal.append(data['Close'][i])
                buy_signal.append(np.nan)
                flag = 0
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)
                
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)

    return buy_signal, sell_signal

# create buy and sell columns
data['Buy_Signal_Price'] = create_signal(data)[0]
data['Sell_Signal_Price'] = create_signal(data)[1]
```

This algorithm uses short-term and long-term moving averages to determine when to buy and sell a stock. When the short-term moving average crosses the long-term moving average upwards, it's a signal to buy. Conversely, when it crosses downwards, it's a signal to sell.

Please note that, this is a simple illustration and an actual trading strategy needs a lot more considerations like transaction cost, order execution price, market impact, risk control etc. along with rigorous back testing before it can be put to use.