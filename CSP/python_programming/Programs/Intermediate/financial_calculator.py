#DD Period 7 Financial Calculator

import sys #this is going to be used later on
print("Hello! I am your personal financial calculator. Please type in all of the information I require.")

income = float(input("How much do you make each month?\n"))
rent = float(input("How much does your rent cost?\n"))
utilities = float(input("How much do your utilities cost?\n"))
groceries = float(input("How much do your groceries cost?\n"))
transportation = float(input("How much does your transportation cost?\n"))

savings = income*0.1
income_left_after_savings = income*0.9

income_left = income_left_after_savings-(rent+utilities+groceries+transportation)
total_expenses = rent+utilities+groceries+transportation
percentage_expenses = total_expenses/income_left_after_savings
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

print("You will be saving $", round(savings, 2), "every month!")
print("That means you will be saving $", round(savings*12, 2), "each year!")
print("You will have $", round(income_left, 2), "after all of your expenses.")
print("And you will have $", round(income_left*12, 2), "to spend each year." )

if percentage_expenses == 50:
    print("Nice job, or not. You are spending ", round(percentage_expenses*100, 2) + "% of your monthly income on expenses.")

elif percentage_expenses << 50:
    print("Also, you are spending", round(percentage_expenses*100, 2) + "% of your monthly income on expenses. Nice job! That isn't that much!")

elif percentage_expenses >> 50:
    print("You need to get help. Your monthly expenses are", round(percentage_expenses*100, 2) + "% of your monthly income.")

print("Here is a more detailed analysis!")
print("You are spending ", round((rent/income_left_after_savings)*100, 2) + "% of your monthly earnings on rent.")
print("You are spending ", round((utilities/income_left_after_savings)*100, 2) + "% of your monthly earnings on utilities.")
print("You are spending ", round((groceries/income_left_after_savings)*100, 2) + "% of your monthly earnings on groceries.")
print("You are spending ", round((transportation/income_left_after_savings)*100, 2) + "% of your monthly earnings on transportation.")
