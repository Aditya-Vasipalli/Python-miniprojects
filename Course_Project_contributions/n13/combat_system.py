import random
import time
from character_creation import Character
from enemies import select_enemy, display_enemy_details, regenerate_enemy_mp, regenerate_enemy_sp
from skills import player_skills, enemy_skills

def playerdmgcalc(player):
    ch = random.random()
    if ch <= player.crit_chance:
        playerdmg = player.critdmg
    else:
        playerdmg = round(random.uniform(0, player.stats['Strength']), 2)
    return playerdmg

def oppdmgcalc(enemy):
    oppdmg = round(random.uniform(0, enemy['attack']), 2)
    return oppdmg

def display_bars(character, enemy):
    print(f"Player HP: {character.hp} | MP: {character.mp} | SP: {character.sp}")
    print(f"Enemy HP: {enemy['hp']} | MP: {enemy['mp']} | SP: {enemy['sp']}")

def animate_action(action_text):
    for char in action_text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def player_turn(player, enemy):
    display_bars(player, enemy)
    print("It's Your turn!")
    print("Choose your move:")
    for i, skill in enumerate(player.skills):
        print(f"{i + 1}. {skill} - {player_skills[skill]['description']}")
    print(f"{len(player.skills) + 1}. Use MP Potion")
    print(f"{len(player.skills) + 2}. Use SP Potion")
    
    selected_skill = None  # Initialize selected_skill to None
    
    while True:
        try:
            choice = int(input("Select a skill or action: ")) - 1
            if choice < 0 or choice > len(player.skills) + 1:
                raise ValueError("Invalid choice. Please select a valid option.")
            break
        except ValueError as e:
            print(e)

    if choice == len(player.skills):
        use_mp_potion(player)
    elif choice == len(player.skills) + 1:
        use_sp_potion(player)
    else:
        selected_skill = player.skills[choice]
        skill_cost = player_skills[selected_skill]["cost"]
        if player.mp >= skill_cost.get("mp", 0) and player.sp >= skill_cost.get("sp", 0):
            player.mp -= skill_cost.get("mp", 0)
            player.sp -= skill_cost.get("sp", 0)
            print(f"\nYou used {selected_skill}!")
            player_skills[selected_skill]["effect"](player, enemy)
        else:
            print("\nNot enough MP or SP!")
    return selected_skill

def use_mp_potion(player):
    if "MP Potion" in player.inventory.items:
        player.mp = min(player.max_mp, player.mp + 20)
        player.inventory.items.remove("MP Potion")
        print("\nYou used an MP Potion and restored 20 MP.")
    else:
        print("\nYou don't have any MP Potions!")

def use_sp_potion(player):
    if "SP Potion" in player.inventory.items:
        player.sp = min(player.max_sp, player.sp + 20)
        player.inventory.items.remove("SP Potion")
        print("\nYou used an SP Potion and restored 20 SP.")
    else:
        print("\nYou don't have any SP Potions!")

def enemy_turn(player, enemy):
    display_bars(player, enemy)
    available_skills = [skill for skill in enemy_skills if 
                        ("mp" not in enemy_skills[skill]["cost"] or enemy["mp"] >= enemy_skills[skill]["cost"]["mp"]) and
                        ("sp" not in enemy_skills[skill]["cost"] or enemy["sp"] >= enemy_skills[skill]["cost"]["sp"])]
    if not available_skills:
        print("The opponent has no available skills to use.")
        return
    
    enemy_skill = random.choice(available_skills)
    skill_cost = enemy_skills[enemy_skill]["cost"]
    
    if "mp" in skill_cost:
        enemy["mp"] -= skill_cost["mp"]
    if "sp" in skill_cost:
        enemy["sp"] -= skill_cost["sp"]
    
    enemy_skills[enemy_skill]["effect"](player, enemy)
    animate_action(f"The opponent used {enemy_skill}!")
    regenerate_enemy_mp(enemy)  # Regenerate MP after enemy's turn
    regenerate_enemy_sp(enemy)  # Regenerate SP after enemy's turn

def turnwise(player, enemy):
    while player.hp > 0 and enemy['hp'] > 0:
        selected_skill = player_turn(player, enemy)
        if selected_skill == "run":
            print("You ran away from the battle!")
            return False
        if enemy['hp'] <= 0:
            break
        if selected_skill not in ["Teleport", "Block"]:
            enemy_turn(player, enemy)
    
    if enemy['hp'] <= 0:
        return True
    elif player.hp <= 0:
        return False

def win_or_loss(player, enemy):
    if turnwise(player, enemy):
        regen_health = int(player.max_hp * 0.65)
        player.hp = min(player.max_hp, player.hp + regen_health)
        player.gain_xp(enemy['xp_value'])  # Gain XP based on enemy's XP value
        print(f"You regenerated {regen_health} HP. Current HP: {player.hp}")
        return "Victory!"
    else:
        print("You are on your last legs, about to die")
        return "Defeat!"
