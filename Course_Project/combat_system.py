import random
from character_creation import Character
from enemies import select_enemy, display_enemy_details
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

def player_turn(player, enemy):
    display_bars(player, enemy)
    print("It's Your turn!")
    print("Choose your move:")
    for i, skill in enumerate(player.skills):
        print(f"{i + 1}. {skill}")
    choice = int(input("Enter the number of your choice: ")) - 1
    selected_skill = player.skills[choice]
    skill_cost = player_skills[selected_skill]["cost"]
    
    if "mp" in skill_cost and player.mp < skill_cost["mp"]:
        print("Not enough MP to use this skill.")
        return player_turn(player, enemy)
    if "sp" in skill_cost and player.sp < skill_cost["sp"]:
        print("Not enough SP to use this skill.")
        return player_turn(player, enemy)
    
    if "mp" in skill_cost:
        player.mp -= skill_cost["mp"]
    if "sp" in skill_cost:
        player.sp -= skill_cost["sp"]
    
    player_skills[selected_skill]["effect"](player, enemy)
    print(f"You used {selected_skill}!")
    display_enemy_details(enemy)
    return selected_skill

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
    print(f"The opponent used {enemy_skill}!")
    print(f"Player's health: {player.hp}")

def turnwise(player, enemy):
    while player.hp > 0 and enemy['hp'] > 0:
        selected_skill = player_turn(player, enemy)
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
        player.hp += 200
        player.gain_xp(enemy['xp_value'])  # Gain XP based on enemy's XP value
        return "Victory!"
    else:
        print("You have died!")
        return "Defeat!"