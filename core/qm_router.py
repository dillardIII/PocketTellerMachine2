# qm_router.py
# Routes thoughts through the quantum AI matrix

import json

def route_thought(thought):
    with open("core/entity_matrix.json") as f:
        matrix = json.load(f)

    responses = []
    for entity in matrix["entities"]:
        if "ghostmind" in entity["access"]:
            responses.append(f"{entity['name']} echoes: {thought}")

    return responses