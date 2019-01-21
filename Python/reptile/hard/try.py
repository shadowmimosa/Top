import requests, json, os
import bs4
from bs4 import BeautifulSoup


class FileOperation(object):
    """文件操作

    包含文件读、写、判断文件大小

    Functions:
        read_file: 
        write_file:
    """

    # def __init__(self, path, content=None):
    #     self.path = path
    #     self.content = content

    def read_file(self, path):
        """打开文件，按行读取；返回所有行

        ``path`` 文件路径  
        ``type(return) = list``
        """
        with open(path, 'r', encoding='utf-8') as fn:
            lists = fn.readlines()
        return lists

    def write_file(self, path, content):
        """打开文件，并写入内容  

        ``path`` 文件路径  
        ``content`` 写入的内容  
        """
        with open(path, 'a', encoding='utf-8') as fn:
            if type(content) == dict:
                json.dump(content, fn)
            elif type(content) == str and content != "\n":
                fn.write(content)
            elif type(content) == list:
                for index in range(len(content)):
                    fn.write(str(content[index]))
            elif type(content) == bytes:
                fn.write(content.decode('utf-8'))
            fn.write("\n")

    import os

    # 字节 bytes 转化 kb\m\g
    def formatSize(self, bytes):
        try:
            bytes = float(bytes)
            kb = bytes / 1024
        except:
            print("传入的字节格式不对")
            return "Error"

        if kb >= 1024:
            M = kb / 1024
            if M >= 1024:
                G = M / 1024
                return "%fG" % (G)
            else:
                return "%fM" % (M)
        else:
            return "%fkb" % (kb)

    # 获取文件大小
    def getDocSize(self, path):
        try:
            size = os.path.getsize(path)
            return size
        except Exception as err:
            print(err)

    # 获取文件夹大小
    def getFileSize(self, path):
        sumsize = 0
        try:
            filename = os.walk(path)
            for root, dirs, files in filename:
                for fle in files:
                    size = os.path.getsize(path + fle)
                    sumsize += size
            return sumsize
        except Exception as err:
            print(err)


def get_json_value(obj, pointer):
    """根据 key, 取出 dicts 或 json 中的 value  

    ``obj`` is a objection json or dict  
    ``pointer`` is the key
    """
    import jsonpointer
    obj_value = jsonpointer.resolve_pointer(obj, pointer)
    return obj_value


def push_post_and_down_element(path, url=None):
    fn = FileOperation()
    raw_url = "http://republish.cspea.org.cn/cspea/ProjectRealServlet?action=list&zone=210000&sertype=2&index_real=more&forwardPage={}"

    for i in range(1, 100):
        url = raw_url.format(i)
        re_return = pull_get(url)
        raw_str = soup_select(re_return, "div.mlist > form > table > tr.td02")

        for index in raw_str:
            raw_need = soup_select(index, "td > a")
            need = raw_need[0].attrs
            fn.write_file(path, need)
        fn.write_file(path, "\n")


def pull_get(url):
    """get 请求

    return response
    """
    re = requests.get(url, verify=False)
    return re


def soup_select(obj, select_ele, encode_type='lxml'):
    """取出网页内容

    Args:  
        ``obj``: 原始数据
        ``select_ele``: 待取出内容标签
        ``encode_type``: 解析器，默认使用 lxml
    Return:  
        返回取出内容
    """
    if type(obj) == requests.models.Response:
        raw_text = BeautifulSoup(obj.text, encode_type)
        need_text = raw_text.select(select_ele)
    elif type(obj) == bs4.element.Tag:
        need_text = obj.select(select_ele)
    return need_text


def parse_element(read_path, write_path):
    fn = FileOperation()
    raw_lists = fn.read_file(read_path)

    for index in range(0, len(raw_lists)):
        try:
            read_data = json.loads(raw_lists[index])
            url = get_json_value(read_data, "/href")
            fn.write_file(write_path, url)
        except json.decoder.JSONDecodeError:
            fn.write_file(write_path, "\n")
            # pass


def open_url(path):
    fn = FileOperation()
    url_lists = fn.read_file(path)
    for index in range(0, len(url_lists)):
        url = url_lists[index].replace("\n", '')
        if len(url) != 0:
            re_return = pull_get(url)
        else:
            continue
        href = soup_select(re_return,
                           'div.content > div.li_top_noclick > a#li_top_font')
        need_url = get_json_value(href[0].attrs, "/href")
        if "61.161.158.178:9090" in need_url:
            fn.write_file("./finally_url.txt", need_url)


def down_finaurl_text(path):
    fn = FileOperation()
    urls = fn.read_file(path)

    template_size = fn.getFileSize("./name.txt")

    for index in range(0, len(urls)):
        url = urls[index].replace("\n", '')
        re_return = pull_get(url)

        # 初始化模板
        if template_size < 32:
            initialization_template(re_return)


def initialization_template(raw):
    """初始化 表格的填充模板"""
    fn = FileOperation()
    soup = BeautifulSoup(raw.text, 'lxml')
    all_tr = soup.find_all('tr')

    for index in range(0, len(all_tr)):
        index_td = all_tr[index].find_all('td')
        length = len(index_td)
        if length == 1:
            if index_td[0].string != '\n':
                fn.write_file('./name.txt', index_td[0].string)
        elif length == 2:
            fn.write_file('./name.txt', index_td[0].text)
            a = type(index_td[0].string)
            if index_td[0].text in ('所在地区', '所属行业'):
                fn.write_file('./name.txt',
                              index_td[1].contents[1].attrs['id'])
                fn.write_file('./name.txt',
                              index_td[1].contents[1].attrs['id'])
            else:
                fn.write_file('./name.txt', index_td[1].attrs['id'])
        elif length == 3:
            fn.write_file('./name.txt', index_td[0].text)
            fn.write_file('./name.txt', index_td[1].text)
            fn.write_file('./name.txt', index_td[2].attrs['id'])
        elif length == 4:
            fn.write_file('./name.txt', index_td[0].text)
            fn.write_file('./name.txt', index_td[1].attrs['id'])
            fn.write_file('./name.txt', index_td[2].text)
            fn.write_file('./name.txt', index_td[3].attrs['id'])
        elif length != 0:
            print(length)


if __name__ == "__main__":
    path = "./try.txt"

    # push_post_and_down_element(path)
    # parse_element(path, "./try_url.txt")
    # open_url("./try_url.txt")
    down_finaurl_text("./python/reptile/hard/finally_url.txt")

    # 安居客
    # re_return = pull_get(
    #     # "https://m.anjuke.com/wh/xinfang/?from=anjuke_home&tdsourcetag=s_pctim_aiomsg"
    #     "https://m.anjuke.com/xinfang/api/loupan/similarities?cid=22&page=2&is_homeIndex=1&history_url=https:%2F%2Fm.anjuke.com%2Fwh%2Fxinfang%2F%3Ffrom%3Danjuke_home%26tdsourcetag%3Ds_pctim_aiomsg"
    # )
