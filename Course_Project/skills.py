# Define player skills
player_skills = {
    "Slash": {
        "description": "A powerful melee attack.",
        "effect": lambda player, enemy: enemy.update({"hp": enemy["hp"] - player.stats["Strength"]}),
        "cost": {"sp": 5}  # Costs 5 SP
    },
    "Block": {
        "description": "Reduces incoming damage by half.",
        "effect": lambda player, enemy: setattr(player, 'hp', player.hp - (enemy["attack"] / 2)),
        "cost": {"sp": 3}  # Costs 3 SP
    },
    "Fireball": {
        "description": "A magical attack that deals damage.",
        "effect": lambda player, enemy: enemy.update({"hp": enemy["hp"] - (player.stats["Intelligence"] * 2)}),
        "cost": {"mp": 10}  # Costs 10 MP
    },
    "Teleport": {
        "description": "Avoids the next attack.",
        "effect": lambda player, enemy: None,  # No effect on hp, just avoids the next attack
        "cost": {"mp": 5}  # Costs 5 MP
    },
    "Steal": {
        "description": "Steals a small amount of health from the enemy.",
        "effect": lambda player, enemy: (enemy.update({"hp": enemy["hp"] - 5}), setattr(player, 'hp', player.hp + 5)),
        "cost": {"sp": 4}  # Costs 4 SP
    },
    "Backstab": {
        "description": "A sneaky attack that deals extra damage.",
        "effect": lambda player, enemy: enemy.update({"hp": enemy["hp"] - (player.stats["Agility"] * 2)}),
        "cost": {"sp": 6}  # Costs 6 SP
    },
    "Cure": {
        "description": "Removes all lingering effects.",
        "effect": lambda player, enemy: player.remove_lingering_effects(),
        "cost": {"mp": 8}  # Costs 8 MP
    }
}

# Define enemy skills
enemy_skills = {
    "Poisoned Dagger": {
        "description": "A poisoned attack that deals damage over time.",
        "effect": lambda player, enemy: setattr(player, 'hp', player.hp - 5),
        "cost": {"sp": 5}  # Costs 5 SP
    },
    "Berserk Rage": {
        "description": "Increases attack power for a short time.",
        "effect": lambda player, enemy: enemy.update({"attack": enemy["attack"] * 1.5}),
        "cost": {"sp": 10}  # Costs 10 SP
    },
    "Fire Breath": {
        "description": "A fiery attack that deals massive damage.",
        "effect": lambda player, enemy: setattr(player, 'hp', player.hp - (enemy["attack"] * 2)),
        "cost": {"mp": 15}  # Costs 15 MP
    },
    "Infectious Bite": {
        "description": "A bite that infects the player, dealing damage over time.",
        "effect": lambda player, enemy: setattr(player, 'hp', player.hp - 5),
        "cost": {"sp": 5}  # Costs 5 SP
    },
    "Frenzy": {
        "description": "A frenzied attack that deals extra damage.",
        "effect": lambda player, enemy: setattr(player, 'hp', player.hp - (enemy["attack"] * 1.5)),
        "cost": {"sp": 10}  # Costs 10 SP
    },
    "Earthquake Stomp": {
        "description": "A powerful stomp that deals area damage.",
        "effect": lambda player, enemy: setattr(player, 'hp', player.hp - 10),
        "cost": {"sp": 15}  # Costs 15 SP
    },
    "Sky Dive": {
        "description": "A diving attack from above.",
        "effect": lambda player, enemy: setattr(player, 'hp', player.hp - (enemy["attack"] * 1.5)),
        "cost": {"sp": 10}  # Costs 10 SP
    },
    "Life Drain": {
        "description": "Drains life from the player to heal the enemy.",
        "effect": lambda player, enemy: (setattr(player, 'hp', player.hp - 10), enemy.update({"hp": enemy["hp"] + 10})),
        "cost": {"mp": 10}  # Costs 10 MP
    },
    "Regeneration": {
        "description": "Regenerates health over time.",
        "effect": lambda player, enemy: enemy.update({"hp": enemy["hp"] + 10}),
        "cost": {"mp": 5}  # Costs 5 MP
    },
    "Curse": {
        "description": "Curses the player, reducing their stats.",
        "effect": lambda player, enemy: setattr(player, 'stats', {k: v - 1 for k, v in player.stats.items()}),
        "cost": {"mp": 5}  # Costs 5 MP
    }
}