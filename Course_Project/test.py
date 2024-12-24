from character_creation import create_character
from combat_system import win_or_loss, display_bars
from enemies import select_enemy, display_enemy_details, adjust_enemy_stats

def main():
    print("Welcome to the RPG Game!")
    character = create_character()
    
    while True:
        print("\nMain Menu")
        print("1. Start Combat")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            enemy_name = 'hydra'
            enemy = select_enemy(enemy_name)
            if enemy:
                level = 1
                adjust_enemy_stats(enemy, level)
                enemy["mp"] = 50  # Default MP for enemy; adjust as needed
                enemy["sp"] = 50  # Default SP for enemy; adjust as needed
                display_enemy_details(enemy)
                result = win_or_loss(character, enemy)
                print(result)
            else:
                print("Enemy not found.")
        elif choice == '2':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()