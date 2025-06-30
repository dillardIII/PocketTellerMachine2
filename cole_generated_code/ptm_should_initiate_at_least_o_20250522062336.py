from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a basic Python code for a trading bot using a simple strategy. Please note that this is a very simplified version and real-world trading bots require a lot more considerations such as handling API rate limits, error handling, etc.

```python
import ccxt  # Cryptocurrency Exchange Library

# Initialize the exchange
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

# Define the trading pair and the amount to trade
symbol = 'BTC/USDT'
amount = 0.01

# Fetch the current price
ticker = exchange.fetch_ticker(symbol)
price = ticker['bid']

# Define the strategy: buy if the price is low, sell if the price is high
if price < 10000:
    # Buy
    order = exchange.create_market_buy_order(symbol, amount)
    print(f'Buy order at {price} executed.')
elif price > 20000:
    # Sell
    order = exchange.create_market_sell_order(symbol, amount)
    print(f'Sell order at {price} executed.')
else:
    print(f'Price {price} not in the range for trading.')

```

This script uses the `ccxt` library to interact with the Binance exchange. It fetches the current price of BTC/USDT and if the price is less than 10000 USDT, it initiates a buy order. If the price is more than 20000 USDT, it initiates a sell order.

Please replace 'YOUR_API_KEY' and 'YOUR_SECRET_KEY' with your actual Binance API key and secret key.

Remember, this is a very basic bot and doesn't take into account many factors that could influence trading decisions, such as transaction fees, the order book, historical price data, etc. For a real trading bot, you would need a more sophisticated strategy and error handling.