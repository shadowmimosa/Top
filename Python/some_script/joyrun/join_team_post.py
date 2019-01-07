import requests
import json

url = "http://119.147.160.85:8158/racelive/team/join"
# url = "https://activity-test.thejoyrun.com/racelive/team/join"
# ypcookie="sid%3d81c13da053016cb68b8aca7ebc45e0b5%26uid%3d32519896"

header = {
    "Content-Type":
    "application/json;charset=UTF-8",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 9.0; MIX 2S Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044408 Mobile Safari/537.36",
    # "Cookie": "ypcookie=sid%3d81c13da053016cb68b8aca7ebc45e0b5%26uid%3d32519896; app_version=android4.5.0; Hm_lvt_7cfaa882ea03f1adfe434be26cc8a294=1546731739,1546656753,1546660031,1546660071; Hm_lpvt_7cfaa882ea03f1adfe434be26cc8a294=1546660071; XSRF-TOKEN=eyJpdiI6InhnUXE3V1lqNHkyK0ZoR2Q0ZE1FR2c9PSIsInZhbHVlIjoiclhDOUM4RFwvV1NSUDliZ1UyS09NaWZoa2pQMHNCWG14bDJRQjF4UFlrTTkzenFXUXRFTFZjSUd4WkVBT1BFSUFMRU9HdWY4b2ordmhSRUdNV05rb013PT0iLCJtYWMiOiJlNzdhNjFmZjQzYzMxYWMxMmVhZDA3MDU0NGFmY2QzZDVmOWQxNWU5OTNkNjI5MWNjMDRiOTljYzY3MGY4ZGU3In0%3D; joyrunactivity=eyJpdiI6Ilc4a1JGN21NQ0xWak9FUzlqRDdJeEE9PSIsInZhbHVlIjoiazA1YWIzeTVmVVhrcFphTXpHMzBVelJ1TmoySjdwWG5rXC96TVpQVTh0aVBFekI1QUI5bWVJWW9JQjlReU14Y1VnQ0p6OEd0cE0xY0g1YVpXZDdTMFJBPT0iLCJtYWMiOiJlM2IyZDNiMGQyZmZiYTdjZGEzNmQwZWNlMzYwZjU5MWI3MjliNDkxNDYxNTAwOTFiODE4MWQwOWE5NDBhZWQ2In0%3D"
    # "Cookie": "ypcookie="+ypcookie
}
# re = requests.post(url, data=json.dumps(data), headers=header)

uid_list = [
    7000310, 3893458, 1989094, 23891932, 12144512, 92796554, 84312628,
    26393816, 85861280, 21435617, 30277300, 92593334, 92624436, 6830198,
    13253298, 84658007, 90816393, 775565, 10764477, 30010339, 11921992,
    33305736, 84698203, 2941020, 1906686, 23565169, 7127801, 13163388,
    22715816, 25141333, 29812709, 13275130, 33770397, 18545523, 29959207,
    29813555, 60082664, 1184741, 11209738, 30680290
]

teamid = 400

for uid in uid_list:
    if uid == 11921992:
        teamid = 401
    data = {
        "uid": uid,
        "teamId": teamid,
        "targetSecs": 30000,
        "bib": str(uid) + 'TB'
    }
    re = requests.post(url, json=data, headers=header, verify=False)

print(re.status_code)