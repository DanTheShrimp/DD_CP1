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
    
    loop_helper=chosen_word_length
    while loop_helper!=0:
        chosen_word_underscore.append("_")
        loop_helper-=1
    current_stage=0 #this number will change from 0-6 as the player guesses the wrong letter

    while True:

        if current_stage==6: #checking if we are on the last stage
            print("You ran out of guesses!")
            print(f"The word was: {chosen_word}")
            sys.exit() #if we are then we end the program
        try:
            chosen_word_underscore.index("_")

        except ValueError:
            print("Congratulations, you win!")
            print(f"The word was: {chosen_word}")
            sys.exit()

        for item in stages[current_stage]: #printing the current stage of the hangman
            print(item)
        print("") #printing a space so the underscores aren't directly underneath the hangman stage
        for item in chosen_word_underscore: #printing the underscores
            print(item, end="")
        print("")
        
        while True:
            print("Please input one letter.")
            input_letter=str(input()) #getting the user's input
            input_letter.lower() #making all of it lowercase
            if len(input_letter)==1: # checking if the input is one character long
                break
        input_letter_position=[index for index, char in enumerate(chosen_word) if char==input_letter] #finding all positions where the inputted letter is

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

