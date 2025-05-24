Sure, here is a simple Python code to simulate trading activity for PTM (Python Trading Model). This code will randomly generate wins or losses for each trading day and record them.

```python
import random

class PTM:
    def __init__(self):
        self.record = []

    def trade(self):
        # Simulate win or loss
        result = random.choice(['win', 'loss'])
        self.record.append(result)

    def get_record(self):
        return self.record

# Create PTM instance
ptm = PTM()

# Simulate 30 trading days
for _ in range(30):
    ptm.trade()

# Print trading record
print(ptm.get_record())
```

This code creates a PTM class with methods to simulate a trade (win or loss) and to get the trading record. It then creates an instance of the PTM, simulates 30 trading days, and prints the trading record.

Please note that this is a very simplified model. Real-world trading involves complex strategies and risk management.