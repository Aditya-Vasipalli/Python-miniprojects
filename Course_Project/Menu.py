from character_creation import create_character

def start_quest(character, main_menu_callback):
    from quest import start_quest as quest_start
    quest_start(character, main_menu_callback)

def main_menu(character=None):
    while True:
        print("\nMain Menu")
        print("1. Create New Character")
        print("2. Select Existing Character")
        print("3. Start Game")
        print("4. Equip Items")
        print("5. Use Potions")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            character = create_character()
        elif choice == '2':
            # Placeholder for selecting an existing character
            print("Selecting existing character...")
            # You can implement the logic to load an existing character here
            # For now, we'll just simulate selecting a character
            character = create_character()  # Simulate selecting an existing character
        elif choice == '3':
            if character:
                start_quest(character, main_menu)
            else:
                print("No character selected. Please create or select a character first.")
        elif choice == '4':
            if character:
                character.inventory.show_inventory()
                try:
                    index = int(input("Enter the index of the item you want to equip: "))
                    character.inventory.equip_item(index)
                except ValueError:
                    print("Invalid input. Please enter a valid index.")
            else:
                print("No character selected. Please create or select a character first.")
        elif choice == '5':
            if character:
                character.inventory.show_inventory()
                try:
                    index = int(input("Enter the index of the potion you want to use: "))
                    character.inventory.use_item(index, character)
                except ValueError:
                    print("Invalid input. Please enter a valid index.")
            else:
                print("No character selected. Please create or select a character first.")
        elif choice == '6':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()