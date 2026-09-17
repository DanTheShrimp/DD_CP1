
import time,random,keyboard,os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def basic_hacker():
    while True:
        number_to_print=random.randint(0,1)
        print(number_to_print,end="")
        do_new_line=random.randint(1,75)
        if do_new_line==1:
            print("")
        time.sleep(0.0001)

def advanced_hacker():
    while True:
        number_to_print=random.randint(0,1)
        try:
            if keyboard.read_key()!="":
                print(number_to_print,end="")
        except:
            time.sleep(0)
        do_new_line=random.randint(1,75)
        if do_new_line==1:
            print("")

while True:
    which_one=input("")
    if "basic" in which_one:
        clear_terminal()
        basic_hacker()
    elif "advanced" in which_one:
        clear_terminal()
        advanced_hacker()