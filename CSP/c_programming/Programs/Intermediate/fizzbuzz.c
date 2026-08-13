// DD Period 7 FizzBuzz

#include <stdio.h>

int main(void){
    int counter = 1;
    while(counter<=50){
        if(counter%3==0 && counter%5==0){
            printf("FizzBuzz\n");
        }else if(counter%5==0){
            printf("Buzz\n");
        }else if(counter%3==0){
            printf("Fizz\n");
        }else{
            printf("%d\n", counter);
        }
        counter++;
    }
    return 0;
}