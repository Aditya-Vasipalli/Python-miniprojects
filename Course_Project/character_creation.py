import mysql.connector
from armor_weapon import armor_options, weapon_options

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
        self.max_hp = self.hp
        self.mp = self.calculate_mp()  # Calculate MP based on Intelligence
        self.sp = self.calculate_sp()  # Calculate SP based on Agility
        self.max_mp = self.mp
        self.max_sp = self.sp
        self.xp_threshold = 100  # XP required to level up
        self.stat_points = 0  # Points to assign to stats
        self.crit_chance = 0.1  # Default critical hit chance
        self.critdmg = 2 * self.stats['Strength']  # Default critical damage
        self.equipped_weapon = None
        self.equipped_armor = None
        self.lingering_effects = []

    def calculate_mp(self):
        base_mp = 10
        return base_mp + (self.stats['Intelligence'] * 5)  # Example multiplier

    def calculate_sp(self):
        base_sp = 10
        return base_sp + (self.stats['Agility'] * 5)  # Example multiplier

    def regenerate_mp(self):
        regen_amount = 5  # Example regeneration amount
        if self.mp < self.max_mp:
            self.mp = min(self.max_mp, self.mp + regen_amount)
            if self.mp < self.max_mp:
                print(f"{self.name} regenerated {regen_amount} MP. Current MP: {self.mp}")

    def regenerate_sp(self):
        regen_amount = 5  # Example regeneration amount
        if self.sp < self.max_sp:
            self.sp = min(self.max_sp, self.sp + regen_amount)
            if self.sp < self.max_sp:
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
            self.max_hp = self.hp
            self.mp = self.calculate_mp()  # Recalculate MP on level up
            self.max_mp = self.mp
            self.sp = self.calculate_sp()  # Recalculate SP on level up
            self.max_sp = self.sp
            self.xp_threshold = int(self.xp_threshold * 1.5)  # Increase XP threshold for next level
            self.stat_points += 1  # Grant 1 stat point per level
            if self.level % 5 == 0:
                self.stat_points += 5  # Grant 5 additional stat points every 5 levels
                self.learn_new_move()
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

    def learn_new_move(self):
        available_moves = ["Thunder Strike", "Heal", "Ice Blast", "Shadow Step"]
        print("You have the opportunity to learn a new move!")
        for i, move in enumerate(available_moves):
            print(f"{i + 1}. {move}")
        choice = int(input("Enter the number of the move you want to learn: ")) - 1
        new_move = available_moves[choice]
        if len(self.skills) >= 4:
            print("You already have 4 moves. Choose a move to forget:")
            for i, skill in enumerate(self.skills):
                print(f"{i + 1}. {skill}")
            forget_choice = int(input("Enter the number of the move you want to forget: ")) - 1
            self.skills[forget_choice] = new_move
        else:
            self.skills.append(new_move)
        print(f"You learned {new_move}!")

    def equip_weapon(self):
        print("Choose a weapon to equip:")
        for i, weapon in enumerate(weapon_options):
            print(f"{i + 1}. {weapon}")
        choice = int(input("Enter the number of your choice: ")) - 1
        self.equipped_weapon = weapon_options[choice]
        print(f"You equipped {self.equipped_weapon.name}!")

    def equip_armor(self):
        print("Choose an armor to equip:")
        for i, armor in enumerate(armor_options):
            print(f"{i + 1}. {armor}")
        choice = int(input("Enter the number of your choice: ")) - 1
        self.equipped_armor = armor_options[choice]
        print(f"You equipped {self.equipped_armor.name}!")

    def apply_lingering_effects(self):
        for effect in self.lingering_effects:
            effect.apply(self)

    def remove_lingering_effects(self):
        self.lingering_effects = []
        print(f"{self.name} removed all lingering effects!")

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
            skills = ["Slash", "Block", "Cure"]
            break
        elif class_choice == '2':
            char_class = "Mage"
            stats = {"Strength": 3, "Agility": 5, "Intelligence": 10}
            skills = ["Fireball", "Teleport", "Cure"]
            break
        elif class_choice == '3':
            char_class = "Thief"
            stats = {"Strength": 5, "Agility": 10, "Intelligence": 5}
            skills = ["Steal", "Backstab", "Cure"]
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