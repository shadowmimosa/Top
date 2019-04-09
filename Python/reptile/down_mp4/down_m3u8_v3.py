import os

globals_list = {}


def get_session(pool_connections=50, pool_maxsize=50, max_retries=3):
    """构造 session"""
    import requests
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    #设置重连次数
    # requests.adapters.DEFAULT_RETRIES = 15
    # 设置连接活跃状态为False
    session = requests.session()
    session.keep_alive = False
    session.verify = False
    session.timeout = (3.05, 5)
    requests.adapters.HTTPAdapter()
    adapter = requests.adapters.HTTPAdapter(
        # pool_connections=pool_connections,
        # pool_maxsize=pool_maxsize,
        max_retries=max_retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session


def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)
        f.flush()


def analy_url(url):
    import re

    raw_m3u8 = session.get(url + "index.m3u8").content.decode("utf-8")
    file_path = globals_list["file_path"]
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    write_file(os.path.join(file_path, "index.m3u8"), raw_m3u8)

    deal_m3u8 = raw_m3u8.split("\n")
    new_m3u8 = []

    pattern = re.compile(r".*[0-9]*.ts")
    for value in deal_m3u8:
        if re.match(pattern, value):
            new_m3u8.append(value)

    return new_m3u8


def download(q):
    import requests.exceptions
    url, file_path = globals_list["url"], globals_list["file_path"]

    while True:
        try:
            index = q.get_nowait()
        except Exception as exc:
            if exc == "Empty":
                break
        size = 0
        num = 0
        print("---> Downloading {} now.".format(index.replace('.ts', '')))
        try:
            resp = session.get(url + index, stream=True)
        except requests.exceptions.ChunkedEncodingError:
            resp = session.get(url + index, stream=True)
        except requests.exceptions.Timeout:
            resp = session.get(url + index, stream=True)
        else:
            with open(os.path.join(file_path, index), 'wb') as mp4:
                try:
                    for chunk in resp.iter_content(
                            chunk_size=1024 * 1024):  #可以边下载边存到硬盘中
                        if chunk:
                            mp4.write(chunk)
                            size += len(chunk)
                            num += 1
                except requests.exceptions.ConnectionError:
                    print("The {} is downloaded fail\n".format(index))
                    continue
                except requests.exceptions.ChunkedEncodingError:
                    print("The {} is downloaded fail\n".format(index))
                    continue
                print(
                    "The {} is down.\nThe size is {}, and writing times is {}.\n".
                    format(index.replace('.ts', ''), size, num))


def single_download(indexs):
    import requests.exceptions
    url, file_path = globals_list["url"], globals_list["file_path"]
    for index in indexs:
        size = 0
        num = 0
        print("---> Downloading {} now.".format(index.replace('.ts', '')))
        try:
            resp = session.get(url + index, stream=True)
        except requests.exceptions.ChunkedEncodingError:
            resp = session.get(url + index, stream=True)
        except requests.exceptions.Timeout:
            resp = session.get(url + index, stream=True)
        else:
            with open(os.path.join(file_path, index), 'wb') as mp4:
                try:
                    for chunk in resp.iter_content(
                            chunk_size=1024 * 1024):  #可以边下载边存到硬盘中
                        if chunk:
                            mp4.write(chunk)
                            size += len(chunk)
                            num += 1
                except requests.exceptions.ConnectionError:
                    print("The {} is downloaded fail\n".format(index))
                    continue
                except requests.exceptions.ChunkedEncodingError:
                    print("The {} is downloaded fail\n".format(index))
                    continue
                print(
                    "The {} is down.\nThe size is {}, and writing times is {}.\n"
                    .format(index.replace('.ts', ''), size, num))


def multi_thread(indexs):
    import threading
    import queue

    q = queue.Queue()
    for index in indexs:
        q.put(index)

    thread0 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread1 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread2 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread3 = threading.Thread(target=download, args=(q, ), name="thread_0")    
    thread4 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread5 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread6 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread7 = threading.Thread(target=download, args=(q, ), name="thread_0")    
    thread8 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread9 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread10 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread11 = threading.Thread(target=download, args=(q, ), name="thread_0")
    thread0.start()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()    
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread0.join()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()    
    thread8.join()
    thread9.join()
    thread10.join()
    thread11.join()


def main(url):
    import time
    globals_list["file_path"] = os.path.join(
        os.path.dirname(__file__),
        url.split('/')[-2])
    globals_list["url"] = url

    indexs = analy_url(url)

    # a1 = time.time()
    # single_download(indexs)
    # print("end time is {}".format(time.time() - a1))

    a2 = time.time()
    multi_thread(indexs)
    print("end time is {}".format(time.time() - a2))


if __name__ == "__main__":
    session = get_session()
    main(url="https://uuxo5.com/videos/5beb9dce9c68d1a465fe1243/")
    import ffmpeg

    