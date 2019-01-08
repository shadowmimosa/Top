import requests, json
import bs4
from bs4 import BeautifulSoup


def write_file(path, content):
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


def read_file(path):
    """打开文件，按行读取；返回所有行

    ``path`` 文件路径  
    ``type(return) = list``
    """
    with open(path, 'r', encoding='utf-8') as fn:
        lists = fn.readlines()
    return lists


def get_json_value(obj, pointer):
    """根据 key, 取出 dicts 或 json 中的 value  

    ``obj`` is a objection json or dict  
    ``pointer`` is the key
    """
    import jsonpointer
    obj_value = jsonpointer.resolve_pointer(obj, pointer)
    return obj_value


def push_post_and_down_element(path, url=None):
    raw_url = "http://republish.cspea.org.cn/cspea/ProjectRealServlet?action=list&zone=210000&sertype=2&index_real=more&forwardPage={}"

    for i in range(1, 100):
        url = raw_url.format(i)
        re_return = pull_get(url)
        raw_str = soup_select(re_return, "div.mlist > form > table > tr.td02")

        for index in raw_str:
            raw_need = soup_select(index, "td > a")
            need = raw_need[0].attrs
            write_file(path, need)
        write_file(path, "\n")


def pull_get(url):
    re = requests.get(url, verify=False)
    return re


def soup_select(obj, select_ele, encode_type='html.parser'):
    if type(obj) == requests.models.Response:
        raw_text = BeautifulSoup(obj.text, 'html.parser')
        need_text = raw_text.select(select_ele)
    elif type(obj) == bs4.element.Tag:
        need_text = obj.select(select_ele)
    return need_text


def parse_element(read_path, write_path):
    raw_lists = read_file(read_path)

    for index in range(0, len(raw_lists)):
        try:
            read_data = json.loads(raw_lists[index])
            url = get_json_value(read_data, "/href")
            write_file(write_path, url)
        except json.decoder.JSONDecodeError:
            write_file(write_path, "\n")
            # pass


def open_url(path):
    url_lists = read_file(path)
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
            write_file("./finally_url.txt", need_url)


def down_finaurl_text(path):
    urls = read_file(path)

    for index in range(0, len(urls)):
        url = urls[index].replace("\n", '')
        re_return = pull_get(url)

        raw_text = soup_select(
            re_return,
            'body > div.list > div > div > div.list_con > table > tbody > tr > td > table > tbody > tr > td'
        )
        soup = BeautifulSoup(re_return.content, 'html.parser')
        text_table=soup.find_all('table')
        text_td=soup.find_all('td')
        print(raw_text)
        write_file("./python/reptile/hard/raw_html.txt", raw_text)


if __name__ == "__main__":
    path = "./try.txt"

    # push_post_and_down_element(path)
    # parse_element(path, "./try_url.txt")
    # open_url("./try_url.txt")
    down_finaurl_text("./python/reptile/hard/finally_url.txt")

    # re_return = pull_get(
    #     # "https://m.anjuke.com/wh/xinfang/?from=anjuke_home&tdsourcetag=s_pctim_aiomsg"
    #     "https://m.anjuke.com/xinfang/api/loupan/similarities?cid=22&page=2&is_homeIndex=1&history_url=https:%2F%2Fm.anjuke.com%2Fwh%2Fxinfang%2F%3Ffrom%3Danjuke_home%26tdsourcetag%3Ds_pctim_aiomsg"
    # )
