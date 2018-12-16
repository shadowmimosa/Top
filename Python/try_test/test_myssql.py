import MySQLdb

# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'passwd': 'shadow',
#     # 'db': 'test',
#     # 'charset': 'utf8'
# }
# HttpRunnner_mysql = MySQLdb.connect(**config)

import pymysql
import os

try:
    ecnu_mysql = pymysql.connect(
        host='test01.mysql.db.thejoyrun.com',
        port=4412,
        user='admin',
        passwd='root123',
        database="yp_php_event",
        charset="utf8")

except pymysql.err.OperationalError as expression:
    print('登录失败！TimeoutError!')
    os._exit(0)

ecnu_cursor = ecnu_mysql.cursor()

if ecnu_cursor:
    print("登录成功")
else:
    print("登录失败")
# sql = """INSERT INTO `yp_php_event`.`ecnu_marathon_runs` ( `id`, `fid`, `uid`, `meter`, `second`, `dateline`, `dateline_time`, `created_at`, `updated_at` )
# VALUES
# 	( 39, 99115391, 32519916, 571, 146, 1544430428, '2018-12-09 16:27:08', '2018-12-09 16:27:21', '2018-12-09 16:27:21' );"""

sql = 'select * from yp_php_event.ecnu_marathon_runs where id > 1'

ecnu_cursor.execute(sql)


print(ecnu_cursor.Error)
print(ecnu_cursor.description)
# print(ecnu_cursor.fetchall())
# print(ecnu_cursor.fetchone())

for i in range(1, 39):
    a = ecnu_cursor.fetchone()
    if ecnu_cursor.fetchone():
        print(ecnu_cursor.fetchone())
    # ecnu_cursor.scroll(1,mode='relative')

# string1 = '123forth五'
# print(string1)
# string1.encode('utf-8').decode('unicode_escape')
# print(string1)