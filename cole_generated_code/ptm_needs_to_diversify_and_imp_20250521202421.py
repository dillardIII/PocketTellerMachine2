from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple example of how you could implement different trading strategies in Python. However, please note that this is a simplified example and real-world trading strategies would be much more complex and would require a deep understanding of financial markets.

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class TradingStrategy:
    def __init__(self, data):
        self.data = data

    def moving_average(self, window_size):
        """
        Simple Moving Average strategy
        """
        self.data['SMA'] = self.data['Close'].rolling(window=window_size).mean()
        return self.data

    def linear_regression(self, window_size):
        """
        Linear Regression strategy
        """
        lr = LinearRegression()
        for i in range(window_size, len(self.data)):
            X = np.array(range(window_size)).reshape(-1, 1)
            y = self.data['Close'].iloc[i-window_size:i].values
            lr.fit(X, y)
            self.data.loc[self.data.index[i], 'LR'] = lr.predict(np.array(window_size).reshape(-1, 1))
        return self.data

# Load your data
data = pd.read_csv('your_data.csv')

# Initialize the strategy
strategy = TradingStrategy(data)

# Apply Moving Average strategy
strategy.moving_average(window_size=20)

# Apply Linear Regression strategy
strategy.linear_regression(window_size=20)
```

In the above code, we have defined two trading strategies: Simple Moving Average (SMA) and Linear Regression. The SMA strategy calculates the average closing price over a specified number of days. The Linear Regression strategy fits a linear model to the closing prices over a specified number of days and uses this model to predict the next closing price.

Please replace 'your_data.csv' with your actual data file. The data file should be a CSV file with a 'Close' column that represents the closing prices.

Please note that this is a very basic implementation and in a real-world scenario, you would need to consider many other factors like transaction costs, slippage, risk management, etc. Also, you would need to backtest your strategies on historical data to evaluate their performance before live trading.