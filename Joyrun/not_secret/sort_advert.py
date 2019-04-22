import random
import time
import requests

exposure_url_list = [
    "http://g.cn.miaozhen.com/x/k=2119242&p=7OMQR&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo={}&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2={}&m4=__AAID__&m5={}&m6=__MAC1__&m6a=__MAC__&o=",
    "http://g.cn.miaozhen.com/x/k=2119242&p=7OMQS&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo={}&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2={}&m4=__AAID__&m5={}&m6=__MAC1__&m6a=__MAC__&o=",
    "http://g.cn.miaozhen.com/x/k=2119242&p=7OMQT&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo={}&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2={}&m4=__AAID__&m5={}&m6=__MAC1__&m6a=__MAC__&o="
]
jump_url_list = [
    "http://e.cn.miaozhen.com/r/k=2119242&p=7OMQR&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo={}&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2={}&m4=__AAID__&m5={}&m6=__MAC1__&m6a=__MAC__&o=",
    "http://e.cn.miaozhen.com/r/k=2119242&p=7OMQS&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo={}&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2={}&m4=__AAID__&m5={}&m6=__MAC1__&m6a=__MAC__&o=",
    "http://e.cn.miaozhen.com/r/k=2119242&p=7OMQT&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo={}&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2={}&m4=__AAID__&m5={}&m6=__MAC1__&m6a=__MAC__&o="
]


def change_url():

    import json

    with open(
            r"C:\Users\ShadowMimosa\Documents\Fiddler2\Fiddler\advert-list.json",
            'r',
            encoding='utf-8') as fn:
        advert_list = json.loads(fn.read())

    final = []

    for value in advert_list["data"]:
        if type(value) != dict:
            continue
        if len(final) == 0:
            final.append(value)
        else:
            ad_type = int(value["ad_type"])
            lenght = len(final)
            for index in range(len(final)):
                ad_type_ = int(final[index]["ad_type"])
                if ad_type > ad_type_ and index != lenght - 1:
                    continue
                else:
                    final.insert(index, value)
                    break
    imp_list = [
        "http://g.cn.miaozhen.com/x/k=2083147&p=7FSIv&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&o=",
        "http://g.cn.miaozhen.com/x/k=2083147&p=7FSIw&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&o=",
        "http://g.cn.miaozhen.com/x/k=2083147&p=7FSIx&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&o=",
        "http://g.cn.miaozhen.com/x/k=2083147&p=7FSIy&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&o=",
        "http://g.cn.miaozhen.com/x/k=2083147&p=7FSIz&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&o=",
        "http://g.cn.miaozhen.com/x/k=2083147&p=7FSJ0&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&o=",
        "http://g.cn.miaozhen.com/x/k=2083147&p=7FSJ1&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&o=",
        "http://g.cn.miaozhen.com/x/k=2083147&p=7FSJ2&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&o="
    ]
    click_list = [
        "http://e.cn.miaozhen.com/r/k=2083147&p=7FSIv&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&vo=38136d3e&vr=2&o=http%3A%2F%2Fwww.bmw.com.cn%2Fzh%2Fcampaign%2F2018%2Fhood_to_coast%2Fmobi%2Findex.html%3Fbmw%3Ddis%3AHTC%3Abrand%3Aa_joyrun_18-q2-x-bd-htc-lau_hp_fs_fs",
        "http://e.cn.miaozhen.com/r/k=2083147&p=7FSIw&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&vo=38136d3e&vr=2&o=http%3A%2F%2Fwww.bmw.com.cn%2Fzh%2Fcampaign%2F2018%2Fhood_to_coast%2Fmobi%2Findex.html%3Fbmw%3Ddis%3AHTC%3Abrand%3Aa_joyrun_18-q2-x-bd-htc-lau_hp_pa_pa",
        "http://e.cn.miaozhen.com/r/k=2083147&p=7FSIx&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&vo=38136d3e&vr=2&o=http%3A%2F%2Fwww.bmw.com.cn%2Fzh%2Fcampaign%2F2018%2Fhood_to_coast%2Fmobi%2Findex.html%3Fbmw%3Ddis%3AHTC%3Abrand%3Aa_joyrun_18-q2-x-bd-htc-lau_hp_bg_bg",
        "http://e.cn.miaozhen.com/r/k=2083147&p=7FSIy&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&vo=38136d3e&vr=2&o=http%3A%2F%2Fwww.bmw.com.cn%2Fzh%2Fcampaign%2F2018%2Fhood_to_coast%2Fmobi%2Findex.html%3Fbmw%3Ddis%3AHTC%3Abrand%3Aa_joyrun_18-q2-x-bd-htc-lau_hp_ba_cb",
        "http://e.cn.miaozhen.com/r/k=2083147&p=7FSIz&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&vo=38136d3e&vr=2&o=http%3A%2F%2Fwww.bmw.com.cn%2Fzh%2Fcampaign%2F2018%2Fhood_to_coast%2Fmobi%2Findex.html%3Fbmw%3Ddis%3AHTC%3Abrand%3Aa_joyrun_18-q2-x-bd-htc-lau_hp_fs_fs2",
        "http://e.cn.miaozhen.com/r/k=2083147&p=7FSJ0&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&vo=38136d3e&vr=2&o=http%3A%2F%2Fwww.bmw.com.cn%2Fzh%2Fcampaign%2F2018%2Fhood_to_coast%2Fmobi%2Findex.html%3Fbmw%3Ddis%3AHTC%3Abrand%3Aa_joyrun_18-q2-x-bd-htc-lau_hp_pa_pa2",
        "http://e.cn.miaozhen.com/r/k=2083147&p=7FSJ1&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&vo=38136d3e&vr=2&o=http%3A%2F%2Fwww.bmw.com.cn%2Fzh%2Fcampaign%2F2018%2Fhood_to_coast%2Fmobi%2Findex.html%3Fbmw%3Ddis%3AHTC%3Abrand%3Aa_joyrun_18-q2-x-bd-htc-lau_hp_bg_bg2",
        "http://e.cn.miaozhen.com/r/k=2083147&p=7FSJ2&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&vo=38136d3e&vr=2&o=http%3A%2F%2Fwww.bmw.com.cn%2Fzh%2Fcampaign%2F2018%2Fhood_to_coast%2Fmobi%2Findex.html%3Fbmw%3Ddis%3AHTC%3Abrand%3Aa_joyrun_18-q2-x-bd-htc-lau_hp_ba_cb2"
    ]

    for value in final:
        num = random.randint(0, 7)
        value["exposure_url"] = imp_list[num]
        value["jump_url"] = click_list[num]

    with open(
            r"C:\Users\ShadowMimosa\Documents\Fiddler2\Fiddler\advert-list.json",
            'w',
            encoding='utf-8') as fn:
        advert_list["data"] = final
        fn.write(json.dumps(advert_list, ensure_ascii=False))


