#Daniel DeLong, Average Grade
import time

def typer(text): #man i love this typer
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

grades=[] #this is going to be very useful for finding the average of the class GPAs

typer("How many classes do you have?")
time.sleep(0.75)
while True:
    try:
        number_of_classes=int(input("")) #asking for an input and making it an integer
    except:
        typer("Please answer the question.") #if it isn't an integer we make them input again
    else:
        break #if it is an integer we break the loop

typer_helper=1 #a little variable to help with a big task
while number_of_classes !=0: #while number of classes does not equal 0
    time.sleep(1)
    #this chunk makes sure that we are putting the right suffix after the number
    if typer_helper==1:
        typer(f"What is the GPA of your {typer_helper}st class?")
    elif typer_helper==2:
        typer(f"What is the GPA of your {typer_helper}nd class?")
    elif typer_helper==3:
        typer(f"What is the GPA of your {typer_helper}rd class?")
    else:
        typer(f"What is the GPA of your {typer_helper}th class?")
    time.sleep(0.75)
    while True:
        try:
            inputted_grade=float(input("")) #another input loop
        except:
            typer("Please answer the question.")
        else:
            grades.append(inputted_grade) #this time we append the inputted grade
            break
    typer_helper+=1 #every time the loop the loop runs we add one to typer_helper
    number_of_classes-=1 #ever time the loop runs we subtract one from number_of_classes

length_grades=float(len(grades)) #getting the length of the grades list
sum_grades=float(sum(grades)) #getting the sum of all integers in the grades list
average_gpa=round(sum_grades/length_grades,2) #dividing the sum of grades by the length of grades and rounding the answer to 2 decimal places

time.sleep(1)
typer(f"Your average GPA is {average_gpa}.") #typing the result