#1、创建列表list--可变数据结构（增、删、改、查）
#1）直接用[]创建
#a=[1,2,3,'中文','one',4,5]
#2)list函数创建--其他类型的数据结构转换成列表
#2、增添append insert extend
#1）append--一次只能增添一个元素，并默认增添到末尾
#列表名.append（待增添的元素）
# a.append(6)
#2)insert 在指定的位置上插入一个元素
#列表名.insert（插入的位置，插入的元素）
#a.insert(4,6)
#3)extend 将两个列表拼接
#b列表 a.extend(b)
# b=[7,8,9]
# a.extend(b)
#3、删除 del pop remove
#a=[1,2,3,'中文','one',4,5]
#1）del 删除指定位置上的元素
#del 列表名[索引位置]
#del a[3]
#2)pop 删除指定位置上的元素，并可以对删除的元素输出
#列表名.pop（索引位置）
#print(a.pop(3))
#3)remove 直接删除指定的元素
#列表名.remove(元素）
#a.remove(4)
#3、修改
#直接改变赋值
#a[3]='英文'
#4、查询 index in
#1）index 元素第一次出现的索引位置
#列表名.index（元素）
#print(a.index('one'))
#2)in 判断元素在不在列表
#print(41 in a)
#5 其他操作
#1）求和 sum
a=[1,2,3,4,5]
print(sum(a))
#2)求长度、元素个数len
print(len(a))