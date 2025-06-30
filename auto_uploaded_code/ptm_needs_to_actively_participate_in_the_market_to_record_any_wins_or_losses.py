from ghost_env import INFURA_KEY, VAULT_ADDRESS
In order to actively participate in the market and record any wins or losses, PTM would need to keep track of its trades. Here is a simple Python code that could simulate this process:

```python
class PTM:
    def __init__(self):
        self.balance = 0
        self.trades = []

    def buy(self, price):
        self.balance -= price
        self.trades.append(('buy', price))

    def sell(self, price):
        self.balance += price
        self.trades.append(('sell', price))

    def record(self):
        win = 0
        loss = 0
        for i in range(len(self.trades)-1):
            if self.trades[i][0] == 'buy' and self.trades[i+1][0] == 'sell':
                if self.trades[i+1][1] > self.trades[i][1]:
                    win += 1
                else:
                    loss += 1
        return win, loss

ptm = PTM()
ptm.buy(100)
ptm.sell(150)
ptm.buy(200)
ptm.sell(150)
win, loss = ptm.record()
print(f"Wins: {win}, Losses: {loss}")
```

In this code, we define a class `PTM` with methods to buy and sell at certain prices, and to record the number of wins and losses. A win is defined as a sell trade at a higher price than the preceding buy trade, and a loss is defined as a sell trade at a lower price than the preceding buy trade. The `record` method iterates over the list of trades and counts the number of wins and losses.