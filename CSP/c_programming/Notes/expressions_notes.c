// DD Period 7 Expressions notes
#include <stdio.h>
#include <math.h>

int main(void){
    int year = 2346;
    float pie = 3.14;
    double pecan_pie = 3.14159265359;
    printf("%d\n", year);
    printf("%d\n", 8/3);
    printf("%.51f\n", 8.0/3.0);
    printf("%.2f\n", pow(2, 4));

    year += 1;
    printf("%d\n", year);
    year ++;
    printf("%d\n", year);
    return 0;
}