import requests
import csv
import re
import time
from urllib.parse import quote
from bs4 import BeautifulSoup

base_url = "http://www.china5080.com/famous/"
level_url = "http://www.china5080.com/user/{}/level"


def post(pagenum=None):
    if pagenum is None:
        resp = requests.post(base_url)
    else:
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "zca_pagedName_op": "zca_pagedName_pagenum",
            "zcp_pagedName_pagenum": pagenum
        }
        resp = requests.post(base_url, data=data, headers=header)

    pattern = r"\<a href\=\"javascript:GoToVipInfo\('.*'\)\"\>"
    nickname_list = re.findall(pattern, resp.text)

    pattern = r'\'.*\''
    nickname = ""
    for value in nickname_list:
        value = re.findall(pattern, value)[0].replace('\'', '')
        nickname += value
        nickname += '\n'

    with open("china0508.txt", 'a') as fn:
        fn.write(nickname)


def get(nickname, filename="china0508_03.txt"):
    resp = requests.get(level_url.format(nickname))
    raw = resp.text
    soup = BeautifulSoup(raw, 'lxml')

    in_addtcnt1 = soup.find(attrs={
        "class": "in_addtcnt1"
    }).text.replace('\t', '').replace('\n', '')
    in_levcnt5 = soup.find(attrs={
        "class": "in_levcnt5"
    }).text.replace('\t', '').replace('\n', '')

    in_addtcnt1 = in_addtcnt1.split('\r')
    in_levcnt5 = in_levcnt5.split('\r')

    in_addtcnt1 = [i for i in in_addtcnt1 if i != '']
    in_levcnt5 = [i for i in in_levcnt5 if i != '']

    final_str = nickname + '\t'

    for value in in_addtcnt1:
        final_str += value
        final_str += '\t'
    for value in in_levcnt5:
        final_str += value
        final_str += '\t'

    with open(filename, 'a') as fn:
        fn.write(final_str)
        fn.write('\n')


def multi_processes(processes=10):

    from multiprocessing import Pool

    pool = Pool(processes)

    with open("china0508.txt", 'r') as fn:
        nickname = fn.readlines()
    for value in nickname:
        pool.apply_async(get, (value.replace('\n', ''), ))

    pool.close()
    pool.join()


def main():
    # for x in range(1, 49):
    #     post(x)

    with open("china0508.txt", 'r') as fn:
        nickname = fn.readlines()
    for value in nickname:
        get(value.replace('\n', ''), "china0508_02.txt")


if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    timestamps = time.time()
    main()
    single_times = time.time() - timestamps

    timestamps = time.time()
    multi_processes()
    multi_times = time.time() - timestamps

    print(single_times, '\n', multi_times)
