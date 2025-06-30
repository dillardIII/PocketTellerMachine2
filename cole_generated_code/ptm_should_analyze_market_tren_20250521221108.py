from ghost_env import INFURA_KEY, VAULT_ADDRESS
To complete this task, we would need to use a library like pandas for data analysis and manipulation, and yfinance to download historical market data from Yahoo finance. We might also use matplotlib for data visualization.

Here's a simple example of how we might start:

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2022-12-31')

# Calculate moving averages
data['MA10'] = data['Close'].rolling(10).mean()
data['MA50'] = data['Close'].rolling(50).mean()

# Create a function to signal when to buy and sell an asset
def create_signals(data):
    buy_signal = []
    sell_signal = []
    
    for i in range(len(data)):
        if data['MA10'][i] > data['MA50'][i]:
            if len(buy_signal) > 0:
                if sell_signal[-1] > buy_signal[-1]:
                    buy_signal.append(data['Close'][i])
                    sell_signal.append(np.nan)
                else:
                    buy_signal.append(np.nan)
                    sell_signal.append(np.nan)
            else:
                buy_signal.append(data['Close'][i])
                sell_signal.append(np.nan)
        elif data['MA10'][i] < data['MA50'][i]:
            if len(sell_signal) > 0:
                if buy_signal[-1] > sell_signal[-1]:
                    sell_signal.append(data['Close'][i])
                    buy_signal.append(np.nan)
                else:
                    buy_signal.append(np.nan)
                    sell_signal.append(np.nan)
            else:
                sell_signal.append(data['Close'][i])
                buy_signal.append(np.nan)
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)
            
    return (buy_signal, sell_signal)

# Create buy and sell column
data['Buy_Signal_Price'] = create_signals(data)[0]
data['Sell_Signal_Price'] = create_signals(data)[1]

# Plot data and signals
plt.figure(figsize=(12.5, 4.5))
plt.plot(data['Close'], label='Close Price', alpha=0.35)
plt.plot(data['MA10'], label='MA10', alpha=0.35)
plt.plot(data['MA50'], label='MA50', alpha=0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Signal_Price'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Stock Buy & Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend(loc='upper left')
plt.show()
```

This script will download the historical data for the Apple stock, calculate the moving averages for the last 10 and 50 days, and generate buy and sell signals based on these moving averages. It will then plot the closing price, moving averages and signals on a graph.

Please note that this is a very basic example of a trading strategy and should not be used for actual trading without further improvements and testing.