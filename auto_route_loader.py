# === FILE: auto_route_loader.py ===

import os
import importlib.util

def load_all_routes(app):
    route_dir = "routes"
    if not os.path.exists(route_dir):
        print("[AutoRouteLoader] Route directory not found.")
        return

    for filename in os.listdir(route_dir):
        if filename.endswith("_route.py"):
            module_name = filename[:-3]
            file_path = os.path.join(route_dir, filename)

            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, "bp"):
                    app.register_blueprint(module.bp)
                    print(f"[AutoRouteLoader] Loaded route: {filename}")
                else:
                    print(f"[AutoRouteLoader] No blueprint found in {filename}")

            except Exception as e:
                print(f"[AutoRouteLoader] Failed to load {filename}: {e}")