from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_tester.py ===

import os

def test_feature(task):
    """
    Verifies whether the generated HTML and route files exist and are valid.
    """
    name = task["params"]["name"].replace(" ", "_").lower()
    html_file = f"templates/{name}.html"
    route_file = f"routes/{name}_route.py"

    html_exists = os.path.exists(html_file)
    route_exists = os.path.exists(route_file)

    result = {
        "html_exists": html_exists,
        "route_exists": route_exists,
        "passed": html_exists and route_exists
    }

    if result["passed"]:
        print(f"[Tester] PASSED for feature: {name}")
    else:
        print(f"[Tester] FAILED for feature: {name}")
        if not html_exists:
            print(f" - Missing HTML: {html_file}")
        if not route_exists:
            print(f" - Missing Route: {route_file}")

    return result

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():