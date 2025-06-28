# === FILE: file_transfer_test.py ===
from team_file_router import send_file_to_team

def test_file_share():
    # Simulate Cole sending strategy.py to Strategist
    send_file_to_team(
        sender="Cole",
        recipient="Strategist",
        file_path="sample_strategies/strategy_alpha.py",
        description="Here's a new alpha strategy I cooked up."
    )

if __name__ == "__main__":
    test_file_share()