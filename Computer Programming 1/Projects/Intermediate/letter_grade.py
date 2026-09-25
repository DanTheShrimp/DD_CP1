#Daniel DeLong, What is My Grade
#for the grade percentages, i will base them off of this:
"""
A: 93+
A-: 90-93

B+: 87-90
B: 83-87
B-: 80-83

C+: 77-80
C: 73-77
C-: 70-73

D+: 67-70
D: 63-67
D-: 60-63

F: 60-
"""
#i think this is either really accurate or spot-on, becaused i guessed for every one of them

import sys, time

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

while True:
    typer("How many classes do you have?")
    try:
        num_of_classes=int(input(""))
    except:
        typer("Please put in a valid number.")
    else:
        break

list_percentages=() #tuple! we use tuple because we only need to add and read items from it, not delete items from it
#WAIT, TUPLES ARE ALMOST THE EQUIVALENT OF READ-ONLY! so that means lists are read-write, cool

copy_of_num=num_of_classes
loop_helper=1
while copy_of_num>0:
    stringed_loop_helper=str(loop_helper) #convert loop_helper to a string
    last_number=stringed_loop_helper[len(stringed_loop_helper)-1] #get the last letter in loop_helper
    while True:
        if last_number=="1":
            typer("put thing here")