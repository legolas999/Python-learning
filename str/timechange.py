#!/usr/bin/python3
#打印百分比进度变化
import time

for i in range(101):
	print("\r{:^3}%".format(i),end="")
	time.sleep(0.1)

