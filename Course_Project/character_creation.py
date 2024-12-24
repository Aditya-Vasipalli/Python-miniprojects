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
        self.mp = self.calculate_mp()  # Calculate MP based on Intelligence
        self.sp = self.calculate_sp()  # Calculate SP based on Agility
        self.xp_threshold = 100  # XP required to level up
        self.stat_points = 0  # Points to assign to stats
        self.crit_chance = 0.1  # Default critical hit chance
        self.critdmg = 2 * self.stats['Strength']  # Default critical damage

    def calculate_mp(self):
        base_mp = 10
        return base_mp + (self.stats['Intelligence'] * 2)  # Example multiplier needs to be tweaked

    def calculate_sp(self):
        base_sp = 10
        return base_sp + (self.stats['Agility'] * 5)  # Example multiplier needs to be tweaked

    def regenerate_mp(self):
        regen_amount = 5  # Example regeneration amount
        self.mp = min(self.calculate_mp(), self.mp + regen_amount)
        print(f"{self.name} regenerated {regen_amount} MP. Current MP: {self.mp}")

    def regenerate_sp(self):
        regen_amount = 5  # Example regeneration amount
        self.sp = min(self.calculate_sp(), self.sp + regen_amount)
        print(f"{self.name} regenerated {regen_amount} SP. Current SP: {self.sp}")

    def __str__(self):
        return f"Name: {self.name}, Class: {self.char_class}, Stats: {self.stats}, Skills: {self.skills}, HP: {self.hp}, MP: {self.mp}, SP: {self.sp}"

    def gain_xp(self, xp_gained):
        print(f"{self.name} gained {xp_gained} XP!")
        self.xp += xp_gained
        self.check_level_up()

    def check_level_up(self):
        while self.xp >= self.xp_threshold:
            self.xp -= self.xp_threshold
            self.level += 1
            self.hp += 20  # Increase HP by 20 on level up; adjust as needed
            self.mp = self.calculate_mp()  # Recalculate MP on level up
            self.sp = self.calculate_sp()  # Recalculate SP on level up
            self.xp_threshold = int(self.xp_threshold * 1.5)  # Increase XP threshold for next level
            self.stat_points += 1  # Grant 1 stat point per level
            if self.level % 5 == 0:
                self.stat_points += 5  # Grant 5 additional stat points every 5 levels
            print(f"{self.name} leveled up to level {self.level}!")
            print(f"HP increased to {self.hp}. MP increased to {self.mp}. SP increased to {self.sp}.")
            print(f"XP needed for next level: {self.xp_threshold}")
            print(f"You have {self.stat_points} stat points to assign.")
            self.assign_stat_points()

    def assign_stat_points(self):
        while self.stat_points > 0:
            print(f"You have {self.stat_points} stat points to assign.")
            print("1. Strength")
            print("2. Agility")
            print("3. Intelligence")
            choice = input("Choose a stat to increase: ")
            if choice == '1':
                self.stats['Strength'] += 1
            elif choice == '2':
                self.stats['Agility'] += 1
            elif choice == '3':
                self.stats['Intelligence'] += 1
            else:
                print("Invalid choice.")
                continue
            self.stat_points -= 1
            print(f"Assigned 1 point to {choice}. Remaining stat points: {self.stat_points}")
            self.critdmg = 2 * self.stats['Strength']  # Update critical damage based on new Strength
            self.mp = self.calculate_mp()  # Recalculate MP after assigning stat points
            self.sp = self.calculate_sp()  # Recalculate SP after assigning stat points

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
    
    return character

def save_character_to_db(character):
    # Placeholder function to save character to a database
    pass

if __name__ == "__main__":
    create_character()