import requests
import json

api_key = 'o25lc4XecQpXpoEIhoUu8AD2MMmQu3xXJLm9J6n2z6XH3wqwUK'


def main():
    print("> This is tumblr_main.")
    like_json = open("./config/like.json", "w", encoding="utf-8")

    blog_identifier = input("Please input blog ID. \n > ")

    # -1 get user info
    info_url = 'https://api.tumblr.com/v2/blog/{0}.tumblr.com/info?api_key={1}'
    info_url = info_url.format(blog_identifier, api_key)

    resp = requests.get(info_url)

    try:
        data = resp.json()
    except ValueError:
        data = {
            'meta': {
                'status': 500,
                'msg': 'Server Error'
            },
            'response': {
                "error": "Malformed JSON or HTML was returned."
            }
        }

    if 200 <= data['meta']['status'] <= 399:
        if data['response']['blog']['share_likes']:
            like_item = data['response']['blog']['likes']
            print('like_item = ', like_item)
        else:
            print('[error]: blog likes is not share')
            return
    else:
        print('error', data)
        print('[error]: blog is not exist')
        return

    # -2 get first user likes
    likes_url = "https://api.tumblr.com/v2/blog/{0}/likes?api_key={1}"
    likes_url = likes_url.format(blog_identifier, api_key)

    like_timestamp = 0

    resp = requests.get(likes_url)
    print(resp)

    try:
        data = resp.json()
    except ValueError:
        data = {
            'meta': {
                'status': 500,
                'msg': 'Server Error'
            },
            'response': {
                "error": "Malformed JSON or HTML was returned."
            }
        }

    if 200 <= data["meta"]["status"] <= 399:
        resp_item_len = len(data["response"]["liked_posts"])
        print("Response item lenght is ", resp_item_len)
        like_timestamp = data["response"]["liked_posts"][resp_item_len -
                                                         1]["liked_timestamp"]
        print("Liked timestamp is ", like_timestamp)

        json.dump(data, like_json)
        like_json.write('\n')  # json 文件分割符

    # get likes before first timestamp
    raw_url = "https://api.tumblr.com/v2/blog/{0}/likes?before={1}&api_key={2}"

    offset = resp_item_len
    while offset < like_item:
        likes_url = raw_url.format(blog_identifier, like_timestamp, api_key)

        resp = requests.get(likes_url)
        print(resp)
        try:
            data = resp.json()
        except ValueError:
            data = {
                'meta': {
                    'status': 500,
                    'msg': 'Server Error'
                },
                'response': {
                    "error": "Malformed JSON or HTML was returned."
                }
            }

        if 200 <= data["meta"]["status"] <= 399:
            resp_item_len = len(data["response"]["liked_posts"])
            print("Response item lenght is ", resp_item_len)

            if resp_item_len:
                like_timestamp = data["response"]["liked_posts"][
                    resp_item_len - 1]["liked_timestamp"]
                print("Now liked timestamp is ", like_timestamp)
                json.dump(data, like_json)
            else:
                break
        else:
            print("error", data)

        offset += resp_item_len
        like_json.write('\n')

    like_json.close()


if __name__ == '__main__':
    main()
