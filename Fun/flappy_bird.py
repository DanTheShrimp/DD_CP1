#Daniel DeLong, Flappy Bird\
import sys, time, random, os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

bird_straight=[
    "  __  ",
    " -  o>",
    "  ̅ ̅   "
]
bird_slantup=[
    "  /--_",
    " |  o/",
    "  ̅ ̅   "
]
for item in bird_straight:
    print(item)
for item in bird_slantup:
    print(item)