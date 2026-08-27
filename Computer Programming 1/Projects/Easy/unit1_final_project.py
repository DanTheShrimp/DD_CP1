#Daniel DeLong, Unit 1 Final Project
import sys,time,random

def typer(text): #a super simple typer function
    for char in text: #for each character in the text
        print(char, end="") #print that character and don't go to a new line
        time.sleep(0.05) #wait 0.05 seconds to add a typing feeling
    print("") #go to a new line

def beginning(): #the introduction to the Random carnival
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

def coin_flip(): #flipping a coin
    typer("Flipping a coin.")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(1)
    coinflip_answer=random.randint(1,2) #getting a random integer, either 1 or 2

    if coinflip_answer==1: #if the coinflip_answer is 1, it's heads
        coinflip_answer="heads"
    elif coinflip_answer==2: #if the coinflip_answer is 2, it's instead tails
        coinflip_answer="tails"
    
    typer(f"It's {coinflip_answer}.") #printing the answer and ending the program
    sys.exit()

def dice_roll(): #rolling a die
    typer("Which dice do you want to roll? Your options are D4, D6, D8, D10, D100, D12, and D20.")

    time.sleep(0.75)
    while True: #we want to be able to loop this part just in case they don't input an answer we want
        diceroll_answer=input("").lower()

        #seeing if there is a 4, 6, 8, 10, 100, 12, or 20 in their answer
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
        else: #if there isn't then we loop and ask them to put in another answer
            typer("Please choose one of the options.")
            continue
    if diceroll_answer != 100: #if diceroll_answer isn't 100
        diceroll_answer=random.randint(1,diceroll_answer) #get a random integer between 1 and the number of faces the die has
        typer("Rolling the die.")
        time.sleep(0.25)
        typer("...")
        time.sleep(0.25)
        typer("...")
        time.sleep(0.25)
        typer("...")
        time.sleep(1)
    else:
        diceroll_answer=random.randint(1,10)*10 #this is specifically for the D100, where each side is increments of 10
        typer("Rolling the die.")
        time.sleep(0.25)
        typer("...")
        time.sleep(0.25)
        typer("...")
        time.sleep(0.25)
        typer("...")
        time.sleep(1)
    typer(f"The rolled number is {diceroll_answer}") #printing the answer and ending the program
    sys.exit()

def card_pull():
    #big deck with every card in it, including jokers
    deck=["Ace of Spades","Two of Spades","Three of Spades","Four of Spades","Five of Spades","Six of Spades","Seven of Spades","Eight of Spades","Nine of Spades","Ten of Spades","Jack of Spades","Queen of Spades","King of Spades","Ace of Clubs","Two of Clubs","Three of Clubs","Four of Clubs","Five of Clubs","Six of Clubs","Seven of Clubs","Eight of Clubs","Nine of Clubs","Ten of Clubs","Jack of Clubs","Queen of Clubs","King of Clubs","Ace of Diamonds","Two of Diamonds","Three of Diamonds","Four of Diamonds","Five of Diamonds","Six of Diamonds","Seven of Diamonds","Eight of Diamonds","Nine of Diamonds","Ten of Diamonds","Jack of Diamonds","Queen of Diamonds","King of Diamonds","Ace of Hearts","Two of Hearts","Three of Hearts","Four of Hearts","Five of Hearts","Six of Hearts","Seven of Hearts","Eight of Hearts","Nine of Hearts","Ten of Hearts","Jack of Hearts","Queen of Hearts","King of Hearts","Joker","Joker"]
    cardpull_answer=random.randint(0,53) #we use 0 to 53 here because when searching, or indexing, a list the first item has the number 0
    typer("Pulling a card.")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(1)
    typer(f"The card is {deck[cardpull_answer]}") #printing the answer and ending the program
    sys.exit()

def random_number():
    typer("What is the first number?") #asking for a number
    #the same loop as in dice_roll(), but a little different and a lot shorter
    while True:
        try:
            first_player_number=int(input(""))
        except:
            typer("Please input a number.")
            time.sleep(1)
        else:
            break
    typer("What is the first number?")
    #i love while True loops
    while True:
        try:
            second_player_number=int(input(""))
        except:
            typer("Please input a number.")
            time.sleep(1)
        else:
            break
    typer("Generating a number.")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(1)
    #i put the random.randint in the typer statement to save me from having to create another variable, and it works the exact same
    typer(f"Your random number is {random.randint(first_player_number,second_player_number)}") #printing the answer and ending the program
    sys.exit()
    

