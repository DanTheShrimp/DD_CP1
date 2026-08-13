// DD Period 7 Strings Notes

#include <stdio.h>
#include <string.h>

int main(void){
    char first_name[] = "Daniel";
    char last_name[25];
    printf("What is your lack-luster last name, human.\n");
    scanf(" %s", last_name);
    char name[50];
    printf("[%s]\n", name);

    strcat(name, first_name);
    printf("[%s]\n", name);

    strcat(name, " ");
    printf("[%s]\n", name);

    strcat(name, last_name);
    printf("[%s]\n", name);

    printf("Your boring name is %s %s, ugh.\n", first_name, last_name);
    printf("%c\n", name[0]);

    printf("%zu\n", strlen(name));
    printf("%zu\n", sizeof(name));
    return 0;
}