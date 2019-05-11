#!/usr/bin/python3.6
#定义初始化数据结构函数
def init(data):
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}


#定义查找人员姓名的函数
def lookup(data,label,name):
	return data[label].get(name)

#定义存储人员信息的函数
def store(data,full_name):
	names = full_name.split()
	if len(names) ==2:
		names.insert(1,'')
	labels = 'first','middle','last'

	for label,name in zip(labels,names):
		people = lookup(data,label,name)
		if people:
			people.append(full_name)
		else:
			data[label][name] = [full_name]

#storage = {}
#init(storage)
#print(storage)

#print(lookup(storage,'middle','Lie'))

MyNames = {}
init(MyNames)
store(MyNames,'Magnus Lie Hetland')
store(MyNames,'Robin Hood')
store(MyNames,'Robin Locksley')
store(MyNames,'Mr. Gumby')
print(MyNames)
print('-'*30)
print(lookup(MyNames,'middle','Lie'))
print(lookup(MyNames,'first','Robin'))
