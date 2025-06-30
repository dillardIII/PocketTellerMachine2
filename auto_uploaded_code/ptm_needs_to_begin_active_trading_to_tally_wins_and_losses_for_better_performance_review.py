from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a basic implementation of the trading strategy using Python. It uses simple buy low sell high strategy and tallies wins and losses at end of day.

Note: Please replace the 'stocks_database.csv' with your own dataset as it's just an arbitrary name.

```python
import pandas as pd

class Trading:
    def __init__(self):
        self.buy_price = 0
        self.stock_in_hand = False
        self.last_action = ""
        self.wins = 0
        self.losses = 0

    def make_decision(self, current_price):
        if not self.stock_in_hand and self.buy_price < current_price:
            self.buy_price = current_price
            self.stock_in_hand = True
            self.last_action = "Bought"
        elif self.stock_in_hand and self.buy_price > current_price:
            self.stock_in_hand = False
            if self.buy_price < current_price:
                self.wins += 1
            else:
                self.losses += 1
            self.last_action = "Sold"
        else:
            self.last_action = "Held"

    def run(self, stock_df):
        for index, row in stock_df.iterrows():
            self.make_decision(row['Price'])
        print(f"Wins: {self.wins}, Losses: {self.losses}")


if __name__ == "__main__":
    stock_df = pd.read_csv('stocks_database.csv')
    trading = Trading()
    trading.run(stock_df)
```

This program reads price data from a CSV, then iterates over each row, calling the `make_decision` method for each price. This method implements a simple trading strategy where the program buys stocks when the price is low and sells when it is high. It uses a wins and losses counter to track profitability. At the end, it prints out the number of profitable and unprofitable trades.

Please note you might need to adjust the trading strategy as per your specific requirement. This is a very basic 'Buy Low - Sell High' strategy and might not yield the best of the results. For serious trading you might need to implement more complex strategies including various indicators.