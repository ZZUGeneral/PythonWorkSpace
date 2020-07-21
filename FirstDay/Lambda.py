# -*- coding: utf-8 -*- 
# @Time : 2020/7/17 17:38 
# @Author : YHL <yanghelong@inspur.com>
# @File : Lambda.py 
# explain : description
def make_incrementor(n):
	return lambda x:x+n
f = make_incrementor(42)
print(f(1))