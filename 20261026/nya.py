#随便写的
sex = int(input("请输入性别, 1表示男性，0表示女性："))
age = int(input("请输入年龄："))

if age < 16 and sex == 0:
    print("哇塞好可爱")
elif age < 16 and sex == 1:
    print("男的走开")
elif age >= 16 and sex == 0:
    print("老了老了")
elif age >= 16 and sex == 1:
    print("走开走开")
else:
    print("输入有误")