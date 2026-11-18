# 创建列表list--可变数据结构（可变数据结构：可以随时增删改查）
# 1）直接用[]创建
a = [1, 2, 3, "中文", "one"]
# 2）用list()函数创建--其他类型的数据结构转换成列表
#2、增添append insert extend
# 1）append()方法：一次只能增加一个元素，并默认在列表的末尾
#列表名.append(元素)
a.append(4)
print(a)


# 2) insert()方法：可以在指定位置插入一个元素(在指定位置之前插入)，其他元素向后移动
#列表名.insert(索引位置,元素)
a.insert(4, 5)
print(a)

# 3) extend()方法：两个列表拼接
#b列表 a.extend(b)
b = [6, 7, 8]
a.extend(b)
print(a)