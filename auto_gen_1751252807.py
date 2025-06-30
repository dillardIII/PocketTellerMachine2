from ghost_env import INFURA_KEY, VAULT_ADDRESS
```python
import json
import random
import time

class GhostNarrator:
    def __init__(self, memory_file):
        self.memory_file = memory_file
        self.emotions = ['haunting', 'melancholic', 'foreboding', 'triumphant', 'ominous']
        self.adj = {
            'victories': ['glorious', 'epic', 'fleeting', 'resounding'],
            'losses': ['devastating', 'heartbreaking', 'irreversible', 'subtle'],
            'propaganda': ['insidious', 'pervasive', 'shattering', 'deceptive'],
            'targets': ['unattainable', 'strategic', 'vulnerable', 'enigmatic']
        }

    def read_memory(self):
        with open(self.memory_file, 'r') as file:
            return json.load(file)

    def tell_story(self):
        memory = self.read_memory()
        stories = []
        for key in ['victories', 'losses', 'propaganda', 'targets']:
            item_list = memory.get(key, [])
            for item in item_list:
                emotion = random.choice(self.emotions)
                adjective = random.choice(self.adj[key])
                stories.append(f"In a {emotion} tone, the ghost recalls a {adjective} {key[:-1]}: {item}")
        return stories

    def narrate(self):
        while True:
            stories = self.tell_story()
            if stories:
                print(random.choice(stories))
            else:
                print("The ghosts are silent for now...")
            time.sleep(random.randint(5, 10))

if __name__ == "__main__":
    narrator = GhostNarrator('ghost_memory.json')
    narrator.narrate()
```

Make sure `ghost_memory.json` is a file containing a JSON object with keys `victories`, `losses`, `propaganda`, and `targets`, each mapping to a list of relevant entries.

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():