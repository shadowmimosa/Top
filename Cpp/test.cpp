#include "Windows.h"
#include "stdio.h"
#include "iostream"
using namespace std;
int main()
{
    for (int i = 0; i < 4; i++)
    {
        if (i == 2)
            continue;
        cout << i << endl;
    }
    int meter = 2222;
    int a = meter / 100;
    int b = meter % 100 / 10;
    int c = meter % 10;
    int second = meter / 100 * 27 + meter % 100 / 10 * 3 + meter % 10 * 1;
    cout << "°Ù:" << a << endl
         << "Ê®:" << b << endl
         << "¸ö:" << c << endl
         << second << endl;
    cout << "7" << endl;
    printf("6");
    printf("\n");
    cout << "This for test cpp." << endl;
    system("pause");
}