#Daniel DeLong, Interactive Introduction Program Pseudocode

#I want to do a random number generator, like coin flips, dice rolls, card pulls, random number, and a russian roulette



#Coin flip - coinflip_answer=random.randint(1,2), use an if statement to reassign coinflip_answer to either heads or tails

#Dice rolls - ask for which dice they want to roll, d4, d6, d8, d10, d% (100, it's 10 sides), d12, and d20, and store it in diceroll_answer. depending on what they input we will write if (placeholder) in (input):

#Card Pulls - all we have to do is have every card name in a list called cardpulls_deck, use random.randint(0,53) (we are including jokers), and display the answer.

#Random Number - literally the easiest one, ask for first number in the range (use a try: so they can't do a float or string), store it in randomnumber_one, do the same for the second number and store it in randomnumber_two

#Russian Roulette - ok this one will be fun.
#have a while True loop and a variable called loophelper that starts at 6. in the loop we have chance_of_death=random.randint(1,loophelper).
#we can ask if the user wants to point the, um, high powered water gun at themself or at the computer, store it in player_choice. if the number rolled in the randint == 1, then the gun fires. otherwise, we print a "click, it doesn't fire." if a click happens, we lower loophelper by one
#on the computer turn we use the same chance_of_death variable thing, but use a 50/50 chance to decide if the computer aims it at its cpu or at the player

#now, i do not condone to playing russian roulette, so i will not display the option to the player. instead, if they input "Roulette" when choosing which game to play, Russian Roulette will start