// DD Period 7 Financial Calculator

#include <stdio.h>
float income, rent, utilities, groceries, transportation;
float inputs(char* monthly_thing){
    float input;
    printf("What is your monthly %s?\n", monthly_thing);
    scanf("%f", &input);

    return input;
}

float percentage(float what_cost){
    float done_percentage = (what_cost/income)*100;
    return done_percentage;
}

int main(void){
    
    printf("Hello user. Please input the information I require to allow me to help you calculate your finances.\n");
    income = inputs("income");
    rent = inputs("rent");
    utilities = inputs("utilities");
    groceries = inputs("groceries");
    transportation = inputs("transportation");
    float savings = income/10.0;
    float spending_money = income-(rent+utilities+groceries+transportation+savings);

    printf("All done.\n");
    printf("You should set aside $%.2f to save. That is 10%% of your income.\n", savings);
    printf("Your rent is %.2f%% of your income.\n", percentage(rent));
    printf("Your utilities are %.2f%% of your income.\n", percentage(utilities));
    printf("Your groceries are %.2f%% of your income.\n", percentage(groceries));
    printf("Your transportation is %.2f%% of your income.\n", percentage(transportation));
    printf("After all of your expenses and savings, you will have $%.2f to spend monthly.\n", spending_money);
    return 0;
}