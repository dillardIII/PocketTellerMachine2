import random
import time
from cole_event_logger import (
    log_info, log_warning, log_error, log_critical, log_recovery
)
from cole_smart_recovery import escalate_recovery_state
from cole_emergency_cooldown import recover_if_cooldown_passed
from cole_health_monitor import run_health_monitor
from cole_autopilot_cycle import is_emergency_mode

# === Failsafe Tester ===
def simulate_failure_scenario():
    print("\n=== Simulating System Failures ===")

    failures = [
        ("CPU Spike", "High CPU usage detected (95%)"),
        ("Memory Leak", "Memory usage critically high (92%)"),
        ("Disk IO Error", "Disk read/write latency spike"),
        ("API Timeout", "Broker API failed to respond"),
        ("Trade Error", "Failed to execute trade order"),
        ("Data Corruption", "Inconsistent market data detected")
    ]

    for source, message in random.sample(failures, 3):
        log_error(source, message)
        escalate_recovery_state(source, message)
        time.sleep(1)

    print("\n=== Running Health Monitor Check ===")
    run_health_monitor()

    if is_emergency_mode():
        log_critical("FailsafeTester", "System has entered EMERGENCY MODE")
    else:
        log_info("FailsafeTester", "System remains in normal mode")

# === Cooldown Recovery Tester ===
def simulate_cooldown_recovery():
    print("\n=== Simulating Cooldown Recovery ===")
    if recover_if_cooldown_passed():
        log_recovery("FailsafeTester", "System successfully exited emergency cooldown")
    else:
        log_info("FailsafeTester", "Cooldown timer still active. Recovery deferred.")

# === Main Test Runner ===
if __name__ == "__main__":
    print("=== Cole Failsafe Tester ===")
    simulate_failure_scenario()

    time.sleep(3)

    simulate_cooldown_recovery()

    print("\n=== Failsafe Test Completed ===")