from src.self_model import SelfModel
from src.memory import MemoryStore
from src.reflection import Reflection

def main():
    # Initialize components
    self_model = SelfModel()
    memory_store = MemoryStore()
    reflection = Reflection()

    print("Welcome to Clyde! Let's add a memory and reflect.\n")

    # Step 1: Add a new memory
    user_input = input("Enter a new memory for Clyde: ")
    memory_store.add_memory(user_input)
    print("Memory added.\n")

    # Step 2: Reflect
    reflection.reflect()

    # Step 3: Update self-model example
    update = input("\nDo you want to update Clyde's goal? (y/n): ") 
    if update.lower() == "y":
        new_goal = input("Enter new goal: ")
        self_model.model["goals"].append(new_goal)
        self_model.save()
        print(f"New goal '{new_goal}' added to Clyde's self-model!")

if __name__ == "__main__":
    main()

