import requests
import json

url = "https://shadowmimosa.tumblr.com/likes"

resp = requests.get(url)
data=resp.text
print(data)
