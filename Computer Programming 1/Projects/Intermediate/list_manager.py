#Daniel DeLong, Shopping List Manager
import time,sys

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")


checking_list=[] #we will need this later to check if every item is checked off
shopping_list=[ #our shopping list
    "☐  Milk",
    "☐  Orange juice",
    "☐  Chips",
    "☐  Oreos",
    "☐  10 cans of beans",
    "☐  Baby food"
]

def add_item(checked,do_input,noinput_newitem): #a function with THREE parameters
    if checked==False: #if we are adding an unchecked item we need an empty box
        checked="☐"
    elif checked==True: #if we are adding a checked item we need a checked box
        checked="☑︎"
    if do_input==True: #if we are doing an input
        time.sleep(0.75)
        typer("What item do you want to add to the list?")
        new_item=input("")
        if "☐  "+new_item in shopping_list or "☑︎  "+new_item in shopping_list: #checking if their input already exists
            typer("That item already exists.")
            add_item(False,True,"nuh uh") #re-call the function, don't worry it won't cause problems. i've tested it!
        else:
            shopping_list.append(checked+"  "+new_item) #if their input doesn't exist then we add the new item to the list
    elif do_input==False: #if we aren't doing an input
        shopping_list.append(checked+"  "+noinput_newitem) #add the new item to the list, using the checked and noinput_newitem argument

def cross_off():
    exit_func=True #set this early on
    while True:
        time.sleep(0.75)
        typer("What item do you want to cross off?")
        time.sleep(0.75)
        cross_what=input("")
        if cross_what=="Daniel": #don't buy me please
            typer("Slavery is gone, stop trying to revive it.")
            sys.exit()
        if "☐  "+cross_what in shopping_list: #if the input does exist in the list and it's unchecked
            what_index=shopping_list.index("☐  "+cross_what) #get its position
            shopping_list[what_index]="☑︎  "+cross_what #replace it with a checked version of it
        elif "☑︎  "+cross_what in shopping_list: #if the input does exist in the list and it's checked
            typer("That item is already crossed off.")
        else: #if the input doesn't exist in the list
            typer("That item is not on the list. Do you want to add it and check it off?")
            while True:
                add_and_cross=input("").lower()
                if "no" in add_and_cross: #if they don't want to add an item and check it off
                    exit_func=False #set this to false
                    break #break this loop
                elif "yes" in add_and_cross: #if they do want to
                    add_item(True,False,add_and_cross) #set checked to true, do_input to false, and the noinput_newitem to the player's input
                    break
                else:
                    time.sleep(0.75)
                    typer("Please answer the question.")
        if exit_func==True: #if we want to exit the loop and the function we need exit_func to be true
            break

typer("Here is your weekly shopping list:")
while True:
    time.sleep(1)
    checking_list.clear() #clear the checking list
    for food in shopping_list: #print the whole shopping list
        print(food)
        time.sleep(0.25)
    for food in shopping_list: #check if each item in the list has the checked box
        if "☑︎" in food:
            checking_list.append(True)
        else:
            checking_list.append(False)
    time.sleep(0.75)
    if all(checking_list): #if each value in checking_list is true, then we say they can leave and end the program
        typer("You've gotten everything on the list! You can go home now.")
        sys.exit()
    while True:
        typer("Do you want to add or cross off an item?")
        add_or_cross=input("").lower() #if 
        if "add" in add_or_cross:
            add_item(False,True,"nuh uh")
            break
        elif "cross" in add_or_cross:
            cross_off()
            break
    time.sleep(1)
    typer("Here is the updated shopping list:")