#Daniel DeLong, Unit 1 Final Project
import sys,time,random

def typer(text): #a super simple typer function
    for char in text: #for each character in the text
        print(char, end="") #print that character and don't go to a new line
        time.sleep(0.025) #wait 0.05 seconds to add a typing feeling
    print("") #go to a new line

def beginning():
    typer("Welcome to the Random Carnival!")
    time.sleep(0.75)
    typer("Here are your options, please choose one:")
    time.sleep(1)
    typer("Coin Flip")
    time.sleep(0.5)
    typer("Dice Roll")
    time.sleep(0.5)
    typer("Card Pull")
    time.sleep(0.5)
    typer("Random Number")
    time.sleep(1.5)
    typer("What game would you like to play?")
    player_chosen_game=input("").lower() #asking for their choice, and making all letters lowercase
    time.sleep(1)
    return player_chosen_game #returning the variable to 

def coin_flip():
    typer("Coin Flip")

def dice_roll():
    typer("Dice Roll")

def card_pull():
    typer("Card Pull")

def random_number():
    typer("Random Number")

def russian_roulette():
    time.sleep(1)
    typer("Are you sure you want to play Russian Roulette?")
    are_you_sure=input("").lower()
    if "yes" in are_you_sure:
        time.sleep(1)
    else:
        time.sleep(2)
        choosing()
    typer("Russian Roulette")

def choosing():
    player_chosen_game=beginning()
    if "coin" in player_chosen_game:
        coin_flip()
    elif "dice" in player_chosen_game:
        dice_roll()
    elif "card" in player_chosen_game:
        card_pull()
    elif "random" in player_chosen_game:
        random_number()
    elif "roulette" in player_chosen_game:
        russian_roulette()
choosing()