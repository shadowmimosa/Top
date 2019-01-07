from pyecharts.datasets.coordinates import get_coordinate
from pyecharts.datasets.coordinates import search_coordinates_by_keyword

coordinate = get_coordinate('北京')
print(coordinate)  # [116.46, 39.92]

coordinate1 = get_coordinate('吉林市')
print(coordinate1)  # None
coordinate1 = get_coordinate('吉林')
print(coordinate1)  # None

print(get_coordinate('眉山'))
print(get_coordinate('上海'))   # 2018.1.7 已更新，只有 "上海" 会被取出

list = ('武陟', '上海', '璧山', '吉林', '祁县', '大竹', '眉山')
i=0
while i < 7:
    result = search_coordinates_by_keyword(list[i])
    print(result,end='\n')
    i = i + 1

# result = search_coordinates_by_keyword('武陟', '上海', '璧山', '吉林', '祁县', '大竹',
#                                        '眉山')
# print(result)  # {'北京':[116.46, 39.92], '北京市': [116.4, 39.9]}
