# Daniel DeLong, Escape Room
import time,sys

# Mrs LaRose's favorite book character is Doomslug
"'You have to do new variables every time.' -Mrs LaRose"

# code is 'I LOVE DOOMSLUG'
# include a poster on the wall containing the text "I LOVE DOOMSLUG" and a picture of doomslug in a heart in the description of the room

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.01)
    print("")
# this program is mostly text
# providing the player with necessary information
typer("You wake up in a dark room, only one window providing light to see by. That window is barred and doesn't seem to be a viable way to get out.")
time.sleep(0.75)
typer("On one concrete wall you see a single aged poster with the words 'I LOVE DOOMSLUG' on it and an image of Doomslug in a red heart below the text.")
time.sleep(0.75)
typer("On the wall opposite of the poster, you see a metal sliding door and a terminal next to it.")
while True:
    time.sleep(1)
    typer("What do you want to do?")
    while True:
        # getting their input about what they want to do
        what_to_do=input("").lower()
        time.sleep(0.75)
        if "terminal" in what_to_do:
            what_to_do="terminal"
            break
        elif "window" in what_to_do:
            what_to_do="window"
            break
        elif "poster" in what_to_do:
            what_to_do="poster"
            break
        else:
            what_to_do="confused"
            break
    if what_to_do=="confused":
        typer("You sit there, not sure of what to do.")
        continue # continue means to pass by everything else and go back to the start of the loop
    elif what_to_do=="window":
        typer("You walk over to the window, test a few of the bars, and determine that you aren't getting out this way.")
        continue
    elif what_to_do=="poster":
        typer("You walk over to the poster to get a better look. It's color has been faded immensely but you can still make out the vague outline of a signature on top of the slug in the heart.")
        continue
    elif what_to_do=="terminal":
        typer("You walk over to the terminal, and see that it's displaying 'INPUT DOOR CODE' on the screen. You also see a digital keyboard displayed just below the input prompt.")
        attempts_failed=0 # they haven't failed any attempts yet
        while True:
            time.sleep(1)
            typer("What do you type into the terminal?")
            player_typed_what=input("").upper() # i want upper here because people are often stupid
            time.sleep(1)
            if player_typed_what=="I LOVE DOOMSLUG":
                correct=True # set this
                break
            else:
                correct=False # set this
                attempts_failed+=1 # add one to attempts_failed
                typer("The terminal buzzes angrily at you; it seems the code you inputted was incorrect.")
                time.sleep(0.75)
                typer("The word 'DOOMSLUG' flashes on the screen for a brief moment, then goes back to the code input.")
            if attempts_failed==3:
                # they fail :o
                typer("You hear footsteps crunching on dry dirt behind the locked door. A voice floats through, 'You have to do new variables every time!' The lights go out at that moment.")
                sys.exit()
        if correct and attempts_failed==2:
            # they fail :O
            typer("The terminal flashes green, then a moment later the door slides open, creaking with age. You rush out into bright sunlight, laughing almost hysterically. You don't know how long you were unconscious for, but it must have been a long time.")
            time.sleep(0.75)
            typer("But wait, what's that figure approaching? They must have heard the failed terminal attempts. You try to run, desperate to keep your newfound freedom, but you slam into a wall. The not-sky glitches for a moment, showing a black panel behind the vibrant colors.")
            sys.exit()
        elif correct:
            # they succeed, but now succeed :D
            typer("The terminal flashes green, then a moment later the door slides open, creaking with age. You rush out into bright sunlight, laughing almost hysterically. You don't know how long you were unconscious for, but it must have been a long time.")
            sys.exit()

# there are now three endings, i kept the fail (tweaking it slightly, now the footsteps crunch on dirt), and changed the previous "win."
# it now actually lets you win, but only if you managed to put in the code before you failed twice.
# if you failed twice then put in the right code, the overseer comes to investigate the Basement and finds you trying to escape.