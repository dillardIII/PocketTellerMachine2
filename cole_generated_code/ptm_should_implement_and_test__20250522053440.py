Sure, here's a simple Python code that implements a basic moving average crossover strategy using pandas. Please note that this is a very basic strategy and might not generate profits in real trading. You should always backtest and refine your strategies before using them in live trading.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
data = yf.download('AAPL','2020-01-01','2021-12-31')

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create a 'signal' (invested or not invested) when short MA crosses long MA
signal = [1 if short_sma[i] > long_sma[i] else 0 for i in range(len(short_sma))]

# Calculate daily returns
data['return'] = data['Close'].pct_change()

# Calculate strategy returns
data['strategy_return'] = data['return'] * signal

# Calculate cumulative returns
data['cumulative_market_returns'] = np.cumprod(1 + data['return']) - 1
data['cumulative_strategy_returns'] = np.cumprod(1 + data['strategy_return']) - 1

# Print the DataFrame
print(data)
```

This code uses the yfinance library to download historical data for the desired ticker symbol. It then calculates short-term and long-term simple moving averages and generates a trading signal based on the crossover of these averages. It also calculates the daily and cumulative returns for both the market and the strategy. Finally, it prints the DataFrame with all this information.

Please note that you need to have the yfinance library installed in your Python environment. You can install it using pip:

```bash
pip install yfinance
```

Also, this is a very basic strategy and might not generate profits in real trading. You should always backtest and refine your strategies before using them in live trading.