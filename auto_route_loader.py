# auto_route_loader.py
# Loads only valid Flask blueprints dynamically into PTM

import os
import importlib.util

def load_dynamic_routes(app, route_folder="."):
    print("[AutoRouteLoader] 🚀 Scanning for blueprints...")

    for file in os.listdir(route_folder):
        if file.endswith("_route.py") and not file.startswith("__"):
            route_path = os.path.join(route_folder, file)

            try:
                spec = importlib.util.spec_from_file_location("module.name", route_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Find any attributes ending in _bp (e.g., market_trend_bp)
                blueprint = next(
                    (getattr(module, attr) for attr in dir(module) if attr.endswith("_bp")),
                    None
                )

                if blueprint:
                    app.register_blueprint(blueprint)
                    print(f"[AutoRouteLoader] ✅ Loaded {file}")
                else:
                    print(f"[AutoRouteLoader] ⚠️ No blueprint found in {file}")

            except Exception as e:
                print(f"[AutoRouteLoader] ❌ Failed to load {file}: {e}")