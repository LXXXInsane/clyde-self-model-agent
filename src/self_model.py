import json
from datetime import datetime

class SelfModel:
    def __init__(self, filepath="../data/self_model.json"):
        self.filepath = filepath
        self.model = {
            "name": "Clyde",
            "traits": ["curious", "cooperative"],
            "goals": ["learn", "assist user", "store memory"],
            "internal_state": {},
            "last_updated": str(datetime.now())
        }
        self.load()

    def load(self):
        try:
            with open(self.filepath, "r") as f:
                self.model = json.load(f)
        except FileNotFoundError:
            self.save()

    def save(self):
        self.model["last_updated"] = str(datetime.now())
        with open(self.filepath, "w") as f:
            json.dump(self.model, f, indent=4)

    def update(self, key, value):
        self.model[key] = value
        self.save()

