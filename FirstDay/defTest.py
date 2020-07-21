# -*- coding: utf-8 -*- 
# @Time : 2020/7/17 15:42 
# @Author : YHL <yanghelong@inspur.com>
# @File : defTest.py 
# explain : description
def fib(n):
	""""创建一个斐波那契序列"""
	a, b = 0, 1
	while b < n:
		print(b)
		a, b = b, a + b

def	ask_ok(prompt,	retries=4,	complaint='Yes	or	no,	please!'):
	while True:
		ok	=	input()
	if	ok	in	('y',	'ye',	'yes'):
		return	True
	if	ok	in	('n',	'no',	'nop',	'nope'):
		return	False
	retries	=	retries	-	1
	if	retries	<	0:
		raise	IOError('refusenik	user')
	print(complaint)
ask_ok("are you ok?")