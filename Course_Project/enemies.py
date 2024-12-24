import random

# Predefined list of 20 enemies with their characteristics
enemies = [
    {
        "name": "Goblin",
        "hp": 50,
        "attack": 5,
        "defense": 2,
        "magical_resistance": 10,
        "special_ability": "Poisoned Dagger",
        "xp_value": 50,
        "level": 1,
        "mp": 20,  # Default MP for enemy
        "sp": 30   # Default SP for enemy
    },
    {
        "name": "Orc",
        "hp": 100,
        "attack": 10,
        "defense": 5,
        "magical_resistance": 20,
        "special_ability": "Berserk Rage",
        "xp_value": 100,
        "level": 1,
        "mp": 30,  # Default MP for enemy
        "sp": 40   # Default SP for enemy
    },
    {
        "name": "Dragon",
        "hp": 300,
        "attack": 25,
        "defense": 15,
        "magical_resistance": 50,
        "special_ability": "Fire Breath",
        "xp_value": 500,
        "level": 1,
        "mp": 50,  # Default MP for enemy
        "sp": 60   # Default SP for enemy
    },
    {
        "name": "Zombie",
        "hp": 40,
        "attack": 4,
        "defense": 2,
        "magical_resistance": 5,
        "special_ability": "Infectious Bite",
        "xp_value": 40,
        "level": 1,
        "mp": 10,  # Default MP for enemy
        "sp": 20   # Default SP for enemy
    },
    {
        "name": "Werewolf",
        "hp": 80,
        "attack": 15,
        "defense": 8,
        "magical_resistance": 7,
        "special_ability": "Frenzy",
        "xp_value": 80,
        "level": 1,
        "mp": 25,  # Default MP for enemy
        "sp": 35   # Default SP for enemy
    },
    {
        "name": "Giant",
        "hp": 200,
        "attack": 25,
        "defense": 18,
        "magical_resistance": 25,
        "special_ability": "Earthquake Stomp",
        "xp_value": 200,
        "level": 1,
        "mp": 40,  # Default MP for enemy
        "sp": 50   # Default SP for enemy
    },
    {
        "name": "Griffin",
        "hp": 130,
        "attack": 18,
        "defense": 10,
        "magical_resistance": 30,
        "special_ability": "Sky Dive",
        "xp_value": 130,
        "level": 1,
        "mp": 35,  # Default MP for enemy
        "sp": 45   # Default SP for enemy
    },
    {
        "name": "Vampire",
        "hp": 120,
        "attack": 20,
        "defense": 10,
        "magical_resistance": 15,
        "special_ability": "Life Drain",
        "xp_value": 120,
        "level": 1,
        "mp": 30,  # Default MP for enemy
        "sp": 40   # Default SP for enemy
    },
    {
        "name": "Troll",
        "hp": 150,
        "attack": 20,
        "defense": 12,
        "magical_resistance": 10,
        "special_ability": "Regeneration",
        "xp_value": 150,
        "level": 1,
        "mp": 35,  # Default MP for enemy
        "sp": 45   # Default SP for enemy
    },
    {
        "name": "Witch",
        "hp": 70,
        "attack": 15,
        "defense": 5,
        "magical_resistance": 40,
        "special_ability": "Curse",
        "xp_value": 70,
        "level": 1,
        "mp": 25,  # Default MP for enemy
        "sp": 35   # Default SP for enemy
    },
    {
        "name": "Skeleton",
        "hp": 30,
        "attack": 5,
        "defense": 3,
        "magical_resistance": 5,
        "special_ability": "Bone Shield",
        "xp_value": 30,
        "level": 1,
        "mp": 10,  # Default MP for enemy
        "sp": 20   # Default SP for enemy
    },
    {
        "name": "Demon",
        "hp": 180,
        "attack": 22,
        "defense": 14,
        "magical_resistance": 35,
        "special_ability": "Hellfire",
        "xp_value": 180,
        "level": 1,
        "mp": 40,  # Default MP for enemy
        "sp": 50   # Default SP for enemy
    },
    {
        "name": "Ghost",
        "hp": 50,
        "attack": 10,
        "defense": 5,
        "magical_resistance": 50,
        "special_ability": "Possession",
        "xp_value": 50,
        "level": 1,
        "mp": 20,  # Default MP for enemy
        "sp": 30   # Default SP for enemy
    },
    {
        "name": "Golem",
        "hp": 250,
        "attack": 20,
        "defense": 20,
        "magical_resistance": 10,
        "special_ability": "Stone Skin",
        "xp_value": 250,
        "level": 1,
        "mp": 45,  # Default MP for enemy
        "sp": 55   # Default SP for enemy
    },
    {
        "name": "Harpy",
        "hp": 60,
        "attack": 12,
        "defense": 6,
        "magical_resistance": 15,
        "special_ability": "Sonic Screech",
        "xp_value": 60,
        "level": 1,
        "mp": 20,  # Default MP for enemy
        "sp": 30   # Default SP for enemy
    },
    {
        "name": "Lich",
        "hp": 100,
        "attack": 18,
        "defense": 8,
        "magical_resistance": 45,
        "special_ability": "Necromancy",
        "xp_value": 100,
        "level": 1,
        "mp": 30,  # Default MP for enemy
        "sp": 40   # Default SP for enemy
    },
    {
        "name": "Minotaur",
        "hp": 140,
        "attack": 22,
        "defense": 12,
        "magical_resistance": 20,
        "special_ability": "Charge",
        "xp_value": 140,
        "level": 1,
        "mp": 35,  # Default MP for enemy
        "sp": 45   # Default SP for enemy
    },
    {
        "name": "Mummy",
        "hp": 80,
        "attack": 10,
        "defense": 8,
        "magical_resistance": 25,
        "special_ability": "Curse of the Pharaoh",
        "xp_value": 80,
        "level": 1,
        "mp": 25,  # Default MP for enemy
        "sp": 35   # Default SP for enemy
    },
    {
        "name": "Phoenix",
        "hp": 100,
        "attack": 20,
        "defense": 10,
        "magical_resistance": 50,
        "special_ability": "Rebirth",
        "xp_value": 100,
        "level": 1,
        "mp": 30,  # Default MP for enemy
        "sp": 40   # Default SP for enemy
    },
    {
        "name": "Hydra",
        "hp": 200,
        "attack": 25,
        "defense": 15,
        "magical_resistance": 30,
        "special_ability": "Regenerate Heads",
        "xp_value": 200,
        "level": 1,
        "mp": 40,  # Default MP for enemy
        "sp": 50   # Default SP for enemy
    }
]

