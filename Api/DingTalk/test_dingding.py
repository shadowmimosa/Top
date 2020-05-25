import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_uri(type_='file', access_token='ae01a86b66a0339f99fcef91a99a6a6c'):
    return f'https://oapi.dingtalk.com/media/upload?access_token={access_token}&type={type_}'


def upload_by_single(file_name):
    '''只使用 requests 发送 multipart/form-data 类型请求
    '''

    header = {}
    file_ = {"media": open(file_name, 'rb')}
    data = {"media": file_name}
    uri = get_uri()

    resp = requests.post(uri,
                         data=data,
                         files=file_,
                         headers=header,
                         verify=False)


def upload_by_urilib3(file_name):
    '''使用 urllib3 库配合发送 multipart/form-data 类型请求
    '''

    from urllib3 import encode_multipart_formdata

    uri = get_uri()
    data, header = {}, {}

    data['media'] = (file_name, open(file_name, 'rb').read())
    encode_data = encode_multipart_formdata(data)
    data = encode_data[0]
    header['Content-Type'] = encode_data[1]

    resp = requests.post(uri, data=data, headers=header, verify=False)


def upload_by_toolbelt(file_name):
    '''使用 requests_toolbelt 库配合发送 multipart/form-data 类型请求
    '''

    from requests_toolbelt.multipart.encoder import MultipartEncoder

    header = {}
    data = MultipartEncoder({
        'media': ('media', open(file_name, 'rb'), 'multipart/form-data'),
    })
    header['Content-Type'] = data.content_type
    uri = get_uri()

    resp = requests.post(uri, data=data, headers=header, verify=False)


def send_text(content):
    uri = 'https://oapi.dingtalk.com/robot/send?access_token=f25e94f67820f5cd25ffb2c146acb3cd500284a974a21a5d9bb23863046ea9ce'
    data = {"msgtype": "text", "text": {"content": content}}
    header = {'Content-Type': 'application/json'}

    resp = requests.post(uri, json=data, headers=header, verify=False)


def send_img(media_id='@lAjPDf0ivBnr6ojOE0LCIM5qc6kR'):
    uri = 'https://oapi.dingtalk.com/robot/send?access_token=f25e94f67820f5cd25ffb2c146acb3cd500284a974a21a5d9bb23863046ea9ce'
    data = {
        "msgtype": "image",
        "image": {
            "media_id":
            media_id,
            "image":
            "http://t1.27270.com/uploads/tu/201809/1151/2016-07-03_0067dt7egw1f5gzr7ejwdj30xd1e01jt.jpg"
        }
    }
    # data = {"msgtype": "image", "image": 'http://t1.27270.com/uploads/tu/201809/1151/2016-07-03_0067dt7egw1f5gzr7ejwdj30xd1e01jt.jpg'}
    header = {'Content-Type': 'application/json'}

    resp = requests.post(uri, json=data, headers=header, verify=False)


def send_link():
    uri = 'https://oapi.dingtalk.com/robot/send?access_token=f25e94f67820f5cd25ffb2c146acb3cd500284a974a21a5d9bb23863046ea9ce'
    data = {
        "msgtype": "link",
        "link": {
            "text":
            "这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是红树林",
            "title":
            "时代的火车向前开",
            "picUrl":
            "https://www.baidu.com/link?url=hCdIU6W0IUuYLTAy_qRioW55dBko6Zgua_yBTZYMXjSOHxOptYHZJYiaNJbBod9WBd8nvzpHlfjKzN4typqLe5bxWAME_0lh5rTEaCaYT1qTGN1af5Ya8K7nZ_SYyxqilDNIuhqIBdwkh8X6B8FrIWPf8qprKo0Mc6xAnF2m7ldNz9WaLBz0P6OpYtw2eQSu74zH5TMbA1YEbVFmGSLsL-l-rT8AKGr7hn6-fQKMNcoQYeXPTKvv84OnAnLXk85Ygvidv4SmtA92EsUARVKhCvGRqqcW4RmWs2Vd2XvEkf_xZLLBViz4v4b8mFpbQL8lmNfKQOZce2-X9y4r-9QrTua3kKGf3X6WZlFVHhZZgI1nsj18pj8cPc0guJIsHBHvvG6PNZfULP2l0Ko5Xkvy0175x529Vgxmu5RfRgAcHa0U5x8YcOvd1TvTkX6zctqt-SOsQtb1Ayaks15R9arQSJe6BrUIGZP3gIQq-v51F9QeJQZ1rnjYc07s7MFNWzXOFzMNdCZv5hopReP_ECGbAQBr1mfHMxANA3DGecIWESkGWg4aXSHJtBWq1564TTHkEGdI0d8IeuS0jjwupnMpR5VYwyP-ENSpJGuWA8fLsbujLpZ1VB8tPDInbFgMuTmG&timg=https%3A%2F%2Fss0.bdstatic.com%2F94oJfD_bAAcT8t7mm9GUKT-xh_%2Ftimg%3Fimage%26quality%3D100%26size%3Db4000_4000%26sec%3D1590393881%26di%3Dbbc2bd7bdbc6752bb06717548717e2af%26src%3Dhttp%3A%2F%2F01.minipic.eastday.com%2F20161215%2F20161215154634_940b4d487aedf8f5c0931f7f3591781b_1.jpeg&click_t=1590393888520&s_info=1903_1008&wd=&eqid=e9e6543100040082000000035ecb7c19",
            "messageUrl":
            "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI"
        }
    }
    header = {'Content-Type': 'application/json'}

    resp = requests.post(uri, json=data, headers=header, verify=False)


