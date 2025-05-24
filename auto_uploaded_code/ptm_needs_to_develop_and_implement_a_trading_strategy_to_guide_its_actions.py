Sure, I can provide a basic example of a Python code for a simple trading strategy using Moving Average Crossover. This strategy is one of the most commonly used by traders. It involves two moving averages, one short-term (fast) and one long-term (slow). A buy signal is generated when the fast moving average crosses above the slow one, and a sell signal is generated when the fast moving average crosses below the slow one.

Please note that this is a simplified example and real trading strategies should consider more factors and be tested thoroughly before live trading.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker
ticker = "AAPL"
ticker_data = yf.download(ticker, start="2020-01-01", end="2021-12-31")

# Calculate moving averages
short_ma = ticker_data['Close'].rolling(window=20).mean()
long_ma = ticker_data['Close'].rolling(window=50).mean()

# Create signals
signals = pd.DataFrame(index=ticker_data.index)
signals['signal'] = 0.0
signals['short_ma'] = short_ma
signals['long_ma'] = long_ma

# Generate trading signals (1 for buy, -1 for sell)
signals['signal'][short_ma > long_ma] = 1.0
signals['signal'][short_ma < long_ma] = -1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

print(signals)
```

This code first downloads historical data for the desired ticker symbol using the yfinance library. Then it calculates the short-term and long-term moving averages of the closing prices. It generates trading signals based on the relationship between the two moving averages. A buy signal is generated when the short-term moving average is greater than the long-term moving average, and a sell signal is generated when the short-term moving average is less than the long-term moving average. Finally, it generates trading orders based on the changes in trading signals.

Please note that you will need to install the yfinance library if you haven't done so already. You can do this by running `pip install yfinance` in your command line.