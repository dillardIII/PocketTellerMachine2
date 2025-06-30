from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement trading strategies, we can use Python's libraries like pandas for data manipulation and analysis, numpy for numerical computation, matplotlib for data visualization, and yfinance to download historical market data from Yahoo finance. 

Here is a simple example of a trading strategy called "Moving Average Crossover Strategy". This strategy is one of the most commonly used strategies in the stock market. It involves two moving averages, one short-term (fast) and one long-term (slow). When the fast moving average crosses above the slow moving average, it's a signal to buy. When the fast moving average crosses below the slow moving average, it's a signal to sell.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for required stocks
data = yf.download('AAPL','2016-01-01','2021-12-31')

# Calculate the short-term simple moving average
short_sma= data.rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma= data.rolling(window=100).mean()

# Create a 'signal' (invested or not invested) data series
signal = [1 if short_sma[i] > long_sma[i] else 0 for i in range(len(long_sma))]

# Create a DataFrame
data = pd.DataFrame(data)
data['short_sma'] = short_sma
data['long_sma'] = long_sma
data['signal'] = signal

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(data['short_sma'], label='Short SMA', color='red')
plt.plot(data['long_sma'], label='Long SMA', color='blue')
plt.plot(data['signal'], label='Signal', color='green')
plt.legend(loc='upper left')
plt.show()
```

This is a simple trading strategy and may not be profitable in real trading. For real trading, you need to consider transaction costs, slippage, and market impact. Also, this strategy doesn't consider risk management. You should adjust the strategy according to your risk tolerance.

Please note that this is a basic example and real-world trading systems are much more complex and take into account many more factors.