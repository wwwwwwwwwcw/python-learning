#假设你的锁屏密码是2022
pw = 2022
a = int(input("请输入锁屏密码:"))
if a == pw:
    print("密码正确，欢迎使用！")
if a != pw:
    print("密码错误，请重新输入！")