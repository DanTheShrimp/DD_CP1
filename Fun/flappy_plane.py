#Daniel DeLong, Flappy Plane
import sys, time, random, os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

plane_straight=[
    "✈︎"
]
"""bird_slantup=[ #some weird stuff happened when using Alt and the up and down keys so I'm immortalizing it
    "  /♦--_",
    " |  o/",
    "  \\ ̅å&    "
]"""
plane_slantup=[
    "🛫"
]
plane_slantdown=[
    "🛬"
]
for item in plane_straight:
    print(item)
for item in plane_slantup:
    print(item)
for item in plane_slantdown:
    print(item)

plane_height=10
