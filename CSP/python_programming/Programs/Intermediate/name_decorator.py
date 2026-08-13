#DD Period 7 Name Decorator

import time
import sys
name = input("Good day user. I am the Name Decorator. Please input your name. ").title()
print(f"Thank you {name}, I will now generate examples for your custom name.")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")

print("Thank you for waiting. Here are your base options.")
print("1. (:<"+name+">:)")
time.sleep(1)
print("2. 123"+name+"456")
time.sleep(1)
print("3. www"+name+"www")
time.sleep(1)
print("4. ._."+name+"._.")
time.sleep(1)
print("5. UwU"+name+"UwU")
time.sleep(1)
print("6. D:"+name+":D")
time.sleep(1)

more = input("If you are unhappy with the premade options, please type 'More'. If you like those six above, please type the number you like. ").capitalize()

if more == "More":
    extra = input("I see. Please type the symbol you would like to decorate your name with. ")
    print("Here is your custom name.")
    time.sleep(1)
    print(extra+extra+extra+name+extra+extra+extra)

else:
    print("Please wait.")
    time.sleep(3)
    if more == "1":
        print("Here is your custom name.")
        time.sleep(1)
        print("(:<"+name+">:)")

    elif more == "2":
        print("Here is your custom name.")
        time.sleep(1)
        print("123"+name+"456")

    elif more == "3":
        print("Here is your custom name.")
        time.sleep(1)
        print("www"+name+"www")

    elif more == "4":
        print("Here is your custom name.")
        time.sleep(1)
        print("._."+name+"._.")

    elif more == "5":
        print("Here is your custom name.")
        time.sleep(1)
        print("UwU"+name+"UwU")

    elif more == "6":
        print("Here is your custom name.")
        time.sleep(1)
        print("D:"+name+":D")

    elif more != "1" "2" "3" "4" "5" "6":
        print("Grrrrrrr, please input one of the options!")
        sys.exit()