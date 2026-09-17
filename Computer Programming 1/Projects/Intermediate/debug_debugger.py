#Daniel DeLong, Debug with the Debugger


#OG Code
"""# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = input("How many would you like? ")

total = price * quantity

discounted_total = total - 2 * 0.10

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snackName)
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(price))
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits"""

#Changed Code
# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ").title() #added .title()
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? ")) #added int()

total = price * quantity

tax_rate = 0.08
total_with_tax = total * (1+tax_rate) #tax is applied by making the number go up, so i added the tax_rate to 1 and multiplied it by the total to get the accurate tax

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) #was previously snackName, so i changed it to snack_name
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(total)) #changed price in the parenthesis to total
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")