#一量卡车违反交规逃跑现场，有三人目击该事件，但均未记住车牌号
#甲：车牌号前两位相同
#乙：车牌号后两位相同，但和前两位不同
#丙：车牌号是一个正整数的平方
#问：车牌号是多少？
i = 0
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                if a == b and c == d and a != c:
                    plate_number = a * 1000 + b * 100 + c * 10 + d
                    if int(plate_number ** 0.5) ** 2 == plate_number:
                        print("车牌号是:", plate_number)
                        i += 1
print("共找到", i, "个符合条件的车牌号")