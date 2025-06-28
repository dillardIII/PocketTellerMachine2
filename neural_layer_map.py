# === FILE: neural_layer_map.py ===
# 🧠 Neural Layer Map – Tracks layers of PTM AI cognition for recursive evolution simulation

class NeuralLayerMap:
    def __init__(self):
        self.layers = {}

    def add_layer(self, name, description, depth, dependencies=None):
        self.layers[name] = {
            "description": description,
            "depth": depth,
            "dependencies": dependencies or []
        }

    def describe_layer(self, name):
        return self.layers.get(name, "Layer not found")

    def all_layers(self):
        return self.layers