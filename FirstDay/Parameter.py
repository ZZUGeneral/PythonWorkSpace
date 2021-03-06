# -*- coding: utf-8 -*- 
# @Time : 2020/7/17 17:10 
# @Author : YHL <yanghelong@inspur.com>
# @File : Parameter.py 
# explain : description
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	print ("-- This parrot wouldn't", action)
	print("if you put",voltage,"volts through it.")
	print("--Lovely plumage, the",type)
	print("-- It's",state,"!")
parrot(1000)											#	1	positional	argument
parrot(voltage=1000)									#	1	keyword	argument
parrot(voltage=1000000,	action='VOOOOOM')				#	2	keyword	arguments
parrot(action='VOOOOOM', voltage=1000000)				#	2	keyword	arguments
parrot('a million',	'bereft	of	life',	'jump')			#	3	positional	arguments
parrot('a thousand', state='pushing up the daisies')	#	1	positional,	1	keyword