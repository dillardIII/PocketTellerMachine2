Sure, I can provide you with a basic example of a trading strategy using Python. In this example, we will use a simple moving average crossover strategy. This strategy is a basic one where we buy when the short-term moving average crosses above the long-term moving average and sell when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic strategy and in real trading scenarios, you would need to consider transaction costs, risk management, and other factors. Also, this code assumes that you have pandas and yfinance (a library to download stock data from Yahoo Finance) installed.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol 
data = yf.download('AAPL','2020-01-01','2021-12-31')

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create a 'signal' (invested or not invested) when short is greater than long
data['signal'] = 0.0  
data['signal'][short_sma > long_sma] = 1.0

# Generate trading orders
data['positions'] = data['signal'].diff()

# Print data
print(data)
```

In this code, we first download the historical data for the desired ticker symbol. Then we calculate the short-term and long-term simple moving averages. We then create a 'signal' which is 1.0 when the short-term average is greater than the long-term average and 0.0 otherwise. Finally, we generate trading orders by taking the difference of the 'signal' column.

This is a very basic strategy and there are many other strategies that you can implement to diversify risk. Also, this code does not take into account transaction costs, risk management, or other factors that would be important in a real trading scenario.