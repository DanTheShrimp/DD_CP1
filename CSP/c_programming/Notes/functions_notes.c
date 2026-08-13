// DD Period 7 Functions Notes

#include <stdio.h>
#include <windows.h>

void birthday(char* name, int age){
    char art[50] = 
    "   /\\\n"
    "  /  \\\n"
    " / BD \\\n"
    "/PERSON\\\n";
    printf("Happy Birthday to you!\n");
    Sleep(1500);
    printf("Happy Birthday to you!\n");
    Sleep(1500);
    printf("Happy Birthday dear %s!\n", name);
    Sleep(1500);
    printf("Happy Birthday to you!\n");
    Sleep(1500);
    printf("You are now %d!\n", age);
    Sleep(1500);
    printf("%s\n", art);
    Sleep(1500);
}

int mul(int x, int y){
    return x*y;
}

int main(void){
    birthday("Daniel", mul(5, 3));
    birthday("Lizzie", mul(4, 4));
    birthday("Doomslug", mul(4,1));
    return 0;
}