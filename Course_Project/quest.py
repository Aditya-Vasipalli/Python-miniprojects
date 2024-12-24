from character_creation import create_character
from combat_system import win_or_loss
from enemies import select_enemy, display_enemy_details, adjust_enemy_stats

def main():
    print("Welcome to the RPG Game!")
    character = create_character()
    
    # Main storyline logic
    start_quest(character)

def start_quest(character):
    print("You are summoned by the king.")
    print("King: Our kingdom is in grave danger. An ancient dragon has awakened and threatens our land.")
    print("King: Brave hero, will you accept the quest to defeat the dragon and save our kingdom?")
    choice = input("Do you accept the quest? (yes/no): ")
    
    if choice.lower() == "yes":
        print("King: Thank you, brave hero. Your journey begins now.")
        first_challenge(character)
    elif choice.lower() == "no":
        print("King: I understand. The kingdom's fate is uncertain without your help.")
        print("Game Over")
    else:
        print("Invalid choice. Please choose again.")
        start_quest(character)

def first_challenge(character):
    print("You must navigate through the haunted forest.")
    choice = input("Do you want to explore deeper or return to the village? (explore/return): ")
    
    if choice.lower() == "explore":
        explore_forest(character)
    elif choice.lower() == "return":
        village_path(character)
    else:
        print("Invalid choice. Please choose again.")
        first_challenge(character)

def explore_forest(character):
    print("You encounter a wild beast!")
    enemy = select_enemy("Goblin")
    adjust_enemy_stats(enemy, character.level)
    display_enemy_details(enemy)
    result = win_or_loss(character, enemy)
    print(result)
    if result == "Victory!":
        print("You have defeated the beast and found a hidden path to the village.")
        village_path(character)
    else:
        print("You have been defeated. Game Over.")

def village_path(character):
    print("You arrive at the peaceful village.")
    choice = input("Do you want to talk to the villagers or visit the market? (talk/market): ")
    
    if choice.lower() == "talk":
        talk_villagers(character)
    elif choice.lower() == "market":
        visit_market(character)
    else:
        print("Invalid choice. Please choose again.")
        village_path(character)

def talk_villagers(character):
    print("The villagers tell you about a hidden treasure that can help you in your quest.")
    # Add more branching paths or challenges here

def visit_market(character):
    print("You find various items for sale.")
    # Add more branching paths or challenges here

if __name__ == "__main__":
    main()