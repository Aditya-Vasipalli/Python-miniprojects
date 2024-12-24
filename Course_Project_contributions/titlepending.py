from Course_Project_contributions.n13.character_creation import create_character
from Course_Project_contributions.n17.combat_system import win_or_loss
from Course_Project_contributions.n15.enemies import select_enemy, display_enemy_details

def main():
    print("Welcome to the RPG Game!")
    character = create_character()
    
    while True:
        print("\nMain Menu")
        print("1. Start Combat")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            enemy_name = input("Enter the name of the enemy to fight: ")
            enemy = select_enemy(enemy_name)
            if enemy:
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