from character_creation import create_character

def start_quest(character, main_menu_callback, current_position):
    from quest import start_quest as quest_start
    quest_start(character, main_menu_callback, current_position)

def main_menu(character=None, current_position=(0, 0)):
    while True:
        print("\nMain Menu")
        print("1. Create New Character")
        print("2. Select Existing Character")
        print("3. Start Game")
        print("4. Continue Game")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            character = create_character()
            current_position = (0, 0)  # Reset position for new character
        elif choice == '2':
            # Logic to select an existing character
            pass
        elif choice == '3':
            if character is None:
                print("Please create or select a character first.")
            else:
                start_game(character, current_position)
        elif choice == '4':
            if character is None:
                print("Please create or select a character first.")
            else:
                start_quest(character, main_menu, current_position)
        elif choice == '5':
            exit()
        else:
            print("Invalid choice. Please select again.")

def start_game(character, current_position):
    talk_to_king(character)
    start_quest(character, main_menu, current_position)

def talk_to_king(character):
    print("King: Brave warrior, our kingdom is in grave danger.")
    print("King: A fearsome dragon is terrorizing our lands.")
    print("King: You must embark on a quest to slay the dragon and save our people.")
    input("Press Enter to begin your quest...")