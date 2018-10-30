from tool_reptile import *
from Usertool_01 import *
from Verification import *
from Verification_Field import *

# convertCode({"path":"谁知道是什么编码呢"},'GBK')

# FindAndValue()


def verify_Json_to_Dict():
    data_one = "{\"b\":789,\"c\": 456,\"a\":123}"
    data_two = {"b": 789, "c": 456, "a": 123}
    data_three = ["This is a List"]
    data_one_change = Json_to_Dict(data_one)
    data_two_change = Json_to_Dict(data_two)
    data_three_change = Json_to_Dict(data_three)
    print(data_one_change, data_two_change, data_three_change)


# e = "[{\"b\":7,\"c\":\"ab\",\"a\":1},{\"b\":9,\"c\":\"4a6\",\"a\":12},{\"b\":9,\"c\":\"4a6\",\"a\":112}]"

# pyfilter(e, "b>=9 And \"c\"==\"4a6\" And a<>112", "c")
# pyfilter(e, "a<>112", "c")

# my_list = []
# my_tuple = list()

# my_list="my_list"
# my_tuple[0]=my_tuple.append("my_tuple")

# print(my_list,my_tuple)

# conditionx="12<>112"
# if eval(conditionx) == False:
#     print("right")


def FindAndValue_clone(yuanstring,
                       leftlimit,
                       rightlimit,
                       ORD=None,
                       valuetype=None,
                       pt=None):
    '''
    通过左右边界来筛选数据,返回列表或字符类型的值，没有符合条件的返回None；
    `param yuanstring` 为源字符串
    :param leftlimit: 为左边界字符串
    :param rightlimit: 为右边界字符串
    :param ORD: 为在查询结果中取第几个值，整数和All，All与0表示返回列表，Num，Count为返回找到的个数,
                基他整数表示返回值列表第N个值，超过列表值个数取最后的值；
    :param valuetype: 表示筛选规则（即取值字符串的类型），为空时，默认json格式除换行符外所有字符，
                json整型int，json大小字母字符串str,json正负小数点数字num,
                json网络连接为url,通用类型gen为除换行符外所有字符,支持非json取值,其他类型为自定义类型
    :param pt: 表示自定义类型的正则表达示，只有当valuetype为自定义类型才会用到，其他类型不用传
    :return:返回列表或字符串，如没有符合条件的返回None
            常用正则表达示的特殊字符用法介绍：0|9  表示0或9；.表示匹配除“\\n”之外的任何单个字符;
            +表示匹配前面的子表达式一次或多次；*匹配前面的子表达式零次或多次；[a-zA-Z0-9]表示0至9数字和大小字母;
            ?匹配前面的子表达式零次或一次；{n}n是一个非负整数。匹配确定的n次；{n,}n是一个非负整数。至少匹配n次;
            ?当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。
            非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。
            例如，对于字符串“oooo”，“o+?”将匹配单个“o”，而“o+”将匹配所有“o”。
    '''
    _leftlimit = leftlimit
    _rightlimit = rightlimit
    if valuetype == None:
        print("默认取值:从json串取除\\n外的所有字符类型字符串")
        _pattern = "\":(.*?)"
        if _leftlimit != None:
            _pattern = _leftlimit + _pattern
        if _rightlimit != None:
            _pattern = _pattern + _rightlimit
    elif valuetype in [
            'num', 'number', 'NUM', 'Num', 'Number', 'DATA', 'data', 'Data'
    ]:
        print("从json串取数字(包括小数和负数)的字符串")
        _pattern = "\":\"([-0-9.]+)\""
        if _leftlimit != None:
            _pattern = _leftlimit + _pattern
        if _rightlimit != None:
            _pattern = _pattern + _rightlimit
    elif valuetype in ['int', 'INT', 'Int', 'Long', 'long', 'LONG']:
        print("从json串取整型（数字）的字符串")
        _pattern = "\":([0-9]+)"
        if _leftlimit != None:
            _pattern = _leftlimit + _pattern
        if _rightlimit != None:
            _pattern = _pattern + _rightlimit
    elif valuetype in ['char', 'string', 'str', 'Char', 'Str', 'CHAR', 'STR']:
        print("从json串取字母类型的字符串")
        _pattern = "\":\"([a-zA-Z]+)\""
        if _leftlimit != None:
            _pattern = _leftlimit + _pattern
        if _rightlimit != None:
            _pattern = _pattern + _rightlimit
    elif valuetype in ['url', 'URL', 'Url']:
        print("从json串取URL类型字符串")
        _pattern = "\":\"([a-zA-z]+://[^\\s]+?)\""
        if _leftlimit != None:
            _pattern = _leftlimit + _pattern
        if _rightlimit != None:
            _pattern = _pattern + _rightlimit
    elif valuetype in ['gen', 'GEN', 'Gen']:
        print("通用取值除\\n外所有字符，支持非json字符串取值")
        _pattern = "(.*?)"
        if _leftlimit != None:
            _pattern = _leftlimit + _pattern
        if _rightlimit != None:
            _pattern = _pattern + _rightlimit
    else:
        print("未匹配到类型，为自定义类型,匹配的规则为", pt)
        _pattern = pt
        if _leftlimit != None:
            _pattern = _leftlimit + _pattern
        if _rightlimit != None:
            _pattern = _pattern + _rightlimit
    print("正则表达示：", _pattern)
    _compile_pattern = re.compile(_pattern)
    print("编译的正则表达示为", _compile_pattern.pattern)
    returnList = re.findall(_compile_pattern, yuanstring, 0)
    print("符合条件的信息列表:", returnList)
    listlen = len(returnList)
    print("符合条件共:", listlen)
    if ORD == None:
        print("ORD为None,默认给值为1:")
        _orderid = 1
        print("取值序号为:", _orderid)
    elif ORD in ['count', 'num', 'Count', 'Num', 'COUNT']:
        print("ORD为%s,将统计个数返回:" % ORD)
        _orderid = 'COUNT'
    else:
        _orderid = ORD
        print("取值序号为:", _orderid)
    if listlen == 0:
        print("没有符合的信息,返回None")
        RT = None
    elif _orderid == 'COUNT':
        print("返回类型为%s,返回查找符合要求的个数" % _orderid)
        RT = listlen
    elif _orderid in ['ALL', 'all', 'All', '0', '', 0]:
        print("返回整个列表")
        RT = returnList
    else:
        if int(_orderid) > 0:
            num = int(_orderid) - 1
        else:
            num = int(_orderid)
        if listlen - num > 0 and listlen + num >= 0:
            print("取值序号正常,取列表下标为:", num)
            returnstring = returnList[num]
        else:
            print("取值序号过大,自动容错为取列表最后的值,取列表下标为:", listlen - 1)
            returnstring = returnList[listlen - 1]
        RT = returnstring
    print("Return Value:", RT)
    return RT


