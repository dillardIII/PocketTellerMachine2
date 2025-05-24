Sure, we can make a simple basic moving average crossover strategy using Python. This strategy will go long if the short-term moving average crosses above the long-term moving average, and short if the short-term moving average crosses below the long-term moving average.

We will use Python's `yfinance` package to fetch stock price data and `pandas` to calculate moving averages. If you currently don't have these in your Python environment, you may need to install this by running `pip install yfinance pandas` in your console.

Here is an example of a simple Moving Average Crossover strategy for a specific stock (In this example, let's assume Apple's stock (AAPL)):

```python
import yfinance as yf
import pandas as pd

# Fetch historical market data for 1 year 
data = yf.download('AAPL', '2020-01-01','2021-12-31')

# Calculate the short-term and long-term moving average
data['short_mavg'] = data['Close'].rolling(window=20).mean() # 20-days MA
data['long_mavg'] = data['Close'].rolling(window=50).mean() # 50-days MA

# Create signals
data['signal'] = 0.0  
data['signal'][20:] = np.where(data['short_mavg'][20:] 
                                    > data['long_mavg'][20:], 1.0, 0.0)

# Generate trading orders
data['positions'] = data['signal'].diff()

# Print the DataFrame
print(data)
```

The output DataFrame (data), has four new columns, short-term moving average (`short_mavg`), long-term moving average (`long_mavg`), a signal (`signal`) for when to make trades and the generated trading orders (`positions`). When the value in `positions` is 1.0, it means go long, -1.0 means go short, and 0 means hold whichever position you are currently in.

Please note that this is a basic trading strategy and in a real-world scenario you would need more sophisticated strategies including stop loss, take profit, position sizing, etc.

DISCLAIMER: This code is for illustration purposes only and does not guarantee any financial gains or results. Please use at your own risk and judgment. In real-life trading, various costs, complexity, and risks are involved which aren't covered by this example.