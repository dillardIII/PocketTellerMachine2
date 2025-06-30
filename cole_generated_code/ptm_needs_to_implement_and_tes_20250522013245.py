from ghost_env import INFURA_KEY, VAULT_ADDRESS
To implement and test different trading strategies, you would need to use a backtesting framework. Backtesting is the process of testing a trading strategy on relevant historical data to ensure its viability before the trader risks any actual capital. 

Here is a simple Python code using the `bt` library, which is a flexible backtesting framework for Python used to test quantitative trading strategies.

```python
import bt

# Define the strategy
def strategy(data):
    if data['AAPL'].iloc[-1] > data['AAPL'].iloc[-2]:
        return pd.Series({'AAPL': 1})
    else:
        return pd.Series({'AAPL': -1})

# Get the data
data = bt.get('AAPL', start='2020-01-01', end='2020-12-31')

# Create the strategy
bt_strategy = bt.Strategy('Trade_When_Price_Increases', [bt.algos.RunDaily(),
                                                         bt.algos.SelectAll(),
                                                         bt.algos.WeighTarget(strategy),
                                                         bt.algos.Rebalance()])

# Create the backtest and run it
backtest = bt.Backtest(bt_strategy, data)
result = bt.run(backtest)

# Plot the result
result.plot(title='Backtest result')
```

In this example, the strategy is to buy AAPL stock when the price increases compared to the previous day, and sell when the price decreases. The backtest is run on the AAPL stock data from 2020, and the result is plotted.

Please note that this is a very simplistic strategy and is unlikely to be profitable in real trading. You would need to implement more complex strategies and consider transaction costs, slippage, etc. Also, past performance is not indicative of future results.