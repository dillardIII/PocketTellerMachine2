from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a trading strategy in Python using the Moving Average Crossover strategy. This strategy is one of the most commonly used strategies in the trading world. It's based on the principle that the price of an asset will revert to its mean price over time.

In this strategy, we will use two moving averages: one short term (10 days) and one long term (50 days). When the short term moving average crosses above the long term moving average, it signals a potential upward price trend and we buy the asset. When the short term moving average crosses below the long term moving average, it signals a potential downward price trend and we sell the asset.

Please note that this is a very basic strategy and doesn't take into account many factors that could influence the success of the trades. It's always recommended to use more sophisticated strategies and to backtest them with historical data.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = "AAPL"
ticker_data = yf.download(ticker, start="2020-01-01", end="2022-12-31")

# Calculate short term and long term moving averages
ticker_data['Short_Term_MA'] = ticker_data['Close'].rolling(window=10).mean()
ticker_data['Long_Term_MA'] = ticker_data['Close'].rolling(window=50).mean()

# Create a column for the trading signals
ticker_data['Buy_Signal'] = (ticker_data['Short_Term_MA'] > ticker_data['Long_Term_MA']).astype(int)

# Shift the signals column down by one to avoid forward-looking bias
ticker_data['Buy_Signal'] = ticker_data['Buy_Signal'].shift()

# Drop the rows with missing values
ticker_data = ticker_data.dropna()

# Print the DataFrame
print(ticker_data)
```

This script will print a DataFrame with the closing prices, the short term and long term moving averages, and the buy signals for the specified ticker symbol. The buy signals are 1 when the short term moving average is above the long term moving average, indicating a potential buy, and 0 otherwise.