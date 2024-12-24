from character_creation import create_character
from combat_system import win_or_loss, display_bars
from enemies import select_enemy, display_enemy_details, adjust_enemy_stats, enemy_skills, enemies

def main():
    print("Welcome to the RPG Game!")
    character = create_character()
    
    while True:
        print("\nMain Menu")
        print("1. Start Combat")
        print("2. Equip Weapon")
        print("3. Equip Armor")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            enemy_name = input("Enter the name of the enemy to fight: ")
            enemy = select_enemy(enemy_name)
            if enemy:
                level = int(input("Enter the level of the enemy: "))
                adjust_enemy_stats(enemy, level)
                display_enemy_details(enemy)
                print("Enemy Skills:")
                for skill in enemy_skills:
                    print(f"- {skill}: {enemy_skills[skill]['description']}")
                result = win_or_loss(character, enemy)
                print(result)
                character.check_level_up()  # Check for level up immediately after the battle
            else:
                print("Enemy not found.")
        elif choice == '2':
            character.equip_weapon()
        elif choice == '3':
            character.equip_armor()
        elif choice == '4':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please select again.")
    
       
print("Viewing all enemies:")
def view_enemies():
    for enemy in enemies:
        if enemy:
            level = 1
            adjust_enemy_stats(enemy, level)
            display_enemy_details(enemy)
            print("Enemy Skills:")
            for skill in enemy_skills:
                print(f"- {skill}: {enemy_skills[skill]['description']}")


if __name__ == "__main__":
    main()

