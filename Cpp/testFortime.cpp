//#include <stdafx.h>
#include "stdlib.h"
#include <iostream>
#include <time.h>

using namespace std;

int standard_to_stamp(const char *str_time)
{
    struct tm stm;
    int iY, iM, iD, iH, iMin, iS;
cout<<iY<<iM<<iD<<iH<<iMin<<iS<<endl;
    cout << str_time << endl;

    memset(&stm, 0, sizeof(stm));
    iY = atoi(str_time);
    cout << iY << endl;

    iM = atoi(str_time + 5);
    cout << iM << endl;
    iD = atoi(str_time + 8);
    cout << iD << endl;
    iH = atoi(str_time + 11);
    iMin = atoi(str_time + 14);
    iS = atoi(str_time + 17);

    stm.tm_year = iY - 1900;
    stm.tm_mon = iM - 1;
    stm.tm_mday = iD;
    stm.tm_hour = iH;
    stm.tm_min = iMin;
    stm.tm_sec = iS;

    printf("%d-%0d-%0d %0d:%0d:%0d\n", iY, iM, iD, iH, iMin, iS); //标准时间格式例如：2016:08:02 12:12:30
    return (int)mktime(&stm);
}
int main()
{
    char *year="2016";
    char *month="08";
    cout<<year<<month<<endl;
    char *s=year;
    cout<<s<<endl;
    // const char *time = "2018:08:08 19:20:20";
    // int times = standard_to_stamp(time);
    // cout << times << endl;
    system("pause");
    return 0;
}
