import sys,time,random
#Make random number gen never pick the face down card, but before everything make the game pick a card, remove it, and set the face down as that card
slug=[
"                                               :===-:                                      -+*#*=-             ",
"                                              +#%%####=-                                  *#%%#%#*=            ",
"                                              =###***%##+-   :=++==-:-=+#*=-:=--         +##*++*##*=           ",
"                                              =###***#%###+--*%%#%%#**#%%%%##%%%*=     -+##++++#%#*=-          ",
"                                              :*%#*****+#%#*####*++#%##++*#%#*+*%#=: ::+#*++*+++*##+-          ",
"                                              -#%#*****+*##%%%***++*%%*+**##*++*#%%%%##%%#++*++**##+-          ",
"                                        -+*#######*****#***####*++*#%%%**#####%**###*####**##*+++*#+           ",
"                                       -*######%%%#**++#%**##%#***##**#%%%#**%##**#*++##++*##*++*##+           ",
"                            ---        =###****##%%#****#%***##**##**#**##*++++++*#****%**##*++**#*=           ",
"                          +*%%###*+--- -*####%%#**#%%#***##**#%#*##*#####%#*++++**#**+*#*##**+++##+            ",
"                         +#%#***#####***%%#*##%%#**#%%#**##**###*##****+*%*+++++*##***#####+++*#%*             ",
"                         +####%%##**#%%%%%%##*******#%%%####*####%##****##*+++++*##*+*%###****##=              ",
"                          +#####%##*#**#%%%%####*****#%%%%%%##**+++**###%##******##**#%####%%%%%*+-            ",
"                  ===++=+=+#%#***##############%##***#%*+===+*########***+*####%%%%%%%%%%#*+==-=*#*=           ",
"                 =*#%#%#%%%%%%%%%%#########*#####%%##+-=+#%#*****#******##%#*+=--------=+#########%*+-         ",
"                 +##***#####%%%%%%%%%%%%#%########*=-+#%#******######%###***####*=----+%#***#####**##*+        ",
"                -=*%##%%%%%#*##%%#####%%%%%%##*%%+-=*##***###%%#*+===++*##%##***##*++##**##*+++####**#*=       ",
"             -+**##%%%#####*########%%%##*##%%%+--=*%#***###*=::::::::::::-+#####**##**#%#=:::::-=###**#+-     ",
"            =*%%####%%%%%%######%%###########%+---+#*****##=:::::::::::::::::-+##%####%#+-::::::::-*%#**#*=    ",
"            -#%###%%%%#####%%%#%%%%%%%%####%#=---+#*++**##=:::::-=****=-::::::::-=+++=-::::---::::::+##**#*+   ",
"             =*%################*#######%%%#=---=*#*++*##=::::-+#####%##*-::::::::::::::-*###%#*+-::-=%##*#+=  ",
"               +*#%%##*######%%###%%###*###+----=##+++#%*-:::=*#####+--=+*=::::::::::::=#%%%*-:=#+::::=##**#=  ",
"                  ++*#%%%%%%%%%%%##*#######=----+#*+++#%+:::-*###%%*=:.:+#+-::::::::::=#####+:.-**=::::*##*#*- ",
"           :=+####%#***#%####%###%%%%###%%*-----+#*+++##+:::-####%%##**###*-::::::::::+#####%#####+-:::=##**#= ",
"           +#%####%%#%%%####%%##***###%%%#=-----+%*+++##*:::-*#####%######*-::::::::::+######%####+::::-##**#*-",
"           *##**#%%%#*###%%#############%*=-----+%*+++##+-::-+######%%####+-::::::::::-####%#####*-::::-*#*+*#=",
"           -+##########**###%%%%%##%%%%%%*--:---=##+++*%*-:::-+#%#########=::::::::::::-+####%%*-::::::-*#*+*#=",
"               =+*%%%######*#%######%####*-------*#*++*##+::::::=*######*=::==--::::=+-::-=+==-::::::::-*#++##=",
"                 #%%%%%%%%%%###%####%##%#=-------*%#*++*#*-:::::::-===--::::=%%+-::=#%=::::::::::::::::+##+*#*:",
"                 #%%%%%%%%%%###%####%##%#=-------*%#*++*#*-:::::::-===--::::=%%+-::=#%=::::::::::::::::+##+*#*:",
"                *#%##%%%#*##%%%%%%%######-------:-##**++##=:-::::::::::::::::-+%%%%%*-::::::::::::::::+%#*+##+ ",
"           -=++**%#########%%%#####%%%%#*--------:+##****#*-:::::::::::::::::::::::::::::::::::::::::+%#+**#*= ",
"          =*%%####%%%%%%########%%%#*###+----------*%#**+*#+-::::::::::::::::::::::::::::::::::::::-+%#++*#%*  ",
"          +##############%%%%%##########=--:--------*%##**##+-::::::::::::::::::::::::::::::::::::=#%*+**#%*+  ",
"          -*####%%%###*#**###%%%%%###%%*-------------*%#***#%*-::::::::::::::::::::::::::::::::::=##++*####*   ",
"            =*#%%#################%%%##+--------------*%##**#%*=::::::::::::::::::::::::::::::::+%#***##*#*+   ",
"               -+#%%%%#%%%%###%%%#**###=---------------*%#***###+-::::::::::::::::::::::::::::=#%****%*=*%#    ",
"               =#%##%######%##%%#####%*-----------------*%##***##+-:::::::::::::::::::::::::-*%#+**##=-+##-    ",
"               *####%%######%%%%%%%%##=-----------------=###****##+-:::::::::::::::::::::::=##*+++*#+-=##+     ",
"               -+#%########%%##%#####+-------------------+##***++*#+-:::::::::::::::::::::=##++++*#+--+##      ",
"                =*#%%%%%%%%%%%%%%##%#=--:-----------------*%*++++*##+::::::::::::::::::::=##*++++**--=##=      ",
"                +####%%####**%%#*###=---------------------+#*+++++*##=::::::::::::::::::-*#*++++*#+:-*#*:      ",
"                =+##%%%######%#==*%*----------------------+#*++++++*#*-:::::::::::::::::=##*++++*#+-=*#=       ",
"               =+##*++**###%%%*=*%#=--=*###%%%%####*++++**###***+++###+-::::::::::::::::-*#*+++++#*-=##-       ",
"            :-+##*=-----=+#%%%++##==*#%%##############%%%%%##******###*-::::::::::::::::-+#****++*#+=##-       ",
"           =*##+=------+##+=**+####%%################%%%%####*****##%##-:::::::::::::::::-##******#%*##=       ",
"         :=*#*=---------=---=+#%%#%###*#######*#############**##*#%**##=::::::::::::::::::=###*****#%%#+:      ",
"        ++*#+=--------------+#%%%############################*##%#+=*#*-:::::::::::::::::::-*#%%#***##%#*=     ",
"     -+##%%#=--------------=*%%%############%%%%%%%%%%%%%%%%%%#*+=-+#%=:::::::::::::::::::::::-+*%##***###+    ",
"   =**%%%##*=------------=+*%%%#**#######%#*+=-=-------=====------=*%*:::::::::::::::::::::::::::-*%#****##+-  ",
" -+#%%***###*+=--------=*#%%%######*#%%%*=-----------------------=*#*-:::::::::::::::::::::::::::::=#%#***#%*= ",
"=+#%#******#%%%%#####%%%%%########%%#*=-----==+++====----------=+##=::::::::::::::::::::::::::::::::-##***+##*:",
"=*%#*******#*################**#%%*=---==+#%#*++++**####*+++**###=-::::::::::::::::::::::::::::::::::+##**+*##=",
"=*###**######################%%#+=----=*%#=:::::::::::::::----:::::::::::::::::::::::::::::::::::::::=##*++*##=",
" +#%######################%%#+=-----=*#%+::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::=##*++*%# ",
"   *#%%%#############%%%%#+---------=%#+::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-#%*++*%#= ",
"      -+##%%%%%%##**++==------------=##=:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-*#*+*#%#   ",
"          +#%*+=---------------=*+=--+#*-:::::::::::::::::::::::::::::::::::::::::::::::::::::::::=*##%%%#     ",
"            *#%#*+==-----------=+#%#+==##+-:::::::::::::::::::::::::::::::::::::::::::::::::::::=*%%*+=        ",
"              -*###%%##**********##%%%###%%#*++==+========------==-------------------------++*#%%%*            ",
"                    +****########%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%#+-                "
]
def typer(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01) 
    print()
