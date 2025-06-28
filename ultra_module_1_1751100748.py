Creating a module that evolves ghost memory weights based on the last 10 trades involves implementing a system that updates its understanding or memory of trades dynamically. The "ghost memory" term typically refers to an augmented, temporary, or simulated memory that can adapt to new information. Here is a simple implementation in Python to illustrate this concept. We'll use a mock trading system where weights are adjusted with each trade.

```python
class GhostMemory:
    def __init__(self, max_trades=10):
        self.max_trades = max_trades
        self.trades = []
        self.weights = [0.1] * max_trades  # Initial weights for the mock memory

    def add_trade(self, trade_value):
        """
        Add a trade value to the memory and update weights.
        The weights evolve based on some characteristic of the trades.
        """
        if len(self.trades) >= self.max_trades:
            self.trades.pop(0)
        self.trades.append(trade_value)
        self.evolve_weights()

    def evolve_weights(self):
        """
        Evolve the ghost memory weights.
        This is a simple example, evolves based on moving average of trades.
        """
        if len(self.trades) == 0:
            return

        total_value = sum(self.trades)
        new_weights = [(trade / total_value) for trade in self.trades]

        # Normalize the weights to maintain a total of 1
        sum_weights = sum(new_weights)
        self.weights = [w / sum_weights for w in new_weights]

    def get_weighted_average(self):
        """
        Get a weighted average of the trades based on the current weights.
        """
        weighted_sum = sum(trade * weight for trade, weight in zip(self.trades, self.weights))
        return weighted_sum

    def __str__(self):
        return f"Trades: {self.trades}\nWeights: {self.weights}\nWeighted Average: {self.get_weighted_average()}"

# Example Usage
if __name__ == "__main__":
    ghost_memory = GhostMemory()

    # Simulate adding trades
    trades = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
    for trade in trades:
        ghost_memory.add_trade(trade)
        print(ghost_memory)
```

### Explanation:

1. **Initialization**: The `GhostMemory` class is initialized with a maximum number of trades (defaulted to 10) and a list of initial weights.

2. **Adding Trades**: The `add_trade` method adds a new trade to the list, popping the oldest if the list exceeds the maximum allowed number. It then calls `evolve_weights`.

3. **Evolving Weights**: The `evolve_weights` method updates the weights based on the proportion of each trade relative to the total, simulating a moving average effect. It normalizes weights so that they sum to 1.

4. **Weighted Average**: `get_weighted_average` computes the weighted average of the trades using the current weights.

5. **Output**: The example usage simulates the behavior of the `GhostMemory` with a sequence of trades, printing the trades, weights, and weighted average after each addition.

This structure can be further refined or replaced with more sophisticated methods like exponential moving averages, neural networks, or other statistical techniques depending on the desired complexity and accuracy.