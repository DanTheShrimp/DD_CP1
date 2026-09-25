#Daniel DeLong, Shopping List Manager
import time,sys

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

shopping_list=[
    "Milk",
    "Orange juice",
    "Chips",
    "Oreos",
    "10 cans of beans",
    "Baby food"
]
def add_item():
    typer("What item do you want to add to the list?")
    new_item=input("")
    shopping_list.append(new_item)

def cross_off():
    while True:
        typer("What item do you want to cross off?")