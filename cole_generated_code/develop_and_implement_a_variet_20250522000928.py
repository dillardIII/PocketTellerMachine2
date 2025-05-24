Sure, here is a simple example of how you might implement a few different trading strategies in Python. Note that this is a very basic example and real trading strategies would be much more complex and take into account a lot more factors.

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load historical data
data = pd.read_csv('historical_data.csv')

# Define strategies
def buy_and_hold(data):
    return data['Close'].iloc[-1] - data['Close'].iloc[0]

def mean_reversion(data):
    mean = data['Close'].mean()
    return (data['Close'].iloc[-1] - mean) * -1

def momentum(data):
    lr = LinearRegression()
    x = np.array(range(len(data))).reshape(-1, 1)
    y = data['Close'].values
    lr.fit(x, y)
    return lr.coef_[0]

# Implement strategies
strategies = [buy_and_hold, mean_reversion, momentum]
results = {}

for strategy in strategies:
    result = strategy(data)
    results[strategy.__name__] = result

print(results)
```

In this code, we define three simple trading strategies:

1. Buy and Hold: This strategy involves buying a stock and holding onto it. The profit or loss is simply the difference between the closing price on the last day and the closing price on the first day.

2. Mean Reversion: This strategy assumes that the price of a stock will revert to its mean over time. The profit or loss is the difference between the closing price on the last day and the mean price.

3. Momentum: This strategy assumes that the price of a stock will continue in its current direction. We fit a linear regression model to the closing prices and use the slope of the line as our profit or loss.

We then implement each of these strategies on our data and store the results in a dictionary.