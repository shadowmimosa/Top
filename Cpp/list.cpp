// ConsoleApplication2.cpp: �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include "stdlib.h"
#include "iostream"
#include <fstream>
#include <time.h>
#include <string.h>
#include <iomanip>

using namespace std;

///	��������

//	�������
int OutputTime(int, int, int);
//	��׼ʱ������ʱ���
int standard_to_stamp(const char *str_time);
//	���������
int BuildRand(int, int);
//	�������
int Output(int time);

//  �����������ں����ʱ�䣨2015-2018��
int BuildTime()
{
	//����ʱ���֡���������Χ
	int MinHour = 16, MaxHour = 21;
	int MinMinute = 0, MaxMinute = 59;
	int MinSecond = 0, MaxSecond = 59;

	//����ѭ�� ����������
	//��
	for (int i = 0; i < 4; i++)
	{
		/*if (i == 2)
			continue;*/
		int year, month; //,day;
		year = i + 2015;

		//��
		for (int j = 0; j < 12; j++)
		{
			month = j + 1;

			//��
			for (int k = 0; k < 31; k++)
			{
				if (year > 2017 && month > 10 && k > 18) //2018.11.19��֮�󣬽���ѭ��
					return 0;
				if (month == 2 && k < 28) //2��ֻ��28��
				{
					//���ú����������
					OutputTime(k, year, month);

					/*day = k + 1;
					int hour = rand() % (MaxHour - MinHour + 1) + MinHour;
					int minute = rand() % (MaxMinute - MinMinute);
					int second = rand() % (MaxSecond - MinSecond);
					cout << year << setfill('0') << setw(2) << month << setfill('0') << setw(2) << day << setfill('0') << setw(2) << hour << setfill('0') << setw(2) << minute << setfill('0') << setw(2) << second << endl;*/
				}
				else if ((month == 4 || month == 6 || month == 9 || month == 11) && k < 30) //30����·�
				{
					//���ú����������
					OutputTime(k, year, month);

					/*day = k + 1;
					int hour = rand() % (MaxHour - MinHour + 1) + MinHour;
					int minute = rand() % (MaxMinute - MinMinute);
					int second = rand() % (MaxSecond - MinSecond);
					cout << year << setfill('0') << setw(2) << month << setfill('0') << setw(2) << day << setfill('0') << setw(2) << hour << setfill('0') << setw(2) << minute << setfill('0') << setw(2) << second << endl;*/
				}
				else if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && k < 31) //31����·�
				{
					//���ú����������
					OutputTime(k, year, month);

					/*day = k + 1;
					int hour = rand() % (MaxHour - MinHour + 1) + MinHour;
					int minute = rand() % (MaxMinute - MinMinute);
					int second = rand() % (MaxSecond - MinSecond);
					cout << year << setfill('0') << setw(2) << month << setfill('0') << setw(2) << day << setfill('0') << setw(2) << hour << setfill('0') << setw(2) << minute << setfill('0') << setw(2) << second << endl;*/
				}
				else
					continue;
			}
		}
	}
	return 0;
}

//	�����������+���ʱ�亯��
int OutputTime(int k, int year, int month)
{
	int day = k + 1;

	//����BuildRand()�������ʱ����
	int hour = BuildRand(16, 21);
	int minute = BuildRand(0, 59);
	int second = BuildRand(0, 59);

	//
	//����ʱ���֡���������Χ
	//int MinHour = 16, MaxHour = 21;
	//int MinMinute = 0, MaxMinute = 59;
	//int MinSecond = 0, MaxSecond = 59;

	////�������ʱ����
	//int hour = rand() % (MaxHour - MinHour + 1) + MinHour;
	//int minute = rand() % (MaxMinute - MinMinute);
	//int second = rand() % (MaxSecond - MinSecond);

	struct tm stm;

	stm.tm_year = year - 1900;
	stm.tm_mon = month - 1;
	stm.tm_mday = day;
	stm.tm_hour = hour;
	stm.tm_min = minute;
	stm.tm_sec = second;

	int time = mktime(&stm);
	Output(time);
	return 0;

	cout << mktime(&stm) << endl;
	return 0;

	//��������ա�ʱ����
	cout << year << "." << setfill('0') << setw(2) << month << "." << setfill('0') << setw(2) << day << " " << setfill('0') << setw(2) << hour << ":" << setfill('0') << setw(2) << minute << ":" << setfill('0') << setw(2) << second << endl;
	return 0;
}

