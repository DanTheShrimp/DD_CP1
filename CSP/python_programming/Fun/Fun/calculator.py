#DD Period 7 for fun :D

import random
import sys
import time

random_number = random.randint(1, 25)
if random_number == 17:
    print("RAAAAARRGGHHHH!!!!!!!!")
    sys.exit()
try:
   first_number = int(input("What is the first number?\n"))
except ValueError:
   print("Please enter a valid integer.")
   sys.exit()
try:
    middle_thing = input("What is the operation? (+,-,/, *, or **)\n")
    if middle_thing not in ['+', '-', '/', '*', '**']:
        raise ValueError()
except ValueError:
    print("Please enter a valid operation: +, -, /, *, or **.")
    sys.exit()
try:
    last_number = int(input("What is the last number?\n"))
except ValueError:
    print("Please enter a valid integer.")
    sys.exit()
time.sleep(2)
print("Calculating...")
time.sleep(2)

if middle_thing == "+":
    print(f"The answer is: {first_number+last_number}")

elif middle_thing == "-":
    print(f"The answer is: {first_number-last_number}")

elif middle_thing == "/":
    print(f"The answer is: {first_number/last_number}")

elif middle_thing == "*":
    print(f"The answer is: {first_number*last_number}")

elif middle_thing == "**":
    print(f"The answer is: {first_number**last_number}")