# conditionx="12<>112"
# print("eval(conditionx)=", eval(conditionx))
# if eval(conditionx) == False:
#     print("right")
def verity_Usertool_01():

    # 获取目录
    Get_pwd()
    a1_pwd = os.getcwd()
    a2_pwd = os.popen('dir').readlines()
    print(a1_pwd, a2_pwd)

    # 提取两个列表中相同值
    list1 = [1, 2, 3, 4, 5, 'skr', 'skr']
    list2 = [9, 8, 7, 6, 5, 'skr']
    list3 = Get_Duplicates_List(list1, list2)
    print(list3)

    # 从列表中随机取值
    value = random.choice(list1)
    print(choiceValue(list1))

    # 去掉字符串开头与结尾双/单引号
    test_str = ''''your are winer"'''
    double_str = stripStr(test_str)
    print(double_str)

    single_str = stripStrSingle(double_str)
    print(single_str)

    # 判断某个值是否存在于列表
    value = ListContainValue(1, list1)
    print(value)

    # 判断列表是否为升降序
    list4 = [888888, 9999999999, 1000000]
    order = listCmp(list4, True)
    print(order)

    # 格式化时间戳
    time_now = '1561234500'
    print(stampTime(time_now))

    #判断字符串是否为空，判断前，过滤单引号及双引号
    str1 = ''
    str2 = ''''you are winner"'''
    try:
        ShouldStringNotBeEmpty(str1)
    except AssertionError as eg:
        print(eg)
    ShouldStringNotBeEmpty(str2)

    #写文件操作，通常用作临时外部存储
    str3 = stripStr(str2)
    str3 = stripStrSingle(str3)
    path = '.\\Lib\\write.txt'
    writeFile(str3, path)

    #读文件，配合写文件使用
    str4 = ReadFile(path)
    print(str4)

    #向指定文件追加内容
    str5 = '\nAlso you are loser.'
    str6 = '\nAlso you are loser.'
    WriteAppendFile(str5, path)
    WriteAppendFile(str6, path)

    #将指定的文件全部读取，写入到列表并返回
    str_list = ReadAllFile(path)
    print(str_list)

    #判断指定文件是否存在，且文件内容是否为空,存在且内容不为空则返回True，反之返回False
    path2 = 'write.txt'
    path_verify = VerifyFileExist(path)
    path2_verify = VerifyFileExist(path2)
    print(path, path2)
    print(path_verify, path2_verify)

    #功能：从返回的内容中提取json串。
    response = 'callback({"songerid":123, "关键字":"关键字"})'
    response_json = getJsonData(response)
    print(response_json)

    # 将data数据以base64进行编解码
    data = 'The String waiting for decoding'
    base64_encode = base64ENCode(data)
    base64_decode = base64Code(base64_encode)
    print(base64_decode.decode())

    #将data数据以gzip进行解压
    waiting_compress = b'This is compression'
    waiting_compress_str = 'This is compression'
    compress_data = gzip.compress(waiting_compress)
    # compress_data_str = gzip.compress(waiting_compress_str)
    decompress_data = gzip.decompress(compress_data)
    print(waiting_compress, compress_data, decompress_data, end='\n')
    # gzip_data = gzipCode(compress_data)

    # 将data字符串以utf-8形式输出
    bytes_str = bytes(waiting_compress_str, encoding='utf-8')
    printUTF(bytes_str)

    #随机从某个取值范围获取整型数值
    if (True):
        i = 0
        while i < 20:
            getRandomValue_Range(4, 16)
            i += 1

    if (False):
        i = 0
        while i < 20:
            getrandomvalue_range(4, 16)
            i += 1

    #随机从列表中获取数值
    list_get = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        20, 19, 18, 17, 16, 15, 14, 13, 12, 12, 'one', 'two', 'three', 'four',
        'five', 'five', 'four', 'three', 'two', 'one', '一', '二', '一', '', ''
    ]
    if (True):
        i = 0
        while i < 60:
            getRandomValue_List(list_get)
            i += 1
    if (False):
        i = 0
        while i < 60:
            getrandomvalue_List(list_get)
            i += 1

    # 生成随机字符串
    random_str = randomstr(20)
    print(random_str)

    # 拓展列表
    print(extendList(list4, list_get))

    # 拓展字典
    you, are, winner, also, loser = 'you', 'are', 'winner', 'alse', 'loser'
    dict1 = {'you': you, 'are': are, 'winner': winner}
    dict2 = {'you': you, 'also': also, 'are': are, 'loser': loser}
    dict3 = extendDict(dict1, dict2)
    print(dict3)

    test = '<script>window.name={"code":0,"data":{"fxId":39097443,"kugouId":582326271,"success":true,"ticket":"016800FDCDCA8847C0C769059957BF5F22F267DFC155319A74F5B8B581BB4A5A464DE0DA364032C704B8008319A255E58D475A3C36407B30E589509E569CF4399C239948EB9EA3A7BF2AE939869EA6CD70FEC4FFC4BABEBB5BBEFFFAFD5308CC366F05ECC2EF3923EE0AD1"},"needCaptcha":0,"times":1458035189124};</script>'
    ShouldStringNotBeEmpty(test)
    # getJsonData(test)
    base64_str = base64ENCode(test)
    print(base64_str.decode())
    base64_str_decompression = base64Code(base64_str)
    print(base64_str_decompression.decode())
    printUTF(base64_str)

    #针对H5返回的JS脚本进行提取有效的数据
    getH5JsonData(test)

    # 传入索引号， 从列表中取值
    getlist(list1, 7)

    # 判断列表中所有的值是否相等
    list_equal_A = [10, 11, 11, 11, 11, 11, 11, 11, 11, 12, 'skr']
    list_equal_B = [10, 11, 11, 11, 11, 11, 11, 11, 11, 12, 'skr']
    print(checkListEqual(list_equal_A))

    print(checkEqual2(list_equal_A))

    listA_isEquel_listB(list_equal_A, list_equal_B)

    stringbyequal(test)
    pattern = re.compile('=')
    pattern = pattern


