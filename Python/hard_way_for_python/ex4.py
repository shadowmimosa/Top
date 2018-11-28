# 100辆车
cars = 100
# 每辆车能坐4个人
space_in_a_car = 4.0
# 有30个司机
drivers = 30
# 90个乘客
passengers = 90
# 没人开的车
cars_not_driven = cars - drivers
# 可以开的车
cars_driven = drivers
# 最多运送人数
carpool_capacity = cars_driven * space_in_a_car
# 平均每辆车人数
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transpot", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")
