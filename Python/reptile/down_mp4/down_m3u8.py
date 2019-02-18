def write_file(path, content):
    with open(path, 'ab') as f:
        f.write(content)
        f.flush()


def download(url):
    import requests, os

    index_m3u8 = requests.get(
        url + "index.m3u8", verify=False).content.decode("utf-8").split('\n')
    file_name = url.split('/')[-2]
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    for value in index_m3u8:
        if "index" in value:
            try:
                pd_content = requests.get(url + value, verify=False).content
                write_file(file_path, pd_content)
                print("---> The {} is down".format(value.replace('.ts', '')))
            except requests.exceptions.ChunkedEncodingError:
                pd_content = requests.get(url + value, verify=False).content
                write_file(file_path, pd_content)


if __name__ == "__main__":
    url = "https://uuxo8.com/videos/5bb88e4b5d4b454c7e8d415d/"
    download(url)
