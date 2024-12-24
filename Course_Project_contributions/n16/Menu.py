from Course_Project_contributions.n13.character_creation import create_character


def main_menu():
    character = None
    while True:
        print("\nMain Menu")
        print("1. Create New Character")
        print("2. Select Existing Character")
        print("3. Start Game")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            character = create_character()
        elif choice == '2':
            # Placeholder for selecting an existing character
            print("Selecting existing character...")
            # You can implement the logic to load an existing character here
        elif choice == '3':
            if character:
                # Placeholder for starting the game
                print("Starting game...")
                # You can call the main game function here
            else:
                print("Please create or select a character first.")
        elif choice == '4':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()