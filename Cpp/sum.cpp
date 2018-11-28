
///***求稳定系数，根据每公里配速与平均配速方差***///

#include "stdlib.h"
#include "iostream"
#include "math.h"

using namespace std;

int main()
{
    int kilometreSpeed[] = {275, 313, 278, 303, 289, 304, 280, 292, 293, 312}; //定义数组，存放每公里配速
    int totalMileage;                                                          //总里程，根据数组得出总里程
    double averageSpeed;                                                       //平均配速
    double errorValue;                                                         //误差值
    double StabilityCoefficient;                                               //稳定系数

    totalMileage = sizeof(kilometreSpeed) / sizeof(kilometreSpeed[0]);

    //求平均配速，存放在averageSpeed
    for (int j = 0; j < totalMileage; j++)
    {
        static double sum = 0;
        sum += kilometreSpeed[j];
        if (j == totalMileage - 1)
            averageSpeed = sum / totalMileage;
    }

    //求稳定系数
    for (int i = 0; i < totalMileage; i++)
    {
        static double sum;
        sum += (kilometreSpeed[i] - averageSpeed) * (kilometreSpeed[i] - averageSpeed);
        if (i == totalMileage - 1)
        {
            errorValue = sqrt((sum / totalMileage));
            StabilityCoefficient = 1 / (sqrt(errorValue) + 1);
        }
    }

    //输出稳定系数
    cout << StabilityCoefficient << endl;

    system("pause");
    return 0;
}