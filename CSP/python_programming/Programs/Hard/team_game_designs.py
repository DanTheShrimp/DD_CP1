#DD Period 7 Build a Game monster designs

import time
import sys
import random
# This section is made by Daniel
goblin = [ # Base goblin
"/|___|\\",
"|o\\ /o|",
"\\__^__/"
]
goblin_hurt = [ # Hurt goblin
"/|___|\\",
"|>\\ /o|",
"\\__^__/"
]
goblin_dead = [ # Dead goblin
"/|___|\\",
"|/x x\\|",
"\\__o__/"
]
bandit = [ # Base bandit
"/*****\\",
"|o\\`/o|",
"\\__w__/"
]
bandit_hurt = [ # Hurt bandit
"/*****\\",
"|>\\`/o|",
"\\__w__/"
]
bandit_dead = [ # Dead bandit
"/*****\\",
"|/x`x\\|",
"\\__o__/"
]
boss = [ # Base boss
"   /\\   ",
" _/ii\\_ ",
" /0``0\\ ",
" | ~~ |",
" ######",
"  #### ",
"   ##  "
]
boss_hurt = [ # Hurt boss
"   /\\   ",
" _/ii\\_ ",
" />``0\\ ",
" | ~~ |",
" ######",
"  #### ",
"   ##  "
]
boss_dead = [ # Dead boss
"   /\\   ",
" _/ii\\_ ",
" /x``x\\ ",
" | ~~ |",
" ######",
"  #### ",
"   ##  "
]
def weapon_use(): # We are gonna use a weapon A LOT, so we can do this to make it easy on future me :D
    while True:
        weapon_choosing = input("What weapon would you like to use? You have a shortsword and shortbow in your inventory. ").strip().capitalize()
        if weapon_choosing == "Shortbow" or weapon_choosing == "Bow":
            weapon_choice = "shortbow"
            break
        elif weapon_choosing == "Shortsword" or weapon_choosing == "Sword":
            weapon_choice = "sword"
            break
    print(f"You have chosen the {weapon_choice}.")
    time.sleep(1)
    if weapon_choice == "shortbow":
        damage = random.randint(1,6)+1
        print(f"You loosed an arrow from your {weapon_choice}, dealing {damage} damage.")
        for item in goblin_hurt:
            print(item)
    elif weapon_choice == "sword":
        damage = random.randint(1,8)+1
        print(f"You advance forward, swinging your sword. The goblin gets caught in your swing, taking {damage} damage.")
        for item in goblin_hurt:
            print(item)
        return damage


def goblin_encounter(): # We are gonna make a function so we can call a goblin fight simply anytime
    time.sleep(2)
    print("Oh no! A goblin has appeared and is ready to attack!")
    for item in goblin:
        print(item)
    time.sleep(2)
    goblin_hp = 10-weapon_use()
    time.sleep(1)
    print("The goblin will attack now.")
    goblin_damage = random.randint(1,6)+2
    
goblin_encounter()