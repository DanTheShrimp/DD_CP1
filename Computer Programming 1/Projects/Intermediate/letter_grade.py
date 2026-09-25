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
        time.sleep(0.75)
        typer("Please put in a valid number.")
    else:
        break

list_percentages=[]
letter_grade_list=[]

copy_of_num=num_of_classes
loop_helper=1
time.sleep(0.25)
while copy_of_num>0:
    stringed_loop_helper=str(loop_helper) #convert loop_helper to a string
    last_number=stringed_loop_helper[len(stringed_loop_helper)-1] #get the last letter in loop_helper
    while True:
        time.sleep(0.75)
        if last_number=="1":
            typer(f"What is the percentage grade of your {stringed_loop_helper}st class?.")
        elif last_number=="2":
                typer(f"What is the percentage grade of your {stringed_loop_helper}nd class?.")
        elif last_number=="3":
                typer(f"What is the percentage grade of your {stringed_loop_helper}rd class?.")
        else:
                typer(f"What is the percentage grade of your {stringed_loop_helper}th class?.")
        try:
            grade_input=float(input(""))
        except:
            time.sleep(0.75)
            typer("Please put in a valid number.")
        else:
             break
    list_percentages.append(grade_input)
    copy_of_num-=1
    loop_helper+=1

copy_of_num=num_of_classes
loop_helper=1
time.sleep(0.25)
while copy_of_num>0:
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
            break
        letter_grade_list.append(letter_grade)
    stringed_loop_helper=str(loop_helper) #convert loop_helper to a string
    last_number=stringed_loop_helper[len(stringed_loop_helper)-1] #get the last letter in loop_helper
    time.sleep(0.75)
    if last_number=="1":
        typer(f"The letter grade of your {stringed_loop_helper}st class is {letter_grade_list[loop_helper-1]}.")
    elif last_number=="2":
        typer(f"The letter grade of your {stringed_loop_helper}nd class is {letter_grade_list[loop_helper-1]}.")
    elif last_number=="3":
        typer(f"The letter grade of your {stringed_loop_helper}rd class is {letter_grade_list[loop_helper-1]}.")
    else:
        typer(f"The letter grade of your {stringed_loop_helper}th class is {letter_grade_list[loop_helper-1]}.")
    copy_of_num-=1
    loop_helper+=1

grade_sum=sum(list_percentages)
average_grade=round(grade_sum/num_of_classes,2)
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
time.sleep(1)
typer(f"Your average percentage grade is {average_grade}, so your average letter grade is {letter_grade}.")