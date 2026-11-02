#猜数字：预设一个炸弹数字会提示猜大了还是猜小了，直到猜中为止
boom = 66
guess = int(input("请输入你猜的数字："))
while guess != boom:
    if guess > boom:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")
    guess = int(input("请重新输入你猜的数字："))
print("恭喜你，猜中了！")