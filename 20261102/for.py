# for循环3.3

# 分别输出字符串字母
# for i in 'python':
#     print(i)

# for i in 'python':
#     print(1)

#range函数
#range(初始值，终止值，步长)
# 终止值不包含终止值截止到前一位
# 步长为1时可以省略
# 如果初始值为0且步长为1 二者都省略
# 不可以只省略初始值
#案例 输出20以内的偶数
for i in range(0, 21, 2):
    print(i)