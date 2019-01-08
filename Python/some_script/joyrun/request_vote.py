import requests

requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
s = requests.session()
s.keep_alive = False  # 关闭多余连接

url = "https://webevent-test.thejoyrun.com/xtepxmlive/vote?teamType=2"
ypcookie = "ypcookie:sid=9b4a95cae6f4f68d39f022f1b4c1db11&uid=32519913"
data = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 9; MIX 2S Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044429 Mobile Safari/537.36",
    "Cookie": {
        "ypcookie=sid%3d01c5e2ce9c3a5968b9bbc434f8aa8055%26uid%3d32519916",
        "app_version=android4.5.0",
        "Hm_lvt_7cfaa882ea03f1adfe434be26cc8a294=1546055735,1546060875,1546062587",
        "Hm_lpvt_7cfaa882ea03f1adfe434be26cc8a294=1546062587",
        "thejoyrun=rs2il0pn92b4l1qj6aoa1bgcns"
    }
}

cookie = {
    "Cookie": {
        "ypcookie": "sid=9b4a95cae6f4f68d39f022f1b4c1db11&uid=32519913"
    }
}

re = requests.post(url, data=data)

re_return = eval(re.content)
print(type(re_return))

re_msg = re_return["msg"]
print(re.text)
