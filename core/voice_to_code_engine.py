# voice_to_code_engine.py
# Converts spoken or text input into actual .py or .json code modules

import datetime

def interpret_command_as_code(command):
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

    if "trade filter" in command:
        return {
            "filename": f"core/trade_filter_{timestamp}.py",
            "code": '''
def filter_trade(trade):
    if trade.get("drawdown", 0) > 0.25:
        return False
    return True
''',
            "description": "Auto-generated trade filter module"
        }

    elif "mood log" in command:
        return {
            "filename": f"memory/mood_log_{timestamp}.json",
            "code": '{ "mood": "neutral", "timestamp": "' + timestamp + '" }',
            "description": "Auto-generated mood snapshot"
        }

    return {
        "filename": f"memory/unrecognized_{timestamp}.txt",
        "code": command,
        "description": "Unclassified voice command"
    }
    