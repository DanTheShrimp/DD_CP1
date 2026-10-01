#Daniel DeLong, Factorial Calculator
import time,math

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
            player_num_list=[player_number]
            break
    if player_number<0: #if they chose an integer below zero, we loop back to the loop at the start
        continue
    else: #do math
        break

factorialed_num=map(math.factorial,player_num_list) #using the math module to factorialize every number in our list
factorialed_list=list(factorialed_num) #turn it back into a list

#print the answer
time.sleep(1)
typer(f"{player_number}! (factorial) is {factorialed_list[-1]}.") #an index number of -1 grabs the last item in the list