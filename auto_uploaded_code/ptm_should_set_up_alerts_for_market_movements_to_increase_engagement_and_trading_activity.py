Here is a simple Python script that uses the `yfinance` library to fetch stock market data and then checks if the stock has moved more than a specified percentage. If the stock has moved more than the specified percentage, it will print an alert message.

Please note that this is a very basic script. For a production environment, you would want to use a more robust solution, possibly involving a database to store historical prices and a web service to send alert notifications.

```python
import yfinance as yf

def check_stock(symbol, threshold):
    # Fetch data
    data = yf.download(symbol, period='1d')

    # Calculate percentage change
    change = ((data['Close'][-1] - data['Open'][-1]) / data['Open'][-1]) * 100

    # Check if change is greater than threshold
    if abs(change) > threshold:
        print(f"Alert: {symbol} has moved {change}%")

# Example usage
check_stock('AAPL', 2)  # Check if Apple stock has moved more than 2%
```

This script will only check the stock once. If you want to continuously monitor the stock, you could put the `check_stock` function in a loop and add a delay with the `time.sleep` function. But be careful not to violate any terms of service by making requests too frequently.

Also, this script currently just prints the alert to the console. If you want to actually send an alert (like an email or a push notification), you would need to add that functionality.