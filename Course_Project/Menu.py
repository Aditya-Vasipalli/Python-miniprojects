from character_creation import create_character

def start_quest(character, main_menu_callback, current_position):
    from quest import start_quest as quest_start
    quest_start(character, main_menu_callback, current_position)

def main_menu(character=None, current_position=(0, 0)):
    while True:
        print("\nMain Menu")
        print("1. Create New Character")
        print("2. Select Existing Character")
        print("3. Continue Game")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            character = create_character()
            current_position = (0, 0)  # Reset position for new character
        elif choice == '2':
            # Placeholder for selecting an existing character
            print("Selecting existing character...")
            # You can implement the logic to load an existing character here
            # For now, we'll just simulate selecting a character
            character = create_character()  # Simulate selecting an existing character
            current_position = (0, 0)  # Reset position for selected character
        elif choice == '3':
            if character:
                start_quest(character, main_menu, current_position)
            else:
                print("No character selected. Please create or select a character first.")
        elif choice == '4':
            print("Exiting the game.")
            exit()
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()