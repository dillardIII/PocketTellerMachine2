To complete this task, we would need to use a combination of data analysis and machine learning techniques. Here is a simplified version of how you might approach this problem using Python. Note that this is a very basic example and real-world trading algorithms are much more complex and take into account many more factors.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load market data
data = pd.read_csv('market_data.csv')

# Assume we have 'Open', 'High', 'Low', 'Close' and 'Volume' in our data
# We will use these to predict the 'Close' price

# Create a feature data set (X) and a target data set (Y)
X = data[['Open', 'High', 'Low', 'Volume']]
Y = data['Close']

# Split the data into 80% training and 20% testing data sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Create and train the Linear Regression Model
lr = LinearRegression()
lr.fit(x_train, y_train)

# Test the model using score
lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

# Predict the 'Close' price
lr_prediction = lr.predict(x_test)
print(lr_prediction)
```

This code will create a simple linear regression model that predicts the 'Close' price based on 'Open', 'High', 'Low', and 'Volume'. It then prints the confidence of the model and the predicted 'Close' prices. 

Please note that this is a very simplified model and doesn't take into account many factors that could influence market trends and patterns. In a real-world scenario, you would likely use much more complex models and take into account many more factors.