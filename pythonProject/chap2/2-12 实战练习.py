# -*- coding: utf-8 -*-
#输出内容到指定文件
fp=open('text.txt','w')
print('人生苦短，我用python',file=fp)
fp.close()#关闭文件

#输出个人自我介绍
name=input('请输入您的姓名：')
age=input('请输入您的年龄：')
tag=input('请输入您的座右铭：')
print('------自我介绍------')
print(name)
print(age)
print(tag)
