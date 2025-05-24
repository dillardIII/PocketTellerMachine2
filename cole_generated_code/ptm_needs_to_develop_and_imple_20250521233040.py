Sure, I can provide a simple example of a pair trading strategy using Python. This strategy involves finding two stocks that move together and trading them when they diverge abnormally.

Please note that this is a simplified example and real-world trading strategies are much more complex and involve many other factors.

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from yfinance import download

# Download historical data for desired time period
data = download(['AAPL', 'MSFT'], '2019-01-01', '2020-12-31')

# Use only close prices
prices = data['Close']

# Calculate the spread between the two stocks
spread = prices['AAPL'] - prices['MSFT']

# Calculate the z-score of the spread
zscore = (spread - spread.mean()) / spread.std()

# Create a trading signal based on the z-score
signal = np.where(zscore > 1, -1, np.where(zscore < -1, 1, 0))

# Calculate daily returns of the strategy
returns = signal * spread.pct_change()

# Calculate cumulative returns
cumulative_returns = (1 + returns).cumprod()

# Print the cumulative returns
print(cumulative_returns)
```

This script downloads historical data for Apple and Microsoft, calculates the spread between their prices, and generates trading signals based on the z-score of the spread. When the z-score is greater than 1, it means that the spread is too high and we should short the spread. When the z-score is less than -1, it means that the spread is too low and we should long the spread. The script then calculates the daily and cumulative returns of this strategy.

Please note that you need to install the yfinance package to download historical data from Yahoo Finance. You can install it using pip:

```bash
pip install yfinance
```

Also, this is a very simplified trading strategy for educational purposes only. Real-world trading strategies involve much more factors and are much more complex.