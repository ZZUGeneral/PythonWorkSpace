# -*- coding: utf-8 -*- 
# @Time : 2020/7/21 16:58 
# @Author : YHL <yanghelong@inspur.com>
# @File : Dict.py 
# explain : description
tel = {'jack':11111,"sape":22222}
tel['tom'] = 33333
print(tel)
print(tel.keys())
for x,y in enumerate(tel):
	print(x,y)
for k,v in tel.items():
	print(k,v)