from ghost_env import INFURA_KEY, VAULT_ADDRESS
Creating a Predictive Trading Model (PTM) involves complex machine learning algorithms and requires a lot of data manipulation. Here is a simple example of how you might start to build such a model using Python. In this example, we'll use the pandas library to handle our data and the sklearn library to create a simple linear regression model.

```python
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load market data
# This data should be in a CSV file with columns for different market indicators and a column for the market trend
data = pd.read_csv('market_data.csv')

# Assume the last column is the one we want to predict
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a linear regression model
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# Use our model to predict the market trend for our testing set
y_pred = regressor.predict(X_test)

# Compare our predictions with the actual values to see how well our model is doing
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)
```

This is a very basic example and might not give very accurate predictions. A real-world trading model would use more sophisticated algorithms and would be trained and tested on a lot more data. Also, this code doesn't include any data preprocessing, which would be necessary in a real-world scenario.