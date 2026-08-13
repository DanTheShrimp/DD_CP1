#DD Period 7 Silly Sentences

import random
import time
randint = random.randint(1, 5)

print("Get ready to laugh! I am the Silly Sentence Generator!")
noun1 = input("First, give me a noun. ")
verb1 = input("Awesome, now give me a verb ending in ing. ")
adjective1 = input("Perfect, I now need an adjective. ")
adverb1 = input("Alright, now give me an adverb. ")
noun2 = input("Almost done, I just need another noun. ")
verb2 = input("Last one! Give me a normal verb. ")

time.sleep(1)
print("Loading your laughter...")
time.sleep(5)

if randint == 1:
    print(f"You and your trusty {noun1} are {adverb1} {verb1} from {noun2}, and must find the {adjective1} statue that loves to {verb2}.")

elif randint == 2:
    print(f"The legendary {noun1} is in the {adjective1} hands of the {verb1}, evil {noun2} that will stop at nothing to {adverb1} {verb2} the world.")

elif randint == 3:
    print(f"You must rescue the {adjective1} king from the {adverb1}, evil {verb1} {noun1}, which will {verb2} the {noun2} if you do not stop them.")

elif randint == 4:
    print(f"I, the {adjective1} {noun1}, will protect you, my {adverb1} {verb1} {noun2}, lest you {verb2} away from me.")

elif randint == 5:
    print(f"You are renouned {adjective1} {noun1}, who always manages to send those {adverb1} {verb1} {noun2}s {verb2}ing.")