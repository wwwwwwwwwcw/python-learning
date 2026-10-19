a = int(input("请输入起始小时"))
b = int(input("请输入起始分钟"))
c = int(input("请输入结束小时"))
d = int(input("请输入结束分钟"))

z = (c-a)*60+d-b
h = z//60
m = (z%60)

print ("时间间隔为：",h,"小时",m,"分钟")