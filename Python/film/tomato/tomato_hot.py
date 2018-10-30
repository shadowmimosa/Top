# -*- coding:utf-8 -*-

import pandas as pd
from pyecharts import Geo

f = open(
    'C:\\Users\\ShadowMimosa\\Desktop\\STU\\Top\\西虹市首富.csv',
    encoding='utf-8')
tomato_com = pd.read_csv(f)
grouped = tomato_com.groupby(['city'])
grouped_pct = grouped['score']  # tip_pct列
city_com = grouped_pct.agg(['mean', 'count'])
city_com.reset_index(inplace=True)
city_com['mean'] = round(city_com['mean'], 2)

data = [(city_com['city'][i], city_com['count'][i])
        for i in range(0, city_com.shape[0])]
geo = Geo(
    '《西虹市首富》全国热力图',
    title_color="#fff",
    title_pos="center",
    width=1200,
    height=600,
    background_color='#404a59')
attr, value = geo.cast(data)
geo.add(
    "",
    attr,
    value,
    type="heatmap",
    visual_range=[0, 200],
    visual_text_color="#fff",
    symbol_size=10,
    is_visualmap=True,
    is_roam=False)
geo.render('西虹市首富全国热力图.html')
