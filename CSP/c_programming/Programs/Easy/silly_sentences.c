// DD Period 7 Silly Sentences

#include <stdio.h>

int main(void){
    char noun[25];
    char verb[25];
    char adjective[25];
    printf("Hello, I am the Happiness Machine. Please give me a noun.\n");
    scanf("%s", &noun);

    printf("Thank you, now I need a past-tense verb.\n");
    scanf("%s", &verb);

    printf("Final thing, an adjective.\n");
    scanf("%s", &adjective);

    printf("The very stupid %s %s over the %s human.\n", noun, verb, adjective);
    return 0;
}