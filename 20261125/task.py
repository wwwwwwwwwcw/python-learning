
# 案例一-字典
# 微信好友记录了联系人的联系方式和基本信息，可关联手机号，邮箱，联系地址等，也可以自由编辑联系人的信息，
# 包括增添，修改，删除联系人，下面是微信好友记录的常见功能
# 1、添加好友
# 2、查看所有联系人
# 3、删除
# 4、查找联系人
# 5、退出微信
#编写小程序，实现上述功能的手机通讯录
# 案例一-字典：微信好友通讯录
# 数据格式：person_info = [ {'姓名':'张三', '手机号':'138...', '邮箱':'...', '地址':'...'}, ... ]

person_info = []

print('欢迎使用微信通讯录：')
print('1、添加好友')
print('2、查看所有联系人')
print('3、删除好友')
print('4、查找好友')
print('5、退出微信')

while True:
    fun_num = input('请输入功能序号(1-5): ')
    
    if fun_num == '1':
        name = input('请输入姓名: ')
        phone = input('请输入手机号: ')
        email = input('请输入邮箱: ')
        address = input('请输入地址: ')
        
        new_friend = {'姓名': name, '手机号': phone, '邮箱': email, '地址': address}
        person_info.append(new_friend)
        print('添加成功')

    elif fun_num == '2':
        if len(person_info) == 0:
            print('通讯录为空')
        else:
            print('--- 所有联系人列表 ---')
            for i in person_info:
                for a, b in i.items():
                    print(a, ':', b)
                print('----------------------')

    elif fun_num == '3':
        del_name = input('请输入要删除的好友姓名: ')
        for i in person_info:
            if i['姓名'] == del_name:
                person_info.remove(i)
                print('已删除好友:', del_name)
                break
        else:
            print('未找到该好友')

    elif fun_num == '4':
        find_name = input('请输入要查找的联系人姓名: ')
        for i in person_info:
            if find_name in i.values():
                for a, b in i.items():
                    print(a, ':', b)
                print('----------------------')
                break
        else:
            print('未找到该联系人')

    elif fun_num == '5':
        print('退出微信')
        break
        
    else:
        print('输入错误，请重新输入')