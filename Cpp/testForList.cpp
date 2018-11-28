#include "stdio.h"
#include "iostream"
using namespace std;
int main()
{
    int year, month, k;
    year = 2018;
    month = 10;
    k = 8;
    if (year > 2017 && month > 8 && k > 7)
    {
        cout << "day";
    }
    else
        cout << "Flase";
    system("pause");
    return 0;
}
