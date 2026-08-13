// DD Period 7 Financial Calculator

#include <stdio.h>

int main(void){
    float income, rent, utilities, groceries, transportation;
    printf("Hello user. Please input the information I require to allow me to help you calculate your finances.\n");
    printf("Please type how much you earn monthly.\n");
    scanf("%f", &income);
    printf("Thank you. Now type in how much you spend on rent each month.\n");
    scanf("%f", &rent);
    printf("Alright, now please type in how much you spend on utilities monthly.\n");
    scanf("%f", &utilities);
    printf("Almost done. Now input how much you pay for groceries each month.\n");
    scanf("%f", &groceries);
    printf("Last one. Now how much do you spend on transportation?\n");
    scanf("%f", &transportation);
    float savings = income/10.0;
    float spending_money = income-(rent+utilities+groceries+transportation+savings);

    printf("All done.\n");
    printf("You should set aside $%.2f to save. That is 10%% of your income.\n", savings);
    printf("Your rent is %.2f%% of your income.\n", (rent/income)*100);
    printf("Your utilities are %.2f%% of your income.\n", (utilities/income)*100);
    printf("Your groceries are %.2f%% of your income.\n", (groceries/income)*100);
    printf("Your transportation is %.2f%% of your income.\n", (transportation/income)*100);
    printf("After all of your expenses and savings, you will have $%.2f to spend monthly.\n", spending_money);
    return 0;
}