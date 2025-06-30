from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ghost_code_deck.py
# Card-like bot summoner interface logic (backend)

class BotCard:
    def __init__(self, name, category, description, launch_function):
        self.name = name
        self.category = category
        self.description = description
        self.launch_function = launch_function

    def activate(self):
        try:
            return self.launch_function()
        except Exception as e:
            return f"[ERROR] Failed to activate bot {self.name}: {str(e)}"

class GhostCodeDeck:
    def __init__(self):
        self.deck = []

    def add_card(self, name, category, description, launch_function):
        card = BotCard(name, category, description, launch_function)
        self.deck.append(card)

    def summon_by_name(self, name):
        for card in self.deck:
            if card.name.lower() == name.lower():
                return card.activate()
        return f"[ERROR] No bot card named '{name}' found."

    def summon_by_category(self, category):
        results = []
        for card in self.deck:
            if card.category.lower() == category.lower():
                results.append(card.activate())
        return results if results else f"[ERROR] No cards in category '{category}'.":
:
    def list_all_cards(self):
        return [
            {
                "name": card.name,
                "category": card.category,
                "description": card.description
            }
            for card in self.deck
        ]

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():