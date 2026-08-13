// DD Period 7 Expressions Practice
#include <stdio.h>
#include <math.h>

int main(void){
    int one = 7-24/8*4+6;
    int two = 18/3-7+2*5;
    int three = 6*4/12+72/8-9;
    int four = (17-6/2)+4*3;
    int five = -2*(1*4-2/2)+(6+2-3);
    int six = -1*((3-4*7)/5)-2*24/6;
    int seven = (3*pow(5,2)/15)-(5-pow(2,2));
    int eight = (pow(1,4)*pow(2,2)+pow(3,3))-pow(2,5)/4;
    int nine = pow((22/2-2*5),2)+pow((4-6/6),2);
    printf("The answer to 7-24/8*4+6 is %d.\n", one);
    printf("The answer to 18/3-7+2*5 is %d.\n", two);
    printf("The answer to 6*4/12+72/8-9 is %d.\n", three);
    printf("The answer to (17-6/2)+4*3 is %d.\n", four);
    printf("The answer to -2*(1*4-2/2)+(6+2-3) is %d.\n", five);
    printf("The answer to -1*((3-4*7)/5)-2*24/6 is %d.\n", six);
    printf("The answer to (3*pow(5,2)/15)-(5-pow(2,2)) is %d.\n", seven);
    printf("The answer to (pow(1,4)*pow(2,2)+pow(3,3))-pow(2,5)/4 is %d.\n", eight);
    printf("The answer to pow((22/2-2*5),2)+pow((4-6/6),2) is %d.\n", nine);
    return 0;
}