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

def panic(): #if something goes wrong we panic
    typer("AAHHHHHHHH")
    sys.exit()

while True:
    typer("How many classes do you have?")
    try:
        num_of_classes=int(input("")) #ask for an integer input
    except:
        time.sleep(0.75)
        typer("Please put in a valid number.") #if they don't put in an integer we tell them to put it one
    else:
        break

#set some helpful lists
list_percentages=[]
letter_grade_list=[]

copy_of_num=num_of_classes #i don't want to change the original number
loop_helper=1 #i <3 loop_helper, it's always so helpful
time.sleep(0.25)
while copy_of_num>0:
    stringed_loop_helper=str(loop_helper) #convert loop_helper to a string
    last_number=stringed_loop_helper[len(stringed_loop_helper)-1] #get the last letter in loop_helper
    while True:
        time.sleep(0.75)
        #make sure that grammar is correct, even if 11, 12, and 13 will show up weird. i'm 100% sure that they do not have more than 10 classes
        if last_number=="1":
            typer(f"What is the percentage grade of your {stringed_loop_helper}st class?.")
        elif last_number=="2":
                typer(f"What is the percentage grade of your {stringed_loop_helper}nd class?.")
        elif last_number=="3":
                typer(f"What is the percentage grade of your {stringed_loop_helper}rd class?.")
        else:
                typer(f"What is the percentage grade of your {stringed_loop_helper}th class?.")
        try:
            grade_input=float(input("")) #get a float/decimal input
        except:
            time.sleep(0.75)
            typer("Please put in a valid decimal number.") #get angry at them
        else:
             break
    list_percentages.append(grade_input) #if the input passes then we add it to list_percentages
    copy_of_num-=1 #subtract one from copy_of_num
    loop_helper+=1 #add one to loop_helper

copy_of_num=num_of_classes #set this again
loop_helper=1 #and this
time.sleep(0.25)
while copy_of_num>0:
    #big boy brain checking
    for item in list_percentages:
        if item>=93:
            letter_grade="A"
        elif item>=90:
            letter_grade="A-"
        elif item>=87:
            letter_grade="B+"
        elif item>=83:
            letter_grade="B"
        elif item>=80:
            letter_grade="B-"
        elif item>=77:
            letter_grade="C+"
        elif item>=73:
            letter_grade="C"
        elif item>=70:
            letter_grade="C-"
        elif item>=67:
            letter_grade="D+"
        elif item>=63:
            letter_grade="D"
        elif item>=60:
            letter_grade="D-"
        elif item<60:
            letter_grade="F"
        else:
            break #if they SOMEHOW make this if-elif train break, break the loop
        letter_grade_list.append(letter_grade) #add the letter grade to letter_grade_list
    stringed_loop_helper=str(loop_helper) #convert loop_helper to a string
    last_number=stringed_loop_helper[len(stringed_loop_helper)-1] #get the last letter in loop_helper
    time.sleep(0.75)
    #grammar!
    if last_number=="1":
        typer(f"The letter grade of your {stringed_loop_helper}st class is {letter_grade_list[loop_helper-1]}.")
    elif last_number=="2":
        typer(f"The letter grade of your {stringed_loop_helper}nd class is {letter_grade_list[loop_helper-1]}.")
    elif last_number=="3":
        typer(f"The letter grade of your {stringed_loop_helper}rd class is {letter_grade_list[loop_helper-1]}.")
    else:
        typer(f"The letter grade of your {stringed_loop_helper}th class is {letter_grade_list[loop_helper-1]}.")
    #the same exact thing, wow i wonder if the loops are literally the exact same! that would be such a coincidence!
    copy_of_num-=1
    loop_helper+=1

grade_sum=sum(list_percentages) #get the sum of all values in the list list_percentages
average_grade=round(grade_sum/num_of_classes,2) #divide it by the number of classes and round to two decimal places
#more checking
if average_grade>=93:
    letter_grade="A"
elif average_grade>=90:
    letter_grade="A-"
elif average_grade>=87:
    letter_grade="B+"
elif average_grade>=83:
    letter_grade="B"
elif average_grade>=80:
    letter_grade="B-"
elif average_grade>=77:
    letter_grade="C+"
elif average_grade>=73:
    letter_grade="C"
elif average_grade>=70:
    letter_grade="C-"
elif average_grade>=67:
    letter_grade="D+"
elif average_grade>=63:
    letter_grade="D"
elif average_grade>=60:
    letter_grade="D-"
elif average_grade<60:
    letter_grade="F"
else:
    panic() #if they SOMEHOW make this if-elif train break, panic

#tell them their average grade percentage and average grade letter
time.sleep(1)
typer(f"Your average percentage grade is {average_grade}, so your average letter grade is {letter_grade}.")