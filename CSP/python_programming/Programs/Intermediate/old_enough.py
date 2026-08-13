#DD Period 7 Old Enough

import sys
try: #I will say, I did ask for HELP from an AI to figure out how to do this part.
    age = int(input("How old are you?\n"))
except ValueError:
    print("AHHHHHHH I'M GONNA EXPLODE!!!")
    sys.exit()

if age >= 50:
    print("Ok, boomer. Your wrinkly hands are dirtying my screen.")

elif age >= 18:
    print("You are old enough to vote. Welcome to politics.")

elif age >= 16:
    print("Congrats! You are old enough to drive!")

elif age >= 15:
    print("Wow! You are old enough to get a learner's permit!")

elif age >= 4:
    print("Hey kiddo, you are old enough to go to school!")

else:
    print("Wut da heck are you doing on a computer?")