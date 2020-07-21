# -*- coding: utf-8 -*- 
# @Time : 2020/7/17 15:34 
# @Author : YHL <yanghelong@inspur.com>
# @File : Else.py 
# explain : description
for n in range(2,10):
	for x in range(2,n):
		if(n%x ==0):
			print(n,"equals",x,'*',n/x)
			break
	else:
		print(n,"is a prime number")

for n in range(2,10):
	if n%2 == 0:
		print('Found a even number ',n)
		continue
	print('Found a number ',n)