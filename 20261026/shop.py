num = int(input("请输入商品销售数量："))
if num < 10:
    print("销量滞销")
elif num < 50:
    print("销量正常")
else:
    print("销量畅销")