# Function to select an enemy
def select_enemy(enemy_name):
    for enemy in enemies:
        if enemy["name"].lower() == enemy_name.lower():
            return enemy.copy()  # Return a copy to avoid modifying the original

# Function to display enemy details
def display_enemy_details(enemy):
    if enemy:
        print(f"Selected enemy: {enemy['name']}")
        print(f"Health: {enemy['hp']}")
        print(f"Attack: {enemy['attack']}")
        print(f"Defense: {enemy['defense']}")
        print(f"Magical Resistance: {enemy['magical_resistance']}")
        print(f"Special Ability: {enemy['special_ability']}")
        print(f"XP Value: {enemy['xp_value']}")
        print(f"Level: {enemy['level']}")
        print(f"MP: {enemy['mp']}")
        print(f"SP: {enemy['sp']}")
    else:
        print("Enemy not found.")

# Function to get story relevance of an enemy
def get_enemy_story(enemy_name):
    story_relevance = {
        "Goblin": "A common creature found in the dark corners of the forest.",
        "Orc": "A fierce warrior guarding the entrance to the ancient cave.",
        "Dragon": "The legendary dragon that holds the key to the kingdom's treasure.",
        "Zombie": "A reanimated corpse that roams the graveyard.",
        "Werewolf": "A cursed human that transforms under the full moon.",
        "Giant": "A massive being that dwells in the mountains.",
        "Griffin": "A majestic creature that soars above the clouds.",
        "Vampire": "A bloodthirsty creature that preys on the living.",
        "Troll": "A monstrous being that regenerates its wounds.",
        "Witch": "A malevolent sorceress who casts dark spells.",
        "Skeleton": "An undead warrior animated by dark magic.",
        "Demon": "A fiendish entity from the depths of hell.",
        "Ghost": "A restless spirit that haunts the living.",
        "Golem": "A magical construct made of stone.",
        "Harpy": "A winged creature with a piercing scream.",
        "Lich": "A powerful undead sorcerer.",
        "Minotaur": "A fearsome beast with the body of a man and the head of a bull.",
        "Mummy": "An ancient undead wrapped in cursed bandages.",
        "Phoenix": "A mythical bird that rises from its ashes.",
        "Hydra": "A multi-headed serpent that regenerates its heads."
    }
    return story_relevance.get(enemy_name, "No story available for this enemy.")

# Function to adjust enemy stats based on level
def adjust_enemy_stats(enemy, level):
    multiplier = 1 + (level - 1) * 0.1  # Example multiplier: 10% increase per level
    enemy["hp"] = int(enemy["hp"] * multiplier)
    enemy["attack"] = int(enemy["attack"] * multiplier)
    enemy["defense"] = int(enemy["defense"] * multiplier)
    enemy["magical_resistance"] = int(enemy["magical_resistance"] * multiplier)
    enemy["xp_value"] = int(enemy["xp_value"] * multiplier)
    enemy["level"] = level
    enemy["mp"] = int(enemy["mp"] * multiplier)  # Adjust MP based on level
    enemy["sp"] = int(enemy["sp"] * multiplier)  # Adjust SP based on level

# Function to regenerate MP for an enemy
def regenerate_enemy_mp(enemy):
    regen_amount = 5  # Example regeneration amount
    max_mp = 10 + (enemy["magical_resistance"] * 5)  # Example calculation for max MP
    enemy["mp"] = min(max_mp, enemy["mp"] + regen_amount)
    print(f"{enemy['name']} regenerated {regen_amount} MP. Current MP: {enemy['mp']}")

# Function to regenerate SP for an enemy
def regenerate_enemy_sp(enemy):
    regen_amount = 5  # Example regeneration amount
    max_sp = 10 + (enemy["defense"] * 5)  # Example calculation for max SP
    enemy["sp"] = min(max_sp, enemy["sp"] + regen_amount)
    print(f"{enemy['name']} regenerated {regen_amount} SP. Current SP: {enemy['sp']}")

# Example usage
if __name__ == "__main__":
    enemy_name = input("Enter the name of the enemy to select: ")
    selected_enemy = select_enemy(enemy_name)
    if selected_enemy:
        level = int(input("Enter the level of the enemy: "))
        adjust_enemy_stats(selected_enemy, level)
        display_enemy_details(selected_enemy)
        story = get_enemy_story(selected_enemy["name"])
        print(f"Story: {story}")