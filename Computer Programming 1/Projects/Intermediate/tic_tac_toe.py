#Daniel DeLong, Tic Tac Toe
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
            try:
                which_row=int(input(""))
            except:
                typer("Please input a valid number (1-3).")
            else:
                if which_row!=1 and which_row!=2 and which_row!=3:
                    typer("Please input a valid number (1-3).")
                else:
                    which_row-=1
                    break
        typer("Which column do you want to go in (1-3)?")
        while True:
            try:
                which_column=int(input(""))
            except:
                typer("Please input a valid number (1-3).")
            else:
                if which_column!=1 and which_column!=2 and which_column!=3:
                    typer("Please input a valid number (1-3).")
                else:
                    which_column-=1
                    break
        if board[which_row][which_column]==" ":
            board[which_row][which_column]=who
            break
        else:
            typer("That square is not available.")
            continue

def checking_for_win(who):
    win=" "

    #horizontal checking
    if board[0][0]==who and board[0][1]==who and board[0][2]==who:
        win=who
    elif board[1][0]==who and board[1][1]==who and board[1][2]==who:
        win=who
    elif board[2][0]==who and board[2][1]==who and board[2][2]==who:
        win=who

    #vertical checking
    elif board[0][0]==who and board[1][0]==who and board[2][0]==who:
        win=who
    elif board[0][1]==who and board[1][1]==who and board[2][1]==who:
        win=who
    elif board[0][2]==who and board[1][2]==who and board[2][2]==who:
        win=who

    #diagonal checking
    elif board[0][0]==who and board[1][1]==who and board[2][2]==who:
        win=who
    elif board[0][2]==who and board[1][1]==who and board[2][0]==who:
        win=who
    
    if win=="X":
        typer("Player X won!")
        sys.exit()
    elif win=="O":
        typer("Player O won!")
        sys.exit()
    else:
        return