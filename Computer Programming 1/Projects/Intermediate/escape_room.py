#Daniel DeLong, Escape Room
import time,sys

#Mrs LaRose's favorite book character is Doomslug
"'You have to do new variables every time.' -Mrs LaRose"

#code is 'I LOVE DOOMSLUG'
#include a poster on the wall containing the text "I LOVE DOOMSLUG" and a picture of doomslug in a heart in the description of the room

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")
#this program is mostly text
#providing the player with necessary information
typer("You wake up in a dark room, only one window providing light to see by. That window is barred and doesn't seem to be a viable way to get out.")
time.sleep(0.75)
typer("On one concrete wall you see a single aged poster with the words 'I LOVE DOOMSLUG' on it and an image of Doomslug in a red heart below the text.")
time.sleep(0.75)
typer("On the wall opposite of the poster, you see a metal sliding door and a terminal next to it.")
while True:
    time.sleep(1)
    typer("What do you want to do?")
    while True:
        #getting their input about what they want to do
        what_to_do=input("").lower()
        time.sleep(0.75)
        if "terminal" in what_to_do:
            what_to_do="terminal"
            break
        elif "window" in what_to_do:
            what_to_do="window"
            break
        else:
            what_to_do="confused"
            break
    if what_to_do=="confused":
        typer("You sit there, not sure of what to do.")
        continue #continue means to pass by everything else and go back to the start of the loop
    elif what_to_do=="window":
        typer("You walk over to the window, test a few of the bars, and determine that you aren't getting out this way.")
        continue
    elif what_to_do=="terminal":
        typer("You walked over to the terminal, and see that it's displaying 'INPUT DOOR CODE' on the screen. You also see a digital keyboard displayed just below the input prompt.")
        attempts_failed=0 #they haven't failed any attempts yet
        while True:
            time.sleep(1)
            typer("What do you type into the terminal?")
            player_typed_what=input("").upper() #i want upper here because people are often stupid
            time.sleep(1)
            if player_typed_what=="I LOVE DOOMSLUG":
                correct=True #set this
                break
            else:
                correct=False #set this
                attempts_failed+=1 #add one to attempts_failed
                typer("The terminal buzzes angrily at you; it seems the code you inputted was incorrect.")
            if attempts_failed==3:
                #they fail :o
                typer("You hear footsteps behind the locked door. A voice floats through, 'You have to do new variables every time!' The lights go out at that moment.")
                sys.exit()
        if correct:
            #they succeed, but still fail
            typer("The terminal dings at you, and the door starts to slide open. You run through the now open doorway, dashing up the creaky, wooden stairs. You don't make it far, however.")
            time.sleep(0.75)
            typer("One of the steps break under your weight, tripping you and sending you to your knees. A figure darkens the doorway, blocking your chance at freedom.")
            sys.exit()