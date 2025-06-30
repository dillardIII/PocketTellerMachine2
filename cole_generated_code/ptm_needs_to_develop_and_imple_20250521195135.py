from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple example of a pair trading strategy using Python. This strategy involves finding two stocks that move together and trading them when they diverge.

Here's a simple implementation:

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from yfinance import download

# Download historical data for required stocks
data = download("AAPL MSFT", start="2020-01-01", end="2021-12-31")

def generate_signals(data):
    # Using linear regression to establish the relationship between the two stocks
    model = LinearRegression().fit(data['AAPL'].values.reshape(-1,1), data['MSFT'])
    data['spread'] = data['MSFT'] - model.predict(data['AAPL'].values.reshape(-1,1))

    # Creating signals
    data['z_score'] = (data['spread'] - data['spread'].mean()) / np.std(data['spread'])
    data['signals'] = 0
    data.loc[data['z_score'] > 1, 'signals'] = -1
    data.loc[data['z_score'] < -1, 'signals'] = 1

    return data

def execute_trades(data):
    # Calculate daily returns
    data['daily_returns'] = data['MSFT'].pct_change()

    # Calculate strategy returns
    data['strategy_returns'] = data['signals'].shift() * data['daily_returns']

    # Calculate cumulative returns
    data['cumulative_returns'] = (1 + data['strategy_returns']).cumprod()

    return data

data = generate_signals(data)
data = execute_trades(data)

print(data)
```

Please note that this is a very simplified example and real trading strategies should consider transaction costs, risk management, etc. Also, this code assumes that you have the `yfinance`, `numpy`, `pandas`, and `sklearn` packages installed in your Python environment. If not, you can install them using pip:

```bash
pip install yfinance numpy pandas scikit-learn
```

This code also uses Yahoo Finance to download the historical data, so make sure you have internet access.