// DD Period 7 Name Decorator

#include <stdio.h>
#include <string.h>

int main(void){
    char name[50];
    char character[10];
    char finished_name[75];
    printf("Good morning user. I am the Name Decorator 69000. Please give me your name. I promise I won't sell it ;)\n");
    scanf("%s", name);
    printf("Thank you, %s. Now give me characters to decorate your name with. Please keep your input to a maximum of 10 characters.\n", name);
    scanf("%s", character);

    strcat(finished_name, character);
    strcat(finished_name, " ");
    strcat(finished_name, name);
    strcat(finished_name, " ");
    strcat(finished_name, character);

    printf("Here is your finished name.\n");
    printf("%s\n", finished_name);
    return 0;
}