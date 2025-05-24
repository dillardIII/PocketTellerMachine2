To diversify trading strategies, we can use different financial indicators and algorithms. Here is a simple example of how to diversify strategies using Python.

```python
import pandas as pd
from pandas_datareader import data as web
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Define the stocks to be used
stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

# Define the start and end dates
start_date = '01/01/2010'
end_date = '01/01/2020'

# Fetch the stock data
stock_data = pd.DataFrame()
for stock in stocks:
    stock_data[stock] = web.DataReader(stock, data_source='yahoo', start=start_date, end=end_date)['Adj Close']

# Calculate the returns
stock_data = stock_data.pct_change()

# Create the target variable
stock_data['Target'] = stock_data['AAPL'].shift(-1)
stock_data.dropna(inplace=True)
stock_data['Target'] = [1 if x > 0 else 0 for x in stock_data['Target']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(stock_data.drop('Target', axis=1), stock_data['Target'], test_size=0.2)

# Define the models
models = {
    'Random Forest': RandomForestClassifier(),
    'Logistic Regression': LogisticRegression(),
    'Support Vector Machine': SVC()
}

# Train and evaluate the models
for model_name, model in models.items():
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f'{model_name} Accuracy: {accuracy * 100:.2f}%')
```

This code fetches the stock data for Apple, Google, Microsoft, and Amazon over a 10-year period. It then calculates the returns and uses these returns to predict whether the next day's return for Apple will be positive or negative. The prediction is done using three different models: Random Forest, Logistic Regression, and Support Vector Machine. The accuracy of each model is then printed.

Please note that this is a very simplistic approach and should not be used for actual trading. Real-world trading strategies are much more complex and take into account a wide variety of factors.