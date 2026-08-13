#DD Period 7 Loops Notes

foods = ["Mushroom", "Pasta", "Pizza", "Mac n cheese", "Coffee"]

for food in foods:
    print(f"{food} is my favorite food!")
    print("Hi!")

for x in range(1, 21):
    print(x)

"""i = 0
while True:
    print(i)
    i += 1"""
#Infinite loop!!! bad >:(

i = 1
while i < 21:
    print(i)
    i += 1

x = 1
while x < 21:
    if x % 2 == 0:
        print(f"{x} is an even number.")
    else:
        print(f"{x} is an odd number.")
    x += 1

import random
import time

d = 1
end = random.randint(1, 20)

"""while d != end:
    print("Duck")
    d += 1
    time.sleep(1)

print("GOOSE!")"""

while True:
    if d == end:
        print("GOOSE!")
        break
    else:
        print("Duck")
        d += 1
        time.sleep(1)