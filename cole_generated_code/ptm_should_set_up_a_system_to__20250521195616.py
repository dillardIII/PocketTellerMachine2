from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code that uses a dictionary to track wins and losses over time. This code assumes that the results of each trade (win or loss) are entered manually.

```python
class PTM:
    def __init__(self):
        self.trading_record = []

    def record_trade(self, result):
        if result.lower() not in ["win", "loss"]:
            print("Invalid input. Please enter 'win' or 'loss'.")
            return
        self.trading_record.append(result.lower())

    def performance_over_time(self):
        wins = self.trading_record.count("win")
        losses = self.trading_record.count("loss")
        try:
            win_loss_ratio = wins / losses
        except ZeroDivisionError:
            win_loss_ratio = "N/A"
        print(f"Wins: {wins}, Losses: {losses}, Win/Loss Ratio: {win_loss_ratio}")

# Usage
ptm = PTM()
ptm.record_trade("win")
ptm.record_trade("loss")
ptm.record_trade("win")
ptm.performance_over_time()
```

In this code, `PTM` is a class that represents the trading system. It has a list `trading_record` to store the results of each trade. The method `record_trade` is used to record a trade result (either "win" or "loss"). The method `performance_over_time` calculates and prints the number of wins, losses, and the win/loss ratio.