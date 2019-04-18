def to_h_m_s(all_second):
    if all_second >= 3600:
        hour = int(all_second / 3600)
        middle = all_second % 3600
        if middle >= 60:
            minute = int(middle / 60)
            second = middle % 60
    else:
        hour = 0
        if all_second >= 60:
            minute = int(all_second / 60)
            second = all_second % 60
        else:
            minute = 0
            second = all_second

    return "{} hours {} minutes {} seconds".format(hour, minute, second)


def to_time(mileage, aver_speed=None, speed_secs=None):
    if aver_speed is not None:
        spend_min, speed_sec = aver_speed.split("'")[0], aver_speed.split(
            "'")[-1]
        speed_secs = int(spend_min) * 60 + int(speed_sec)
    # elif speed_secs is not None:

    time = mileage * speed_secs

    print(to_h_m_s(time))


def main():
    to_time(869.90, aver_speed="5'29")
    to_time(869.90, speed_secs=44715 / 135830 * 1000)
    to_time(1.77, aver_speed="7'00")
    to_time(2.65, aver_speed="7'00")
    
    to_time(0.24, aver_speed="10'00")
    to_time(7.69, aver_speed="10'00")
    to_time(7.69, aver_speed="3'00")

    print("平均配速：", to_h_m_s(44715 / 135830 * 1000))
    print("平均配速：", to_h_m_s(4471500 / 135830 * 1000))
    print("平均配速：", to_h_m_s(447 / 135830 * 1000))


if __name__ == "__main__":
    main()

    allmeter = 135830
    allsecond = 44715
