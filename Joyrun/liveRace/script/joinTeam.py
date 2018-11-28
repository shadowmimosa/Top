import requests


# 加入战队post请求
def join(uid, teamId, bib):
    # headers = {'Content-Type': 'application/json'}
    data = {
        'uid': uid,
        'teamId': teamId,
        'targetSecs': '10000',
        'bib': bib,
    }
    joinTeam = requests.post(
        url="http://119.147.160.85:8158/racelive/team/join", json=data)
    print(joinTeam.text)


# uid表
uidList = [
    7000310, 3893458, 1989094, 23891932, 12144512, 92796554, 84312628,
    26393816, 85861280, 21435617, 30277300, 92593334, 92624436, 6830198,
    13253298, 84658007, 90816393, 775565, 10764477, 30010339, 11921992,
    33305736, 84698203, 2941020, 1906689, 23565169, 7127801, 13163388,
    22715816, 25141333, 29812709, 13275130, 33770397, 18545523, 29959207,
    29813555, 60082664, 1184741, 11209738, 30680290
]

# teamId表
teamIdList = [213, 214, 215, 216]

# 每10人加入一个战队，并输出uid,teamId
for index, uid in enumerate(uidList):
    if index < 10:
        bib = 'beijing' + str(index)
        join(uid, teamIdList[0], bib)
        print(uid, teamIdList[0])
    elif index < 20:
        bib = 'chengdu' + str(index)
        join(uid, teamIdList[1], bib)
        print(uid, teamIdList[1])
    elif index < 30:
        bib = 'guangzhou' + str(index)
        join(uid, teamIdList[2], bib)
        print(uid, teamIdList[2])
    elif index < 40:
        bib = 'shanghai' + str(index)
        join(uid, teamIdList[3], bib)
        print(uid, teamIdList[3])

# 测试join用
# join(333,17)