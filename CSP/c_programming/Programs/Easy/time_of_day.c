// DD Period 7 Time of Day
#include <stdio.h>
#include <string.h>

int main(void){
    int time;
    printf("What is the time in MILITARY TIME? Example: 6 PM is now 18.\n");
    scanf("%d", &time);

    if(time>=18 || time<=6){
        printf("It is nighttime.\n");
    }
    else if(time>=13 && time<=17){
        printf("Good afternoon.\n");
    }
    else if(time==12){
        printf("It is noon.\n");
    }
    else if(time>=7 && time<=11){
        printf("Good morning.\n");
    }
    return 0;
}