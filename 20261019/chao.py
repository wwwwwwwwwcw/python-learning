a = input("请输入字母，数字，符号")
if len(a) != 1:
    print("请输入一个字符")
else:
    print("对应的ASCII码为：", ord(a))