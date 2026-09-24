#Daniel DeLong, User Sign In
import time, sys

users=[ #using parenthesis means that they can't ever be changed, this is called a tuple
    ("Admin","noHackers_123"), #admin account
    ("Guest","guest123"), #guest account
    ("Pedro","tung67"), #pedro's account
    ("Daniel","lightw3aver_Storml1ght") #daniel's account
]

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

def sign_in():
    number_of_attempts=0 #set our number of attempts to zero
    while True:
        time.sleep(0.75)
        typer("Username:")
        time.sleep(0.75)
        username_input=input("") #ask for the username
        #setting some helpful variables
        loop_helper=0
        doesnt_exist=False
        while True:
            try:
                if username_input==users[loop_helper][0]: #seeing if their input matches 
                    break
                else:
                    loop_helper+=1 #if we can't find it we add one to loop_helper so the first indexing number goes up
            except:
                typer("That username does not exist.") #if we get and error that means that we've gotten to the point where no username has worked so far
                doesnt_exist=True #set doesnt_exist to true
                break
        if doesnt_exist==True: #if it doesn't exist we continue past the rest of the code in the loop and go back to the start of the loop
            continue

        typer("Password:")
        password_input=input("") #ask for the password
        time.sleep(0.75)
        if password_input!=users[loop_helper][1]: #if their input doesn't equal the selected username's password
            typer("Incorrect password.")
            number_of_attempts+=1 #add one to number_of_attempts
        else:
            typer("Correct password.") #if it doesn't doesn't equal the selected username's password then it does equal it
            return username_input
        if number_of_attempts==3: #if they put in the incorrect password three times
            typer("Too many failed attempts.")
            sys.exit() #end the program

def create_account():
    while True:
        username_exists=False #i need this
        time.sleep(0.75)
        typer("Account username:")
        create_username=input("") #get their input
        time.sleep(0.75)
        for user in users: #for each user in users
            if create_username==user[0]: #check if the player's input equals the current username we are checking
                username_exists=True #if the if statement passes then we set to username_exists to True
        if username_exists==True: #then we check if it's True
            typer("That username already exists.")
            continue #loop
        else:
            break
    while True:
        typer("Account password:")
        create_password=input("") #get their input
        #we don't need to check the password because passwords can be the same while usernames can't
        break
    new_user=(create_username,create_password) #make both their inputs into a tuple (a list that can't be changed)
    users.append(new_user) #tack the new user onto the users tuple

def null(): #funny things
    typer("How have you gotten here...?")
    time.sleep(3)
    typer("You shouldn't be here.")
    time.sleep(1.5)
    sys.exit()

while True:
    current_user="null" #set this so we don't get an error later
    typer("Welcome to Gethib.com!")
    while True:
        typer("Would you like to sign in, create an account, or close the tab?")
        their_choice=input("").lower() #get their input
        if "sign" in their_choice: #if they want to sign in we call the sign_in function and set current_user to its return variable
            current_user=sign_in()
            break
        elif "create" in their_choice: #if they want to create an account we call the create_account function
            create_account()
            continue
        elif "close" in their_choice: #close the gethib.com tab (end the program)
            time.sleep(0.75)
            typer("Closing the tab.")
            sys.exit()
        elif their_choice=="null": #funny things
            time.sleep(2)
            null()
        else: #if they don't put in anything we want then we loop
            continue

    if current_user=="Admin": #check and see if the Admin is logged in
        #im sorry for all the indentation, it was required
        time.sleep(1)
        typer("Welcome Admin. Here is the current list of users and their passwords:")
        time.sleep(0.75)
        for user in users: #print every user and its password
            print(f"{user[0]} : {user[1]}")
            time.sleep(0.5)
        while True:
            typer("Would you like to sign out or delete an account?")
            another_choice=input("").lower() #get their input
            time.sleep(0.75)
            if "out" in another_choice:
                typer("Signing out.")
                another_choice="SignOut" #set this for later
            elif "delete" in another_choice:
                while True:
                    typer("Which account do you want to delete?")
                    delete_account=input("") #get their input
                    time.sleep(0.75)
                    loop_helper=0
                    doesnt_exist=False
                    while True:
                        try:
                            if delete_account==users[loop_helper][0]: #literally the same code as in sign_in()
                                break
                            else:
                                loop_helper+=1
                        except:
                            typer("That username does not exist.")
                            doesnt_exist=True
                            break
                    if doesnt_exist==True: #loop
                        continue
                    if delete_account=="Admin": #we don't want the admin account deleted
                        typer("That account cannot be deleted.")
                        continue
                    elif delete_account=="Guest": #we don't want the guest account deleted
                        typer("That account cannot be deleted.")
                        continue
                    else:
                        users=list(users) #turn users into a list so we can change it
                        del users[loop_helper] #delete the user the players wants to delete
                        users=tuple(users) #turn it back into a tuple
                        another_choice="Deleted" #set this for later
                        typer(f"{delete_account} has been deleted.")
                        time.sleep(0.75)
                        typer("Here is the new list of users and their passwords:") #printing the new list of users
                        for user in users:
                            print(f"{user[0]} : {user[1]}")
                            time.sleep(0.5)
                        break
            if another_choice=="SignOut": #if they want to sign out we break the loop, then because there are no more lines after this the admin if statement ends too
                time.sleep(0.75)
                break
            elif another_choice=="Deleted":
                time.sleep(0.75)
                continue #loop!
    else:
        time.sleep(1)
        if current_user=="Daniel": #praise Daniel
            typer("Oh, hail Daniel, the creator of this code!")
        else:
            typer(f"Welcome {current_user}.") #don't praise Daniel
        time.sleep(0.75)
        while True:
            #they literally can't do anything so the only option is to sign out
            typer("Would you like to sign out? (you can't do anything)")
            one_more_choice=input("").lower() #get their input one last time
            time.sleep(1)
            if "yes" in one_more_choice:
                break