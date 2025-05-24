As an AI, I can't directly interact with PTM's trading strategies or systems. However, I can provide a basic Python code that could be used to analyze trading data and optimize trading strategies. 

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Assuming you have a CSV file with trading data
# Columns: 'TradeID', 'Strategy', 'Profit', 'Volume', 'Duration', 'Risk'

# Load the data
df = pd.read_csv('trading_data.csv')

# Preprocess the data
# Convert categorical data (trading strategies) into numerical data
df['Strategy'] = pd.Categorical(df['Strategy'])
df['Strategy'] = df['Strategy'].cat.codes

# Split the data into features (X) and target (y)
X = df[['Strategy', 'Volume', 'Duration', 'Risk']]
y = df['Profit']

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# You can use the trained model to predict the profit of future trades
# and optimize your trading strategies accordingly.
```

This is a very basic example of how you could use machine learning to optimize trading strategies. Depending on the complexity of your trading strategies and the amount of data you have, you might need more sophisticated models and techniques.