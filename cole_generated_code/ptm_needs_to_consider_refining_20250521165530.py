To refine your current trading algorithms, you may want to consider various approaches such as adjusting existing parameters, introducing new parameters, or applying machine learning techniques to better predict market movements.

Please note that following is a simplistic representation of a trading algorithm using Python, adjustments according to specifics of your trading strategy would be needed. Also, implement real trading actions and algorithms using real money needs a professional knowledge and thorough understanding of the market.

```python
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class TradingStrategy:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def preprocess_data(self):
        # Scale the data
        scaler = preprocessing.MinMaxScaler()
        scaled_df = scaler.fit_transform(self.data_frame)
        scaled_df = pd.DataFrame(scaled_df, columns=self.data_frame.columns)
        return scaled_df

    def apply_regression(self):
        # Split the data into 'x' (independent variables) and 'y' (dependent variable)
        x = self.data_frame.drop('Market price', axis=1)
        y = self.data_frame['Market price']
        
        # Split the data into training and testing data
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
        
        # Use Linear Regression algorithm
        regressor = LinearRegression()
        regressor.fit(x_train, y_train)

        # Make predictions
        y_pred = regressor.predict(x_test)

        return y_pred, y_test

    def calculate_accuracy(self, y_test, y_pred):
        # Calculate the accuracy
        accuracy = metrics.r2_score(y_test, y_pred)
        return accuracy
        

# Create an object of the class and call the functions
trading = TradingStrategy(data_frame)
scaled_data = trading.preprocess_data()
y_pred, y_test = trading.apply_regression()
accuracy = trading.calculate_accuracy(y_test, y_pred)

print(f"Model Accuracy: {accuracy}")
```

This example uses a very simple linear regression model to predict market prices. This strategy can be substantially improved by refining the model (using a different algorithm that better suits the data, adjusting parameters, etc.) or by incorporating additional parameters like market sentiment or news events. Note that live trading should only be performed based on thoroughly tested and evaluated models.