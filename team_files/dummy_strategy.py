def should_buy(price, rsi):
    if price < 200 and rsi < 30:
        return True
    return False

risk = 0.05
threshold = 0.7
confidence = 0.6