def getrandomvalue_range(min_num, max_num):

    result_choice = []

    f1 = open("id.pkl", "a")
    f2 = open("id.pkl", "r")
    f2_content = f2.readlines()

    for line in f2_content:
        line = line.replace('\n', '')
        result_choice.append(int(line))

    print(result_choice)

    if len(result_choice) >= (max_num - min_num + 1):
        print("所有数字已取完！")
        return None

    else:
        while (len(result_choice)) < max_num - min_num + 1:
            random_num = random.choice(range(min_num, max_num + 1))
            if random_num not in result_choice:
                f1.write(str(random_num))
                f1.write("\n")
                print("第%d次随机的数:%d" % (len(result_choice) + 1, random_num))
                f1.close()
                f2.close()
                return str(random_num)
            else:
                print("第%d次随机的数:%d,已重复，自动重新获取" % (len(result_choice) + 1,
                                                  random_num))
                continue

    f1.close()
    f2.close()


def getrandomvalue_List(list1):

    news_list = []
    for id in list1:
        if id not in news_list:
            news_list.append(id)

    print('去重后的新列表为:\n', news_list)

    list_len = len(news_list)

    result_choice = []

    f1 = open("id_list.pkl", "a")
    f2 = open("id_list.pkl", "r")
    f2_content = f2.readlines()

    for line in f2_content:
        line = line.replace('\n', '')
        result_choice.append(str(line))

    print(result_choice)

    if len(result_choice) >= list_len:
        print("列表中所有的值已取完！")

    else:
        while (len(result_choice)) < list_len:
            random_num = random.choice(news_list)

            if str(random_num) not in result_choice:
                f1.write(str(random_num))
                f1.write("\n")
                print("第%d次随机的值为:%s" % (len(result_choice) + 1, random_num))
                f1.close()
                f2.close()
                return str(random_num)

            else:
                print("第%d次随机的值为:%s,已重复，自动重新获取" % (len(result_choice) + 1,
                                                   random_num))
                continue

    f1.close()
    f2.close()


