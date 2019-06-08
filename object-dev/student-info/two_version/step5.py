#!/usr/bin/python3.6
#定义全局变量存储学生信息
student_info = []

def print_menu():
    '''实现打印功能提示菜单功能'''
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

def add_stu_info():
    '''实现添加一个新的学生信息功能'''

    global student_info
    #获取用户输入的信息
    new_number = input('请输入你的学号：')
    new_name = input('请输入你的姓名：')
    new_id = input('请输入你的身份证号码：')
    new_phone = input('请输入你的电话号码：')
    new_dormitory = input('请输入你的宿舍号码：')
    new_addr = input('请输入你的籍贯地址：')

    #定义一个新的字典，来存储新的学生信息
    new_info = {}
    new_info['number'] = new_number
    new_info['name'] = new_name
    new_info['id'] = new_id
    new_info['phone'] = new_phone
    new_info['dormitory'] = new_dormitory
    new_info['address'] = new_addr

    #将新的学生信息，添加到学生整体列表中
    student_info.append(new_info)

    #print(student_info)    # for test

def find_stu_info():
    '''实现查找学员信息功能'''

    global student_info

    #获取要查询的学员姓名
    find_name = input('请输入要查找的学员姓名：')

    find_flag = 0 #默认表示没有找到的标志
    for item in student_info:
        if find_name == item['name']:
            print('{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}'.format('学号','姓名','身份证','电话','宿舍','籍贯'))
            print('{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}'.format(item['number'],item['name'],item['id'],item['phone'],\
item['dormitory'],item['address']))
            find_flag = 1 #表示已经找到了学员信息
            break     #找到后打印退出
    #判断是否找到了学员信息
    if find_flag == 0:
        print("查无此人")

def show_stu_info():
    '''实现显示所有学生信息功能'''
    global student_info

    print('{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}'.format('学号','姓名','身份证','电话','宿舍','籍贯'))
    for item in student_info:
        print('{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\t{:<20}'.format(item['number'],item['name'],item['id'],item['phone'],\
item['dormitory'],item['address']))

def save_stu_info():
    '''实现将学员信息保存到文件中'''

    global student_info

    f = open('stu_info.data','w')

    f.write(str(student_info))

    f.close()

def load_stu_info():
    '''实现加载学生信息功能'''

    global student_info

    try:
        f = open('stu_info.data')
        student_info = eval(f.read())
        f.close()
    except Exception:
        pass    

def modify_stu_info():
    '''实现修改学生信息功能'''

    global student_info

    
    find_flag = 0
    modify_name = input('请输入需要修改的学生名字：')
    for item in student_info:
        if modify_name == item['name']:
            modify_number = input('请输入你的新的学号：')
            modify_id = input('请输入你的新的身份证号码：')
            modify_phone = input('请输入你的新的电话号码：')
            modify_dormitory = input('请输入你的新的宿舍号码：')
            modify_addr = input('请输入你的新的籍贯地址：')
            
            item['number'] = modify_number
            item['id'] = modify_id
            item['phone'] = modify_phone
            item['dormitory'] = modify_dormitory
            item['address'] = modify_addr

            find_flag = 1
            break
    if find_flag == 0:
        print('输入的名字不正确，重新输入')

def delete_stu_info():
    '''实现删除学生信息功能'''

    global student_info

    find_flag = 0
    del_name = input('请输入要删除的学生名字：')

    for item in student_info:
        if del_name == item['name']:
            del student_info[student_info.index(item)]
            find_flag = 1
            break
    if find_flag == 0:
        print('此学生不存在，请重新输入')

def main():
    #恢复以前数据到程序中
    load_stu_info()

    #打印功能提示菜单
    print_menu()

    while True:

        #2. 获取用户的输入
        num = int(input('请输入操作序号：'))

        #3. 根据用户的数据执行相应的功能
        if num==1:
            find_stu_info() 
        elif num==2:
            add_stu_info()
        elif num==3:
            modify_stu_info()
        elif num==4:
            delete_stu_info()
        elif num==5:
            show_stu_info()
        elif num==6:
            save_stu_info()
        elif num==7:
            break
        else:
            print('输入有误，请重新输入')
    
        print('-'*50)
        print('')

if __name__ == '__main__':
    main()
