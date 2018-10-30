# 导入argv模组
from sys import argv

# 获取文件名
script, filenmae = argv

# 打开文件
txt = open(filenmae)

# 输出文件名
print("Here is your file %r:" % filenmae)
# 输出文件内容
print(txt.read())
txt.close()

# 再次输入文件名
print("Tpye the filename again:")
# 输出'>'
file_again = input('> ')

# 再次打开文件
txt_again = open(file_again)

# 再次输出文件
print(txt_again.read())
txt_again.close()
