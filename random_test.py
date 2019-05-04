#!/usr/bin/python3.6
import random

checkcode=''
for i in range(5):
	current = random.randrange(0,5)
	if current == i:
		#65-90是A-Z的ASCII编码
		tmp = chr(random.randint(65,90))
	else:
		tmp = random.randint(0,9)
	checkcode += str(tmp)
print(checkcode)
