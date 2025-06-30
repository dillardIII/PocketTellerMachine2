from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example where we'll implement and test two basic trading strategies: Moving Average Crossover and Mean Reversion. We'll use the `yfinance` library to get historical stock data and `pandas` for data manipulation.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol 
data = yf.download('AAPL','2020-01-01','2021-12-31')

# Calculate moving averages
data['MA10'] = data['Close'].rolling(10).mean()
data['MA50'] = data['Close'].rolling(50).mean()

# Create a 'signals' column
data['Buy_Signal'] = (data['MA10'] > data['MA50'])

# Calculate daily returns
data['Return'] = data['Close'].pct_change()

# Create a 'strategy' column
data['Strategy_Return'] = data['Buy_Signal'].shift() * data['Return']

# Calculate cumulative returns
data['Buy_and_Hold'] = (1 + data['Return']).cumprod()
data['Strategy'] = (1 + data['Strategy_Return']).cumprod()

# Plot the strategies
data[['Buy_and_Hold', 'Strategy']].dropna().plot()

# Mean Reversion Strategy
data['Rolling_Mean'] = data['Close'].rolling(window=20).mean()
data['Rolling_STD'] = data['Close'].rolling(window=20).std()
data['Bollinger_High'] = data['Rolling_Mean'] + (data['Rolling_STD'] * 1)
data['Bollinger_Low'] = data['Rolling_Mean'] - (data['Rolling_STD'] * 1)

# Create signals
data['Sell_Signal'] = data['Close'] > data['Bollinger_High'] 
data['Buy_Signal'] = data['Close'] < data['Bollinger_Low'] 

# Calculate daily strategy returns
data['Daily_Return'] = data['Return'] * data['Buy_Signal'].shift() - data['Return'] * data['Sell_Signal'].shift()

# Calculate cumulative strategy returns
data['Cumulative_Strategy_Returns'] = (1 + data['Daily_Return']).cumprod()

# Plot the strategy returns
data['Cumulative_Strategy_Returns'].plot()
plt.show()
```

Please note that this is a very simplified example. Real-world trading strategies are much more complex and take into account many more factors. Also, past performance is not indicative of future results.