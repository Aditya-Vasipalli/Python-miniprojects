class Armor:
    def __init__(self, name, defense, magic_resistance, description):
        self.name = name
        self.defense = defense
        self.magic_resistance = magic_resistance
        self.description = description

    def __str__(self):
        return f"{self.name}: Defense={self.defense}, Magic Resistance={self.magic_resistance}, Description={self.description}"

class Weapon:
    def __init__(self, name, attack, magic_power, description):
        self.name = name
        self.attack = attack
        self.magic_power = magic_power
        self.description = description

    def __str__(self):
        return f"{self.name}: Attack={self.attack}, Magic Power={self.magic_power}, Description={self.description}"

# List of armor options
armor_options = [
    Armor("Leather Armor", 5, 2, "Basic armor made of leather."),
    Armor("Chainmail Armor", 10, 5, "Sturdy armor made of interlocking metal rings."),
    Armor("Plate Armor", 20, 10, "Heavy armor made of metal plates."),
    Armor("Mage Robe", 3, 15, "Light robe that offers high magic resistance."),
    Armor("Dragon Scale Armor", 25, 20, "Legendary armor made from dragon scales.")
]

# List of weapon options
weapon_options = [
    Weapon("Iron Sword", 10, 0, "A basic iron sword."),
    Weapon("Steel Sword", 15, 0, "A sturdy steel sword."),
    Weapon("Magic Staff", 5, 15, "A staff imbued with magical power."),
    Weapon("Battle Axe", 20, 0, "A heavy axe designed for battle."),
    Weapon("Dragon Slayer", 30, 10, "A legendary sword designed to slay dragons.")
]

# Function to display armor options
def display_armor_options():
    print("Available Armor:")
    for armor in armor_options:
        print(armor)

# Function to display weapon options
def display_weapon_options():
    print("Available Weapons:")
    for weapon in weapon_options:
        print(weapon)

if __name__ == "__main__":
    display_armor_options()
    display_weapon_options()