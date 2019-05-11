#!/usr/bin/python3.6

while True:
	fp = open('/root/input_file.txt','a',encoding='utf-8')
	ch = input("请输入一些字符，‘#’结束：")
	if ch != '#':
		fp.write(ch + '\n')
		fp.close()
	else:
		break

	
