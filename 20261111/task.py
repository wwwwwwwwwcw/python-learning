# 案例一  编写程序实现用户登录管理系统
# 系统可以提示用户输入用户名和密码，判断用户名和密码是否正确
# 要求：用户名admin 密码：123456
# 若正确，则提示登陆成功，错误则提示用户重新输入，最多可尝试三次，错误三次之后直接退出系统

unlock = False
for i in range(3):
    if unlock == False:
        username = input("请输入用户名：")
        password = input("请输入密码：")
        if username == "admin" and password == "123456":
            print("登录成功！")
            unlock = True
        else:
            print("用户名或密码错误，请重新输入！")

# 案例二 
# 小明有五本新书，要借给A，B，C三位小朋友，若每人每次只能借一本，则有多少种借法
count = 0
for a in range(1, 6):
    for b in range(1, 6):
        for c in range(1, 6):
            if a != b and a != c and b != c:
                count += 1
print(count)


# 案例三
# 一个口袋中有12个球，已知3个红球，3个白球，6个黑球
# 现从中取出8个，共有多少种可能的颜色搭配
count = 0
for r in range(4):
    for w in range(4):
        for b in range(7):
            if r + w + b == 8:
                count += 1
print(count)

