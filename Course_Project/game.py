import pygame
import sys
from character_creation import Character, predefined_classes
from combat_system import win_or_loss, select_enemy
from armor_weapon import weapon_options, armor_options

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Game")

# Load images (placeholder for pixel art)
player_image = pygame.Surface((50, 50))
player_image.fill(WHITE)
enemy_image = pygame.Surface((50, 50))
enemy_image.fill(BLACK)

# Player position
player_pos = [100, 100]

# Font
font = pygame.font.Font(None, 36)

# Menu options
menu_options = ["Create Character", "Equip Weapon", "Equip Armor", "Start Combat", "Exit"]
selected_option = 0

# Character
character = None

# Delay for menu navigation
menu_delay = 200  # milliseconds
last_menu_action_time = 0

# Character creation state
character_creation_state = 0
character_name = ""
character_class = ""
character_stats = {"Strength": 0, "Intelligence": 0, "Agility": 0}
character_skills = ""
selected_class_index = 0

def draw_menu():
    screen.fill(BLACK)
    for i, option in enumerate(menu_options):
        color = WHITE if i == selected_option else (100, 100, 100)
        text = font.render(option, True, color)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 100 + i * 40))
    pygame.display.flip()

def handle_menu_input():
    global selected_option, character, last_menu_action_time, character_creation_state
    current_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and current_time - last_menu_action_time > menu_delay:
        selected_option = (selected_option - 1) % len(menu_options)
        last_menu_action_time = current_time
    elif keys[pygame.K_DOWN] and current_time - last_menu_action_time > menu_delay:
        selected_option = (selected_option + 1) % len(menu_options)
        last_menu_action_time = current_time
    elif keys[pygame.K_RETURN] and current_time - last_menu_action_time > menu_delay:
        if selected_option == 0:  # Create Character
            character_creation_state = 1
        elif selected_option == 1 and character:  # Equip Weapon
            equip_weapon()
        elif selected_option == 2 and character:  # Equip Armor
            equip_armor()
        elif selected_option == 3 and character:  # Start Combat
            start_combat()
        elif selected_option == 4:  # Exit
            pygame.quit()
            sys.exit()
        last_menu_action_time = current_time

def draw_character_creation():
    screen.fill(BLACK)
    if character_creation_state == 1:
        text = font.render("Enter Character Name: " + character_name, True, WHITE)
    elif character_creation_state == 2:
        class_options = list(predefined_classes.keys())
        for i, class_name in enumerate(class_options):
            color = WHITE if i == selected_class_index else (100, 100, 100)
            text = font.render(class_name, True, color)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 100 + i * 40))
    elif character_creation_state == 3:
        selected_class = predefined_classes[character_class]
        text = font.render(f"Class: {character_class}", True, WHITE)
        screen.blit(text, (50, 50))
        text = font.render(f"Strength: {selected_class['stats']['Strength']}", True, WHITE)
        screen.blit(text, (50, 100))
        text = font.render(f"Intelligence: {selected_class['stats']['Intelligence']}", True, WHITE)
        screen.blit(text, (50, 150))
        text = font.render(f"Agility: {selected_class['stats']['Agility']}", True, WHITE)
        screen.blit(text, (50, 200))
        text = font.render(f"Skills: {', '.join(selected_class['skills'])}", True, WHITE)
        screen.blit(text, (50, 250))
        text = font.render("Press Enter to confirm or Backspace to change class", True, WHITE)
        screen.blit(text, (50, 300))
    pygame.display.flip()

def handle_character_creation_input(event):
    global character_creation_state, character_name, character_class, character_stats, character_skills, character, selected_class_index, last_menu_action_time
    current_time = pygame.time.get_ticks()
    if event.type == pygame.KEYDOWN and current_time - last_menu_action_time > menu_delay:
        if character_creation_state == 1:
            if event.key == pygame.K_RETURN:
                character_creation_state = 2
            elif event.key == pygame.K_BACKSPACE:
                character_name = character_name[:-1]
            else:
                character_name += event.unicode
        elif character_creation_state == 2:
            class_options = list(predefined_classes.keys())
            if event.key == pygame.K_UP:
                selected_class_index = (selected_class_index - 1) % len(class_options)
            elif event.key == pygame.K_DOWN:
                selected_class_index = (selected_class_index + 1) % len(class_options)
            elif event.key == pygame.K_RETURN:
                character_class = class_options[selected_class_index]
                character_creation_state = 3
            last_menu_action_time = current_time
        elif character_creation_state == 3:
            if event.key == pygame.K_RETURN:
                selected_class = predefined_classes[character_class]
                character_stats = selected_class['stats']
                character_skills = ', '.join(selected_class['skills'])
                character = Character(character_name, character_class, character_stats, character_skills.split(", "))
                print(f"Character created: {character.name}, Class: {character.char_class}")
                character_creation_state = 0
            elif event.key == pygame.K_BACKSPACE:
                character_creation_state = 2
            last_menu_action_time = current_time

def equip_weapon():
    global character
    weapon_index = int(input("Enter the index of the weapon to equip (0 for Sword, 1 for Axe, 2 for Bow): "))
    if 0 <= weapon_index < len(weapon_options):
        character.equip_weapon(weapon_options[weapon_index])
        print(f"Equipped weapon: {character.equipped_weapon.name}")

def equip_armor():
    global character
    armor_index = int(input("Enter the index of the armor to equip (0 for Leather Armor, 1 for Chainmail Armor, 2 for Plate Armor): "))
    if 0 <= armor_index < len(armor_options):
        character.equip_armor(armor_options[armor_index])
        print(f"Equipped armor: {character.equipped_armor.name}")

def start_combat():
    global character
    enemy_name = input("Enter the name of the enemy to fight (e.g., Goblin): ")
    enemy = select_enemy(enemy_name)
    if enemy:
        result = win_or_loss(character, enemy)
        print(f"Combat result: {result}")

# Main game loop
def main():
    global selected_option, character_creation_state
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if character_creation_state > 0:
                handle_character_creation_input(event)

        if character_creation_state == 0:
            handle_menu_input()
            draw_menu()
        else:
            draw_character_creation()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()