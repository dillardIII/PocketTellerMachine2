from ghost_env import INFURA_KEY, VAULT_ADDRESS
In order to develop and implement new trading strategies, we would need to have access to market data and a trading platform. However, I can provide you with a simple example of a Python code that implements a basic moving average crossover strategy using pandas library. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it means that recent prices are getting higher than older ones, which might be an indication of an uptrend, thus a buy signal is generated. Conversely, when the short moving average crosses below the long moving average, a sell signal is generated.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
data = yf.download('AAPL','2020-01-01','2022-12-31')

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create signals based on crossover
data['signal'] = 0.0
data['signal'][short_sma > long_sma] = 1.0
data['signal'][short_sma < long_sma] = -1.0

# Generate trading orders
data['position'] = data['signal'].diff()

# Print data
print(data)
```

Please note that this is a very basic trading strategy and in real-world trading, you would need to consider transaction costs, risk management, portfolio optimization and many other factors. Also, this strategy is based on historical data and past performance is not indicative of future results. 

You would also need to implement this strategy in a trading platform that allows automated trading, such as Interactive Brokers, Alpaca, Quantopian, etc. 

Lastly, this code assumes that you have the pandas and yfinance libraries installed. If not, you can install them using pip:

```bash
pip install pandas yfinance
```