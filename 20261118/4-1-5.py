#查询index in
#1）index()方法：查询指定元素的一个索引位置
#列表名.index(元素)
a = [1, 2, 3, "中文", "one", 4, 5, 6, 7, 8]
print(a.index("中文"))
#2）in运算符：判断指定元素是否在列表中
#元素 in 列表名
print("中文" in a)