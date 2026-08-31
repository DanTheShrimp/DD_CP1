#Daniel DeLong, Average Grade
import time

def typer(text): #man i love this typer
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

classes=[]
grades=[]

typer("How many classes do you have?")
time.sleep(0.75)
while True:
    try:
        number_of_classes=int(input(""))
    except:
        typer("Please answer the question.")
    else:
        break

typer_helper=1
while number_of_classes !=0:
    time.sleep(1)
    if typer_helper==1:
        typer(f"What is the grade of your {typer_helper}st class?")
    elif typer_helper==2:
        typer(f"What is the grade of your {typer_helper}nd class?")
    elif typer_helper==3:
        typer(f"What is the grade of your {typer_helper}rd class?")
    else:
        typer(f"What is the grade of your {typer_helper}th class?")
    time.sleep(0.75)
    while True:
        try:
            inputted_grade=int(input(""))
        except:
            typer("Please answer the question.")
        else:
            grades.append(inputted_grade)
            break
    typer_helper+=1
    number_of_classes-=1

length_grades=float(len(grades))
sum_grades=float(sum(grades))
average_gpa=(sum_grades/length_grades)
