#创建一个元组，其元素包含cat、dog、10、20、hat、mice，并对其进行以下操作：
# 1)查询元素dog所在的位置；
# 2）提取数值元素；
# 3）求元组中元素的个数

# 创建元组
tup = ("cat", "dog", 10, 20, "hat", "mice")
print("原元组:", tup)

# 1) 查询元素 dog 所在的位置
pos = tup.index("dog")
print("dog 的位置(索引):", pos)          # 输出: 1

# 2) 提取数值元素（用 for 循环 + type 判断）
numbers = ()                             # 先建一个空元组
for x in tup:
    if type(x) == int:                   # 判断是不是整数
        numbers = numbers + (x,)         # 元组拼接，把 x 加进去
print("数值元素:", numbers)               # 输出: (10, 20)

# 3) 求元组中元素的个数
count = len(tup)
print("元素个数:", count)                 # 输出: 6