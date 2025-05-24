# === FILE: auto_route_loader.py ===

import os
import importlib.util

ROUTES_FOLDER = "routes"

def load_all_routes(app):
    if not os.path.exists(ROUTES_FOLDER):
        print("[AutoRouteLoader] No routes/ folder found.")
        return

    for filename in os.listdir(ROUTES_FOLDER):
        if filename.endswith("_route.py"):
            module_path = os.path.join(ROUTES_FOLDER, filename)
            module_name = filename[:-3]  # Remove .py

            try:
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Automatically find the Blueprint object
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if hasattr(obj, "url_map"):  # crude check for Flask Blueprint
                        app.register_blueprint(obj)
                        print(f"[AutoRouteLoader] Registered: {module_name}.{attr}")
                        break

            except Exception as e:
                print(f"[AutoRouteLoader] Failed to load {filename}: {e}")