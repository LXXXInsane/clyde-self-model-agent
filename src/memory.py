import json
from datetime import datetime

class MemoryStore:
    def __init__(self, filepath="../data/memories.json"):
        self.filepath = filepath
        self.memories = []
        self.load()

    def load(self):
        """Load memories from disk, or create empty list if file doesn't exist."""
        try:
            with open(self.filepath, "r") as f:
                self.memories = json.load(f)
        except FileNotFoundError:
            self.memories = []
            self.save()

    def save(self):
        """Save current memories to disk."""
        with open(self.filepath, "w") as f:
            json.dump(self.memories, f, indent=4)

    def add_memory(self, text, context=None):
        """Add a new memory with optional context."""
        memory = {
            "timestamp": str(datetime.now()),
            "text": text,
            "context": context or {}
        }
        self.memories.append(memory)
        self.save()

    def get_recent(self, n=5):
        """Return the last n memories."""
        return self.memories[-n:]

    def search(self, keyword):
        """Simple search: return memories containing keyword in text."""
        return [m for m in self.memories if keyword.lower() in m["text"].lower()]

