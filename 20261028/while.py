#while循环基本语句
# i = 0
# while i < 3:
#     print('python')
#     i = i + 1

#输出1-10
# i = 0
# while i < 10:
#     i = i + 1
#     print(i)

#输出十以内，包括十的偶数
# i = 1
# while i < 10:
#     i = i + 2
#     print(i)


#计算1-10的和
# i = 1
# m = 0
# while i <= 10:
#     m = m + i
#     i = i + 1
# print("1-10的和为:", m)   # 55

#输出1-100之间的奇数和
# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i = i + 2
# print("1-100之间的奇数和为:", sum)

#输出1-100之间的偶数和
# i = 2
# mun = 0
# while i <= 100:
#     mun = mun + i
#     i = i + 2
# print(mun)

#案例一， 输入一个正整数x，输出所有不包含他本身的因子
#因子：所有能被他整除的数
# x = int(input("请输入一个正整数: "))
# i = 1
# while i < x:
#     if x % i == 0:
#         print(i)
#     i = i + 1