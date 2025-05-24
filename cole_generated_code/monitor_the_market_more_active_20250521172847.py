Here's a simple Python script that uses Alpha Vantage's API to monitor market price changes for a specific stock, in this case, Apple Inc. (AAPL). This will give us some idea of market trends in real-time. For the purpose of illustration, I'll assume that we're identifying trading opportunities as situations where the stock price has gone down 5% or more from the latest high price.

Please note that Alpha Vantage's free tier includes up to 5 API requests per minute and up to 500 requests per day.

```python
import time
import requests
import json

def get_price(symbol):
    API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
    BASE_URL = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(symbol, API_KEY)
    response = requests.get(BASE_URL)
    response_json = json.loads(response.text)
    return float(response_json["Global Quote"]["05. price"])

def monitor_price(symbol, decrease_percent):
    max_price = get_price(symbol)
    while True:
        time.sleep(60)  # wait for a minute between each price check
        current_price = get_price(symbol)
        if current_price > max_price:
            max_price = current_price
        elif current_price <= (1 - decrease_percent/100) * max_price:
            print("ALERT: The stock price has dropped by more than {}%. This might be a good time to buy.".format(decrease_percent))
            max_price = current_price  # reset max_price

if __name__ == '__main__':
    monitor_price('AAPL', 5)
```
Remember to replace `'YOUR_ALPHA_VANTAGE_API_KEY'` with your actual API Key.

This script sends a request to the Alpha Vantage API every minute to get the latest price for the specified symbol (stock), and it will alert you when the stock price has dropped by more than the specified percentage from the latest high price.

This is a simple example. In practice, one would probably use a more sophisticated method for identifying trading opportunities, and would also account for trading fees and potential taxes in their calculations. Also, you should be careful to ensure this code doesn't exceed Alpha Vantage's rate limits.