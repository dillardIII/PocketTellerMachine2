from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple implementation of a moving average crossover strategy using Python and the pandas library. This strategy buys when the short term moving average crosses above the long term moving average and sells when the short term moving average crosses below the long term moving average.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = "AAPL"
data = yf.download(ticker, start="2020-01-01", end="2021-12-31")

# Calculate short term and long term moving averages
short_term = 50
long_term = 200
data['Short_Term_MA'] = data['Close'].rolling(window=short_term).mean()
data['Long_Term_MA'] = data['Close'].rolling(window=long_term).mean()

# Create a 'Signal' column where 1 indicates a buy signal and -1 indicates a sell signal
data['Signal'] = 0
data.loc[data['Short_Term_MA'] > data['Long_Term_MA'], 'Signal'] = 1
data.loc[data['Short_Term_MA'] < data['Long_Term_MA'], 'Signal'] = -1

# Calculate daily returns
data['Return'] = data['Close'].pct_change()

# Calculate strategy returns
data['Strategy_Return'] = data['Return'] * data['Signal'].shift()

# Calculate cumulative returns
data['Cumulative_Market_Returns'] = (data['Return']+1).cumprod()-1
data['Cumulative_Strategy_Returns'] = (data['Strategy_Return']+1).cumprod()-1

# Print the last few rows of the data
print(data.tail())

# Plot cumulative returns
data[['Cumulative_Market_Returns', 'Cumulative_Strategy_Returns']].plot()
```

Please note that this is a very basic trading strategy and is not guaranteed to generate profits. It is always recommended to thoroughly backtest any trading strategy before live trading. Also, this strategy does not take into account trading fees or slippage.