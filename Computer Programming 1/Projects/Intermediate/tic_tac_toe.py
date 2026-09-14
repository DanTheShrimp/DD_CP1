#Daniel DeLong, Tic Tac Toe
import sys,time

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

board=[
    [" "," "," "], #setting the board to be an array, that way we can change individual spots
    [" "," "," "],
    [" "," "," "]
]
def print_board(): #this prints the board
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print("-|-|-")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print("-|-|-")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")

def input_getter(who): #i used "who" that way this function can be used for any player
    typer(f"It is {who}'s turn.")
    while True:
        time.sleep(0.75)
        typer("Which row do you want to go in (1-3)?")
        while True:
            try:
                which_row=int(input("")) #getting their input
            except:
                time.sleep(0.5)
                typer("Please input a valid number (1-3).") #if it isn't an integer, make them answer again
            else:
                if which_row!=1 and which_row!=2 and which_row!=3: #if it isn't 1, 2, or 3, make them answer again
                    time.sleep(0.5)
                    typer("Please input a valid number (1-3).")
                else:
                    which_row-=1 #we need to subtract one because indexing starts at 0
                    break
        time.sleep(0.75)
        #this next column part is the same as the row part but with which_column
        typer("Which column do you want to go in (1-3)?")
        while True:
            try:
                which_column=int(input(""))
            except:
                time.sleep(0.5)
                typer("Please input a valid number (1-3).")
            else:
                if which_column!=1 and which_column!=2 and which_column!=3:
                    time.sleep(0.5)
                    typer("Please input a valid number (1-3).")
                else:
                    which_column-=1
                    break
        time.sleep(1)
        if board[which_row][which_column]==" ": #if the space they've chosen is empty
            board[which_row][which_column]=who #set it to whoever's turn it is
            print_board() #print the new board
            break
        else:
            typer("That square is not available.") #if it isn't empty we loop the entire thing
            continue

def checking_for_win(who):
    win="" #set win to nothing for now

    #horizontal checking, checking each row for a win
    if board[0][0]==who and board[0][1]==who and board[0][2]==who:
        win=who
    elif board[1][0]==who and board[1][1]==who and board[1][2]==who:
        win=who
    elif board[2][0]==who and board[2][1]==who and board[2][2]==who:
        win=who

    #vertical checking, checking each column for a win
    elif board[0][0]==who and board[1][0]==who and board[2][0]==who:
        win=who
    elif board[0][1]==who and board[1][1]==who and board[2][1]==who:
        win=who
    elif board[0][2]==who and board[1][2]==who and board[2][2]==who:
        win=who

    #diagonal checking, checking each diagonal for a win
    elif board[0][0]==who and board[1][1]==who and board[2][2]==who:
        win=who
    elif board[0][2]==who and board[1][1]==who and board[2][0]==who:
        win=who
    
    if win=="X": #if win was set to "X"
        time.sleep(1)
        typer("Player X won!")
        sys.exit() #player X wins and end the program
    elif win=="O": #if win was set to "O"
        time.sleep(1)
        typer("Player O won!")
        sys.exit() #player O wins and eng the program
    else:
        return #if no one has won yet we exit the function

print_board() #print the board

#i don't need to check for the first time until someone has gone 3 times
input_getter("X") #look, i can just set who to "X" and not have to make two separate functions
input_getter("O")
input_getter("X")
input_getter("O")
input_getter("X")
checking_for_win("X") #now i need to check because player X has gone 3 times
input_getter("O")
checking_for_win("O") #i can also set who here to "O" and not have to make another function
input_getter("X")
checking_for_win("X")
input_getter("O")
checking_for_win("O")
input_getter("X")
checking_for_win("X")
#the only way to have gotten here is if no one has won after filling all nine squares
time.sleep(1)
typer("It's a tie.")
sys.exit() #no one wins and end the program