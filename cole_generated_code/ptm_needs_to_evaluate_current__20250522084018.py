Sure, to accomplish this task we can use the `yfinance` library in Python to download stock data. However, please note that identifying potential winning trades involves complex algorithms and strategies that consider various factors like price trends, trading volumes, market news, company fundamentals, etc. Here is a simple Python code that fetches the latest stock data and calculates the percentage change:

```python
import yfinance as yf

def calculate_percentage_change(old, new):
    return ((new - old) / old) * 100

def evaluate_market(stock_symbols):
    potential_winning_trades = []

    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="5d")

        # Calculate the percentage change over the last 5 days
        percentage_change = calculate_percentage_change(hist["Close"][0], hist["Close"][-1])

        # If the stock has grown over the last 5 days, it might be a potential winning trade
        if percentage_change > 0:
            potential_winning_trades.append((symbol, percentage_change))
    
    return potential_winning_trades

# List of stock symbols to evaluate
stock_symbols = ["AAPL", "GOOGL", "TSLA", "AMZN"]

potential_winning_trades = evaluate_market(stock_symbols)

for trade in potential_winning_trades:
    print(f"Stock: {trade[0]}, Growth over the last 5 days: {trade[1]}%")
```

This code fetches the last 5 days of historical data for the given stock symbols and calculates the percentage change in closing price. If the stock has grown over the last 5 days, it is considered a potential winning trade. 

Please note that this is a very simplistic approach and might not yield the best results in a real-world scenario. A more sophisticated approach would involve the use of machine learning algorithms and a more comprehensive set of data.