# bot_router.py
# Central dispatcher for routing commands to the correct bot or module

from ghost_code_deck import GhostCodeDeck

class BotRouter:
    def __init__(self):
        self.deck = GhostCodeDeck()
        self.context_memory = {}
        self.priority_rules = {
            "emergency": 0,
            "critical": 1,
            "high": 2,
            "normal": 3,
            "low": 4
        }

    def register_bot(self, name, category, description, function):
        self.deck.add_card(name, category, description, function)

    def set_context(self, user_id, context):
        self.context_memory[user_id] = context

    def get_context(self, user_id):
        return self.context_memory.get(user_id, {})

    def route_command(self, user_id, command_text, priority="normal"):
        try:
            context = self.get_context(user_id)
            target_bot_name = self._parse_command_for_bot(command_text, context)
            result = self.deck.summon_by_name(target_bot_name)
            return {
                "status": "routed",
                "bot": target_bot_name,
                "result": result
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    def _parse_command_for_bot(self, command_text, context):
        # Naive NLP-style intent match (placeholder — replace with LLM later)
        text = command_text.lower()
        if "translate" in text:
            return "TranslatorBot"
        elif "code" in text or "program" in text:
            return "CodeCompilerBot"
        elif "ai" in text and "train" in text:
            return "TrainerBot"
        elif "security" in text:
            return "GhostSecurityBot"
        elif "bridge" in text:
            return "BridgeBot"
        else:
            raise ValueError("Could not identify bot from command.")

    def list_available_bots(self):
        return self.deck.list_all_cards()