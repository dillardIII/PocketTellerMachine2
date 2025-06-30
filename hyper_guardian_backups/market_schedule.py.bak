from datetime import datetime, time
import pytz

def is_market_open():
    now = datetime.now(pytz.timezone("US/Eastern"))
    weekday = now.weekday()  # 0 = Monday, 6 = Sunday
    market_open = time(9, 30)
    market_close = time(16, 0)

    if weekday >= 5:
        return False  # Weekend

    current_time = now.time()
    return market_open <= current_time <= market_close