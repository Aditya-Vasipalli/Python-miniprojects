import random

# Predefined list of 20 enemies with their characteristics
enemies = [
    {
        "name": "Goblin",
        "health": 50,
        "attack": 5,
        "defense": 2,
        "magical_resistance": 10,
        "special_ability": "Poisoned Dagger",
        "xp_value": 50,
        "level": 1
    },
    {
        "name": "Orc",
        "health": 100,
        "attack": 10,
        "defense": 5,
        "magical_resistance": 20,
        "special_ability": "Berserk Rage",
        "xp_value": 100,
        "level": 1
    },
    {
        "name": "Dragon",
        "health": 300,
        "attack": 25,
        "defense": 15,
        "magical_resistance": 50,
        "special_ability": "Fire Breath",
        "xp_value": 500,
        "level": 1
    },
    {
        "name": "Zombie",
        "health": 40,
        "attack": 4,
        "defense": 2,
        "magical_resistance": 5,
        "special_ability": "Infectious Bite",
        "xp_value": 40,
        "level": 1
    },
    {
        "name": "Werewolf",
        "health": 80,
        "attack": 15,
        "defense": 8,
        "magical_resistance": 7,
        "special_ability": "Frenzy",
        "xp_value": 80,
        "level": 1
    },
    {
        "name": "Giant",
        "health": 200,
        "attack": 25,
        "defense": 18,
        "magical_resistance": 25,
        "special_ability": "Earthquake Stomp",
        "xp_value": 200,
        "level": 1
    },
    {
        "name": "Griffin",
        "health": 130,
        "attack": 18,
        "defense": 10,
        "magical_resistance": 30,
        "special_ability": "Sky Dive",
        "xp_value": 130,
        "level": 1
    },
    {
        "name": "Vampire",
        "health": 120,
        "attack": 20,
        "defense": 10,
        "magical_resistance": 15,
        "special_ability": "Life Drain",
        "xp_value": 120,
        "level": 1
    },
    {
        "name": "Troll",
        "health": 150,
        "attack": 20,
        "defense": 12,
        "magical_resistance": 10,
        "special_ability": "Regeneration",
        "xp_value": 150,
        "level": 1
    },
    {
        "name": "Witch",
        "health": 70,
        "attack": 15,
        "defense": 5,
        "magical_resistance": 40,
        "special_ability": "Curse",
        "xp_value": 70,
        "level": 1
    },
    {
        "name": "Skeleton",
        "health": 30,
        "attack": 5,
        "defense": 3,
        "magical_resistance": 5,
        "special_ability": "Bone Shield",
        "xp_value": 30,
        "level": 1
    },
    {
        "name": "Demon",
        "health": 180,
        "attack": 22,
        "defense": 14,
        "magical_resistance": 35,
        "special_ability": "Hellfire",
        "xp_value": 180,
        "level": 1
    },
    {
        "name": "Ghost",
        "health": 50,
        "attack": 10,
        "defense": 5,
        "magical_resistance": 50,
        "special_ability": "Possession",
        "xp_value": 50,
        "level": 1
    },
    {
        "name": "Golem",
        "health": 250,
        "attack": 20,
        "defense": 20,
        "magical_resistance": 10,
        "special_ability": "Stone Skin",
        "xp_value": 250,
        "level": 1
    },
    {
        "name": "Harpy",
        "health": 60,
        "attack": 12,
        "defense": 6,
        "magical_resistance": 15,
        "special_ability": "Sonic Screech",
        "xp_value": 60,
        "level": 1
    },
    {
        "name": "Lich",
        "health": 100,
        "attack": 18,
        "defense": 8,
        "magical_resistance": 45,
        "special_ability": "Necromancy",
        "xp_value": 100,
        "level": 1
    },
    {
        "name": "Minotaur",
        "health": 140,
        "attack": 22,
        "defense": 12,
        "magical_resistance": 20,
        "special_ability": "Charge",
        "xp_value": 140,
        "level": 1
    },
    {
        "name": "Mummy",
        "health": 80,
        "attack": 10,
        "defense": 8,
        "magical_resistance": 25,
        "special_ability": "Curse of the Pharaoh",
        "xp_value": 80,
        "level": 1
    },
    {
        "name": "Phoenix",
        "health": 100,
        "attack": 20,
        "defense": 10,
        "magical_resistance": 50,
        "special_ability": "Rebirth",
        "xp_value": 100,
        "level": 1
    },
    {
        "name": "Hydra",
        "health": 200,
        "attack": 25,
        "defense": 15,
        "magical_resistance": 30,
        "special_ability": "Regenerate Heads",
        "xp_value": 200,
        "level": 1
    }
]

# Function to select an enemy
def select_enemy(enemy_name):
    for enemy in enemies:
        if enemy["name"].lower() == enemy_name.lower():
            return enemy
    return None

# Function to display enemy details
def display_enemy_details(enemy):
    if enemy:
        print(f"Selected enemy: {enemy['name']}")
        print(f"Health: {enemy['health']}")
        print(f"Attack: {enemy['attack']}")
        print(f"Defense: {enemy['defense']}")
        print(f"Magical Resistance: {enemy['magical_resistance']}")
        print(f"Special Ability: {enemy['special_ability']}")
        print(f"XP Value: {enemy['xp_value']}")
        print(f"Level: {enemy['level']}")
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
    multiplier = 1 + (level - 1) * 0.007  # Example multiplier: 10% increase per level
    enemy["health"] = int(enemy["health"] * multiplier)
    enemy["attack"] = int(enemy["attack"] * multiplier)
    enemy["defense"] = int(enemy["defense"] * multiplier)
    enemy["magical_resistance"] = int(enemy["magical_resistance"] * multiplier)
    enemy["xp_value"] = int(enemy["xp_value"] * multiplier)
    enemy["level"] = level

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