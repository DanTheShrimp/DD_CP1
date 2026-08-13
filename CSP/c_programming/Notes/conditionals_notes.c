// DD Period 7 Conditionals notes

#include <stdio.h>
#include <string.h>

int main(void){
    int grade;
    char name[50];
    printf("What is your grade?\n");
    scanf("%f", &grade);

    printf("What is your name?\n");
    scanf("%s", &name);

    if (strcmp(name, "Daniel") == 0){
        printf("You don't get a grade >:)\n");
    }
    else{
        if (grade >= 90){
        printf("You have an A :O\n");
        }else if (grade >= 80){
        printf("You have an B :o\n");
        }else if (grade >= 70){
        printf("You have an C ._.\n");
        }else if (grade >= 60){
        printf("You have an D :(\n");
        }else{
        printf("YOU ARE FAILING >:(\n");
        }
    }
    return 0;
}