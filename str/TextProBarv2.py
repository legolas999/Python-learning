#!/usr/bin/python3
#打印进度条
import time
scale = 50
print("{0:=^50}".format("执行开始"))
start_time = time.perf_counter()
for i in range(scale+1):
	a = "*" * i
	b = '.' * (scale - i)
	c = (i/scale)*100
	dur_time = time.perf_counter() - start_time
	print("\r{:^3.0f}%[{}-->{}]{:.2f}".format(c,a,b,dur_time),end="")
	time.sleep(0.2)
print("\n"+"{0:=^50}".format("执行结束"))
