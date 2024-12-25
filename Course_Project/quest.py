import random
from character_creation import create_character
from combat_system import win_or_loss
from enemies import select_enemy, display_enemy_details, adjust_enemy_stats
from Menu import main_menu

def main():
    print("Welcome to the RPG Game!")
    character = create_character()
    
    # Main storyline logic
    start_quest(character, main_menu)

def start_quest(character, main_menu_callback):
    while True:
        print("You are summoned by the king.")
        print("King: Our kingdom is in grave danger. An ancient dragon has awakened and threatens our land.")
        print("King: Brave hero, will you accept the quest to defeat the dragon and save our kingdom?")
        choice = input("Do you accept the quest? (yes/no/menu): ")
        
        if choice.lower() == "yes":
            print("King: Thank you, brave hero. Your journey begins now.")
            traverse_paths(character, main_menu_callback)
        elif choice.lower() == "no":
            print("King: I understand. The kingdom's fate is uncertain without your help.")
            break
        elif choice.lower() == "menu":
            main_menu_callback()
        else:
            print("Invalid choice. Please select again.")

def traverse_paths(character, main_menu_callback):
    # Define the matrix representing the paths
    paths = [
        ["village", "market", "forest"],
        ["hidden_treasure", "wise_old_man", "deeper_forest"],
        ["return_to_king", None, "dragon_lair"]
    ]
    
    descriptions = {
        "village": "A peaceful village with friendly villagers.",
        "market": "A bustling market with various items for sale.",
        "forest": "A dense forest filled with wild creatures.",
        "hidden_treasure": "A hidden treasure rumored to be nearby.",
        "wise_old_man": "A wise old man who offers guidance.",
        "deeper_forest": "A deeper part of the forest with more dangers.",
        "return_to_king": "Return to the king to report your progress.",
        "dragon_lair": "The lair of the ancient dragon."
    }
    
    current_position = (0, 0)  # Start at the village

    while True:
        x, y = current_position
        location = paths[x][y]
        
        if location == "village":
            village_path(character)
        elif location == "market":
            visit_market(character)
        elif location == "forest":
            explore_forest(character)
        elif location == "hidden_treasure":
            find_hidden_treasure(character)
        elif location == "wise_old_man":
            visit_wise_old_man(character)
        elif location == "deeper_forest":
            deeper_forest(character)
        elif location == "return_to_king":
            return_to_king(character)
        elif location == "dragon_lair":
            dragon_lair(character)
        
        print("\nWhat would you like to do next?")
        if y < len(paths[0]) - 1 and paths[x][y + 1] is not None:
            print(f"1. Move Right to {paths[x][y + 1]}: {descriptions[paths[x][y + 1]]}")
        if x < len(paths) - 1 and paths[x + 1][y] is not None:
            print(f"2. Move Down to {paths[x + 1][y]}: {descriptions[paths[x + 1][y]]}")
        if y > 0 and paths[x][y - 1] is not None:
            print(f"3. Move Left to {paths[x][y - 1]}: {descriptions[paths[x][y - 1]]}")
        if x > 0 and paths[x - 1][y] is not None:
            print(f"4. Move Up to {paths[x - 1][y]}: {descriptions[paths[x - 1][y]]}")
        print("5. Exit to Main Menu")
        choice = input("Select an option: ")

        if choice == '1' and y < len(paths[0]) - 1 and paths[x][y + 1] is not None:
            current_position = (x, y + 1)
        elif choice == '2' and x < len(paths) - 1 and paths[x + 1][y] is not None:
            current_position = (x + 1, y)
        elif choice == '3' and y > 0 and paths[x][y - 1] is not None:
            current_position = (x, y - 1)
        elif choice == '4' and x > 0 and paths[x - 1][y] is not None:
            current_position = (x - 1, y)
        elif choice == '5':
            main_menu_callback()
        else:
            print("Invalid choice or move out of bounds. Please select again.")

def village_path(character):
    print("You arrive at the village. The villagers tell you about a hidden treasure and a wise old man in the forest.")
    random_encounter(character)

def visit_market(character):
    print("You find various items for sale in the market.")
    print(f"Merchant: Welcome, traveler! Take a look at my wares. You have {character.money} gold.")
    while True:
        print("\nItems for sale:")
        print("1. Health Potion - 50 gold")
        print("2. Mana Potion - 50 gold")
        print("3. Sword - 100 gold")
        print("4. Shield - 100 gold")
        print("5. Return to the village")
        choice = input("Select an option: ")

        if choice == '1' and character.money >= 50:
            print("You bought a Health Potion.")
            character.money -= 50
            character.inventory.add_item("Health Potion")
        elif choice == '2' and character.money >= 50:
            print("You bought a Mana Potion.")
            character.money -= 50
            character.inventory.add_item("Mana Potion")
        elif choice == '3' and character.money >= 100:
            print("You bought a Sword.")
            character.money -= 100
            character.inventory.add_item("Sword")
        elif choice == '4' and character.money >= 100:
            print("You bought a Shield.")
            character.money -= 100
            character.inventory.add_item("Shield")
        elif choice == '5':
            break
        else:
            print("Invalid choice or insufficient funds. Please select again.")

def explore_forest(character):
    print("You venture into the forest.")
    random_encounter(character)

def find_hidden_treasure(character):
    print("You search for the hidden treasure.")
    print("After a long search, you find a chest hidden in the ground.")
    print("You open the chest and find a powerful weapon.")
    character.inventory.add_item("Powerful Weapon")

def visit_wise_old_man(character):
    print("Wise Old Man: Greetings, traveler. I have been expecting you.")
    print("Wise Old Man: I can offer you guidance and a powerful artifact to aid you in your quest.")
    print("You receive a magical amulet from the wise old man.")
    character.inventory.add_item("Magical Amulet")
    print("Wise Old Man: I will also teach you a new skill.")
    new_skill = random.choice(["Fireball", "Heal", "Lightning Strike"])
    character.skills.append(new_skill)
    print(f"You have learned a new skill: {new_skill}")

def deeper_forest(character):
    print("You follow the path deeper into the forest.")
    random_encounter(character)

def return_to_king(character):
    print("You return to the king and report your progress.")

def dragon_lair(character):
    print("You enter the dragon's lair and prepare for the final battle.")
    enemy_name = "Dragon"
    enemy = select_enemy(enemy_name)
    if enemy:
        level = 5
        adjust_enemy_stats(enemy, level)
        display_enemy_details(enemy)
        result = win_or_loss(character, enemy)
        print(result)
        character.check_level_up()  # Check for level up immediately after the battle
    else:
        print("Enemy not found.")

def random_encounter(character):
    enemies = ["Goblin", "Orc", "Wolf"]
    enemy_name = random.choice(enemies)
    enemy = select_enemy(enemy_name)
    if enemy:
        level = random.randint(1, 3)
        adjust_enemy_stats(enemy, level)
        display_enemy_details(enemy)
        result = win_or_loss(character, enemy)
        print(result)
        character.money += random.randint(10, 50)  # Reward money for defeating the enemy
        print(f"You have earned some gold. Current gold: {character.money}")
        character.check_level_up()  # Check for level up immediately after the battle
    else:
        print("Enemy not found.")

if __name__ == "__main__":
    main()