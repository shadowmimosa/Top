def guess_win(func):
    def rooftop_status():
        result = func()
        print('天台已满，请排队！')
        return result

    return rooftop_status


@guess_win
def germen_team():
    print("德国必胜！")


germen_team()


def func(name):
    print('我是{}！，我现在慌得一逼！'.format(name))


func('梅西')
y = func
y('勒夫')

a = [1, 2, 4]
r = map(lambda x: x * 3, a)
for i in r:
    print('当前天台人数:', i)


###
def f(l):
    return map(lambda x: x * 5, l)


a = f(a)
for i in a:
    print('当前天台人数：', i)
