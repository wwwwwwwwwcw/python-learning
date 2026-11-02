# 计算n的阶乘
n = int(input("请输入 n："))
result = 1      # 累乘结果，初始为 1
i = 1           # 计数器
while i <= n:
    result = result * i   # 把 i 乘进结果
    i = i + 1             # 计数器 +1
print(f"{n} 的阶乘为: {result}")