def write_file(path, content):
    with open(path, 'ab') as f:
        f.write(content)
        f.flush()

def get_session(pool_connections, pool_maxsize, max_retries):
    """构造 session"""
    
    
def download(url):
    import requests, os
    import urllib3
    from requests.adapters import HTTPAdapter
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    file_path = os.path.join(os.path.dirname(__file__), url.split('/')[-2])
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    #设置重连次数
    requests.adapters.DEFAULT_RETRIES = 15
    # 设置连接活跃状态为False
    session = requests.session()
    session.keep_alive = False

    adapter = HTTPAdapter(max_retries=3)
    #将重试规则挂载到http和https请求
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    index_m3u8 = session.get(
        url + "index.m3u8", verify=False).content.decode("utf-8").split('\n')
    for value in index_m3u8:
        if "index" in value:
            size = 0
            num = 0
            print("---> Downloading {} now.".format(value.replace('.ts', '')))
            try:
                resp = session.get(
                    url + value, stream=True, verify=False, timeout=(3.05, 5))
            except requests.exceptions.ChunkedEncodingError:
                resp = session.get(url + value, stream=True, verify=False)
            except requests.exceptions.Timeout:
                resp = session.get(url + value, stream=True, verify=False)
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
                    print(
                        "The {} is down.\nThe size is {}, and writing times is {}.\n"
                        .format(value.replace('.ts', ''), size, num))

def main():
    download("https://uuxo5.com/videos/5beb9dce9c68d1a465fe122b/")

if __name__ == "__main__":
    main()
    # url = "https://uuxo8.com/videos/5bb88e4b5d4b454c7e8d415d/"
    url = "https://uuxo5.com/videos/5beb9dce9c68d1a465fe122b/"
