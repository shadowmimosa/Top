import requests
import time

from Config import *

server_timestamp = 0


def get_server_time(content=''):
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


def get(url):
    header = {
        "ypcookie":
        "ypcookie=" + "sid=" + "0540af2a7d569d7831ebba6e7d18c53f" + "&" +
        "uid=" + "32519818",
        "APPVERSION":
        APPVERSION,
        "Content-Type":
        ContentType,
        "User-Agent":
        UserAgent,
        "APP_DEV_INFO":
        APPDEVINFO,
        "SYSVERSION":
        SYSVERSION,
        "MODELTYPE":
        MODELTYPE
    }


if __name__ == "__main__":
    print(get_server_time())
