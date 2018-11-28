import requests
import os

get = requests.get(url="http://www.baidu.com", params={"name": "name"})

print(get.status_code)
print(get.text)

post = requests.post(url="http://www.baidu.com", data={"data1": "888"})

print(post.status_code)
print(post.text)