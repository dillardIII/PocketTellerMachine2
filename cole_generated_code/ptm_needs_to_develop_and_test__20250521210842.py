from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and test new trading strategies, we need to use a backtesting framework. Here's a simple example using the `bt` library in Python. This library allows us to create and test strategies in a simple and straightforward way.

First, we need to install the `bt` library. You can do this by running the command `pip install bt`.

Here's an example of a simple moving average crossover strategy:

```python
import bt
import pandas as pd

# Fetch some data
data = bt.get('spy,agg', start='2010-01-01')

# Create strategy
sma = data.rolling(50).mean()
cross = bt.Strategy('cross', 
                    [bt.algos.SelectWhere(data > sma),
                     bt.algos.WeighEqually(),
                     bt.algos.Rebalance()])

# Create backtest and run
t = bt.Backtest(cross, data)
res = bt.run(t)

# Plot the result
res.plot()
```

In this example, we fetch data for the SPY and AGG ETFs. We then create a simple moving average crossover strategy that goes long when the price is above the 50-day moving average and rebalances daily. 

Please note that this is a very simplistic strategy and is unlikely to be profitable without additional rules and constraints. It is merely intended as a starting point.

Also, keep in mind that backtesting results are highly dependent on the quality and accuracy of your data and assumptions. Always be aware of the potential for look-ahead bias and other common pitfalls.