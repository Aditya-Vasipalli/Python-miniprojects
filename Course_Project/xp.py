from enemies import enemies
class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.level = 1
        self.xp = 0
        self.hp = 100  # Default HP; you can adjust based on class
        self.xp_threshold = 100  # XP required to level up
        self.stat_points = 0  # Points to assign to stats

    def gain_xp(self, xp_gained):
        print(f"{self.name} gained {xp_gained} XP!")
        self.xp += xp_gained
        self.check_level_up()

    def check_level_up(self):
        while self.xp >= self.xp_threshold:
            self.xp -= self.xp_threshold
            self.level += 1
            self.hp += 20  # Increase HP on level up; adjust as needed
            self.xp_threshold = int(self.xp_threshold * 1.5)  # Increase XP threshold for next level
            if self.level % 10 == 0:
                self.stat_points += 5  # Grant 5 stat points every 10 levels
            print(f"{self.name} leveled up to level {self.level}!")
            print(f"HP increased to {self.hp}.")
            print(f"XP needed for next level: {self.xp_threshold}")
            if self.stat_points > 0:
                print(f"You have {self.stat_points} stat points to assign.")

    def assign_stat_points(self):
        while self.stat_points > 0:
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

class Enemy:
    def __init__(self, name, xp_value):
        self.name = name
        self.xp_value = xp_value

# Example enemies with different XP values


# Example of gameplay
if __name__ == "__main__":
    player = Player("Hero", "Warrior")
    player.stats = {"Strength": 10, "Agility": 5, "Intelligence": 3}  # Example initial stats
    for enemy in enemies:
        print(f"Defeated {enemy.name} and gained {enemy.xp_value} XP!")
        player.gain_xp(enemy.xp_value)
        player.assign_stat_points()