def file_write(content):

    with open("imei.txt", "a", encoding="utf-8") as fw:
        fw.write(content + '\n')


def build_idfa(content):
    import hashlib

    md5_obj = hashlib.md5((content + 'joyrun').encode('utf-8'))
    md5_obj.update(content.encode("utf-8"))

    secret = md5_obj.hexdigest().upper()

    secret = secret[:8] + '-' + secret[8:12] + '-' + secret[
        12:16] + '-' + secret[16:20] + '-' + secret[20:]

    return secret


def build_imei():

    random_list = random.sample(range(1, 9000000), 30000)

    lenght = len(random_list)
    for index in range(lenght // 2):
        random1 = random_list[index] + 1000000
        random2 = random_list[lenght - index - 1] + 1000000

        temp_num = str(random1) + str(random2)

        num1 = 0
        num2 = 0
        for index in temp_num:
            index = int(index)
            if index % 2 == 0:
                num1 += index
            else:
                temp = index * 2
                num2 = num2 + temp / 10 + temp % 10

        last_num = int((num1 + num2) % 10)
        if last_num == 0:
            last_num = 0
        else:
            last_num = 10 - last_num

        final_secret = temp_num + str(last_num)
        final_secret = final_secret + '\n' + build_idfa(final_secret)

        file_write(final_secret)


def get_session():
    """创建 session 示例，以应对多线程"""

    #设置重连次数
    requests.adapters.DEFAULT_RETRIES = 5
    # 设置连接活跃状态为False
    session = requests.session()
    session.keep_alive = False
    session.verify = False

    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    #将重试规则挂载到http和https请求
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session


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


def deal_re(url):
    """requests of get"""

    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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


def get_imei():
    """生成用于遍历的迭代器，以应对大文件"""

    with open('./imei.txt', 'r') as fn:
        for line in fn:
            yield line


def deal_url(imei):

    if len(imei) < 20:
        for exposure_url in exposure_url_list:
            deal_re(exposure_url.format("0", imei, "__IDFA__"))
        for jump_url in jump_url_list:
            deal_re(jump_url.format("0", imei, "__IDFA__"))
    else:
        for exposure_url in exposure_url_list:
            deal_re(exposure_url.format("1", "__IMEI__", imei))
        for jump_url in jump_url_list:
            deal_re(jump_url.format("1", "__IMEI__", imei))


def request_miaozhen():

    yield_imei = get_imei()
    while True:
        try:
            imei = next(yield_imei).replace('\n', '')
            time.sleep(random.randint(3, 10))
        except TypeError as exc:
            if exc == 'WebsiteError':
                continue
        except StopIteration:
            yield_imei.close()
            break

        deal_url(imei)


def multi_processes(processes=4):
    """多进程，默认最多 4 个进程"""

    from multiprocessing import Process, Queue, Pool, freeze_support

    pool = Pool(processes)
    yield_imei = get_imei()

    while True:
        try:
            pool.apply_async(deal_url, (next(yield_imei), ))
        except TypeError as exc:
            if exc == 'WebsiteError':
                continue
        except StopIteration:
            yield_imei.close()
            break
    pool.close()
    pool.join()


def main():
    change_url()  # 修改 advert 中 url
    # build_imei()  # 生成 IMEI & IDFA
    # request_miaozhen()
    # multi_processes(100)


if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()