def russian_roulette(): #this is russion roulette, but i changed one rule
    #the game part of russian roulette
    def game():
        typer("Welcome to Russian Roulette.")
        time.sleep(0.75)
        typer("There are six bullets in the revolver, one is live.")
        time.sleep(0.75)
        typer("You will have the option to aim at yourself, or at the computer facing you.")
        time.sleep(0.75)
        typer("Let us begin.")
        #this is a nested function, a function that can only be called in the function it's in
        def player_turn(remaining_bullets): #the remaining_bullets in the function name is an parameter, or a variable that can only be used in that specific function
            time.sleep(1.5)
            typer("You now hold the gun.")
            time.sleep(0.75)
            typer("Who do you want to aim at?")
            #another while True loop, gosh i love these things
            while True:
                player_aim_who=input("").lower()
                #based on what key words are in their answer, we set a variable to player or computer so we can easily reference them later
                if "me" in player_aim_who or "myself" in player_aim_who:
                    player_aim_who="player"
                    break
                elif "computer" in player_aim_who or "other" in player_aim_who:
                    player_aim_who="computer"
                    break
                else: #if we don't find a word we are looking for we loop the loop
                    typer("Please choose a valid option.")
                    continue
            #if the player is aiming at themself we run this code
            if player_aim_who=="player":
                time.sleep(1)
                typer("You point the gun at yourself.")
                time.sleep(0.5)
                typer("...")
                time.sleep(0.5)
                typer("...")
                time.sleep(0.5)
                typer("...")
                time.sleep(2.5)
                does_it_fire=random.randint(1,remaining_bullets) #using the argument to get a random number between 1 and the value of the parameter
                if does_it_fire==1: #if the random number is 1 the gun fires
                    does_it_fire="y"
                    print("BANG")
                    sys.exit() #player dies
                else:
                    does_it_fire="n"
                    print("*click*")
                    return does_it_fire #we return "n" so we can update the remaining number of bullets later
            #if the player is aiming at the computer we run this code
            if player_aim_who=="computer":
                time.sleep(1)
                typer("You point the gun at the computer.")
                time.sleep(0.5)
                typer("...")
                time.sleep(0.5)
                typer("...")
                time.sleep(0.5)
                typer("...")
                time.sleep(2.5)
                #this code is the exact same as before
                does_it_fire=random.randint(1,remaining_bullets)
                if does_it_fire==1:
                    does_it_fire="y"
                    print("BANG")
                    sys.exit() #computer dies
                else:
                    does_it_fire="n"
                    print("*click*")
                    return does_it_fire
        #another nested function
        def computer_turn(remaining_bullets): #hey, look! it's the same parameter. yes i copied my existing code and tweaked it
            time.sleep(1.5)
            typer("The computer now holds the gun.")
            time.sleep(0.75)
            computer_aim_who=random.randint(1,2) #it's a 50/50 whether the computer aims at itself or the player
            if computer_aim_who==1: #if it's 1 they aim at the player
                time.sleep(1)
                typer("The computer points the gun at you.")
                time.sleep(0.5)
                typer("...")
                time.sleep(0.5)
                typer("...")
                time.sleep(0.5)
                typer("...")
                time.sleep(2.5)
                #the same code as before
                does_it_fire=random.randint(1,remaining_bullets)
                if does_it_fire==1:
                    does_it_fire="y"
                    print("BANG")
                    sys.exit()
                else:
                    does_it_fire="n"
                    print("*click*")
                    return does_it_fire
            if computer_aim_who==2: #if it's 2 they aim at themself
                time.sleep(1)
                typer("The computer points the gun at itself.")
                time.sleep(0.5)
                typer("...")
                time.sleep(0.5)
                typer("...")
                time.sleep(0.5)
                typer("...")
                time.sleep(2.5)
                #still the same
                does_it_fire=random.randint(1,remaining_bullets)
                if does_it_fire==1:
                    does_it_fire="y"
                    print("BANG")
                    sys.exit()
                else:
                    does_it_fire="n"
                    print("*click*")
                    return does_it_fire
        remaining_bullets=6
        while True:
            did_it_fire=player_turn(remaining_bullets)
            if did_it_fire=="n":
                remaining_bullets-=1
            did_it_fire=computer_turn(remaining_bullets)
            if did_it_fire=="n":
                remaining_bullets-=1
    time.sleep(1)
    typer("Are you sure you want to play Russian Roulette?")
    are_you_sure=input("").lower()
    if "yes" in are_you_sure:
        time.sleep(1)
        game()
    else:
        time.sleep(2)
        choosing()
        


def choosing():
    beginning()
    typer("What game would you like to play?")
    player_chosen_game=input("").lower() #asking for their choice, and making all letters lowercase
    time.sleep(1)
    while True:
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
        else:
            typer("What game would you like to play?")
            player_chosen_game=input("").lower() #asking for their choice, and making all letters lowercase
            time.sleep(1)

choosing()