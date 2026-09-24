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
    number_of_attempts=0
    while True:
        time.sleep(0.75)
        typer("Username:")
        time.sleep(0.75)
        username_input=input("")
        loop_helper=0
        doesnt_exist=False
        while True:
            try:
                if username_input==users[loop_helper][0]:
                    break
                else:
                    loop_helper+=1
            except:
                typer("That username does not exist.")
                doesnt_exist=True
                break
        if doesnt_exist==True:
            continue

        typer("Password:")
        password_input=input("")
        time.sleep(0.75)
        if password_input!=users[loop_helper][1]:
            typer("Incorrect password.")
            number_of_attempts+=1
        else:
            typer("Correct password.")
            return username_input
        if number_of_attempts==3:
            typer("Too many failed attempts.")
            sys.exit()

def create_account():
    while True:
        username_exists=False
        time.sleep(0.75)
        typer("Account username:")
        create_username=input("")
        time.sleep(0.75)
        for user in users:
            if create_username==user[0]:
                username_exists=True
        if username_exists==True:
            typer("That username already exists.")
            continue
        else:
            break
    while True:
        typer("Account password:")
        create_password=input("")
        break
    new_user=(create_username,create_password)
    users.append(new_user)

def null():
    typer("How have you gotten here...?")
    time.sleep(3)
    typer("You shouldn't be here.")
    time.sleep(1.5)
    sys.exit()

while True:
    current_user="null"
    typer("Welcome to Gethib.com!")
    while True:
        typer("Would you like to sign in, create an account, or close the tab?")
        their_choice=input("").lower()
        if "sign" in their_choice:
            current_user=sign_in()
            break
        elif "create" in their_choice:
            create_account()
            continue
        elif "close" in their_choice:
            time.sleep(0.75)
            typer("Closing the tab.")
            sys.exit()
        elif their_choice=="null":
            time.sleep(2)
            null()
        else:
            continue

    if current_user=="Admin":
        time.sleep(1)
        typer("Welcome Admin. Here is the current list of users and their passwords:")
        time.sleep(0.75)
        for user in users:
            print(f"{user[0]} : {user[1]}")
            time.sleep(0.5)
        while True:
            typer("Would you like to sign out or delete an account?")
            another_choice=input("").lower()
            time.sleep(0.75)
            if "out" in another_choice:
                typer("Signing out.")
                another_choice="SignOut"
            elif "delete" in another_choice:
                while True:
                    typer("Which account do you want to delete?")
                    delete_account=input("")
                    time.sleep(0.75)
                    loop_helper=0
                    doesnt_exist=False
                    while True:
                        try:
                            if delete_account==users[loop_helper][0]:
                                break
                            else:
                                loop_helper+=1
                        except:
                            typer("That username does not exist.")
                            doesnt_exist=True
                            break
                    if doesnt_exist==True:
                        continue
                    if delete_account=="Admin":
                        typer("That account cannot be deleted.")
                        continue
                    elif delete_account=="Guest":
                        typer("That account cannot be deleted.")
                        continue
                    else:
                        users=list(users)
                        del users[loop_helper]
                        users=tuple(users)
                        another_choice="Deleted"
                        typer(f"{delete_account} has been deleted.")
                        time.sleep(0.75)
                        typer("Here is the new list of users and their passwords:")
                        for user in users:
                            print(f"{user[0]} : {user[1]}")
                            time.sleep(0.5)
                        break
            if another_choice=="SignOut":
                time.sleep(0.75)
                break
            elif another_choice=="Deleted":
                time.sleep(0.75)
                continue
    else:
        time.sleep(1)
        typer(f"Welcome {current_user}.")
        time.sleep(0.75)
        while True:
            typer("Would you like to sign out? (you can't do anything)")
            one_more_choice=input("").lower()
            time.sleep(1)
            if "yes" in one_more_choice:
                break