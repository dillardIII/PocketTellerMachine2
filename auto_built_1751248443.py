from ghost_env import INFURA_KEY, VAULT_ADDRESS
```python
# ghost_ai.py
import random
import string
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class GhostAI:
    def __init__(self):
        self.personalities = {}
        logging.info("Ghost AI initialized with no personalities.")

    def spawn_personality():> str:
        if not name:
            name = self.generate_random_name()
        personality = {
            "id": self.generate_unique_id(),
            "emotional_state": random.choice(["happy", "sad", "angry", "neutral"]),
            "knowledge_base": []
        }
        self.personalities[name] = personality
        logging.info(f"Spawned new personality: {name} with ID {personality['id']}")
        return name

    def generate_random_name():> str:
        name = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        logging.debug(f"Generated random name: {name}")
        return name

    def generate_unique_id():> str:
        unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        logging.debug(f"Generated unique ID: {unique_id}")
        return unique_id

    def get_personalities():> Dict[str, Dict]:
        logging.debug(f"Current personalities: {self.personalities}")
        return self.personalities

    def simulate_interaction():> None:
        if name in self.personalities:
            personality = self.personalities[name]
            # Simplified interaction model that just logs interactions
            logging.info(f"Interacting with {name}: {interaction}")
            personality["knowledge_base"].append(interaction)
            personality["emotional_state"] = random.choice(["happy", "sad", "angry", "neutral"])
            logging.debug(f"Updated emotional state to: {personality['emotional_state']}")

    def delete_personality():> bool:
        if name in self.personalities:
            del self.personalities[name]
            logging.info(f"Deleted personality: {name}")
            return True
        logging.warning(f"Attempted to delete non-existent personality: {name}")
        return False


if __name__ == "__main__":
    ai = GhostAI()
    name1 = ai.spawn_personality()
    ai.simulate_interaction(name1, "Told a joke")
    name2 = ai.spawn_personality("Casper")
    ai.simulate_interaction(name2, "Discussed philosophy")
    ai.get_personalities()
    ai.delete_personality(name1)
    ai.get_personalities()
```


def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():