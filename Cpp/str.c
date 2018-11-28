#include <iostream>

int main()
{
    char a;
    char *str = &a;
    strcpy(str, "helllo");
    printf(str);
    system("pause");
    return 0;
}
