###求稳定系数，根据每公里配速与平均配速方差

kilometreSpeed = [275, 313, 278, 303, 289, 304, 280, 292, 293, 312]  #每公里配速
totalMileage = len(kilometreSpeed)  #总里程

#求平均配速
sum = 0
for j in kilometreSpeed:
    sum = sum + j
averageSpeed = sum / len

#求和
i = 0
sum = 0
while not i == totalMileage:
    num = kilometreSpeed[i] - averageSpeed
    sum = num * num + sum
    i = i + 1

errorValue = (sum / totalMileage)**0.5  #误差值
StabilityCoefficient = 1 / (errorValue**0.5 + 1)  #稳定系数

print(StabilityCoefficient)
