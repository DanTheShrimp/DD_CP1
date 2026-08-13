// DD Period 7 Loops Notes
#include <stdio.h>
#include <string.h>
#include <windows.h> // we can access sleep() from this

int main(void){
    int numbs[] = {69, 42, 17, 89, 5, 21, 19}; //arrays, not lists
    char candies[][20] = {"Twix", "Milky way", "Reeces"}; // we need a second bracket for the max length of a string
    int heeheehee = 1;

    for(int x=0; x<7; x++){
        Sleep(1000); // basically time.sleep() in c, but the number is in milliseconds
        printf("%d\n", numbs[x]);
    }

    for(int i=0; i<3; i++){
        Sleep(1000);
        printf("I like %s\n", candies[i]);
    }

    while(heeheehee>0){ // you cannot stop me from making an infinite loop >:)
        printf("%d\n", heeheehee);
        heeheehee++;
        Sleep(10);
    }
    return 0;
}