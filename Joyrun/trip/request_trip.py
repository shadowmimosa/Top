import requests

url = r"http://os2-test.thejoyrun.com/trip/topic/add"

headers = {
    "Host":
    "os2-test.thejoyrun.com",
    "Proxy-Connection":
    "keep-alive",
    "Accept":
    "*/*",
    "Origin":
    "http://os2-test.thejoyrun.com",
    "X-Requested-With":
    "XMLHttpRequest",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Content-Type":
    "multipart/form-data; boundary=----WebKitFormBoundaryEsUTVmGtep4MftBi",
    "Referer":
    "http://os2-test.thejoyrun.com/trip/topic/operatrion?type=add",
    "Accept-Encoding":
    "gzip, deflate",
    "Accept-Language":
    "zh-CN,zh;q=0.9",
    "Cookie":
    r"UM_distinctid=166c3a6c30f159-07568a7a32746c-b781e3e-1fa400-166c3a6c310820; gr_user_id=42719e1b-86fb-4019-acdf-963b457fe938; zg_did=%7B%22did%22%3A%20%221683ba2e0d62ad-0b42803df1db1c-b781636-1fa400-1683ba2e0d73e%22%7D; zg_b0f2e372185740dd9915675e8242fad1=%7B%22sid%22%3A%201548152417666%2C%22updated%22%3A%201548152440707%2C%22info%22%3A%201548145232702%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22WEBEVENT%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22zg.thejoyrun.com%3A8080%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwebevent.thejoyrun.com%2Factivity%2Fzhshanghai%2F%22%7D; zg_e2048a170f6a42afb504a7de7b1b5e7a=%7B%22sid%22%3A%201552371890953%2C%22updated%22%3A%201552371891914%2C%22info%22%3A%201552371890957%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22zg.thejoyrun.com%3A8080%22%2C%22cuid%22%3A%20%2215044290331%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D; Hm_lvt_7cfaa882ea03f1adfe434be26cc8a294=1551409961,1552373396; zg_23c6fbc560ae48f58a9f3653bca017c5=%7B%22sid%22%3A%201552987855275%2C%22updated%22%3A%201552987855295%2C%22info%22%3A%201552981762028%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22zg.thejoyrun.com%3A8080%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%2215044290331%22%7D; yp-webapp-jwt-token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbXBOYW1lIjoi5rWL6K-V6YOoIC0g6L2m54Kr5LicIiwiZXhwIjoxNTUzNzM5ODg1LCJlbWFpbCI6ImNoZXh1YW5kb25nQHRoZWpveXJ1bi5jb20iLCJlbXBJZCI6MTkyLCJnZW5kZXIiOjF9.V6pe9dT2AzoBy4rHnAUH5mxkuYk1uYBZ2TBCRlJ7VPvtpWeV3E7I19d_astpHthOObxacuiJkGnrDBamIJU643IJUd7PbtbRwIH_t971TyQZY2pexY1XLsb5RV6TSEjuA0X06-Q8_xUjEp3vt_emY5QSythGa_P5NaZ7nHyZKP4; JSESSIONID=FE4958480ACA13ACFAC02CABA161FDF3; yp-webapp-jwt-token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbXBOYW1lIjoi5rWL6K-V6YOoIC0g6L2m54Kr5LicIiwiZXhwIjoxNTUzNzU3MjM3LCJlbWFpbCI6ImNoZXh1YW5kb25nQHRoZWpveXJ1bi5jb20iLCJlbXBJZCI6MTkyLCJnZW5kZXIiOjF9.cjAAqxXvRa_4agjCffFvHYmY2OWNAYnuypRHh2GhHKq3VCSZ5jHYRXUJWAf2UXAzI1HyZlbnqIhzV3KOvWvzHa4YzpYOv_-ojp8PaAmRQZ7iYmTVyuUr6l1vhkeEtht2kBw2PJhoRczJoS9ygAZQM1Bm357VY7z7vfk0LqdRQBY"
}
datas = {
    'Content-Disposition: form-data; name="topicName"':
    "感遇",
    'Content-Disposition: form-data; name="weight"':
    9999,
    'Content-Disposition: form-data; name="content"':
    "兰叶春葳蕤，桂华秋皎洁。欣欣此生意，自尔为佳节。谁知林栖者，闻风坐相悦。草木有本心，何求美人折？江南有丹橘，经冬犹绿林。岂伊地气暖，自有岁寒心。可以荐嘉客，奈何阻重深。运命惟所遇，循环不可寻。徒言树桃李，此木岂无阴？",
    # 'Content-Disposition: form-data; name="topicId"':,
    # 'Content-Disposition: form-data; name="extendId"':
}
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

files = {'file': open('robot', 'rb')}

# resp = requests.post(url=url, files=files, headers=headers)

