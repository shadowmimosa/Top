import os

# # 四种套餐
# mouth_40 = 17
# mouth_60 = 22
# mouth_100 = 29
# mouth_150 = 45

# # 充值金额
# recharge = [50, 100, 200, 500]

# 初始化充值次数，购买次数
mouthNum_17 = mouthNum_22 = mouthNum_45 = 0
mouthNum_29 = 0
recharge_frequency = 0

while True:
    # 充值一次50元，优先购买29元套餐
    recharge_frequency += 1
    mouthNum_29 += 1
    recharge_number = 50 * recharge_frequency

    # 购买套餐
    while True:
        # 消费总额
        total_cost = 17 * mouthNum_17 + 22 * mouthNum_22 + 29 * mouthNum_29 + 45 * mouthNum_45
        # 余额
        balance_number = recharge_number - total_cost

        # 购买套餐操作
        if balance_number == 0:
            print(recharge_frequency, total_cost, recharge_number)
            print(
                mouthNum_17,
                mouthNum_22,
                mouthNum_29,
                mouthNum_45,
            )
            # os._exit(0)
            if recharge_frequency <= 100:
                break
            else:
                os._exit(0)
        elif balance_number < 0:
            os._exit('error')
        elif balance_number >= 45 and balance_number < 90:
            mouthNum_45 += 1
        elif balance_number >= 29:
            mouthNum_29 += 1
        elif balance_number >= 22:
            mouthNum_22 += 1
        elif balance_number >= 17:
            mouthNum_17 += 1
        else:
            break

