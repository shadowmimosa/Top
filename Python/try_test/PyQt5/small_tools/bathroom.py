def requests_get():
    """Not Empty"""
    url = "https://beta.thejoyrun.com/bathroom/bathrooms?key=0fc37aac2993ed1894b1dfde9ef686b8"

    import requests

    resp = requests.get(url, verify=False)

    if resp.status_code == 200:
        pass
    else:
        requests_get()

    return resp.text


def wait_three():
    import urllib3, time
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    while True:
        start_timestamp = time.time()
        raw_json = eval(requests_get())
        single_left, single_right = raw_json[0], raw_json[1]
        time.sleep(3 - time.time() + start_timestamp)  # 算上请求时间，一共 sleep 3s
        print(single_left)
        print(single_right)


def just_once():
    import urllib3, time
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    raw_json = eval(requests_get())
    single_left, single_right = raw_json[0], raw_json[1]

    return single_left, single_right


# main()


def twoSum(nums, target):
    data = {nums[i]: i for i, n in enumerate(nums)}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in data and data.get(complement) != i:
            return [i, data.get(complement)]


# print(twoSum([3, 3], 6))


def lengthOfLongestSubstring(s: str) -> int:

    sub = ''
    biggest = 0
    index = 0
    
    while True:
        for single in s[index:-1]:
            if single not in sub:
                sub += single
            elif biggest < len(sub):
                biggest = len(sub)
                break
                
        if biggest < len(sub):
            biggest = len(sub)

        index += 1
        sub = ''
        if index == len(s) or len(s) == 0:
            break
                
    
    return biggest

indices = [-1] * 127
ord()
print(lengthOfLongestSubstring("au"))

a=list
a.append