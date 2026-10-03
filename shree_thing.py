#SM Shopping list manager

#A Bunch of Color codes for terminal text styling for yk coolness *Enter sigma music*

# DAN - this is highly suspicious, this isn't even hex codes
# DAN - also, we were taught to NOT fully capitalize variable names
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
STRIKE = "\033[9m"
BOLD = "\033[1m"

# DAN - why not name it something normal like shopping_list?
ict = [] #This is the list that will store the items

#asking for their choice # DAN - ah, look at this! the classic lowercase comment, while most of the others are capitalized. this makes me think that he kept some of the generated comments and made this one himself

# DAN - the backslash n is useless, why add it?
while True:
    print(f"\n {BLUE} ShreeTech {YELLOW}Shopping List Manager!")
    print(f"{GREEN} Type 1 to View list")
    print("Type 2 to Add item")
    print("Type 3 to Remove item")
    print("Type 4 to Exit")
    print("")
    choice = input(f"{GREEN}choose number between 1-4: ")

#For choice 1 # DAN - these comments aren't in line with the rest of the code, that makes me a little suspicious
    
    if choice == "1":
        if ict:
            print(f"\n {BOLD} Your list: ")
            for i, item in enumerate(ict, 1): # DAN - bro the class literally just learned about for loops and he is doing something like this?
                print(f"{i}. {item}")
        else:
            print("\nYour list is empty")

#For choice 2

    elif choice == "2":
        item = input("Enter item to add: ").strip()
        if item: # DAN - this if statement is useless, as long as the user put at least SOMETHING in it'll be true
            ict.append(item)
            print(f"\n'{item}' added!")
            print("Updated list:", ict) # DAN - no star for unpacking the list, even though we learned about it. 

#For choice 3
    
    elif choice == "3":
        if ict:
            print("\nYour list:", ict)
            try:
                idx = int(input(f"{BOLD} {RED} Enter item number to remove: ")) - 1
                removed = ict.pop(idx)
                print(f"\n'{STRIKE} {removed}' {RESET} {BOLD} {RED} removed!")
                print("Updated list:", ict)
            except (ValueError, IndexError): # DAN - you're telling me that he knows about try/except and knows the specific errors to look for when someone is inputting something here? also just having a blank except covers ALL errors, not just specific ones.
                print("Invalid selection")
        else:
            print("\nList is empty")

#For choice 4
    
    elif choice == "4":
        print(f"{BOLD} {YELLOW} Goodbye!")
        break

#IDIOT PROOFING
    
    else:
        print(f"{RED}{BOLD}Invalid choice{RESET}")
