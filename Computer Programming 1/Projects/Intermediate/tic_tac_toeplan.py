#Daniel DeLong, Tic Tac Toe Plan

#make a list for the board:
"""
board=[
[" "," "," "],
[" "," "," "],
[" "," "," "]
]

final board should look like this

 | | 
-|-|-
 | | 
-|-|-
 | | 

"""

#then I can ask the player to input which row they want to go into, subtract 1 because indexing starts at 0
#then I can ask the player to input which column they want to go into, subtract 1 because indexing starts at 0

#turn it into something like this:
#if board[x_input_one][player_input_two]==" ":
    #board[x_input_one][player_input_two]="X"

#so basically if the space they want to go into is empty, we let them go into it. if it isn't empty then we don't let them
#if we do replace the spot then we print a new board, with the new spot taken

#then for the o player we can just do the same exact code but with different variables

#after every turn we can check if someone won

#and do something fancy by setting an argument for a function to "X" or "O"
"""
def checking_for_win(argument)
    win=" "

    #horizontal checking
    if board[0][0]==argument and board[0][1]==argument and board[0][2]==argument:
        win=argument
    elif board[1][0]==argument and board[1][1]==argument and board[1][2]==argument:
        win=argument
    elif board[2][0]==argument and board[2][1]==argument and board[2][2]==argument:
        win=argument

    #vertical checking
    elif board[0][0]==argument and board[1][0]==argument and board[2][0]==argument:
        win=argument
    elif board[0][1]==argument and board[1][1]==argument and board[2][1]==argument:
        win=argument
    elif board[0][2]==argument and board[1][2]==argument and board[2][2]==argument:
        win=argument

    #diagonal checking
    elif board[0][0]==argument and board[1][1]==argument and board[2][2]==argument:
        win=argument
    elif board[0][2]==argument and board[1][1]==argument and board[2][0]==argument:
        win=argument
    
    if win=="X"
        do something like say the x player won and end the program
    elif win=="O"
        do something like say the o player won and end the program
"""


#even though the assignment doesn't include coding the actual thing i will anyway, i have become emotionally attached to this

import sys,time

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

board=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
def print_board():
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print("-|-|-")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print("-|-|-")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")

def input_getter(who):
    typer(f"It is {who}'s turn.")
    while True:
        typer("Which row do you want to go in (1-3)?")
        while True:
            which_row=input("")
            if which_row!=1 or which_row!=2 or which_row!=3:
                typer("Please input a valid number (1-3).")
            else:
                break
        typer("Which column do you want to go in (1-3)?")
        while True:
            which_column=input("")
            if which_column!=1 or which_column!=2 or which_column!=3:
                typer("Please input a valid number (1-3).")
            else:
                break
        if board[which_row][which_column]==" ":
            board[which_row][which_column]=who