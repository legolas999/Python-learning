#!/usr/bin/python3.6
#1.打印功能提示菜单
print('=' * 40)
print('\t{:<40}'.format('学生信息管理系统V1.0'))
print('\t{:<40}'.format('1.查询学员信息'))
print('\t{:<40}'.format('2.增加学员信息'))
print('\t{:<40}'.format('3.修改学员信息'))
print('\t{:<40}'.format('4.删除学员信息'))
print('\t{:<40}'.format('5.显示学员信息'))
print('\t{:<40}'.format('6.保存学员信息'))
print('\t{:<40}'.format('7.退出系统'))
print('=' * 40)

while True:
    #2. 获取用户的输入
    num = int(input('请输入操作序号：'))

    #3. 根据用户的数据执行相应的功能
    if num==1:
        pass
    elif num==2:
        pass
    elif num==3:
        pass
    elif num==4:
        pass
    elif num==5:
        pass
    elif num==6:
        pass
    elif num==7:
        break
    else:
        print('输入有误，请重新输入')
