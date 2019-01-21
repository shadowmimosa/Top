import time
from datetime import datetime, timedelta
import json


def read_file(path):
    """打开文件，按行读取；返回所有行

    ``path`` 文件路径  
    ``type(return) = list``
    """

    with open(path, 'r', encoding='utf-8') as fn:
        raw_text = fn.read().replace("\n", '').replace(' ', '')
        text_json = json.loads(raw_text)
    return text_json


def write_file(path, content):
    """打开文件，并写入内容  

     ``path`` 文件路径  
     ``content`` 写入的内容  
    """
    
    with open(path, 'w', encoding='utf-8') as fn:
        if type(content) == dict:
            json.dump(content, fn, ensure_ascii=False)
        elif type(content) == str and content != "\n":
            fn.write(content)
        elif type(content) == list:
            for index in range(len(content)):
                fn.write(str(content[index]))
        elif type(content) == bytes:
            fn.write(content.decode('utf-8'))
        fn.write("\n")


def change_time(item_json, change_id=False):
    """改变给定赛事相关时间；

    ``item_json`` 给定赛事信息
    ``change_id`` 是否改变赛事与赛事项目 id
    """
    # start_timestamp = int(time.time()) * 1000

    start_timestamp = int(time.mktime(datetime.now().timetuple())) * 1000
    end_timestamp = int(
        time.mktime((datetime.now() + timedelta(days=1)).timetuple())) * 1000

    item_json['startTime'] = start_timestamp
    item_json['endTime'] = end_timestamp

    item_json['shelveTime'] = start_timestamp
    item_json['unshelveTime'] = end_timestamp

    item_json['updateTime'] = start_timestamp

    for index in range(0, len(item_json['raceItems'])):
        item_json['raceItems'][index]['createTime'] = start_timestamp

        # item_json['raceItems'][0]['startLatitude']
        # item_json['raceItems'][0]['endLatitude']
        # item_json['raceItems'][0]['startLongitude']
        # item_json['raceItems'][0]['endLongitude']

        item_json['raceItems'][index]['startValidTime'] = start_timestamp
        item_json['raceItems'][index]['startInvalidTime'] = end_timestamp

        item_json['raceItems'][index]['startTime'] = start_timestamp
        item_json['raceItems'][index]['closeTime'] = end_timestamp

        item_json['raceItems'][index]['updateTime'] = start_timestamp

    if change_id:
        item_json = change_raceid_itemid(item_json)

    return item_json


def change_raceid_itemid(item_json):
    item_json['raceId'] += 1
    for index in range(0, len(item_json['raceItems'])):
        item_json['raceItems'][index]['raceId'] += 1
        item_json['raceItems'][index]['id'] += 1

    return item_json

def change_item(json_json):
    pass


if __name__ == "__main__":
    race_item_path = "C:\\Users\\ShadowMimosa\\Documents\\Fiddler2\\Fiddler\\raceItem_forApple.json"
    race_item_json = read_file(race_item_path)

    for index in range(0, len(race_item_json['data'])):
        race_item_json['data'][index] = change_time(
            race_item_json['data'][index], change_id=True)

    write_file(race_item_path, race_item_json)
