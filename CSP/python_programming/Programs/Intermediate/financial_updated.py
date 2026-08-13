#DD Period 7 Financial Calculator, but updated!

import sys #this is going to be used later on
import time
print("Hello! I am your personal financial calculator. Please type in all of the information I require.")
time.sleep(2) #this is just to make it seem more realistic
def get_stuff(request):
    if request == "income":
        result = float(input("How much do you make each month?\n"))

    elif request == "rent" or "transportation":
        result = float(input(f"How much does your {request} cost?\n"))

    elif request == "utilities" or "groceries":
        result = float(input(f"How much do your {request} cost?\n"))

    return result

income = get_stuff("income")
time.sleep(1)
print("Thank you! Now I need to know about your expenses.")
time.sleep(1)
rent = get_stuff("rent")
time.sleep(1)
utilities = get_stuff("utilities")
time.sleep(1)
groceries = get_stuff("groceries")
time.sleep(1)
transportation = get_stuff("transportation")
time.sleep(1)
print("Thank you for all of the information! I am now calculating your finances.")
time.sleep(3) #again, just to make it seem more realistic

savings = income*0.1
income_left_after_savings = income*0.9

income_left = income_left_after_savings-(rent+utilities+groceries+transportation)
total_expenses = rent+utilities+groceries+transportation

if income_left_after_savings < total_expenses:
    print("I am unable to help you. Your finances are in ruins.")
    end = 1

elif income_left_after_savings > total_expenses:
    end = 0

if end == 1:
    sys.exit() #this is so we can stop the program from continuing if they are spending more than they earn

if total_expenses == 0:
    print("You must be lying! I refuse to help you.")
    sys.exit() #fool proofing. no lying allowed...

def percentage(type):
    if type == "total":
        result2 = round((total_expenses/income_left_after_savings)*100, 2)

    elif type == "rent":
        result2 = round((rent/income)*100 ,2)

    elif type == "utilities":
        result2 = round((utilities/income)*100, 2)

    elif type == "groceries":
        result2 = round((groceries/income)*100, 2)

    elif type == "transportation":
        result2 = round((transportation/income)*100, 2)

    return result2

if percentage("total") == 50:
    print(f"Nice job, or not. You are spending {percentage("total")}% of your monthly income on expenses.")

elif percentage("total") < 50:
    print(f"Also, you are spending {percentage("total")}% of your monthly income on expenses. Nice job! That isn't that much!")

elif percentage("total") > 50:
    print(f"You need to get help. Your monthly expenses are {percentage("total")}% of your monthly income.")

time.sleep(2)
print("Here is a more detailed analysis!")
print(f"You are spending {percentage("rent")}% of your monthly earnings on rent.")
time.sleep(1)
print(f"You are spending {percentage("utilities")}% of your monthly earnings on utilities.")
time.sleep(1)
print(f"You are spending {percentage("groceries")}% of your monthly earnings on groceries.")
time.sleep(1)
print(f"You are spending {percentage("transportation")}% of your monthly earnings on transportation.")
time.sleep(2)
print("Here is a summary of your finances!")

print("You will be saving $", round(savings, 2), "every month!")
time.sleep(1)
print("That means you will be saving $", round(savings*12, 2), "each year!")
time.sleep(1)
print("You will have $", round(income_left, 2), "after all of your expenses.")
time.sleep(1)
print("And you will have $", round(income_left*12, 2), "to spend each year." )