//	����ָ����Χ�����
int BuildRand(int MinNum, int MaxNum)
{

	int RandNum = rand() % (MaxNum - MinNum + 1) + MinNum;
	return RandNum;

	////���������
	//int hour = rand() % (MaxNum - MinNum + 1) + MinNum;
	//int hour = rand() % (MaxNum - MinNum + 1) + MinNum;
	//int hour = rand() % (MaxNum - MinNum + 1) + MinNum;
}

//	��׼ʱ������ʱ���
int standard_to_stamp(const char *str_time)
{
	struct tm stm;
	int iY, iM, iD, iH, iMin, iS;

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

	//	printf("%d-%0d-%0d %0d:%0d:%0d\n", iY, iM, iD, iH, iMin, iS);   //��׼ʱ���ʽ���磺2016:08:02 12:12:30
	return (int)mktime(&stm);
}

int Output(int time)
{
	static int fid = 99044994;
	int meter = BuildRand(100, 20000);
	int second = meter / 100 * 27 + meter % 100 / 10 * 3 + meter % 10 * 1;

	cout << "{\"uid\":32519920,\"fid\":" << fid << ",\"timeconflict\":0,\"meter\":" << meter << ",\"source\":\"\",\"second\":" << second << ",\"lasttime\":" << time << ",\"postrunid\":1600057862,\"fraud\":0,\"type\":7,\"private\":0,\"runid\":\"f52b6140791642109f916ca0ae29a107\"}," << endl;
	//fid++;

	ofstream f("C:\\Users\\ShadowMimosa\\Desktop\\RunList.txt", ios::app);
	if (!f)
		return 0;
	else
		cout << "open it at:";
	f << "{\"uid\":32519920,\"fid\":" << fid << ",\"timeconflict\":0,\"meter\":" << meter << ",\"source\":\"\",\"second\":" << second << ",\"lasttime\":" << time << ",\"postrunid\":1600057862,\"fraud\":0,\"type\":7,\"private\":0,\"runid\":\"f52b6140791642109f916ca0ae29a107\"},";
	//f.close();
	fid++;
	static int i = 0;
	cout << "��" << ++i << "��!" << endl;
	return 0;

	//for (int i = 0; i < 10; i++)
	//{
	//	static int fid = 99044994;
	//	int meter = BuildRand(100, 20000);
	//	//int meter = rand() % (maxmeter - minmeter);
	//	cout << "{\"uid\":32519920,\"fid\":"<<fid<< ",\"timeconflict\":0,\"meter\":"<<meter<<",\"source\":\"\",\"second\":38,\"lasttime\":"<<time<<",\"postrunid\":1600057862,\"fraud\":0,\"type\":7,\"private\":0,\"runid\":\"f52b6140791642109f916ca0ae29a107\"},";
	//	fid++;
	//}
	//return 0;
}

//int BuildMeter()
//{
//	int meter = BuildRand(100, 20000);
//	return meter;
//}

int main()
{
	//put_rand();
	//output();
	////���������100-20000
	//int MinMeter = 100, MaxMeter = 20000;
	//rand() % (MaxMeter - MinMeter);
	//���ɳ�ʼʱ��
	//
	//int time = standard_to_stamp("2015:08:02 8:10:10");
	//cout << time;
	//for (int i = 0; i < 10; i++)
	//{
	////"20150102030405"
	//	const char *initialtime = "2015:08:02 8:10:10";
	//	int time = standard_to_stamp(initialtime);
	//	cout << time;
	//	//initialtime
	//}

	BuildTime();

	//Output();

	//for (int i = 0; i < 10; i++)
	//{
	//	static int fid = 99044994;
	//	int meter = BuildRand(100, 20000);
	//	//int meter = rand() % (maxmeter - minmeter);
	//	cout << "{\"uid\":32519920,\"fid\":"<<fid<< ",\"timeconflict\":0,\"meter\":"<<meter<<",\"source\":\"\",\"second\":38,\"lasttime\":"<<time<<",\"postrunid\":1600057862,\"fraud\":0,\"type\":7,\"private\":0,\"runid\":\"f52b6140791642109f916ca0ae29a107\"},";
	//	fid++;
	//}
	system("pause");
	return 0;
}
