from self_model import SelfModel
from memory import MemoryStore

class Reflection:
    def __init__(self, self_model_path="../data/self_model.json", memory_path="../data/memories.json"):
        # Load Clyde's self-model and memory store
        self.self_model = SelfModel(filepath=self_model_path)
        self.memory_store = MemoryStore(filepath=memory_path)

    def summarize_self(self):
        """Return a summary of Clyde's identity and state."""
        model = self.self_model.model
        summary = f"Name: {model.get('name')}\n"
        summary += f"Traits: {', '.join(model.get('traits', []))}\n"
        summary += f"Goals: {', '.join(model.get('goals', []))}\n"
        summary += f"Internal state: {model.get('internal_state', {})}\n"
        summary += f"Last updated: {model.get('last_updated')}"
        return summary

    def recent_memories(self, n=5):
        """Return the last n memories."""
        return self.memory_store.get_recent(n)

    def reflect(self):
        """
        This is the placeholder for external reflection.
        In the future, we could send this data to Kai for critique and suggestions.
        """
        print("---- Self Model Summary ----")
        print(self.summarize_self())
        print("\n---- Recent Memories ----")
        for mem in self.recent_memories():
            print(f"{mem['timestamp']}: {mem['text']}")