def addTripRaceTopicRaceRelevance():
    headers = {
        "Host":
        "os2-test.thejoyrun.com",
        "Proxy-Connection":
        "keep-alive",
        "Accept":
        "application/json, text/plain, */*",
        "Origin":
        "http://os2-test.thejoyrun.com",
        "X-Requested-With":
        "XMLHttpRequest",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Content-Type":
        "application/x-www-form-urlencoded",
        "Referer":
        "http://os2-test.thejoyrun.com/trip/topic/listRelevancePage?type=edit&topicName=&topicId=23&raceName=&currentpage=2&pageSize=10",
        "Accept-Encoding":
        "gzip, deflate",
        "Accept-Language":
        "zh-CN,zh;q=0.9",
        "Cookie":
        r"UM_distinctid=166c3a6c30f159-07568a7a32746c-b781e3e-1fa400-166c3a6c310820; gr_user_id=42719e1b-86fb-4019-acdf-963b457fe938; zg_did=%7B%22did%22%3A%20%221683ba2e0d62ad-0b42803df1db1c-b781636-1fa400-1683ba2e0d73e%22%7D; zg_b0f2e372185740dd9915675e8242fad1=%7B%22sid%22%3A%201548152417666%2C%22updated%22%3A%201548152440707%2C%22info%22%3A%201548145232702%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22WEBEVENT%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22zg.thejoyrun.com%3A8080%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwebevent.thejoyrun.com%2Factivity%2Fzhshanghai%2F%22%7D; zg_e2048a170f6a42afb504a7de7b1b5e7a=%7B%22sid%22%3A%201552371890953%2C%22updated%22%3A%201552371891914%2C%22info%22%3A%201552371890957%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22zg.thejoyrun.com%3A8080%22%2C%22cuid%22%3A%20%2215044290331%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D; Hm_lvt_7cfaa882ea03f1adfe434be26cc8a294=1551409961,1552373396; zg_23c6fbc560ae48f58a9f3653bca017c5=%7B%22sid%22%3A%201552987855275%2C%22updated%22%3A%201552987855295%2C%22info%22%3A%201552981762028%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22zg.thejoyrun.com%3A8080%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%2215044290331%22%7D; yp-webapp-jwt-token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbXBOYW1lIjoi5rWL6K-V6YOoIC0g6L2m54Kr5LicIiwiZXhwIjoxNTUzNzM5ODg1LCJlbWFpbCI6ImNoZXh1YW5kb25nQHRoZWpveXJ1bi5jb20iLCJlbXBJZCI6MTkyLCJnZW5kZXIiOjF9.V6pe9dT2AzoBy4rHnAUH5mxkuYk1uYBZ2TBCRlJ7VPvtpWeV3E7I19d_astpHthOObxacuiJkGnrDBamIJU643IJUd7PbtbRwIH_t971TyQZY2pexY1XLsb5RV6TSEjuA0X06-Q8_xUjEp3vt_emY5QSythGa_P5NaZ7nHyZKP4; JSESSIONID=FE4958480ACA13ACFAC02CABA161FDF3; yp-webapp-jwt-token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbXBOYW1lIjoi5rWL6K-V6YOoIC0g6L2m54Kr5LicIiwiZXhwIjoxNTUzNzU3MjM3LCJlbWFpbCI6ImNoZXh1YW5kb25nQHRoZWpveXJ1bi5jb20iLCJlbXBJZCI6MTkyLCJnZW5kZXIiOjF9.cjAAqxXvRa_4agjCffFvHYmY2OWNAYnuypRHh2GhHKq3VCSZ5jHYRXUJWAf2UXAzI1HyZlbnqIhzV3KOvWvzHa4YzpYOv_-ojp8PaAmRQZ7iYmTVyuUr6l1vhkeEtht2kBw2PJhoRczJoS9ygAZQM1Bm357VY7z7vfk0LqdRQBY"
    }
    topic_id = 22
    race_id = 0
    import time

    for i in range(0, 9):
        topic_id += 1
        for j in range(0, 2700):
            race_id += 1

            data = {'topicId': topic_id, 'weight': 0, 'raceId': race_id}
            resp = requests.post(
                url=
                "http://os2-test.thejoyrun.com/trip/topic/addTripRaceTopicRaceRelevance",
                data=data,
                headers=headers)
            print(resp.status_code)
            print(time.time())
            time.sleep(5)
            print(time.time())
        requests.post(
            url=
            "http://os2-test.thejoyrun.com/trip/topic/upOrDownTripRaceTopic",
            data={
                "topicId": topic_id,
                "status": 1
            },
            headers=headers)

        pass


def opea_sql():
    import pymysql
    import os

    try:
        ecnu_mysql = pymysql.connect(
            host='test01.mysql.db.thejoyrun.com',
            port=4412,
            user='admin',
            passwd='root123',
            database="yp_trip",
            charset="utf8")

    except pymysql.err.OperationalError as expression:
        print('登录失败！TimeoutError!')
        os._exit(0)

    ecnu_cursor = ecnu_mysql.cursor()

    if ecnu_cursor:
        print("登录成功")
    else:
        print("登录失败")

    sql = 'SELECT activity_id FROM yp_trip.trip_assists_activity;'
    init_id = 29
    ecnu_cursor.execute(sql)
    queue_ = ecnu_cursor.fetchall()
    for i in queue_:
        init_id += 1
        sql = "INSERT INTO `yp_trip`.`trip_assists_reg`(`reg_id`, `user_id`, `create_time`, `activity_id`, `update_time`, `be_assists_number`, `del_flag`) VALUES ({}, 501321, '2019-03-25 15:18:50', {}, '2019-03-25 15:18:50', 1, 0);".format(
            init_id, i[0])
        try:
            ecnu_cursor.execute(sql)
        except:
            continue

    ecnu_mysql.commit()
    ecnu_cursor.close()
    ecnu_mysql.close()
    pass


# opea_sql()

addTripRaceTopicRaceRelevance()
