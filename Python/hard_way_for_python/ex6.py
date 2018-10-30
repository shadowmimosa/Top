# 定义字符串变量x
x = "there are %s type of people." % 10
# 定义字符串变量binary
binary = "binary"
# 定义字符串变量do_not
do_not = "don't"
# 定义字符串变量y，包含binary,与do_not字符串
y = "Those who know %s and those who %s" % (binary, do_not)

# 输出字符串变量x
print(x)
# 输出字符串变量y
print(y)
# 输出字符串，并包含字符串x
print("I said:%r." % x)
# 输出字符串，并包含字符串y
print("I also said:'%s'." % y)  # 格式化字符加不加引号都一样
# 定义布尔类型
hilarious = False
# 定义字符串变量joke_evaluation，传递空格式化字符
joke_evaluation = "Isn't that joke so funny?!%r"  # 字符串变量可传递格式化字符

# 输出字符串变量joke_evalution，并包含布尔型变量hilarious
print(joke_evaluation % hilarious)

# 定义字符串变量w与e
w = "This is the left side of..."
e = "a string with a right side."

# 输出w+e
print(w + e)
