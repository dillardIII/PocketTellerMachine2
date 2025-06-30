from ghost_env import INFURA_KEY, VAULT_ADDRESS
To actively monitor the market trends for profitable trading opportunities, you may utilize a popular Python library called yfinance. yfinance is a useful tool that lets you access real-time Yahoo Finance data. However, please note that this might not be a sophisticated solution for large scale algorithmic trading, just a simple interactive script for small scale monitoring.

Here's an example of how you could use it for market analysis:

```python
import yfinance as yf
import time

# Function to monitor market trends for a specific stock
def monitor_market_trends(ticker_symbol, interval):

    while True:
        # Retrieve stock data
        stock = yf.Ticker(ticker_symbol)
        # Get historical market data
        history = stock.history(period='1d')
        # Print the last price
        print(f'Time: {history.index[-1]}, Close price: {history["Close"][-1]}')
        
        # Delay the script for the defined interval in seconds
        time.sleep(interval)

# Monitor market trends for Apple Inc. every 60 seconds 
monitor_market_trends('AAPL', 60)

```

This script will monitor the closing price for the of Apple Inc.'s stock every 60 seconds.

However, since "profitable trading opportunities" can be subjective and usually require complex analysis including considerations such as volume data, historical trends, financial indicators like RSI, MACD etc., you may want to develop or incorporate more advanced trading algorithms or strategies into this script, or use other more professional trading APIs. 

Also, please beware that you should obey the related rules and laws regarding automated trading in your jurisdiction. It’s possible that in some regions, continuously polling price data and making many requests to Yahoo finance may violate their term of service.