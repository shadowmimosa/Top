def exchange_order(raw_str):
    return raw_str[::-1]


string = "换个滤镜 这个滤镜眉毛太浓了"

print((lambda x: x[::-1])(string))
