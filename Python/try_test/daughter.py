import itchat
import time


def itchat_SendMsg(nm, msg, second=None):
    from time import time

    try:
        itchat.auto_login(hotReload=True)
        myfriend = itchat.search_friends(name=nm)
        myfriendUserName = myfriend[0]['UserName']
        print(myfriendUserName)
        itchat.send(msg, toUserName=myfriendUserName)
        if second != None:
            t = time(second, itchat_SendMsg(nm, msg, second))
            t.start()
    except:
        message = u'It is wrong!!'
        itchat.send(message, toUserName='filehelper')


if __name__ == '__main__':

    lines_list = ["1", "2", "3", "4", "5", "6"]
    sleep_list = [5, 10, 4, 13, 9, 6, 11]

    j = 0

    while True:
        for i in range(len(lines_list)):
            itchat_SendMsg('Shadow', lines_list[i])
            j += 1

        # for num in range(len(sleep_list)):
        #     time.sleep(sleep_list[num])

        if j >= 30:
            break

    print("It's OK!!!")




