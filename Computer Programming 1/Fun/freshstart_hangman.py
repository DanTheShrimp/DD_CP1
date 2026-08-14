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
words=["Food","Computer","Somewhere","Attacked","Disoriented","Alright","Chili","Bridge","Programmer","Number"]

def start():
    #choosing the word, assigning it to a variable, and getting its length
    chosen_word=random.randint(0,9) #update this if the number of words change
    chosen_word=str(words[chosen_word])
    chosen_word_length=len(chosen_word)

    current_stage=0 #this number will change from 0-6 as the player guesses the wrong letter

    while True:
        for item in stages[current_stage]: #printing the current stage of the hangman
            print(item)
        
        break
        

        
start()

