import os, random, time
import requests


def data_claean():
    """格式化 header 文件"""

    import re
    pattern = re.compile(r'".*"')

    with open('./headers.txt', 'r', encoding='utf-8') as fn:
        ua_list = fn.readlines()
        for index in range(0, len(ua_list)):
            ua_list[index] = re.search(pattern, ua_list[index]).group(0)

    with open('./headers.txt', 'w', encoding='utf-8') as fn:
        # for value in ua_list:
        fn.writelines([line + '\n' for line in ua_list])

    print('down')


def custom_header():
    """定制请求头，遍历配置文件，返回 header"""

    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html,application/xhtml+xml,*/*']
    head_accept_language = [
        'zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3'
    ]
    # head_user_agent = []
    with open('./headers.txt', 'r', encoding='utf-8') as fn:
        ua_list = fn.readlines()

    #header 为随机产生一套由上边信息的header文件
    header = {
        'Connection':
        head_connection[random.randrange(0, len(head_connection))],
        'Accept':
        head_accept[0],
        'Accept-Language':
        head_accept_language[random.randrange(0, len(head_accept_language))],
        'User-Agent':
        ua_list[random.randrange(0, len(ua_list))].replace('\n', ''),
    }
    # print(header)

    return header  #返回值为 header这个字典


def get_url():
    """生成用于遍历的迭代器，以应对大文件"""

    with open('./url_list.txt', 'r') as fn:
        for line in fn:
            yield line


def get_session():
    """创建 session 示例，以应对多线程"""

    #设置重连次数
    requests.adapters.DEFAULT_RETRIES = 15
    # 设置连接活跃状态为False
    session = requests.session()
    session.keep_alive = False
    session.verify = False

    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    #将重试规则挂载到http和https请求
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session


def deal_url(url):
    """格式化 url, 以应对网址不规范"""

    if url == '\n':
        raise TypeError('WebsiteError')
    url = url.replace('\n', '')
    if 'http' not in url:
        url = r"http://{}".format(url)

    return url


def deal_re(url):
    """requests of get"""

    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = deal_url(url)
    sesscion_a = get_session()

    print("---> 开始请求网址：{}".format(url))
    start_time = time.time()
    try:
        resp = sesscion_a.get(url, headers=custom_header(), timeout=(3.2, 30))
    except UnicodeEncodeError as exc:
        print(
            "---> The error is {}, and the website is {}. Now try again just one time."
            .format(exc, url))
        deal_re(url)
    end_time = time.time()

    if resp.status_code == 200:
        print("---> [{}]请求成功！共耗时{:.3}秒\n".format(url, end_time - start_time))
    else:
        print("---> [{}]请求失败！状态码为{}，共耗时{:.3}秒\n".format(
            url, resp.status_code, end_time - start_time))


def single_process():
    """单进程、单线程"""

    yield_url = get_url()

    while True:
        try:
            deal_re(next(yield_url))
            time.sleep(random.randint(3, 10))
        except TypeError as exc:
            if exc == 'WebsiteError':
                continue
        except StopIteration:
            yield_url.close()
            break


def thread_four():
    """多线程，初始四线程"""

    import threading
    import queue
    q = queue.Queue()
    yield_url = get_url()
    q.put(next(yield_url))
    while True:
        try:
            t1 = threading.Thread(
                target=deal_re,
                args=(next(yield_url), ),
                name="child_thread_1")
            t2 = threading.Thread(
                target=deal_re,
                args=(next(yield_url), ),
                name="child_thread_2")
            t3 = threading.Thread(
                target=deal_re,
                args=(next(yield_url), ),
                name="child_thread_3")
            t4 = threading.Thread(
                target=deal_re,
                args=(next(yield_url), ),
                name="child_thread_4")
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
        except TypeError as exc:
            if exc == 'WebsiteError':
                continue
        except StopIteration:
            yield_url.close()
            break


def multi_processes(processes=10):
    """多进程，默认最多 10 个进程"""
    from multiprocessing import Process, Queue, Pool, freeze_support

    pool = Pool(processes)
    yield_url = get_url()
    while True:
        try:
            pool.apply_async(deal_re, (next(yield_url), ))
        except TypeError as exc:
            if exc == 'WebsiteError':
                continue
        except StopIteration:
            yield_url.close()
            break
    pool.close()
    pool.join()


def main(run_type="single", number=10):
    """入口函数"""

    if run_type == "single":
        single_process()
    elif run_type == "threads":
        thread_four()
    elif run_type == "processes":
        multi_processes(number)
    else:
        print("---> The parameter is error, please check it. \nParameter: {}".
              format(run_type))


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # requests_headers()

    main_start = time.time()
    # main("processes", 256)
    # main("processes", 1000)
    main("processes")
    # multi_processes(5)
    main_end = time.time()

    # thread_four()
    pro_start = time.time()
    # multi_processes()
    pro_end = time.time()

    print(
        "---> Single process's time is {:.8}\n---> Multi process's time is {:.8}"
        .format(main_end - main_start, pro_end - pro_start))
