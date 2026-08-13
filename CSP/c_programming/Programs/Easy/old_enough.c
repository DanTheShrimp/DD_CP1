// DD Period 7 Old Enough
#include <stdio.h>
#include <string.h>

int main(void){
    int age;
    printf("Hello, how old are you? I am totally not some internet creep or something.\n");
    scanf("%d", &age);

    if(age>=18){
        printf("You are old enough to vote!\n");
    }
    else if(age>=16){
        printf("You are old enough to drive!\n");
    }
    else if(age>=15){
        printf("You are old enough to get a learners permit!\n");
    }
    else if(age>=5){
        printf("You are old enough to go to school!\n");
    }
    else{
        printf("I aint answering!\n");
    }
    return 0;
}