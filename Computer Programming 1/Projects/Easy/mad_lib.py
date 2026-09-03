#Daniel DeLong, Madlib
import time,random

def typer(text): #my super simply typer
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

things_to_ask=["noun","verb","adjective","noun","verb ending in ing"] # list of things to ask the player
list_of_words=[] #we will store their answers in here

for word in things_to_ask: #for each word in the list
    time.sleep(0.75)
    if word=="adjective": #if it's adjective we will use "an" for proper grammer
        typer(f"Hey! Give me an {word}.")
    else: #if it's not adjective we do this
        typer(f"Hey! Give me a {word}.")
    inputted_word=input("") #get their input
    list_of_words.append(inputted_word) #put their answer in list_of_words

time.sleep(0.9)
typer("Generating your laughter.")
time.sleep(0.5)
typer("...")
time.sleep(0.5)
typer("...")
time.sleep(0.5)
typer("...")
time.sleep(2.5)
typer(f"Your trusty {list_of_words[0]} {list_of_words[1]}s beside you. \"Hey! Stop {list_of_words[1]}ing!\" They run off to investigate a {list_of_words[2]} {list_of_words[3]}, you following behind. You pick up the {list_of_words[3]}, then it dawns on you. You know you should do something to save yourself, but there is no point in {list_of_words[4]}.")
#this whole formatted string uses list indexing to find the word for each spot. so list_of_words[0] will grab our first answer, or the noun