from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a basic Python code that implements a simple moving average crossover strategy. This strategy is one of the most common systematic trading strategies. It uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it generates a buy signal. When the short moving average crosses below the long moving average, it generates a sell signal.

Please note that this is a very basic trading strategy and in real-world trading, you would need to consider many other factors such as transaction costs, risk management, portfolio optimization, etc.

```python
# Import necessary libraries
import pandas as pd
import yfinance as yf
from datetime import datetime

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data for this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end=datetime.today().strftime('%Y-%m-%d'))

# Calculate the short moving average
short_window = 20
signals = pd.DataFrame(index=tickerDf.index)
signals['signal'] = 0.0
signals['short_mavg'] = tickerDf['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Calculate the long moving average
long_window = 100
signals['long_mavg'] = tickerDf['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print the DataFrame
print(signals)
```

This code will print a DataFrame that includes the short moving average, the long moving average, the signals (1.0 for "buy" and 0.0 for "hold"), and the positions (1.0 for "buy" and -1.0 for "sell").

Please replace 'AAPL' with the actual ticker symbol of the stock you want to analyze. Also, you may need to adjust the short_window and long_window parameters according to your trading strategy.