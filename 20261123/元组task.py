#创建一个元组，其元素包含cat、dog、10、20、hat、mice，并对其进行以下操作：
# 1)查询元素dog所在的位置；
# 2）提取数值元素；
# 3）求元组中元素的个数

# 创建元组
tuple1 = ('cat', 'dog', 10, 20, 'hat', 'mice')

# 1) 查询元素dog所在的位置
print(tuple1.index('dog')) 

# 2) 提取数值元素（教材直接通过索引提取）
print(tuple1[2])
print(tuple1[3])

# 3) 求元组中元素的个数
print(len(tuple1))