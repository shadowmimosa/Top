#include <cstdio>
#include <cstdlib>
#include <time.h>
#include <math.h>
using namespace std;

char operation(int operation);
float createEquation();
float calculate(int number1, int number2, int operation);

const int plus = 1, subtract = 2, multiplication = 3, division = 4, Remainder = 5, exponential = 6;
int main()
{
    int num, i, score;
    printf("请输入题目个数:");
    scanf("%d", &num);

    for (i = 0; i < num; i++)
    {
        score = createEquation();
    }
    printf("你的得分是%d\n\n", score);
    
    if score

    system("pause");
}

float createEquation()
{
    int number1, number2, operation1;
    float input_answer, answer = 0;
    static int score = 0;

    do
    {
        // srand(time(0));

        number1 = rand() % 10 + 1;
        number2 = rand() % 10 + 1;
        operation1 = rand() % 6 + 1;

        answer = calculate(number1, number2, operation1);

    } while (answer < 0);
    printf("%d %c %d =", number1, operation(operation1), number2);
    scanf("%f", &input_answer);


    if (answer == input_answer)
    {
        score += 10;
    }

    printf("\n");

    return score;
}

char operation(int operation)
{
    char c;
    switch (operation)
    {
    case plus:
        c = '+';
        break;
    case subtract:
        c = '-';
        break;
    case multiplication:
        c = '*';
        break;
    case division:
        c = '/';
        break;
    case Remainder:
        c = '%';
        break;
    case exponential:
        c = '^';
        break;
    }
    return c;
}

float calculate(int number1, int number2, int operation)
{
    switch (operation)
    {
    case plus:
        return (float)number1 + number2;
    case subtract:
        return (float)number1 - number2;
    case multiplication:
        return (float)number1 * number2;
    case division:
        return (float)number1 / number2;
    case Remainder:
        return (int)number1 % number2;
    case exponential:
        return (int)pow(number1, number2);
    }
}