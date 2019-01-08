import pytumblr
import json

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    'o25lc4XecQpXpoEIhoUu8AD2MMmQu3xXJLm9J6n2z6XH3wqwUK',
    'uD4EVD7rHG2iGYkWrxY6diZLTkd3WhjuCGrc8zryL731whXBb5',
    '8coTZoxNQSNzwpB2h60w3A8iNnzt7PhrxtK59vQd57zWfpCNqi',
    'mKoZEtvRWhU8ahmBt5iX9Z1lCXeM5xQeu9CaumZHcUPUthU30e')

# # Make the request
# data = client.likes(limit=5)
# print(data)


def get_info():
    data = client.info()
    likes_total = data["user"]["likes"]
    return likes_total


def get_likes(likes_total, limit_num=20, last_timestamp=0):

    data = client.likes(limit=limit_num, before=last_timestamp)


def write_file(abc):
    likes_json = open('.//config//likes.txt', 'a', encoding='utf-8')
    likes_json.write(abc + '\n')
    likes_json.write(abc + '\n')
    likes_json.write(abc + '\n')
    likes_json.write(abc + '\n')
    likes_json.write(abc + '\n')
    likes_json.close


if __name__ == "__main__":
    # likes_total = get_info()
    # if likes_total > 0:
    #     get_likes(likes_total)
    write_file("asa")
    write_file("asb")
    write_file("asc")
