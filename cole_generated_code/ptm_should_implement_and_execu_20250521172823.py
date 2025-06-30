from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I'll outline a basic version of a pair trading strategy implemented in Python. This strategy involves finding two stocks that move together and trading on the rare occasions when they diverge. It's an example of statistical arbitrage.

Assumptions:
1. You have yfinance library installed. You can use pip install yfinance command to install.
2. The historical data for the trading pairs are available on Yahoo Finance.

```python
import yfinance as yf
from statsmodels.tsa.stattools import coint
import matplotlib.pyplot as plt
import numpy as np

# define the pairs of stocks
stock_1 = 'AAPL'
stock_2 = 'MSFT'

# get historical data for a specific period
start_date= '2020-01-01'
end_date = '2021-12-31'
stock1_data = yf.download(stock_1, start_date, end_date)
stock2_data = yf.download(stock_2, start_date, end_date)

# calculate p-value 
_, pvalue, _= coint(stock1_data['Close'], stock2_data['Close'])
if pvalue < 0.05:
    print('The pair ' + stock_1 + ' and ' + stock_2 + ' is cointegrated')
else:
    print('The pair ' + stock_1 + ' and ' + stock_2 + ' is not cointegrated')

# calculate the spread
spread = stock1_data['Close'] - stock2_data['Close']
spread.plot()
plt.axhline(spread.mean(), color='red', linestyle='--') 
plt.xlabel('Time')
plt.legend(['Spread'])
plt.show()

# define the trading strategy
entry_z = 1 
exit_z = 0 

longs = spread < -entry_z
shorts = spread > entry_z
exits = np.abs(spread) < exit_z

positions = np.array([0]* spread.count())
positions[longs[longs].index] = 1
positions[shorts[shorts].index] = -1
positions[exits[exits].index] = 0

# calculate and plot cumulative returns
returns = positions[:-1]*spread.diff()[1:]
returns = returns[returns != 0]
cumulative_returns = returns.cumsum()
cumulative_returns.plot()
plt.xlabel('Time')
plt.legend(['Cumulative returns'])
plt.show()
```

Note: Please be aware that pair trading strategy is one type of statistical arbitrage with its own pros and cons. It mainly relies on the assumption that the price spread of two co-integrated securities is mean reverting. However, this might not always be the case which can result in losses. Therefore, any kind of trading involving monetary risks should be done with caution. It is also advised to do a thorough backtesting before implementing the strategy.