# strategist_brain.py
def evaluate_strategy(payload):
    """
    Simple evaluator that chooses a mock strategy based on inputs.
    Later: replace with ML or signal-based logic.
    """
    signal_strength = payload.get("signal_strength", 50)

    if signal_strength > 75:
        return "Momentum Breakout"
    elif signal_strength > 50:
        return "EMA Crossover"
    else:
        return "Wait and Watch"