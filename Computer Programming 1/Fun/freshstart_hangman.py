#Daniel DeLong, Hangman for Fun
import sys,time,random

stages=[ #There are seven stages, number 0 is the first one, 6 is the last
    [" ___    ",
    " |  |    ",
    "\\o/ |    ",
    " |  |    ",
    "/ \\ |    ",
    "    |    ",
    "____|____"],

    [" ___     ",
    " |  |    ",
    "\\o/ |    ",
    " |  |    ",
    "/   |    ",
    "    |    ",
    "____|____"],

    [" ___     ",
    " |  |    ",
    "\\o/ |    ",
    " |  |    ",
    "    |    ",
    "    |    ",
    "____|____"],

    [" ___     ",
    " |  |    ",
    "\\o  |    ",
    " |  |    ",
    "    |    ",
    "    |    ",
    "____|____"],

    [" ___     ",
    " |  |    ",
    " o  |    ",
    " |  |    ",
    "    |    ",
    "    |    ",
    "____|____"],

    [" ___     ",
    " |  |    ",
    " o  |    ",
    "    |    ",
    "    |    ",
    "    |    ",
    "____|____"],

    [" ___     ",
    " |  |    ",
    "    |    ",
    "    |    ",
    "    |    ",
    "    |    ",
    "____|____"],
]

def tester_function(): #this function exists so I can test if the stages print properly
    loop_helper=0
    while True:
        for item in stages[loop_helper]:
            print(item)
        print(" ")
        if loop_helper==6:
            break
        loop_helper+=1

# \/ list of words, if I change the number of words I have to update the random number generator \/
words=["food","computer","somewhere","attacked","disorient","alright","chili","bridge","programmer","number","student","lunch","pasta","ocean","hangman"]

def start():
    #choosing the word, assigning it to a variable, and getting its length
    chosen_word=random.randint(0,14) #update this if the number of words change
    chosen_word=str(words[chosen_word])
    chosen_word_length=len(chosen_word)
    chosen_word_underscore=[]
    
    #creating the underscore word that will be changed and displayed to players at will
    loop_helper=chosen_word_length
    while loop_helper!=0:
        chosen_word_underscore.append("_")
        loop_helper-=1
    current_stage=0 #this number will change from 0-6 as the player guesses the wrong letter

    while True:
        #this chunk is checking if we lost or won
        if current_stage==6: #checking if we are on the last stage
            print("You ran out of guesses!")
            time.sleep(1)
            print(f"The word was: {chosen_word}")
            sys.exit() #if we are then we end the program
        try:
            chosen_word_underscore.index("_")
        except ValueError:
            print("Congratulations, you win!")
            time.sleep(1)
            print(f"The word was: {chosen_word}")
            sys.exit()

        #printing the stage and hidden word
        for item in stages[current_stage]: #printing the current stage of the hangman
            print(item)
        print("") #printing a space so the underscores aren't directly underneath the hangman stage
        time.sleep(1)
        for item in chosen_word_underscore: #printing the underscores
            print(item, end="")
        print("")
        
        #asking the player for a letter
        while True:
            print("Please input one letter.")
            input_letter=str(input()) #getting the user's input
            input_letter.lower() #making all of it lowercase
            if len(input_letter)==1: # checking if the input is one character long, if it isn't we re-ask them
                break
        input_letter_position=[index for index, char in enumerate(chosen_word) if char==input_letter] #finding all positions where the inputted letter is

        #changing all positions where the inputted letter is, if any
        loop_helper=0
        while True:
            try:
                chosen_word_underscore[input_letter_position[loop_helper]]=input_letter #checking if the inputted letter is in the chosen word

            except IndexError: #this triggers if an Index Error occurs, when an item in a list doesn't exist

                if loop_helper==0: #checking if this is the first time the while loop has run, if this passes it means that the letter we inputted isn't in the chosen word
                    current_stage+=1 #changing the stage
                    break

                else:
                    break
            loop_helper+=1     
start()