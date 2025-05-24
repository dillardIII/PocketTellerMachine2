Sure, I can provide a simple example of a trading strategy using Python. This strategy will be based on a simple moving average (SMA) crossover, which is a common trading strategy. 

This strategy will buy when the short-term SMA crosses above the long-term SMA, and sell when the short-term SMA crosses below the long-term SMA. 

Please note that this is a simplified example and real-world trading strategies can be much more complex and take into account many other factors.

```python
import pandas as pd
import yfinance as yf
from datetime import datetime

# Download historical data for desired ticker symbol
ticker = "AAPL"
ticker_data = yf.download(ticker, start="2020-01-01", end=datetime.today().strftime('%Y-%m-%d'))

# Calculate short-term simple moving average (SMA)
short_sma = ticker_data['Close'].rolling(window=20).mean()

# Calculate long-term SMA
long_sma = ticker_data['Close'].rolling(window=100).mean()

# Create a column in the data frame to hold the trading signals
ticker_data['signal'] = 0.0

# Generate trading signals based on SMA crossover
ticker_data['signal'][20:] = np.where(short_sma[20:] > long_sma[20:], 1.0, 0.0)

# Generate trading orders based on the trading signals
ticker_data['positions'] = ticker_data['signal'].diff()

# Print the DataFrame
print(ticker_data)
```

In this code:

- We first download historical data for the desired ticker symbol using the yfinance library.
- We then calculate the short-term and long-term SMAs of the closing prices.
- We create a new column in the DataFrame to hold the trading signals, which are generated based on the SMA crossover.
- We generate trading orders based on the change in trading signals. A positive change (from 0 to 1) indicates a buy order, and a negative change (from 1 to 0) indicates a sell order.

Please note that this is a simplified example and real-world trading strategies can be much more complex and take into account many other factors. Also, this code does not include any risk management or portfolio optimization strategies.