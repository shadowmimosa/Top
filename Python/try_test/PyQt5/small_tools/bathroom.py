def requests_get():
    """Not Empty"""
    url = "https://beta.thejoyrun.com/bathroom/bathrooms?key=0fc37aac2993ed1894b1dfde9ef686b8"

    import requests

    resp = requests.get(url, verify=False)

    if resp.status_code == 200:
        return resp.text
    else:
        requests_get()


def main():
    while True:
        raw_list = requests_get()
        single_left, single_right = raw_list[0], raw_list[1]
        print('2')



main()