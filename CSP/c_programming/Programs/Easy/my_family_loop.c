// DD Period 7 My Family Loop

#include <stdio.h>

int main(void){
    char family[][25] = {"Lizzie", "Sarah", "Dave", "Doomslug", "Chubs", "Fine", "Boomslug", "Bubbles", "Rose", "Boomerslug"};

    for(int x=0; x<10; x++){
        printf("One of my family members is %s.\n", family[x]);
    }
    return 0;
}