# import threading, multiprocessing

# # 一个死循环
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

verity_Usertool_01()


def verify_itchat():
    f = open('itchat.pkl', 'rb')
    data = f.read()
    print(data.decode())


def verify_verification():

    you, are, winner, also, loser = 'you', 'are', 'winner', 'alse', 'loser'
    parameter_dict_empty = {}
    parameter_dict = {'you': you, 'are': are, 'winner': winner}
    parameter_list_empty = []
    parameter_list = ['you', 'are', 'winner', 'alse', 'loser']

    data = [{
        "songId": 8269,
        "singerId": 5785,
        "hash": "A31F9FBFC5E73AA93CBF7EC1C6247A98",
        "recomflag": 5,
        "singerName": "1",
        "singerImg": "20140117151145992387.jpg",
        "startTime": 75000,
        "climaxHash": "B349729F8E040F849C532C904B2A4C22",
        "krc": "jj"
    },
            [{
                "songId": 8269,
                "singerId": 5785,
                "hash": "A31F9FBFC5E73AA93CBF7EC1C6247A98",
                "recomflag": 5,
                "singerName": "1",
                "singerImg": "20140117151145992387.jpg",
                "startTime": 75000,
                "climaxHash": "B349729F8E040F849C532C904B2A4C22",
                "krc": "jj"
            }]]
    msg = 'This is a niubi news'
    verfication_data(parameter_dict_empty)
    verfication_data(parameter_dict)
    verfication_data(parameter_list_empty)
    verfication_data(parameter_list)
    verfication_data(data, msg)


# verify_verification()


def rate_error(actual_value, app_count=1.5):

    return (app_count - actual_value) / actual_value


def calculation():

    actual_value = eval(input('Please input your actual mileage:'))
    i = 4
    while i > 0:
        app_count = eval(input('Please input your mileage of App count:'))
        rate = rate_error(actual_value, app_count) * 100
        print('The rate of error is: %.2f%%' % rate)
        i -= 1


# calculation()


# 获取用户输入十进制数
def decimal():

    decimal = int(input("输入数字："))

    binary = bin(decimal)
    octal = oct(decimal)
    hexadecimal = hex(decimal)

    print("十进制数为：", decimal)
    print("转换为二进制为：", binary)
    print("转换为八进制为：", octal)
    print("转换为十六进制为：", hexadecimal)


def format_logging():

    import logging

    logging.basicConfig(level=logging.debug)
    logging.debug('debug 信息')
    logging.info('info 信息')
    logging.warning('warning 信息')
    logging.error('error 信息')
    logging.critical('critial 信息')


def verify_Verification_Field():
    data = [{
        "songId": 8269,
        "singerId": 5785,
        "hash": "A31F9FBFC5E73AA93CBF7EC1C6247A98",
        "recomflag": 5,
        "singerName": "1",
        "singerImg": "20140117151145992387.jpg",
        "startTime": 75000,
        "climaxHash": "B349729F8E040F849C532C904B2A4C22",
        "krc": "jj"
    },
            [{
                "songId": 8269,
                "singerId": 5785,
                "hash": "A31F9FBFC5E73AA93CBF7EC1C6247A98",
                "recomflag": 5,
                "singerName": "1",
                "singerImg": "20140117151145992387.jpg",
                "startTime": 75000,
                "climaxHash": "B349729F8E040F849C532C904B2A4C22",
                "krc": "jj"
            }]]

    test = ['songId', 'hash', 'singerId']

    verfication_Field(data, test)


verify_Verification_Field()