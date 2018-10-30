def mouth_sum():
    first_num = 0.01
    i = 1
    while i < 31:
        last_num = first_num * 2
        sum = first_num + last_num
        first_num = last_num
        print("第%r天%r元" % (i, last_num))
        i = i + 1
    print("一个月总共%r元 " % sum)


# mouth_sum()


def method_for_e():
    i = 987654321
    j = 0.987654321
    print("普通十进制表示:\ni:{} j:{}\n科学计数法表示:\ni:{:.10e} j:{:.10e}".format(
        i, j, i, j))


# method_for_e()
