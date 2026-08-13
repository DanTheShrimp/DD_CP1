// DD, LC, RV & JD 7th Final Project, Tic tac Toe

#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h>

char playername[2];
int player = 0;
int computer = 0;
char board[3][3]={{' ',' ',' '},
                {' ',' ',' '},
                {' ',' ',' '}};

// Fernando, print questions and variables

// Lindon, make board and double check/ fix bugs

// Daniel, print plays and figure out how to put symbols in squares computer turns

// Jesus, win conditions, if staments, check speling

void name(void){ // daniel and lindon
    printf("Hello, what are your initials (Two letters): \n");
    scanf("%s", &playername);
}

int checker(void){ // dan lindon and romeo
    //player check
    if(board[0][0] == 'X' && board[0][1] == 'X' && board[0][2] == 'X'){
        player = 1;
    }else if(board[1][0] == 'X' && board[1][1] == 'X' && board[1][2] == 'X'){
        player = 1;
    }else if(board[2][0] == 'X' && board[2][1] == 'X' && board[2][2] == 'X'){
        player = 1;
    }else if(board[0][0] == 'X' && board[1][0] == 'X' && board[2][0] == 'X'){
        player = 1;
    }else if(board[0][1] == 'X' && board[1][1] == 'X' && board[2][1] == 'X'){
        player = 1;
    }else if(board[0][2] == 'X' && board[1][2] == 'X' && board[2][2] == 'X'){
        player = 1;
    }else if(board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X'){
        player = 1;
    }else if(board[0][2] == 'X' && board[1][1] == 'X' && board[2][0] == 'X'){
        player = 1;
    }
    if(board[0][0] == 'O' && board[0][1] == 'O' && board[0][2] == 'O'){
        computer = 1;
    }else if(board[1][0] == 'O' && board[1][1] == 'O' && board[1][2] == 'O'){
        computer = 1;
    }else if(board[2][0] == 'O' && board[2][1] == 'O' && board[2][2] == 'O'){
        computer = 1;
    }else if(board[0][0] == 'O' && board[1][0] == 'O' && board[2][0] == 'O'){
        computer = 1;
    }else if(board[0][1] == 'O' && board[1][1] == 'O' && board[2][1] == 'O'){
        computer = 1;
    }else if(board[0][2] == 'O' && board[1][2] == 'O' && board[2][2] == 'O'){
        computer = 1;
    }else if(board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O'){
        computer = 1;
    }else if(board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == 'O'){
        computer = 1;
    }
    if (player == 1){ // dan and lindon
        printf("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|              %s wins!             |\n", playername);
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n");
        exit;

    }else if (computer == 1){
        printf("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|           Computer wins!          |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n");
        exit;

    }
    return 0;
}

int computerturn(void){ // dan
    srand(time(NULL));
    printf("The computer will go now. Please wait \n");
    Sleep(1000);
    while (TRUE){
        int compturn1 = rand() % 3;
        int compturn2 = rand() % 3;
        if (board[compturn1][compturn2] == ' '){
            board[compturn1][compturn2] = 'O';
            printf(" %c|%c|%c\n", board[0][0], board[0][1], board[0][2]);
            printf("--|-|--\n");
            printf(" %c|%c|%c\n", board[1][0], board[1][1], board[1][2]);
            printf("--|-|--\n");;
            printf(" %c|%c|%c\n", board[2][0], board[2][1], board[2][2]);
            Sleep(2000);
            break;
        }
    }
    return 0;
}

int playerturn(void){ //dan and romeo
    int move1;
    int move2;
    while (TRUE){
        printf("Which row would you like to go (BTW you are X, do 1-3) \n");
        scanf("%d", &move1);
        printf("Which column would you like to go (BTW you are X, do 1-3) \n");
        scanf("%d", &move2);
        if (board[move1-1][move2-1] == ' '){
            board[move1-1][move2-1] = 'X';
            printf(" %c|%c|%c\n", board[0][0], board[0][1], board[0][2]);
            printf("--|-|--\n");
            printf(" %c|%c|%c\n", board[1][0], board[1][1], board[1][2]);
            printf("--|-|--\n");;
            printf(" %c|%c|%c\n", board[2][0], board[2][1], board[2][2]);
            Sleep(2000);
            break;
        }
        
    }
    
    return 0;
}

int main(void){ // everyone
    printf("-----Tick Tack Toe-----\n");
    name();
    playerturn();
    checker();
    computerturn();
    checker();
    playerturn();
    checker();
    computerturn();
    checker();
    playerturn();
    checker();
    computerturn();
    checker();
    playerturn();
    checker();
    computerturn();
    checker();
    playerturn();
    checker();
    if (player == 0 && computer == 0){
        printf("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                Tie                |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|                                   |\n");
        printf("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n");
    }
    return 0;
}