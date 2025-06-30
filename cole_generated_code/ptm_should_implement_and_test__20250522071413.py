from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a Python script that uses a basic trading strategy. This strategy will buy when the 50-day moving average crosses above the 200-day moving average and sell when the 50-day moving average crosses below the 200-day moving average.

Please note that this is a very basic strategy and in real-world trading, you would need to consider many other factors such as transaction costs, slippage, risk management, etc. Also, you would need to use real-time data, which is not covered in this example.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
data = yf.download('AAPL', start='2020-01-01', end='2021-12-31')

# Calculate 50-day Simple Moving Average
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Calculate 200-day Simple Moving Average
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# Create a column to hold the buy (1) and sell (-1) signals
data['Signal'] = 0.0  
data['Signal'][50:] = np.where(data['SMA_50'][50:] > data['SMA_200'][50:], 1.0, 0.0)

# Generate trading orders
data['Position'] = data['Signal'].diff()

# Print the DataFrame
print(data)

# The result DataFrame will have -1.0 for selling points and 1.0 for buying points
```

This code uses the `yfinance` package to download historical data for a specific ticker symbol. It then calculates the 50-day and 200-day simple moving averages and generates trading signals based on these. The `Position` column in the resulting DataFrame indicates the trading orders: -1.0 for selling and 1.0 for buying.

Please note that you will need to install the `yfinance` package if you haven't already done so. You can install it using pip:

```bash
pip install yfinance
```

This is a simple moving average crossover strategy. There are many other trading strategies that you could implement depending on your trading goals and risk tolerance.