#DD Period 7 Time of Day

import sys
try:
    time = int(input("Please tell me the hour. I am suffering because importing time is not working.\n"))
except ValueError:
    print("I fudging hate you... I JUST WANT MY [nope] CODE TO WORK!! WHY DO YOU HAVE TO MAKE IT SO HARD FOR ME?!?!")
    sys.exit()

if time >= 20 and time <= 24 or time < 5:
    print("Why are you still awake? Go to sleep!")
elif time >= 5 and time < 12:
    print("Good morning!")
elif time >= 12 and time < 18:
    print("Good afternoon!")
elif time >= 18 and time < 20:
    print("Good evening!")
else:
    print("I hate you... so so much... All I want is my code to work :(")