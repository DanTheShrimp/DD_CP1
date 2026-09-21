#Daniel DeLong, Crew Shares
import time,random
def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

while True:
    typer("My system memory has been wiped. Please input the number of crew on Yondu's ship, not including Yondu and Peter.")
    try:
        number_of_crew=int(input("")) #ask for the number of crew, making sure it's a number
    except:
        time.sleep(0.75)
    else:
        break #if it is a number we exit this loop

loop_helper=1 #set our handy-dandy loop_helper
list_of_names=[] #set our list_of_names
while number_of_crew>0: #while the number of crew is greater than 0
    stringed_loop_helper=str(loop_helper) #convert loop_helper to a string
    last_number=stringed_loop_helper[len(stringed_loop_helper)-1] #get the last letter in loop_helper
    #this chunk below just makes sure that we print with proper grammar
    if last_number=="1":
        typer(f"What is the name of the {loop_helper}st crew member?") #so we could have the 13334536771 crew member but it would still print correctly
    elif last_number=="2":
        typer(f"What is the name of the {loop_helper}nd crew member?")
    elif last_number=="3":
        typer(f"What is the name of the {loop_helper}rd crew member?")
    else:
        typer(f"What is the name of the {loop_helper}th crew member?")
    name=input("").title().strip() #get the name of the crew member, capitalizing all the letters that start a word and stripping excess white space away
    list_of_names.append(name) #tacking it onto the end of out list of names
    loop_helper+=1 #add one to loop_helper
    number_of_crew-=1 #subtract one from number_of_crew
    time.sleep(0.75) #wait a little

total_credits=random.randint(500,5000)*10 #get a random number between 500 and 5000,
yondu_share=round(total_credits*0.13,2) #take 13% of total_credits and round it to the 2nd decimal place
remaining_credits=total_credits-yondu_share #subtract yondu's share from total credits to get remaining credits
peter_share=round(remaining_credits*0.11,2) #take 11% of remaining_credits and round it to the 2nd decimal place
remaining_credits-=peter_share #subtract peter's share from remaining credits

number_of_crew=loop_helper-1 #get our number_of_crew back using logic
credits_per_crew=round(remaining_credits/(number_of_crew+2),2) #divide the rest of the credits by the number_of_crew plus 2, round it to two decimal places
typer(f"The most recent mission earned {total_credits} credits.") #print the information our user needs
typer(f"Yondu's share: {round(yondu_share+credits_per_crew,2)} credits.") #more rounding just in case
typer(f"Peter's share: {round(peter_share+credits_per_crew,2)} credits.")

loop_helper=0 #set our loop_helper to 0 because we gonna do some indexing
while number_of_crew>0: #same loop as before
    try:
        typer(f"{list_of_names[loop_helper]}'s share: {round(credits_per_crew,2)} credits.") #except now we print stuff instead of getting inputs
    except:
        break #if we get an error we just break the loop
    else:
        #if no error occurs then we add one to loop_helper and subtract one from number_of_crew
        loop_helper+=1
        number_of_crew-=1