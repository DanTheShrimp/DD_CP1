#Daniel DeLong, Factorial Calculator
import time

#get input
#check if it is an integer
#check if it is less than 0
#check if it is 0
    #if it is 0 then set answer to 1
#else
    #use a loop to multiply the input by every number below it

#super simple!

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

while True: #big loop
    while True: #loopdy loop in a loop
        typer("Please input a number, not decimal, above 0.")
        try:
            player_number=int(input("")) #make sure their input is an integer, not a float or string
        except:
            continue
        else:
            break
    if player_number<0: #if they chose an integer below zero, we loop back to the loop at the start
        continue
    elif player_number==0: #if they chose 0, set the answer to one and don't do the math later
        answer=1
        do_math="no"
        break
    elif player_number==1: #if they chose 1, set the answer to one and don't do the math later
        answer=1
        do_math="no"
        break
    else: #do math
        do_math="yes"
        break

copyof_playernumber=player_number #we need our player's input

#so this section first sets answer to player_number times player_number minus 1 (so if player_number=2 then we'd do 2*1)
if do_math=="yes":
    answer=player_number*(player_number-1)
    player_number-=1
    while player_number>1: #then as long as player number is above one (because we don't want to multiply by zero)
        answer=answer*(player_number-1) #do the same thing (don't worry, if player_number=2 then we multiply by one, subtract one (setting player_number to 1), and exit the loop)
        player_number-=1

#print the answer
time.sleep(1)
typer(f"{copyof_playernumber}! (factorial) is {answer}.")