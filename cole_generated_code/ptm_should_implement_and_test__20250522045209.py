from ghost_env import INFURA_KEY, VAULT_ADDRESS
To implement and test new trading strategies, we can create a Python class named `TradingStrategy`. This class will have methods to implement and test strategies. Here's a simple example:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class TradingStrategy:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestRegressor()

    def implement_strategy(self, features, target):
        X = self.data[features]
        y = self.data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        print("Strategy implemented successfully.")

    def test_strategy(self, test_data):
        X_test = test_data.drop(target, axis=1)
        y_test = test_data[target]
        predictions = self.model.predict(X_test)
        mse = np.mean((predictions - y_test)**2)
        print(f"Strategy tested. Mean Squared Error: {mse}")
```

In this example, we are using a Random Forest model to implement a trading strategy. The `implement_strategy` method trains the model on the provided features and target. The `test_strategy` method tests the strategy on the test data and prints the Mean Squared Error of the predictions.

Please note that this is a very basic example. In a real-world scenario, the trading strategy could be much more complex and might involve multiple models and complex algorithms.

Also, this code assumes that you have preprocessed your data and it's ready for training/testing. If not, you might need to add data preprocessing steps before implementing/testing the strategy.