// #include "stdafx.h"
#include "stdlib.h"
#include "iostream"
#include <fstream>
#include <time.h>
#include <string.h>
#include <iomanip>

using namespace std;

/*int put_rand()
{
	int a = 100, b = 20000;
	rand() % (b - a);

}

int output()
{
	fstream f("C:\\Users\\ShadowMimosa\\Desktopme\\RunList.txt");
}
*/

//	标准时间生成时间戳
int standard_to_stamp(const char *str_time)
{
    struct tm stm;
    int iY, iM, iD, iH, iMin, iS;

    cout << str_time << endl;

    memset(&stm, 0, sizeof(stm));
    iY = atoi(str_time);
    cout << iY << endl;
    iM = atoi(str_time + 4);
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

    //	printf("%d-%0d-%0d %0d:%0d:%0d\n", iY, iM, iD, iH, iMin, iS);   //标准时间格式例如：2016:08:02 12:12:30
    return (int)mktime(&stm);
}
//	创建日期（2015-2018）
int BulidTime()
{
    for (int i = 0; i < 4; i++)
    {
        int year, month, day;
        year = i + 2015;
        for (int j = 0; j < 12; j++)
        {
            if (i > 2017 && j > 8)
            {
                cout << "oh,month";
                break;
            }
            month = j + 1;
            for (int k = 0; k < 31; k++)
            {
                if (j > 8 && k > 7)
                    break;
                if (month == 2 && k < 27)
                {
                    day = k + 1;
                    cout << year << setfill('0') << setw(2) << month << setfill('0') << setw(2) << day << endl;
                }
                else if ((month == 4 || month == 6 || month == 9 || month == 11) && k < 30)
                {
                    day = k + 1;
                    cout << year << setfill('0') << setw(2) << month << setfill('0') << setw(2) << day << endl;
                }
                else if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && k < 31)
                {
                    day = k + 1;
                    cout << year << setfill('0') << setw(2) << month << setfill('0') << setw(2) << day << endl;
                }
                else
                    continue;
            }
        }
    }
    return 0;
}

int main()
{
    //	put_rand();
    //	output();

    //生成随机数100-20000
    int MinMeter = 100, MaxMeter = 20000;
    rand() % (MaxMeter - MinMeter);
    //生成初始时间
    BulidTime();
    //int time = standard_to_stamp("2015:08:02 8:10:10");
    //cout << time;
    //for (int i = 0; i < 10; i++)
    //{
    //	"20150102030405"
    //	const char *initialtime = "2015:08:02 8:10:10";
    //	int time = standard_to_stamp(initialtime);
    //	cout << time;
    //	initialtime
    //}
    //for (int i = 0; i < 10; i++)
    //{
    //	static int fid = 99044994;
    //	int meter = rand() % (maxmeter - minmeter);
    //	cout << "{\"uid\":32519920,\"fid\":"<<fid<< ",\"timeconflict\":0,\"meter\":"<<meter<<",\"source\":\"\",\"second\":38,\"lasttime\":"<<time<<",\"postrunid\":1600057862,\"fraud\":0,\"type\":7,\"private\":0,\"runid\":\"f52b6140791642109f916ca0ae29a107\"},";
    //	fid++;
    //}
    system("pause");
    return 0;
}
