def write_file(path, content):
    with open(path, 'ab') as f:
        f.write(content)
        f.flush()


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


def download(url):
    import os
    import requests.exceptions

    file_path = os.path.join(os.path.dirname(__file__), url.split('/')[-2])
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    index_m3u8 = session.get(url +
                             "index.m3u8").content.decode("utf-8").split('\n')
    for value in index_m3u8:
        if "index" in value:
            size = 0
            num = 0
            print("---> Downloading {} now.".format(value.replace('.ts', '')))
            try:
                resp = session.get(url + value, stream=True)
            except requests.exceptions.ChunkedEncodingError:
                resp = session.get(url + value, stream=True)
            except requests.exceptions.Timeout:
                resp = session.get(url + value, stream=True)
            else:
                with open(os.path.join(file_path, value), 'wb') as mp4:
                    try:
                        for chunk in resp.iter_content(
                                chunk_size=1024 * 1024):  #可以边下载边存到硬盘中
                            if chunk:
                                mp4.write(chunk)
                                size += len(chunk)
                                num += 1
                    except requests.exceptions.ConnectionError:
                        print("The {} is downloaded fail\n".format(value))
                        continue
                    except requests.exceptions.ChunkedEncodingError:
                        print("The {} is downloaded fail\n".format(value))
                        continue
                    print(
                        "The {} is down.\nThe size is {}, and writing times is {}.\n"
                        .format(value.replace('.ts', ''), size, num))


def multi_thread():
    """多线程，默认 4 线程"""

    import threading
    
    
    thread0 = threading.Thread(target=download, args=path, name="thread_0")
    thread1 = threading.Thread(target=download, args=path, name="thread_0")
    thread2 = threading.Thread(target=download, args=path, name="thread_0")
    thread3 = threading.Thread(target=download, args=path, name="thread_0")


def main():
    """The function of main"""

    while True:
        pass
    # download("https://uuxo5.com/videos/5beb9dce9c68d1a465fe1230/")

    # resp=session.get(url="https://uuxo5.com/videos/5beb9dce9c68d1a465fe122b/thumbnails.jpg")
    # with open("thumbnails.jpg","wb") as fb:
    #     fb.write(resp.content)
    # download("https://uuxo5.com/videos/5beb9dce9c68d1a465fe122b/")


if __name__ == "__main__":
    session = get_session()
    main()
    # url = "https://uuxo8.com/videos/5bb88e4b5d4b454c7e8d415d/"
    # url = "https://uuxo5.com/videos/5beb9dce9c68d1a465fe122b/"
    # url = "https://uuxo5.com/videos/5beb9dce9c68d1a465fe1230"
