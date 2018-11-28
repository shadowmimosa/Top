import requests

def visitKibana():
    # Kibana=requests.get(
    #     url="http://kibana.cloud.thejoyrun.com/app/kibana"
    # )
    # print(Kibana.text)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    url="http://192.168.1.11:9200/_search"
    response = requests.get(url,headers=headers)
    print(response.text)
    pass



if __name__ == '__main__':
    visitKibana()
