from pyecharts import Geo, Style

#读取城市数据
city = []
with open('xie_zheng.txt',mode='r',encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            city.append(row.split(',')[2].replace('\n',''))

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

data = []
for item in all_list(city):
    data.append((item,all_list(city)[item]))
    style = Style(
        title_color = "#fff",
        title_pos = "center",
        width = 1905,
        height = 996,
        background_color = "#404a59"
        )

geo = Geo("《邪不压正》粉丝人群地理位置","数据来源：恋习Python",**style.init_style)
attr,value= geo.cast(data)
geo.add("",attr,value,visual_range=[0,20],
    visual_text_color="#fff",symbol_size=20,
    is_visualmap=True,is_piecewise=True, 
    visual_split_number=4)

geo.render()