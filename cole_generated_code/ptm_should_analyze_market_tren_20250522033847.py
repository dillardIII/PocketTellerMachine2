Analyzing market trends and patterns to identify potential trading opportunities is a complex task that involves machine learning and data analysis. Here is a simplified example of how you might approach this task using Python. This example uses the pandas library to analyze stock data and the yfinance library to download stock data.

Please note that this is a very basic example and real-world trading algorithms are much more complex and take into account many more factors.

```python
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Download historical data for desired ticker
ticker = 'AAPL'
tickerData = yf.Ticker(ticker)
df = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# Calculate moving average
df['MA_50'] = df['Close'].rolling(50).mean()
df['MA_200'] = df['Close'].rolling(200).mean()

# Create a new data frame with only closing price and date
data = df.filter(['Close'])

# Convert data to numpy array and split it to train and test sets
dataset = data.values
training_data_len = int(len(dataset) * .8)
train_data = dataset[0:training_data_len, :]
test_data = dataset[training_data_len - 50: , :]

# Create a new dataframe with only the 'Close' column and convert it to an array
close_data = df.filter(['Close'])
dataset_close = close_data.values

# Create the independent data set (X) and dependent data set (y)
x_train, x_test, y_train, y_test = train_test_split(dataset, dataset_close, test_size=0.2, random_state=0)

# Create and train the Linear Regression Model
lr = LinearRegression()
lr.fit(x_train, y_train)

# Test the model using score
lr_confidence = lr.score(x_test, y_test)
print("lr confidence: ", lr_confidence)

# Get the models predictions
lr_prediction = lr.predict(x_test)
print(lr_prediction)
```

This script downloads historical data for a specific ticker, calculates the moving average for the past 50 and 200 days, and then uses a linear regression model to predict future prices based on this data. The model's predictions are then printed out. 

Please note that this is a very simplified example and real-world trading algorithms are much more complex and take into account many more factors. Also, this script does not actually execute any trades, it just identifies potential trading opportunities based on the model's predictions.