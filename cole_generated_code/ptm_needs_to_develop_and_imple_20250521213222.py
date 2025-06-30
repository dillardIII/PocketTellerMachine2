from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a basic structure for a simple trading strategy using Python. However, please note that this is a simplified example and real trading strategies involve complex algorithms, risk management, and are based on extensive financial knowledge.

We will use pandas for data manipulation and matplotlib for data visualization. We will also use yfinance to download the historical stock data from Yahoo finance.

```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data as dataframe
data = yf.download('AAPL', start='2020-01-01', end='2021-12-31')

# Calculate the short term exponential moving average (EMA)
ShortEMA = data.Close.ewm(span=12, adjust=False).mean() 

# Calculate the long term exponential moving average (EMA)
LongEMA = data.Close.ewm(span=26, adjust=False).mean() 

# Calculate the Moving Average Convergence/Divergence (MACD)
MACD = ShortEMA - LongEMA

# Calculate the signal line
signal = MACD.ewm(span=9, adjust=False).mean()

# Create a new column in the dataframe to hold the trading strategy signals
data['Buy_Signal_Price'] = 0
data['Sell_Signal_Price'] = 0

# When MACD crosses above the signal line, we will buy the stock
# When MACD crosses below the signal line, we will sell the stock
for i in range(1, len(data)):
    if MACD[i] > signal[i]:
        if MACD[i - 1] < signal[i - 1]:
            data['Buy_Signal_Price'][i] = data['Close'][i]
    elif MACD[i] < signal[i]:
        if MACD[i - 1] > signal[i - 1]:
            data['Sell_Signal_Price'][i] = data['Close'][i]

# Plot the stock price, along with the buy and sell signals
plt.figure(figsize=(12,5))
plt.scatter(data.index, data['Buy_Signal_Price'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Signal_Price'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.35)
plt.title('Close Price Buy & Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()
```

This is a simple trading strategy based on MACD. When the MACD line crosses above the signal line, it's a buy signal and when it crosses below, it's a sell signal. This strategy is called a crossover strategy.

Please note that this is a very basic strategy and in real trading scenarios, strategies can be much more complex and involve multiple indicators and risk management techniques. Also, past performance is not indicative of future results.