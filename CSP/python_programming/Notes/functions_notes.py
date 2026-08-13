#DD Period 7 Functions Notes

import sys
def your_mom():

    print("Your mom.")
    mom = input("Who is Your Mom? ").title()
    if mom != "Your Mom":
        print("WRONG!! TRY AGAIN.")
        sys.exit()

your_mom()

def add(number, number_two):
    print(number + number_two)
    print(number)

num_one = 42
num_two = 69

add(80, 8)
add(3, 4)
add(9, 89)
add(11, 163)
add(num_one, num_two)

import random

def roll(mod):
    return random.randint(2, 18) + mod

print(f"Strength: {roll(0)}\nDex: {roll(1)}\nInt: {roll(-1)}\nWis: {roll(3)}\nChar: {roll(4)}\nCon: {roll(2)}")
