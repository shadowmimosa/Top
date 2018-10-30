#coding:utf-8
import requests
import re
import sys
import cx_Oracle


# reload(sys)
# sys.setdefaultencoding('utf8')
class spider(object):
    def __init__(self):
        print(u'开始爬取...')

    #获取网页源码
    def getSource(self, url):
        html = requests.get(url)
        return html.text

    #改变url实现抓取12~16年的假日
    def changePage(self, url, total_page):
        now_page = int(url[32:36])
        page_group = []
        t = 1
        for i in range(now_page, total_page + 1):
            link = 'http://wannianrili.51240.com/?q=' + str(i)
        for t in range(1, 13):
            if t < 10:
                t1 = '0' + str(t)
            else:
                t1 = str(t)
                page_group.append(link + '-' + t1)
                t += 1
            return page_group

    #截取节日名称和对应的日期,并更新到数据库
    def geteveyTable(self, source, ym):
        everytable = re.findall('(<div class="wnrl_riqi">.*?</div>)', source,
                                re.S)
        for i in range(0, len(everytable) - 1):
            #print( ''.join(everytable[i]) )
            if everytable[i].find('wnrl_td_bzl wnrl_td_bzl_hong') > 0:
                hdate = ym + '-' + everytable[i].split('')[-3].split('>')[-1]
                hname = everytable[i].split('')[-2].split('>')[-1]
                sql = "update dim_dateA set HolidayName=/'" + hname + "/' where to_char(DateKey,'yyyy-mm-dd') =/'" + hdate + "/'"
                self.updateDB(sql)
                return ('不知道return什么')

    #更新数据库
    def updateDB(self, url):
        conn = cx_Oracle.connect('showbi', 'soa123', '127.0.0.1:1521/showbi')
        cursor = conn.cursor()
        cursor.execute(url)
        conn.commit()
        cursor.close()
        conn.close()
        if __name__ == '__main__':
            url = 'http://wannianrili.51240.com/?q=2012-01'
            print(u'初始化类..')
            myspider = spider()
            all_links = myspider.changePage(url, 2019)
            for link in all_links:
                print(u'正在处理页面..' + link)
                html = myspider.getSource(link)
                ym = link[32:]
                everyyear = myspider.geteveyTable(html, ym)
                print('-----------------')
                print('更新完成!')





#coding:utf-8
import requests
import re
import sys
import cx_Oracle
reload(sys)
sys.setdefaultencoding('utf8')


class spider(object):
    def __init__(self):
        print(u'开始爬取...')

    #获取网页源码
    def getSource(self, url):
        html = requests.get(url)
        return html.text

    #改变url实现抓取12~16年的假日
    def changePage(self, url, total_page):
        now_page = int(url[25:29])
        page_group = []
        for i in range(now_page, total_page + 1):
            link = 'http://fangjia.51240.com/' + str(i) + '__fangjia/'
            page_group.append(link)
            return page_group

    #把页面上假日的table截取出来
    def geteveyTable(self, source):
        everytable = re.findall('(<table width="520".*?</table>)', source,
                                re.S)
        return everytable

    # 修改日期格式以便sql使用
    def changeType(self, str):
        # str1=re.sub(re.S,str,'(*)','')
        if str.find('~') == -1:
            str = str + '~' + str[7:]
            str1 = str.split('月')
            m1 = str1[0][7:]
            index = str1[1].index('日')
            index2 = str1[1].index('~')
            d1 = str1[1][0:index]
            m2 = str1[1][index2 + 1:]
            d2 = str1[2].split('日')[0]
            if int(m1) < 10:
                m1 = '0' + m1
                if int(d1) < 10:
                    d1 = '0' + d1
                    if int(m2) < 10:
                        m2 = '0' + m2
                        if int(d2) < 10:
                            d2 = '0' + d2
                            return 'between /' '+str1[0][0:4]+' - '+m1+' - '+d1+' / ' and /' '+ str1[0][0:4]+' - '+m2+' - '+d2+' / ''

    #更新数据库
    def updateDB(self, url):
        conn = cx_Oracle.connect('showbi', 'soa123', '127.0.0.1:1521/showbi')
        cursor = conn.cursor()
        cursor.execute(url)
        conn.commit()
        cursor.close()
        conn.close()

    #分割源码获得每个假日对应的日期
    def getInfo(self, eachyear):
        info = {}
        ho = re.findall('jiad/">(.*?)</a>', eachyear, re.S)
        year = re.search('<a href="/(.*?)_', eachyear, re.S).group(1)
        a = re.findall('<td>(.*?)</td>', eachyear, re.S)
        j = len(a)
        i = 0
        k = 0
        while (i < j):
            if i > j:
                continue
                holidayname = ''.join(ho[k])
                temp = year + '年' + ''.join(a[i])
                holiday = self.changeType(str(temp))
                sql = "update dim_dateA set HolidayName=/'" + holidayname + "/',IsHolidays=1 where to_char(DateKey,'yyyy-mm-dd') " + holiday
                self.updateDB(sql)
                i += 3
                k += 1


if __name__ == '__main__':
    url = 'http://fangjia.51240.com/2012__fangjia/'
    print(u'初始化类..')
    myspider = spider()
    all_links = myspider.changePage(url, 2016)
    for link in all_links:
        print(u'正在处理页面..' + link)
        html = myspider.getSource(link)
        everyyear = myspider.geteveyTable(html)
        for each in everyyear:
            myspider.getInfo(each)
            print('更新完成!')
