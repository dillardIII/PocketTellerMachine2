As an AI language model I cannot fetch or retrieve real-time information and hence, cannot fetch current market conditions. But I can certainly help you in writing a python program that fetch the market data using various APIs and based on that set the trading criteria.

Below is an example of how we can adjust trading criteria based on fetched market data using API:

Please replace `'Your API Key'` with your real API Key.

```python
import requests
import json

def get_market_data(stock_symbol):
    API_KEY = 'Your API Key'
    r = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={API_KEY}')
    market_data = r.json()
    return market_data

def trading_criteria(market_data, symbol):
    close_price = float(market_data["Global Quote"]["05. price"])
    open_price = float(market_data["Global Quote"]["02. open"])
    volume = float(market_data["Global Quote"]["06. volume"])
    # Implement your own trading criteria
    if close_price > open_price and volume > 10000:
        print(f'Recommend to BUY {symbol}')
    elif close_price < open_price and volume > 10000:
        print(f'Recommend to SELL {symbol}')
    else:
        print(f'No action for {symbol}')

if __name__ == "__main__":
    symbol = 'IBM'
    market_data = get_market_data(symbol)
    trading_criteria(market_data, symbol)
```

This script fetches the real-time market data of a specific stock symbol using Alpha Vantage API then it applies trading logic based on closing price, opening price and volume, and prints out the action to take.

Remember that this is an extremely rudimentary form of trading advice, and a real-life trading bot or algorithm would be much more complex, incorporating much more data and more sophisticated decision-making. Always consult with a qualified professional or trusted advisor before making trading decisions.