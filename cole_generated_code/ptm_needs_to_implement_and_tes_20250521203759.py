from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code to implement and test two different trading strategies. The strategies are Moving Average Crossover and Buy and Hold. We will use the `yfinance` library to download stock data and `pandas` to manipulate the data.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol 
data = yf.download('AAPL','2019-01-01','2020-12-31')

# Calculate the short-term simple moving average
data['Short_SMA'] = data['Close'].rolling(window=20).mean()

# Calculate the long-term simple moving average
data['Long_SMA'] = data['Close'].rolling(window=100).mean()

# Create a column 'Signal' such that if the short-term SMA is greater than the long-term SMA then set Signal as 1 else 0
data['Signal'] = 0.0  
data['Signal'][data['Short_SMA'] > data['Long_SMA']] = 1.0

# Create a column 'Position' which is the difference of the present and previous day's 'Signal'
data['Position'] = data['Signal'].diff()

# Plotting
plt.figure(figsize=(20,10))
# plot close price, short-term and long-term moving averages 
data['Close'].plot(color = 'b', label= 'Close Price') 
data['Short_SMA'].plot(color = 'r',label = 'Short-term SMA') 
data['Long_SMA'].plot(color = 'g', label = 'Long-term SMA') 

# plot 'buy' signals
plt.plot(data[data['Position'] == 1].index, 
         data['Short_SMA'][data['Position'] == 1], 
         '^' , markersize=15, color='g', label = 'buy')

# plot 'sell' signals
plt.plot(data[data['Position'] == -1].index, 
         data['Short_SMA'][data['Position'] == -1], 
         'v' , markersize=15, color='r', label = 'sell')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.title('Apple Inc. - Moving Average Crossover')
plt.legend()
plt.grid()
plt.show()

# Buy and Hold strategy
initial_investment = 10000
shares = initial_investment/data['Close'][0]
portfolio_value = shares*data['Close'][-1]
print(f"Value of portfolio using Buy and Hold strategy: {portfolio_value}")
```

This code will plot the moving averages and trading signals for the Moving Average Crossover strategy and calculate the final portfolio value for the Buy and Hold strategy. Note that this is a very basic implementation and real trading strategies would be much more complex and take into account many other factors. 

Also, please install the required libraries using pip if they are not installed.

```shell
pip install yfinance pandas matplotlib
```