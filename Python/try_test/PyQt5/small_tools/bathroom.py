def requests_get():
    """Not Empty"""
    url = "https://beta.thejoyrun.com/bathroom/bathrooms?key=0fc37aac2993ed1894b1dfde9ef686b8"

    import requests

    res = requests.get(url, verify=False)

    if res.status_code == 200:
        return res.text
    else:
        


def main():
    while True:
        requests_get()

main()