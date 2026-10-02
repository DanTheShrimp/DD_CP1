# Daniel DeLong, Password Strength Checker Code
import time

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

# these are lists of all capital and lowercase letters, numbers, and special characters. i have set them to be tuples because i want them to be read-only and not be able to be changed
capital_tuple=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
#lower_tuple=tuple(word.lower() for word in capital_tuple) i used this to lower-ify every letter in capital_tuple, then i printed it and copied the result. i love laziness
lower_tuple=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
number_tuple=("1","2","3","4","5","6","7","8","9","0")
special_tuple=("!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",",",".","<",">","?","/","\\") # so special, i know

# here's the actual code:
while True:
    typer("Please input a strong password (8 characters, lowercase, uppercase, number, special character):")
    password_input=input("")

    # set some variables that will be used later on
    total_pass=0
    length_pass=False
    capital_pass=False
    lower_pass=False
    number_pass=False
    special_pass=False

    # do an initial check for password length
    if len(password_input)>=8:
        length_pass=True
        total_pass+=1

    #each of these loops go through every character and see if it occurs in any of the lists, so is "J" in capital_tuple, is "#" in number_tuple, etc
    for char in password_input:
        if char in capital_tuple:
            capital_pass=True
            total_pass+=1
            break
    for char in password_input:
        if char in lower_tuple:
            lower_pass=True
            total_pass+=1
            break
    for char in password_input:
        if char in number_tuple:
            number_pass=True
            total_pass+=1
            break
    for char in password_input:
        if char in special_tuple:
            special_pass=True
            total_pass+=1
            break

    # this assigns a string to strength and do_advice depending on the value of total_pass
    if total_pass==5:
        strength="Very Strong"
        do_advice="no"
    elif total_pass==4:
        strength="Strong"
        do_advice="yes"
    elif total_pass==3:
        strength="Medium"
        do_advice="yes"
    elif total_pass==2:
        strength="Weak"
        do_advice="yes"
    elif total_pass==1:
        strength="Very Weak"
        do_advice="yes"

    # printing all the necessary information
    typer(f"Password strength: {strength}.")
    if do_advice=="yes":
        typer("Here are all the areas you passed and failed in:")
        typer(f"Length of 8: {length_pass}.")
        typer(f"Capital letter: {capital_pass}.")
        typer(f"Lowercase letter: {lower_pass}.")
        typer(f"Number (0-9): {number_pass}.")
        typer(f"Special character: {special_pass}.")
    else:
        typer("Your password is perfect!")
    break