def send_markdown():
    uri = 'https://oapi.dingtalk.com/robot/send?access_token=f25e94f67820f5cd25ffb2c146acb3cd500284a974a21a5d9bb23863046ea9ce'
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title":
            "杭州天气",
            "text":
            "#### 杭州天气 @150XXXXXXXX \n> 9度，西北风1级，空气良89，相对温度73%\n> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n> ###### 10点20分发布 [天气](https://www.dingalk.com) \n"
        },
        "at": {
            "atMobiles": ["150XXXXXXXX"],
            "isAtAll": False
        }
    }
    header = {'Content-Type': 'application/json'}

    resp = requests.post(uri, json=data, headers=header, verify=False)


def send_image():
    uri = 'https://oapi.dingtalk.com/robot/send?access_token=f25e94f67820f5cd25ffb2c146acb3cd500284a974a21a5d9bb23863046ea9ce'
    header = {'Content-Type': 'application/json'}
    for img in [
            'https://pic3.zhimg.com/80/v2-0c384647247cd981d9170adbce601f4e_720w.jpg',
            'https://pic2.zhimg.com/80/v2-b375817ac4f9b8b81c01e8400eb873fd_720w.jpg',
            'https://pic4.zhimg.com/80/v2-2fae3fa82fae0ecd16a72464c3de65f5_720w.jpg',
            'https://pic3.zhimg.com/80/v2-fb55274e55acf662ef373ce20551415d_720w.jpg',
            'https://pic3.zhimg.com/80/v2-bc855ba9bb3f50e959de9fbbf0ce1912_720w.jpg',
            'https://pic4.zhimg.com/80/v2-5817309d6246d338880df41721b1a070_720w.jpg',
            'https://pic2.zhimg.com/80/v2-14e963d393c51c0bfae2f1e2b03cd2ce_720w.jpg',
            'https://pic4.zhimg.com/80/v2-8df344c02345573fc54f4a31e0153b37_720w.jpg',
            'https://pic4.zhimg.com/80/v2-d4794efca631537d3a67b81f72f64d8a_720w.jpg',
            'https://pic3.zhimg.com/80/v2-b065684e597631fadfec115108d9ffed_720w.jpg',
            'https://pic3.zhimg.com/80/v2-43d945b9a4e31165eacadd4931c9f20b_720w.jpg',
            'https://pic4.zhimg.com/80/v2-639c4e828ba9f49a4f4c8b9394065090_720w.jpg',
            'https://pic3.zhimg.com/80/v2-b01266a14a426b19d7af02f265abaf9e_720w.jpg',
            'https://pic3.zhimg.com/80/v2-8415032c8268ee4312d731a6ca44c3db_720w.jpg',
    ]:
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "图片测试",
                "text": f"![screenshot]({img})"
            },
            "at": {
                # "atMobiles": ["150XXXXXXXX"],
                # "isAtAll": True
            }
        }

        resp = requests.post(uri, json=data, headers=header, verify=False)


if __name__ == "__main__":
    file_name = '6b544c5c2c664e4581b8da3533d3217b-3.png'

    upload_by_single(file_name)
    # upload_by_urilib3(file_name)
    # upload_by_toolbelt(file_name)

    # send_text('曾三的请假申请')
    # send_img()
    # send_link()
    # send_markdown()
    send_image()