deck=[
    [" _____ ",
    "|\\   /|",
    "| \\ / |",
    "|  &  |",
    "| / \\ |",
    "|/___\\|"],

    [" _____ ",
    "|A .  |",
    "| /.\\ |",
    "|(_._)|",
    "|  |  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  ^  |",
    "|     |",
    "|  ^  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| ^ ^ |",
    "|     |",
    "|  ^  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| ^ ^ |",
    "|     |",
    "| ^ ^ |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| ^ ^ |",
    "|  ^  |",
    "| ^ ^ |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| ^ ^ |",
    "| ^ ^ |",
    "| ^ ^ |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| ^ ^ |",
    "|^ ^ ^|",
    "| ^ ^ |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|^ ^ ^|",
    "| ^ ^ |",
    "|^ ^ ^|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|____6|"],

    [" _____ ",
    "|10 ^ |",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "| ^ {)|",
    "|(.)% |",
    "| | % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "| ^ {(|",
    "|(.)%%|",
    "| |%%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "| ^ {)|",
    "|(.)%%|",
    "| |%%%|",
    "|_%%%>|"],

    [" _____ ",
    "|A _  |",
    "| ( ) |",
    "|(_'_)|",
    "|  |  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  &  |",
    "|     |",
    "|  &  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| & & |",
    "|     |",
    "|  &  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| & & |",
    "|     |",
    "| & & |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| & & |",
    "|  &  |",
    "| & & |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| & & |",
    "| & & |",
    "| & & |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| & & |",
    "|& & &|",
    "| & & |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|& & &|",
    "| & & |",
    "|& & &|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|& & &|",
    "|& & &|",
    "|& & &|",
    "|____6|"],

    [" _____ ",
    "|10 & |",
    "|& & &|",
    "|& & &|",
    "|& & &|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "| o {)|",
    "|o o% |",
    "| | % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "| o {(|",
    "|o o%%|",
    "| |%%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "| o {)|",
    "|o o%%|",
    "| |%%%|",
    "|_%%%>|"],

    [" _____ ",
    "|A_ _ |",
    "|( v )|",
    "| \\ / |",
    "|  .  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  v  |",
    "|     |",
    "|  v  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| v v |",
    "|     |",
    "|  v  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| v v |",
    "|     |",
    "| v v |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| v v |",
    "|  v  |",
    "| v v |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| v v |",
    "| v v |",
    "| v v |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| v v |",
    "|v v v|",
    "| v v |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|v v v|",
    "| v v |",
    "|v v v|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|v v v|",
    "|v v v|",
    "|v v v|",
    "|____6|"],

    [" _____ ",
    "|10 v |",
    "|v v v|",
    "|v v v|",
    "|v v v|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "|   {)|",
    "|(v)% |",
    "| v % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "|   {(|",
    "|(v)%%|",
    "| v%%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "|   {)|",
    "|(v)%%|",
    "| v%%%|",
    "|_%%%>|"],

    [" _____ ",
    "|A ^  |",
    "| / \\ |",
    "| \\ / |",
    "|  v  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  o  |",
    "|     |",
    "|  o  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| o o |",
    "|     |",
    "|  o  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| o o |",
    "|     |",
    "| o o |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| o o |",
    "|  o  |",
    "| o o |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| o o |",
    "| o o |",
    "| o o |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| o o |",
    "|o o o|",
    "| o o |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|o o o|",
    "| o o |",
    "|o o o|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|o o o|",
    "|o o o|",
    "|o o o|",
    "|____6|"],

    [" _____ ",
    "|10 o |",
    "|o o o|",
    "|o o o|",
    "|o o o|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "| /\\{)|",
    "| \\/% |",
    "|   % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "| /\\{(|",
    "| \\/%%|",
    "|  %%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "| /\\{)|",
    "| \\/%%|",
    "|  %%%|",
    "|_%%%>|"],
]
house_hand=[]
player_hand=[
    ["       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "       "]
]
pairtwo_list=[
    ["       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "       "]
]
def house_valuefinder(card):
    decklen=len(deck)
    chosenh_card=random.randint(1,decklen-1)
    house_hand.append(deck[chosenh_card])
    del deck[chosenh_card]
    if "A" in house_hand[card][1]:
        hc_value=1
    elif "J" in house_hand[card][1] or "Q" in house_hand[card][1] or "K" in house_hand[card][1]:
        hc_value=10
    elif "2" in house_hand[card][1]:
        hc_value=2
    elif "3" in house_hand[card][1]:
        hc_value=3
    elif "4" in house_hand[card][1]:
        hc_value=4
    elif "5" in house_hand[card][1]:
        hc_value=5
    elif "6" in house_hand[card][1]:
        hc_value=6
    elif "7" in house_hand[card][1]:
        hc_value=7
    elif "8" in house_hand[card][1]:
        hc_value=8
    elif "9" in house_hand[card][1]:
        hc_value=9
    elif "10" in house_hand[card][1]:
        hc_value=10
    return hc_value

def player_valuefinder(card):
    if card=="thing":
        decklen=len(deck)
        chosenp_card=random.randint(1,decklen-1)
        pairtwo_list.append(deck[chosenp_card])
        del deck[chosenp_card]
        help_my_pain_ease=(len(pairtwo_list))-1
        if "A" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=1
        elif "J" in pairtwo_list[help_my_pain_ease][1] or "Q" in pairtwo_list[help_my_pain_ease][1] or "K" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=10
        elif "2" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=2
        elif "3" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=3
        elif "4" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=4
        elif "5" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=5
        elif "6" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=6
        elif "7" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=7
        elif "8" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=8
        elif "9" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=9
        elif "10" in pairtwo_list[help_my_pain_ease][1]:
            pc_value=10
        return pc_value
    else:
        decklen=len(deck)
        chosenp_card=random.randint(1,decklen-1)
        player_hand.append(deck[chosenp_card])
        del deck[chosenp_card]
        if "A" in player_hand[card][1]:
            pc_value=1
        elif "J" in player_hand[card][1] or "Q" in player_hand[card][1] or "K" in player_hand[card][1]:
            pc_value=10
        elif "2" in player_hand[card][1]:
            pc_value=2
        elif "3" in player_hand[card][1]:
            pc_value=3
        elif "4" in player_hand[card][1]:
            pc_value=4
        elif "5" in player_hand[card][1]:
            pc_value=5
        elif "6" in player_hand[card][1]:
            pc_value=6
        elif "7" in player_hand[card][1]:
            pc_value=7
        elif "8" in player_hand[card][1]:
            pc_value=8
        elif "9" in player_hand[card][1]:
            pc_value=9
        elif "10" in player_hand[card][1]:
            pc_value=10
        return pc_value

def basic_printer(norm):
    typer("House's cards: Your cards:")
    if norm=="yes":
        printer_helper=0
        for item in deck[0]:
            print(f" {item}        {player_hand[1][printer_helper]}")
            printer_helper+=1
        printer_helper=0
        for item in house_hand[1]:
            print(f" {item}        {player_hand[2][printer_helper]}")
            printer_helper+=1
    elif norm=="yesnt":
        printer_helper=0
        for item in deck[0]:
            print(f" {item}        {player_hand[1][printer_helper]}   {player_hand[2][printer_helper]}")
            printer_helper+=1
        printer_helper=0
        for item in house_hand[1]:
            print(f" {item}        {player_hand[3][printer_helper]}   {player_hand[4][printer_helper]}")
            printer_helper+=1
    elif norm=="house":
        printer_helper=0
        for item in house_hand[0]:
            print(f" {item}        {player_hand[1][printer_helper]}")
            printer_helper+=1
        printer_helper=0
        for item in house_hand[1]:
            print(f" {item}        {player_hand[2][printer_helper]}")
            printer_helper+=1
    else:
        printer_helper=0
        for item in deck[0]:
            print(f" {item}        {player_hand[1][printer_helper]}   {player_hand[2][printer_helper]}")
            printer_helper+=1
        printer_helper=0
        for item in house_hand[1]:
            print(f" {item}        {player_hand[3][printer_helper]}   {player_hand[4][printer_helper]}")
            printer_helper+=1

def advanced_printer(hhandnum,phandnum1,phandnum2):
    try:
        printer_helper=0
        for item in hhandnum:
            print(f" {item}        {player_hand[phandnum1][printer_helper]}   {pairtwo_list[phandnum2][printer_helper]}")
            printer_helper+=1
    except IndexError:
        while printer_helper<6:
            print(f" {player_hand[0][printer_helper]}        {player_hand[0][printer_helper]}   {player_hand[0][printer_helper]}")
            printer_helper+=1

def checker(splitted,card1,card2,card3,card4,extra):
    if splitted=="no":
        split_able="no"
        if card1==1 and card2==1:
            typer(f"Your total card value is 2 or 12.")
        elif card1==1:
            if card2+11==21:
                typer("Blackjack! You win.")
                sys.exit()
            else:
                typer(f"Your total card value is {card2+1} or {card2+11}.")
        elif card2==1:
            if card1+11==21:
                typer("Blackjack! You win.")
                sys.exit()
            else:
                typer(f"Your total card value is {card1+1} or {card1+11}.")
        else:
            typer(f"Your total card value is {card1+card2}.")
    else:
        if extra==1:
            if card1==1 and card3==1:
                typer(f"Your total card value for pair one is 2 or 12.")
            elif card3==1:
                if card1+11==21:
                    typer("Blackjack! That pair is now locked.")
                    card3=1
                    pair1_locked="yes"
                else:
                    typer(f"Your total card value for pair one is {card1+1} or {card1+11}.")
                    pair1_locked="no"
            elif card1==1:
                if card3+11==21:
                    typer("Blackjack! That pair is now locked.")
                    card1=1
                    pair1_locked="yes"
                else:
                    typer(f"Your total card value for pair one is {card3+1} or {card3+11}.")
                    pair1_locked="no"
            else:
                typer(f"Your total card vaiue for pair one is {card1+card3}.")
        elif extra==2:
            if card2==1 and card4==1:
                typer(f"Your total card value for pair two is 2 or 12.")
            elif card4==1:
                if card2+11==21:
                    typer("Blackjack! That pair is now locked.")
                    card4=1
                    pair2_locked="yes"
                else:
                    typer(f"Your total card value for pair two is {card2+1} or {card2+11}.")
                    pair2_locked="no"
            elif card2==1:
                if card4+11==21:
                    typer("Blackjack! That pair is now locked.")
                    card2=1
                    pair2_locked="yes"
                else:
                    typer(f"Your total card value for pair two is {card4+1} or {card4+11}.")
                    pair2_locked="no"
            else:
                typer(f"Your total card vaiue for pair two is {card2+card4}.")
    if extra==1:
        return card1+card3
    elif extra==2:
        return card2+card4
    elif extra==3:
        return card1+card2

def house_checker(card1,card2,extra):
    if card1==1 and card2==1:
        typer(f"The House's total card value is 2 or 12.")
    elif card1==1:
        if card2+11==21:
            typer("Blackjack! The House wins.")
            sys.exit()
        else:
            typer(f"The House's total card value is {card2+1} or {card2+11}.")
    elif card2==1:
        if card1+11==21:
            typer("Blackjack! The House wins.")
            sys.exit()
        else:
            typer(f"The House's total card value is {card1+1} or {card1+11}.")
    else:
        typer(f"The House's total card value is {card1+card2}.")
    if extra==1:
        return card1+card2

extra=0
zero=0
hc0_value=house_valuefinder(0)
pc1_value=player_valuefinder(1)
hc1_value=house_valuefinder(1)
pc2_value=player_valuefinder(2)

def player_part():
    split_able="no"
    will_split="no"
    cards_drawn=0
    checker("no",pc1_value,pc2_value,zero,zero,extra)
    if pc1_value==pc2_value:
        split_able="yes"
    while True:
        if split_able=="yes":
            typer("You are able to split because your cards' values are equal. Do you want to split?")
            will_split=input("")
            if "yes" in will_split or "split" in will_split:
                pair1_bust=0
                pair2_bust=0
                typer("Hitting on both.")
                pc3_value=player_valuefinder(3)
                pc4_value=player_valuefinder(4)
                basic_printer("yesnt")
                pair1_value=checker("yes",pc1_value,pc2_value,pc3_value,pc4_value,1)
                pair2_value=checker("yes",pc1_value,pc2_value,pc3_value,pc4_value,2)
                time.sleep(0.5)
                loop_helper=5
                while True:
                    typer("Do you want to hit or stand on pair one?")
                    hit_stand=input("")
                    if "hit" in hit_stand:
                        typer("Hitting on pair one.")
                        pc5_value=player_valuefinder(loop_helper)
                        basic_printer("no")
                        if loop_helper==5:
                            advanced_printer(player_hand[0],loop_helper,0)
                            cards_drawn=1
                        elif loop_helper==6:
                            advanced_printer(player_hand[0],5,0)
                            advanced_printer(player_hand[0],loop_helper,0)
                            cards_drawn=2
                        elif loop_helper==7:
                            advanced_printer(player_hand[0],5,0)
                            advanced_printer(player_hand[0],6,0)
                            advanced_printer(player_hand[0],loop_helper,0)
                            cards_drawn=3
                        elif loop_helper==8:
                            advanced_printer(player_hand[0],5,0)
                            advanced_printer(player_hand[0],6,0)
                            advanced_printer(player_hand[0],7,0)
                            advanced_printer(player_hand[0],loop_helper,0)
                            cards_drawn=4
                        elif loop_helper==9:
                            advanced_printer(player_hand[0],5,0)
                            advanced_printer(player_hand[0],6,0)
                            advanced_printer(player_hand[0],7,0)
                            advanced_printer(player_hand[0],8,0)
                            advanced_printer(player_hand[0],loop_helper,0)
                            cards_drawn=5
                        elif loop_helper==10:
                            advanced_printer(player_hand[0],5,0)
                            advanced_printer(player_hand[0],6,0)
                            advanced_printer(player_hand[0],7,0)
                            advanced_printer(player_hand[0],8,0)
                            advanced_printer(player_hand[0],9,0)
                            advanced_printer(player_hand[0],loop_helper,0)
                            cards_drawn=6
                        if pc5_value==1:
                            if pair1_value+1>21:
                                pc5_value=21
                            elif pair1_value+1<22:
                                if pair1_value+11>21:
                                    pc5_value=1
                                elif pair1_value+11<22:
                                    pc5_value=11
                        pair1_value=pair1_value+int(pc5_value)
                        if pair1_value>21:
                            typer("You bust on pair one.")
                            pair1_bust=1
                            break
                        else:
                            if cards_drawn==0 and pc5_value==1:
                                typer(f"Your total card value for pair one is 21.")
                            else:
                                typer(f"Your total card value for pair one is {pair1_value}")
                        loop_helper+=1
                    elif "stand" in hit_stand:
                        typer(f"Standing on pair one. Your total value for pair one is {pair1_value}.")
                        break
                while True:
                    typer("Do you want to hit or stand on pair two?")
                    hit_stand=input("")
                    if "hit" in hit_stand:
                        typer("Hitting on pair two.")
                        pc6_value=player_valuefinder("thing")
                        basic_printer("no")
                        if cards_drawn==1:
                            advanced_printer(player_hand[0],5,1)
                        elif cards_drawn==2:
                            advanced_printer(player_hand[0],5,1)
                            advanced_printer(player_hand[0],6,2)
                        elif cards_drawn==3:
                            advanced_printer(player_hand[0],5,1)
                            advanced_printer(player_hand[0],6,2)
                            advanced_printer(player_hand[0],7,3)
                        elif cards_drawn==4:
                            advanced_printer(player_hand[0],5,1)
                            advanced_printer(player_hand[0],6,2)
                            advanced_printer(player_hand[0],7,3)
                            advanced_printer(player_hand[0],8,4)
                        elif cards_drawn==5:
                            advanced_printer(player_hand[0],5,1)
                            advanced_printer(player_hand[0],6,2)
                            advanced_printer(player_hand[0],7,3)
                            advanced_printer(player_hand[0],8,4)
                            advanced_printer(player_hand[0],9,5)
                        elif cards_drawn==6:
                            advanced_printer(player_hand[0],5,1)
                            advanced_printer(player_hand[0],6,2)
                            advanced_printer(player_hand[0],7,3)
                            advanced_printer(player_hand[0],8,4)
                            advanced_printer(player_hand[0],9,5)
                            advanced_printer(player_hand[0],10,6)
                        if pc6_value==1:
                            if pair2_value+1>21:
                                pc6_value=21
                            elif pair2_value+1<22:
                                if pair2_value+11>22:
                                    pc6_value=1
                                else:
                                    pc6_value=11
                        pair2_value=pair2_value+pc6_value
                        if pair2_value>21 and pair1_bust==1:
                            typer("You bust on both pairs. You lose.")
                            sys.exit()
                        elif pair2_value>21:
                            typer("You bust on pair two.")
                            break
                        else:
                            typer(f"Your total card value for pair two is {pair2_value}.")
                        loop_helper+=1
                    elif "stand" in hit_stand:
                        typer(f"Standing on pair two. Your total value for pair two is {pair2_value}.")
                        break
            else:
                not_split=1
                break
        else:
            not_split=1
            break
    if not_split==1:
        loop_helper=3
        pair1_value=int(checker(0,pc1_value,pc2_value,zero,zero,3))
        while True:
            typer("Do you want to hit or stand?")
            hit_stand=input("")
            if "hit" in hit_stand:
                typer("Hitting.")
                pc5_value=player_valuefinder(loop_helper)
                basic_printer("yes")
                if loop_helper==3:
                    advanced_printer(player_hand[0],loop_helper,0)
                    cards_drawn=1
                elif loop_helper==4:
                    advanced_printer(player_hand[0],3,0)
                    advanced_printer(player_hand[0],loop_helper,0)
                    cards_drawn=2
                elif loop_helper==5:
                    advanced_printer(player_hand[0],3,0)
                    advanced_printer(player_hand[0],4,0)
                    advanced_printer(player_hand[0],loop_helper,0)
                    cards_drawn=3
                elif loop_helper==6:
                    advanced_printer(player_hand[0],3,0)
                    advanced_printer(player_hand[0],4,0)
                    advanced_printer(player_hand[0],5,0)
                    advanced_printer(player_hand[0],loop_helper,0)
                    cards_drawn=4
                elif loop_helper==7:
                    advanced_printer(player_hand[0],3,0)
                    advanced_printer(player_hand[0],4,0)
                    advanced_printer(player_hand[0],5,0)
                    advanced_printer(player_hand[0],6,0)
                    advanced_printer(player_hand[0],loop_helper,0)
                    cards_drawn=5
                elif loop_helper==8:
                    advanced_printer(player_hand[0],3,0)
                    advanced_printer(player_hand[0],4,0)
                    advanced_printer(player_hand[0],5,0)
                    advanced_printer(player_hand[0],6,0)
                    advanced_printer(player_hand[0],7,0)
                    advanced_printer(player_hand[0],loop_helper,0)
                    cards_drawn=6
                if pc5_value==1:
                    if pair1_value+1>21:
                        pc5_value=21
                    elif pair1_value+1<22:
                        if pair1_value+11>22:
                            pc5_value=1
                        else:
                            pc5_value=11
                pair1_value=pair1_value+int(pc5_value)
                if pair1_value>21:
                    typer("You bust.")
                    sys.exit()
                else:
                    typer(f"Your total card value is {pair1_value}.")
                loop_helper+=1
            elif "stand" in hit_stand:
                typer(f"Standing. Your total card value is {pair1_value}.")
                break
    def house_part():
        typer("The House will now reveal their card. Then they will hit until they reach 17 or more, or bust.")
        time.sleep(1)
        while True:
            basic_printer("house")
            time.sleep(1)
            if "yes" in will_split or "split" in will_split:
                hcard_helper=2
                loop_helper=(len(player_hand))-1
                if hc0_value+hc1_value>17:
                    loop_helper=11
                    break
                next_hcard=house_valuefinder(hcard_helper)
                if loop_helper==5:
                    advanced_printer(house_hand[2],loop_helper,1)
                    time.sleep(1)
                elif loop_helper==6:
                    advanced_printer(house_hand[2],5,1)
                    advanced_printer(house_hand[3],loop_helper,2)
                    time.sleep(1)
                elif loop_helper==7:
                    advanced_printer(house_hand[2],5,1)
                    advanced_printer(house_hand[3],6,2)
                    advanced_printer(house_hand[4],loop_helper,3)
                    time.sleep(1)
                elif loop_helper==8:
                    advanced_printer(house_hand[2],5,1)
                    advanced_printer(house_hand[3],6,2)
                    advanced_printer(house_hand[4],7,3)
                    advanced_printer(house_hand[5],loop_helper,4)
                    time.sleep(1)
                elif loop_helper==9:
                    advanced_printer(house_hand[2],5,1)
                    advanced_printer(house_hand[3],6,2)
                    advanced_printer(house_hand[4],7,3)
                    advanced_printer(house_hand[5],8,4)
                    advanced_printer(house_hand[6],loop_helper,5)
                    time.sleep(1)
                elif loop_helper==10:
                    advanced_printer(house_hand[2],5,1)
                    advanced_printer(house_hand[3],6,2)
                    advanced_printer(house_hand[4],7,3)
                    advanced_printer(house_hand[5],8,4)
                    advanced_printer(house_hand[6],9,5)
                    advanced_printer(house_hand[7],loop_helper,6)
                    time.sleep(1)
                house_total=house_checker(hc0_value,hc1_value,1)
                time.sleep(0.5)
                if next_hcard==1:
                    if house_total+1>21:
                        next_hcard=21
                    elif house_total+1<22:
                        if house_total+11>22:
                            next_hcard=1
                        else:
                            next_hcard=11
                house_total=house_total+int(next_hcard)
                if house_total>21:
                    typer("The House busts.")
                    sys.exit()
                else:
                    if house_total>pair1_value and house_total<pair2_value:
                        typer("You lose on pair one.")
                        sys.exit()
                    elif house_total>pair2_value and house_total<pair1_value:
                        typer("You lose on pair two.")
                        sys.exit()
                    elif house_total>pair1_value and house_total>pair2_value:
                        typer("You lose on both pairs.")
                        sys.exit()
                    elif house_total<pair1_value and house_total<pair2_value:
                        typer("You win on both pairs.")
                        sys.exit()
                    elif house_total==pair1_value:
                        typer("You push on pair one.")
                        sys.exit()
                    elif house_total==pair2_value:
                        typer("You push on pair two.")
                        sys.exit()
                    elif house_total==pair2_value:
                        typer("You push on both pairs.")
                        sys.exit()
                loop_helper+=1
            else:
                loop_helper=(len(player_hand))-1
                next_hcard=house_valuefinder(2)
                if hc0_value+hc1_value>17:
                    loop_helper=11
                    break
                if loop_helper==2:
                    advanced_printer(house_hand[2],loop_helper,0)
                    time.sleep(1)
                elif loop_helper==3:
                    advanced_printer(house_hand[2],3,0)
                    advanced_printer(house_hand[3],loop_helper,0)
                    time.sleep(1)
                elif loop_helper==4:
                    advanced_printer(house_hand[2],3,0)
                    advanced_printer(house_hand[3],4,0)
                    advanced_printer(house_hand[4],loop_helper,0)
                    time.sleep(1)
                elif loop_helper==5:
                    advanced_printer(house_hand[2],3,0)
                    advanced_printer(house_hand[3],4,0)
                    advanced_printer(house_hand[4],5,0)
                    advanced_printer(house_hand[5],loop_helper,0)
                    time.sleep(1)
                elif loop_helper==6:
                    advanced_printer(house_hand[2],3,0)
                    advanced_printer(house_hand[3],4,0)
                    advanced_printer(house_hand[4],5,0)
                    advanced_printer(house_hand[5],6,0)
                    advanced_printer(house_hand[6],loop_helper,0)
                    time.sleep(1)
                elif loop_helper==7:
                    advanced_printer(house_hand[2],3,0)
                    advanced_printer(house_hand[3],4,0)
                    advanced_printer(house_hand[4],5,0)
                    advanced_printer(house_hand[5],6,0)
                    advanced_printer(house_hand[6],7,0)
                    advanced_printer(house_hand[7],loop_helper,0)
                    time.sleep(1)
                house_total=house_checker(hc0_value+hc1_value,next_hcard,1)
                time.sleep(0.5)
                if next_hcard==1:
                    if house_total+1>21:
                        next_hcard=21
                    elif house_total+1<22:
                        if house_total+11>22:
                            next_hcard=1
                            house_total=house_total+int(next_hcard)
                        else:
                            next_hcard=11
                            house_total=house_total+int(next_hcard)
                if house_total>21:
                    typer("The House busts.")
                    sys.exit()
                else:
                    if house_total>pair1_value:
                        typer("You lose.")
                        sys.exit()
                    elif house_total<pair1_value:
                        typer("You win.")
                        sys.exit()
                    elif house_total==pair1_value:
                        typer("You push.")
                        sys.exit()
                loop_helper+=1
    house_part()

def slug_logo():
    for item in slug:
        print(item)
    time.sleep(3)
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

def menu():
    typer("Welcome to Doomslug Blackjack.")
    time.sleep(0.75)
    typer("Here are the rules:")
    time.sleep(0.5)
    typer("1: You will be given 2 cards, hitting means you get another card; standing means you stop. The House will have 2 cards, but one will be hidden.")
    time.sleep(0.25)
    typer("2: Number cards are their own number in value.")
    time.sleep(0.25)
    typer("3: Aces are worth 1 or 11, Face cards are worth 10.")
    time.sleep(0.25)
    typer("4: Always assume the House has a 10 hidden.")
    time.sleep(0.25)
    typer("5: Do not go over 21, or you bust and lose.")
    time.sleep(1)

    basic_printer("yes")
    player_part()

menu()