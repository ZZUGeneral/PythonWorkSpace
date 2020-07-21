# -*- coding: utf-8 -*- 
# @Time : 2020/7/17 15:04 
# @Author : YHL <yanghelong@inspur.com>
# @File : ForTest.py 
# explain : description
words = ['cat','dog','tiger','fish','sheep']
for w in words:
	print(w,len(w))
for w in words[:]:
	if len(w) <4:
		words.insert(1,w+w)
		words.remove(w)
print(words)
for i in range(10):
	print(i)
for i in  range(3,6):
	print(i)
for i in range(0,10,4):
	print(i)

for i in range(len(words)):
	print (i,words[i])