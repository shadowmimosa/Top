# coding=utf-8
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


#class tools_reptile():
#    ''' It is reptile;信息清洗方法集合
#     '''

def pyfilter(yuanstring, leftlimit, rightlimit, ORD=None, valuetype=None, pt=None):
        # type: (object, object, object, object, object, object) -> object
        '''  通过左右边界来筛选数据,返回列表或字符类型的值；yuanstring为源字符串,leftlimit为左边界字符串,rightlimit为右边界字符串
            ORD为在查询结果中取第几个值，整数和All，All与0表示返回列表，基他整数表示返回值列表第N个值，超过列表值个数取最后的值；
            valuetype 表示筛选规则（即取值字符串的类型），为空时，默认json格式除换行符外所有字符，json整型int，json大小字母字符串str,json正负小数点数字num,,
            json网络连接为url,通用类型gen为除换行符外所有字符,支持非json取值,其他类型为自定义类型，
            pt表示自定义类型的正则表达示，只有当valuetype为自定义类型才会用到，其他类型不用传；
            常用正则表达示的特殊字符用法介绍：0|9  表示0或9；.表示匹配除“\n”之外的任何单个字符;
            +表示匹配前面的子表达式一次或多次；*匹配前面的子表达式零次或多次；[a-zA-Z0-9]表示0至9数字和大小字母;
            ?匹配前面的子表达式零次或一次；{n}n是一个非负整数。匹配确定的n次；{n,}n是一个非负整数。至少匹配n次;
            ?当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。
            非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。
            例如，对于字符串“oooo”，“o+?”将匹配单个“o”，而“o+”将匹配所有“o”。
            '''
        _leftlimit = leftlimit
        _rightlimit = rightlimit
        if valuetype == None :
            print  "默认取值:从json串取除\\n外的所有字符类型字符串"
            _pattern = _leftlimit  +  "\":(.*?)" +  _rightlimit
        elif valuetype in ['num', 'number', 'NUM', 'Num', 'Number', 'DATA', 'data', 'Data']:
            print  "从json串取数字(包括小数和负数)的字符串"
            _pattern = _leftlimit  +  "\":\"([-0-9.]+)\"" +  _rightlimit
        elif valuetype in ['int', 'INT', 'Int', 'Long', 'long', 'LONG']:
            print  "从json串取整型（数字）的字符串"
            _pattern = _leftlimit  +  "\":([0-9]+)" +  _rightlimit
        elif valuetype in ['char', 'string', 'str', 'Char', 'Str', 'CHAR', 'STR']:
            print  "从json串取字母类型的字符串"
            _pattern = _leftlimit  +  "\":\"([a-zA-Z]+)\"" +  _rightlimit
        elif valuetype in ['url', 'URL', 'Url']:
            print  "从json串取URL类型字符串"
            _pattern = _leftlimit  +  "\":\"([a-zA-z]+://[^\s]+?)\"" +  _rightlimit
        elif valuetype in ['gen', 'GEN', 'Gen']:
            print  "通用取值除\\n外所有字符，支持非json字符串取值"
            _pattern = _leftlimit   +  "(.*?)" +  _rightlimit
        else:
            print  "未匹配到类型，为自定义类型,匹配的规则为", pt
            _pattern = _leftlimit  +  pt  +  _rightlimit
        print "正则表达示：", _pattern
        _compile_pattern = re.compile(_pattern)
        print "编译的正则表达示为", _compile_pattern.pattern
        returnList = re.findall(_compile_pattern, yuanstring, flags=0)
        print "符合条件的信息列表:", returnList
        listlen = len(returnList)
        print "符合条件共:", listlen
        if ORD == None:
            print "ORD为None,默认给值为1:"
            _orderid = 1
        else:
            _orderid = ORD
        print "取值序号为:", _orderid
        if listlen == 0:
            print "没有符合的信息,返回None"
            RT = None
        elif _orderid in ['ALL','all','All','0','',0]:
            print "返回整个列表"
            RT = returnList
        else:
            if int(_orderid)>0:
                num = int(_orderid) - 1
            else:
                num = int(_orderid)
            if listlen-num>0 and listlen+num>=0:
                print "取值序号正常,取列表下标为:", num
                returnstring = returnList[num]
            else:
                print "取值序号过大,自动容错为取列表最后的值,取列表下标为:", listlen - 1
                returnstring = returnList[listlen - 1]
            RT = returnstring
        print  "Return Value:", RT
        return RT

    # def searchstr(a,b,c):


# 测试代码
if __name__ == '__main__':
    #t = tools_reptile()
    a = pyfilter("[{\"ret\":11111},{\"ret\":2222},{\"ret\":\"ab1cd_w\"}]","ret","}",1)