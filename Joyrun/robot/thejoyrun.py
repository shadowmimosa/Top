import requests
import time
import hashlib
import urllib

from Config import *

server_timestamp = 0


def get_server_time(content=''):
    """获取服务器时间"""

    base_url = "http://api{}.thejoyrun.com/GetTimestamp.aspx"

    if "test" in content:
        url = base_url.format("-test")
    elif "beta" in content:
        url = base_url.format("-beta")
    else:
        url = base_url.format('')

    global server_timestamp
    local_time = int(time.time())
    diff_time = local_time - server_timestamp - 280

    if diff_time > 0:
        re = requests.get(url)
        server_timestamp = eval(re.text)["lasttime"]

    return server_timestamp


class RequestMethod(object):
    """request 相关方法集合"""

    def __init__(self):
        """公共变量"""

        self.sign_online = "A4729E62-3701-48C3-A15D-7391838FA186"
        self.sign_test = "a9ff6970eb814e6894389ca8b12f3030"
        self.sign_beta = "A9FF6970EB814E6894389CA8B12F3030"

        self.ypcookie = "uid={}&sid={}"
        self.url = "{}{}"

    def uid_sid(self, user):
        """分离出 uid sid"""

        if user == '':
            user = "32519818/17d5a5172d2dddbcaea9ccd91fe3eef6"

        uid = user.split('/')[0]
        sid = user.split('/')[1]

        return uid, sid

    def build_cookie(self, user):
        """生成 ypcookie"""

        uid, sid = self.uid_sid(user)

        ypcookie = self.ypcookie.format(uid, sid)

        return ypcookie

    def build_signature(self, maps={}, user=''):
        """构造 signature"""

        uid, sid = self.uid_sid(user)

        # if server_timestamp==0:
        #     get_server_time()

        sign_dict = {"timestamp": server_timestamp}

        for map_ in sorted(maps.items()):
            sign_dict[map_[0]] = map_[1]

        sign_list = sorted(sign_dict.items())
        signparam = ''
        for index in range(len(sign_list)):
            key = sign_list[index][0]
            value = sign_list[index][1]
            string = key + str(value)
            signparam = signparam + string

        signkey = signparam + appkey2 + uid + sid
        signature = hashlib.md5(signkey.encode('utf-8')).hexdigest().upper()

        return signature

    def get(self, path, maps={}, user='', base_url=api_URL):
        """get 方法"""

        url = self.url.format(base_url, path)
        ypcookie = self.build_cookie(user)

        header = {
            "ypcookie": ypcookie,
            "APPVERSION": APPVERSION,
            "Content-Type": ContentType,
            "User-Agent": UserAgent,
            "APP_DEV_INFO": APPDEVINFO,
            "SYSVERSION": SYSVERSION,
            "MODELTYPE": MODELTYPE,
            "_sign": self.sign_beta,
        }
        cookies = {
            "app_version": appversion,
            "ypcookie": urllib.parse.quote(ypcookie)
        }

        signature = self.build_signature(maps, user)

        post_dict = {"timestamp": server_timestamp}
        post_dict["signature"] = signature

        for map_ in sorted(maps.items()):
            post_dict[map_[0]] = map_[1]

        re = requests.get(
            url=url, params=post_dict, headers=header, cookies=cookies)
        print(re.status_code)


def cut_string(sign):

    new_sign = ''

    if '?' in sign:
        sign_list = sign.split('?')
        new_sign = new_sign + sign_list[0]
        sign = sign_list[-1]

    if '&' in sign:
        sign_list = sign.split('&')
        sign_list = sorted(sign_list)
        for index in sign_list:
            new_sign = new_sign + index
    #         if '=' in index:
    #             index = index.split('=')
    #             new_sign = new_sign + index[0] + index[-1]
    # elif '=' in sign:
    #     sign=sign.split('=')
    #     new_sign = new_sign + sign[0] + sign[-1]

    return new_sign


def check(sign):

    sign = cut_string(sign)

    _sign = "0AA65D69C29E0FF7D4F5E7840565D951"
    # "A20E12CBEF371E51785C09988144F751"
    # "43136B804F02E9662C2C81629DDEB9A3"
    # "00CF00A55EB5AD6550577F8CCD048F02"
    # "8CC06A1729F338FCC4ADAF60C2BC9F67"
    # "0AA65D69C29E0FF7D4F5E7840565D951"

    _signed = hashlib.md5(sign.encode('utf-8')).hexdigest().upper()
    print(_signed)
    if _signed == _sign:
        print("It's Rriht!!!")


if __name__ == "__main__":
    get = RequestMethod().get

    print(get_server_time())
    print(get("/user/getUserInfo", base_url=trip_URL))

    # print(
    #     get("http://trip-test.api.thejoyrun.com/user/getUserInfo",
    #         user=["32519818", "17d5a5172d2dddbcaea9ccd91fe3eef6"]))

    print(get(
        "/notify-list-id",
        {"ntfId": 13002},
        base_url=advert_URL,
    ))
    print(get("/daily/getDaily", base_url=api_URL))

    arg = "http://advert-test.api.thejoyrun.com/advert-list?signature=3D46E029E48D817BB4132D0B21E7ECDF&timestamp=1548233533"

    sign1 = arg.split('/')[-1]
    sign2 = arg.split('?')[-1]

    check(sign1)
    check(sign2)
