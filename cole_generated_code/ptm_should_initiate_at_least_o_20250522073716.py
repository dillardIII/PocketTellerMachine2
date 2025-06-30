from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that simulates a trade initiation. Please note that this is a very basic example and doesn't involve any real trading. You would need to use a trading API (like Alpaca, Interactive Brokers, etc.) to perform real trades.

```python
import random

class PTM:
    def __init__(self):
        self.trades = []
        self.strategy_effectiveness = {}

    def initiate_trade(self, strategy):
        # Simulate a trade
        trade = {
            'strategy': strategy,
            'buy_price': random.uniform(100, 200),  # Random buy price between 100 and 200
            'sell_price': random.uniform(100, 200),  # Random sell price between 100 and 200
        }
        self.trades.append(trade)

        # Assess strategy effectiveness
        profit = trade['sell_price'] - trade['buy_price']
        if strategy not in self.strategy_effectiveness:
            self.strategy_effectiveness[strategy] = {
                'total_profit': 0,
                'num_trades': 0,
            }
        self.strategy_effectiveness[strategy]['total_profit'] += profit
        self.strategy_effectiveness[strategy]['num_trades'] += 1

    def print_strategy_effectiveness(self):
        for strategy, data in self.strategy_effectiveness.items():
            avg_profit = data['total_profit'] / data['num_trades']
            print(f'Strategy: {strategy}, Average Profit: {avg_profit}')


# Create PTM and initiate a trade
ptm = PTM()
ptm.initiate_trade('Strategy 1')
ptm.initiate_trade('Strategy 2')

# Print strategy effectiveness
ptm.print_strategy_effectiveness()
```

This code creates a PTM (Portfolio Trading Model) which can initiate trades and assess the effectiveness of its strategies. The effectiveness is measured by the average profit of the trades initiated by each strategy.