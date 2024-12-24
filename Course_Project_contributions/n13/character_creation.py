import mysql.connector

class Character:
    def __init__(self, name, char_class, stats, skills):
        self.name = name
        self.char_class = char_class
        self.stats = stats
        self.skills = skills
        self.inventory = []
        self.level = 1
        self.xp = 0
        self.hp = 100  # Default HP; you can adjust based on class
        self.xp_threshold = 100  # XP required to level up

    def __str__(self):
        return f"Name: {self.name}, Class: {self.char_class}, Stats: {self.stats}, Skills: {self.skills}"

    def gain_xp(self, xp_gained):
        print(f"{self.name} gained {xp_gained} XP!")
        self.xp += xp_gained
        self.check_level_up()

    def check_level_up(self):
        while self.xp >= self.xp_threshold:
            self.xp -= self.xp_threshold
            self.level += 1
            self.hp += 20  # Increase HP on level up; adjust as needed
            print(f"{self.name} leveled up to level {self.level}!")
            print(f"HP increased to {self.hp}.")

def create_character():
    print("Welcome to Character Creation!")
    while True:
        name = input("Enter your character's name: ")
        print("Choose your class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Thief")
        class_choice = input("Enter the number of your choice: ")
        
        if class_choice == '1':
            char_class = "Warrior"
            stats = {"Strength": 10, "Agility": 5, "Intelligence": 3}
            skills = ["Slash", "Block"]
            break
        elif class_choice == '2':
            char_class = "Mage"
            stats = {"Strength": 3, "Agility": 5, "Intelligence": 10}
            skills = ["Fireball", "Teleport"]
            break
        elif class_choice == '3':
            char_class = "Thief"
            stats = {"Strength": 5, "Agility": 10, "Intelligence": 5}
            skills = ["Steal", "Backstab"]
            break
        else:
            print("Invalid choice.")
    
    character = Character(name, char_class, stats, skills)
    print("Character created successfully!")
    print(character)
    
    # Save character to database
    #save_character_to_db(character)
    
    return character

def save_character_to_db(character):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database'
        )
        
        cursor = connection.cursor()
        
        add_character = ("INSERT INTO characters "
                         "(name, char_class, strength, agility, intelligence, skills, level, xp, hp) "
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        
        data_character = (character.name, character.char_class, character.stats['Strength'], 
                          character.stats['Agility'], character.stats['Intelligence'], 
                          ','.join(character.skills), character.level, character.xp, character.hp)
        
        cursor.execute(add_character, data_character)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        print("Character saved to database successfully!")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_character()