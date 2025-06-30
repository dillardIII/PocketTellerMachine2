from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help you write a simple Python code for a trading strategy. However, please note that this is a very basic example and real-world trading strategies are much more complex and require thorough backtesting and risk management.

We'll use the Moving Average Crossover strategy which is a popular strategy used in algorithmic trading. This strategy is based on two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. Conversely, when the short moving average crosses below the long moving average, it's a signal to sell.

Here is the Python code using pandas library:

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
data = yf.download('AAPL','2020-01-01','2021-12-31')

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create signals based on crossover
data['Buy_Signal'] = (short_sma > long_sma)

# Print data
print(data)
```

This code will print a dataframe where 'Buy_Signal' column is True if the short moving average is greater than the long moving average (indicating a buy signal) and False otherwise.

Please note that you need to install yfinance and pandas library to run this code. You can install it using pip:

```bash
pip install yfinance pandas
```

Also, this is a very basic strategy and doesn't take into account transaction costs, slippage, risk management, etc. Always do thorough backtesting before using any trading strategy.