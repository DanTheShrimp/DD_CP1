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
    typer("Flipping a coin.")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(1)
    coinflip_answer=random.randint(1,2)

    if coinflip_answer==1:
        coinflip_answer="heads"
    elif coinflip_answer:
        coinflip_answer="tails"
    
    typer(f"It's {coinflip_answer}.")

def dice_roll():
    typer("Which dice do you want to roll? Your options are D4, D6, D8, D10, D100, D12, and D20.")

    time.sleep(0.75)
    while True:
        diceroll_answer=input("").lower()

        if "4" in diceroll_answer:
            diceroll_answer=4
            break
        elif "6" in diceroll_answer:
            diceroll_answer=6
            break
        elif "8" in diceroll_answer:
            diceroll_answer=8
            break
        elif "10" in diceroll_answer:
            diceroll_answer=10
            break
        elif "100" in diceroll_answer or "%" in diceroll_answer:
            diceroll_answer=100
            break
        elif "12" in diceroll_answer:
            diceroll_answer=12
            break
        elif "20" in diceroll_answer:
            diceroll_answer=20
            break
        else:
            typer("Please choose one of the options.")
            continue
    if diceroll_answer != 100:
        diceroll_answer=random.randint(1,diceroll_answer)
        typer("Rolling the die.")
        time.sleep(0.25)
        typer("...")
        time.sleep(0.25)
        typer("...")
        time.sleep(0.25)
        typer("...")
        time.sleep(1)
    else:
        diceroll_answer=random.randint(1,10)*10
        typer("Rolling the die.")
        time.sleep(0.25)
        typer("...")
        time.sleep(0.25)
        typer("...")
        time.sleep(0.25)
        typer("...")
        time.sleep(1)
    typer(f"The rolled number is {diceroll_answer}")

def card_pull():
    deck=["Ace of Spades","Two of Spades","Three of Spades","Four of Spades","Five of Spades","Six of Spades","Seven of Spades","Eight of Spades","Nine of Spades","Ten of Spades","Jack of Spades","Queen of Spades","King of Spades","Ace of Clubs","Two of Clubs","Three of Clubs","Four of Clubs","Five of Clubs","Six of Clubs","Seven of Clubs","Eight of Clubs","Nine of Clubs","Ten of Clubs","Jack of Clubs","Queen of Clubs","King of Clubs","Ace of Diamonds","Two of Diamonds","Three of Diamonds","Four of Diamonds","Five of Diamonds","Six of Diamonds","Seven of Diamonds","Eight of Diamonds","Nine of Diamonds","Ten of Diamonds","Jack of Diamonds","Queen of Diamonds","King of Diamonds","Ace of Hearts","Two of Hearts","Three of Hearts","Four of Hearts","Five of Hearts","Six of Hearts","Seven of Hearts","Eight of Hearts","Nine of Hearts","Ten of Hearts","Jack of Hearts","Queen of Hearts","King of Hearts","Joker","Joker"]
    cardpull_answer=random.randint(0,53)
    typer("Pulling a card.")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(1)
    typer(f"The card is {deck[cardpull_answer]}")

def random_number():
    typer("What is the first number?")

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