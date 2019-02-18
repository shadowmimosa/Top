import requests

from .thejoyrun import *


def get_daily(mothod):

    if mothod == 'post':
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'ypcookie': 'sid=acd3c71c52e3e69c351a19fed3c9dc04&uid=3330087'
        }
        # data = {
        #     'signature':'10036CDCC0BB6C9920B6BFAA710C7775',
        #     'latitude':23177326,
        #     'totalSteps':1820,
        #     'startRunTime':1536382738,
        #     'raceItemId':103,
        #     'totalMeters':2002,
        #     'totalSeconds':3289,
        #     'bib':'MIX',
        #     'longitude':113334831,
        #     'timestamp':1536386028,
        #     'legsData':[{"latitude":23177863,"longitude":113334960,"meters":1000,"seconds":2338},{"latitude":23177326,"longitude":113334831,"meters":2000,"seconds":951}]
        # }
        data = "timestamp=1535796925&legsData=%5B%7B%22latitude%22%3A23177932%2C%22longitude%22%3A113334290%2C%22meters%22%3A1000%2C%22seconds%22%3A250%7D%2C%7B%22latitude%22%3A23177230%2C%22longitude%22%3A113334128%2C%22meters%22%3A2000%2C%22seconds%22%3A250%7D%2C%7B%22latitude%22%3A23176591%2C%22longitude%22%3A113334784%2C%22meters%22%3A3000%2C%22seconds%22%3A245%7D%2C%7B%22latitude%22%3A23176778%2C%22longitude%22%3A113335322%2C%22meters%22%3A4000%2C%22seconds%22%3A250%7D%2C%7B%22latitude%22%3A23177457%2C%22longitude%22%3A113335638%2C%22meters%22%3A5000%2C%22seconds%22%3A250%7D%2C%7B%22latitude%22%3A23177370%2C%22longitude%22%3A113335646%2C%22meters%22%3A6000%2C%22seconds%22%3A270%7D%2C%7B%22latitude%22%3A23178125%2C%22longitude%22%3A113335199%2C%22meters%22%3A7000%2C%22seconds%22%3A245%7D%5D&longitude=113335199&latitude=23178125&totalMeters=7006&raceItemId=50&totalSteps=6720&totalSeconds=1764&bib=3330087&signature=DC1730B3B07846BED2EE965AE6DCC60D&startRunTime=1535796925"
        upload = requests.post(
            url='http://racelive-test.api.thejoyrun.com/live/rundata/upload',
            # json=data,
            data=data,
            headers=headers)
        print(upload.text)

    elif mothod == 'get':
        header = {
            "ypcookie": "sid=4aa6fff54cee4197ad5c880128791825&uid=32519888",
            # "MODELTYPE":
            # "Xiaomi MIX 2S",
            # "SYSVERSION":
            # "9",
            "APPVERSION": "4.6.0.01.21.10",
            # "MODELIMEI":
            # "868144035936779",
            # "Accept-Language":
            # "zh_CN",
            # "APP_DEV_INFO":
            # "Android#4.6.0.01.21.10#Xiaomi MIX 2S#9#868144035936779#32519888#alpha",
            "_sign": "A9FF6970EB814E6894389CA8B12F3030",
            # "Host":
            # "api-test.thejoyrun.com",
            # "Connection":
            # "Keep-Alive",
            # "Accept-Encoding":
            # "gzip",
            # "User-Agent":
            # "okhttp/3.11.0"
        }
        cookie = {
            "ypcookie":
            "sid%3d4aa6fff54cee4197ad5c880128791825%26uid%3d32519888"
        }

        signature = RequestMethod().build_signature(
            user="32519888/4aa6fff54cee4197ad5c880128791825")
        post_dict = {"timestamp": server_timestamp}
        post_dict["signature"] = signature

        re = requests.get(
            url='http://api-test.thejoyrun.com/daily/getDaily',
            params=post_dict,
            headers=header,
            cookies=cookie)
        print(re.text)


# if __name__ == "__main__":
#     get_daily('get')

#     url = "http://api-test.thejoyrun.com/GetTimestamp.aspx"
#     re = requests.get(url)
#     print(re.text)
#     content = eval(re.text)["lasttime"]
#     print(content)