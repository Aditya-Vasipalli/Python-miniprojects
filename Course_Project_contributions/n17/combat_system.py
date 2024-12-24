# import random

# global playerstrnth #To keep track of the player's strength
# playerstrnth=100 #Just an example
# global oppstr #To keep track of the opponent's strength
# oppstr=100 #Example
# global critchance #Chance of landing a critical hit doing critical damage, depends on the player's progression of the story
# critchance=0.10 #Example
# global critdmg
# critdmg=playerstrnth*1.5 #The crit damage would do maximum damage, i.e. , 1.5 times the strength attribute will contribute to the damage.
# global opphealth #To keep count of the opponent's health
# opphealth=100 #Example
# global playerhealth #To keep count of the player health
# playerhealth=100 #Example
# global increase
# increase=200 #Example

# def playerdmgcalc():  #Calculates the damage the player deals to the opponent
#     ch=random.random(0,1)
#     ch=round(ch,2)
#     if ch==critchance: #Checks if the chance of the player landing a critical hit is the same as the critical chance that depends on the player's progression in the game
#         playerdmg=critdmg
#     else:
#         playerdmg=round(random.random(0,playerstrnth),2)
#     return playerdmg

# def oppdmgcalc(): #Calculates the damage the opponent deals to the opponent
#     oppdmg=round(random.random(0,oppstr),2) #Opponent doesn't do any critical damage :)
#     return oppdmg

# def turnwise(): #The turnwise logic
#     while playerhealth>0 and opphealth>0:
#         #Player's turn
#         print("It's Your turn!")
#         ch=int(input("Enter if you will 1. Block or 2. Attack: "))
#         if ch==1:
#             dmgrec=oppdmgcalc()/2 #To keep track of how much damage is recieved
#             playerhealth=playerhealth-dmgrec
#             print("\n opponent did half damage!",dmgrec,"damage recieved")
#             print("Player health: ",playerhealth)
#         if ch==2:
#             dmg=playerdmgcalc()
#             opphealth=opphealth-dmg
#             print("\n you have done",dmg,"Damage to the opponent!")
#             print("\n Opponent's health: ",opphealth)
        
#         #Opponent's turn
#         ch=random.randint(1,2) #Chooses randomly whether the opponent will block or attack
#         if ch==1: #1 represents block
#             print("The opponent has chosen to block! Only half damage will be inflicted")
#             dmg=playerdmgcalc()/2
#             opphealth=opphealth-dmg
#             print("Opponent recieved half damage!",dmg,"damage inflicted")
#             print("Opponent's health: ",opphealth)
#         if ch==2: #2 represents attack 
#             print("The Opponent has decided to attack! Brace yourself!")
#             dmgrec=oppdmgcalc()
#             playerhealth=playerhealth-dmgrec
#             print("\n the opponent has done",dmgrec,"damage")
#             print("\n Player's health:",playerhealth)
#     if opphealth<=0:
#         return True
#     elif playerhealth<=0:
#         return False


# def win_or_loss(): #Checks whether the Player won or lost
#     if turnwise():
#         playerhealth=playerhealth+increase #Gives the player 200HP after every win.
#         return "Victory!"
#     else:
#         print("You have died!")
#         return "Defeat!"

import random
from Course_Project_contributions.n13.character_creation import Character
from Course_Project_contributions.n15.enemies import select_enemy, display_enemy_details

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

def turnwise(player, enemy):
    while player.hp > 0 and enemy['health'] > 0:
        # Player's turn
        print("It's Your turn!")
        print("Choose your move:")
        for i, skill in enumerate(player.skills):
            print(f"{i + 1}. {skill}")
        ch = int(input("Enter the number of your choice: "))
        if ch == 1:
            dmgrec = oppdmgcalc(enemy) / 2
            player.hp -= dmgrec
            print("\nOpponent did half damage!", dmgrec, "damage received")
            print("Player health: ", player.hp)
        elif ch == 2:
            dmg = playerdmgcalc(player)
            enemy['health'] -= dmg
            print("\nYou have done", dmg, "Damage to the opponent!")
            print("\nOpponent's health: ", enemy['health'])
        
        # Opponent's turn
        ch = random.randint(1, 2)
        if ch == 1:
            print("The opponent has chosen to block! Only half damage will be inflicted")
            dmg = playerdmgcalc(player) / 2
            enemy['health'] -= dmg
            print("Opponent received half damage!", dmg, "damage inflicted")
            print("Opponent's health: ", enemy['health'])
        elif ch == 2:
            print("The Opponent has decided to attack! Brace yourself!")
            dmgrec = oppdmgcalc(enemy)
            player.hp -= dmgrec
            print("\nThe opponent has done", dmgrec, "damage")
            print("\nPlayer's health:", player.hp)
    
    if enemy['health'] <= 0:
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