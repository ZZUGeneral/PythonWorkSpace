# -*- coding: utf-8 -*- 
# @Time : 2020/7/21 17:01 
# @Author : YHL <yanghelong@inspur.com>
# @File : Zipo.py 
# explain : description
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q, a))

for i in reversed(range(1,10,2)):
	print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
	print(i)
