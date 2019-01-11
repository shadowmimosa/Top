import pymysql
import os
import requests

re = requests.get("http://119.147.160.84:16780/")
re = requests.get("http://119.147.160.84:3306/")
re.status_code

ecnu_mysql = pymysql.connect(
    host='119.147.160.84',
    port=3306,
    user='root',
    passwd='JoyrunTest@123',
    database="mysql",
    charset="utf8")
