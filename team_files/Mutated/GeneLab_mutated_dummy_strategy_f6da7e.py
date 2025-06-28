def should_buy(price, rsi):
    if price < 202 and rsi < 35:
        return True
    return False

risk = 0.07
threshold = 0.65
confidence = 0.75

