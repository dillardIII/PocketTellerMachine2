from ghost_env import INFURA_KEY, VAULT_ADDRESS
# route_loader.py – Dynamically loads all Flask routes into the app

import importlib
import os

def load_routes(app, routes_directory="routes"):
    print("[Route Loader] 🔍 Scanning for route modules...")

    for filename in os.listdir(routes_directory):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module_path = f"{routes_directory}.{module_name}"

            try:
                module = importlib.import_module(module_path)
                if hasattr(module, "bp"):
                    app.register_blueprint(module.bp)
                    print(f"[Route Loader] ✅ Loaded route module: {module_name}")
                elif hasattr(module, "trend_analysis_bp"):
                    app.register_blueprint(module.trend_analysis_bp)
                    print(f"[Route Loader] ✅ Loaded trend analysis route: {module_name}")
                elif hasattr(module, "market_trend_bp"):
                    app.register_blueprint(module.market_trend_bp)
                    print(f"[Route Loader] ✅ Loaded market trend route: {module_name}")
                else:
                    print(f"[Route Loader] ⚠️ No blueprint(found in: {module_name}"))
            except Exception as e:
                print(f"[Route Loader] ❌ Failed to load {module_name}: {e}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():