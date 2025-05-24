def grade_trade(trade, result):
    if result >= 200:
        return "A"
    elif result >= 100:
        return "B"
    elif result >= 0:
        return "C"
    elif result >= -50:
        return "D"
    else:
        return "F"