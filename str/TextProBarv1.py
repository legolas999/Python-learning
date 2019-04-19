#!/usr/bin/python3
#打印进度条
import time
scale = 20
print("{0:=^30}".format("执行开始"))
for i in range(scale+1):
	a = "*" * i
	b = '.' * (scale - i)
	c = (i/scale)*100
	print("{:^3.0f}%[{}-->{}]".format(c,a,b))
	time.sleep(0.3)
print("{0:=^30}".format("执行结束"))
