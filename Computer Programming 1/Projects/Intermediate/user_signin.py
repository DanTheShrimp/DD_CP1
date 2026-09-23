#Daniel DeLong, User Sign In
import time, sys

users=[
    ["Admin","noHackers_123"], #admin account
    ["Guest","guest123"], #guest account
    ["Pedro","tung67"], #pedro's account
    ["Daniel","lightw3aver_Storml1ght"] #daniel's account
]

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

number_of_attempts=0
def sign_in():
    while True:
        typer("Username:")
        username_input=input("")
        if username_input==users[0][0]:
            username_input=users[0][0]
            break

        if username_input==users[1][0]:
            username_input=users[1][0]
            break

        if username_input==users[2][0]:
            username_input=users[2][0]
            break

        if username_input==users[3][0]:
            username_input=users[3][0]
            break

        else:
            number_of_attempts+=1

        if number_of_attempts==3:
            typer("Too many failed attempts.")
            sys.exit()

def create_account():
    while True:
        username_exists=False
        typer("Account username:")
        create_username=input("")
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
    new_user=[create_username,create_password]
    users.append(new_user)
