# import chardet

# response = chardet.detect(
#     b'\xe8\xa5\xbf\xe8\x99\xb9\xe5\xb8\x82\xe9\xa6\x96\xe5\xaf\x8c.csv')
# print(response)

# response = b'\xe8\xa5\xbf\xe8\x99\xb9\xe5\xb8\x82\xe9\xa6\x96\xe5\xaf\x8c.csv'
# print(response.decode('utf8'))


# response = b'\xe8\xa5\xbf\xe8\x99\xb9\xe5\xb8\x82\xe9\xa6\x96\xe5\xaf\x8c.csv'
# print(response.decode('utf8'))

response = '\u4e0d\u8981\u91cd\u590d\u53d1\u9001\u540c\u6837\u7684\u5185\u5bb9'
print(type(response))
print(response.encode('utf-8').decode('utf-8'))

def encode_decode(content):
    """Change the content to string that human can see."""

    if type(content)==bytes:
        try:
            return content.decode('utf-8')
        except:
            import chardet

            return chardet.detect(content)
    elif type(content)==str and '\\u' in content:
        return content.encode('utf-8').decode('utf-8')


a=encode_decode(response)

