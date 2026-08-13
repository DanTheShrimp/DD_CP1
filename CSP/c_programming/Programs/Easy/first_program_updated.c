// DD Period 7 First Program
#include <stdio.h>
#include <windows.h>

void namefinder(char* name_of_person){
    if(name_of_person=="Mrs.LaRose"){
        printf("Oh...\n");
        Sleep(1000);
        printf("It's you... %s.\n", name_of_person);
        Sleep(1500);
        printf("...\n");
        Sleep(500);
        printf("...\n");
        Sleep(500);
        printf("...\n");
        Sleep(500);
        printf("Clang\n");
    }else{
        printf("Hello, %s! What a wonderful name! Would you like to go fly and maybe blow up?\n", name_of_person);
    }
}

int main(void){
    printf("Hi! Oh, you aren't Spensa... Oh well! I really have been wanting to say some names!\n");
    namefinder("Daniel");
    namefinder("Doomslug");
    namefinder("Lizzie");
    namefinder("Mrs.LaRose");
    namefinder("Spensa");
    return 0;
}