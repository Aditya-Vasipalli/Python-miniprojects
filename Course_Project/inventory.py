class Inventory:
    def __init__(self):
        self.items = []
        self.equipped_items = {
            "weapon": None,
            "armor": None
        }

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} has been added to your inventory.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} has been removed from your inventory.")
        else:
            print(f"{item} is not in your inventory.")

    def equip_item(self, index):
        if 0 <= index < len(self.items):
            item = self.items[index]
            if "Weapon" in item:
                self.equipped_items["weapon"] = item
            elif "Armor" in item:
                self.equipped_items["armor"] = item
            print(f"You have equipped {item}.")
        else:
            print("Invalid index. Please select a valid item.")

    def use_item(self, index, character):
        if 0 <= index < len(self.items):
            item = self.items[index]
            if item == "Health Potion":
                character.hp = min(100, character.hp + 50)
                print(f"Your health is restored. Current HP: {character.hp}")
            elif item == "Mana Potion":
                character.mp = min(50, character.mp + 30)
                print(f"Your mana is restored. Current MP: {character.mp}")
            self.remove_item(item)
        else:
            print("Invalid index. Please select a valid item.")

    def show_inventory(self):
        print("Inventory:")
        for i, item in enumerate(self.items):
            print(f"{i}. {item}")
        print("Equipped Items:")
        for slot, item in self.equipped_items.items():
            print(f"{slot.capitalize()}: {item if item else 'None'}")