# -*- coding: utf-8 -*-
print('北京')
print('欢迎你')
print('------------')

print('北京\n欢迎你')
print('------------')

#水平制表位多大取决于前面字符个数的多少
#一个中文占2字节，一个字母占1字节
print('北京\t欢迎你') # 4-2=2
print('北京北京\t欢迎你') #北京北京是4个字符，一个制表位是4个字符（64字节）  4-4=0（没有剩余的情况再插入一个制表位）
print('hello\toooo') #hello是5个字符，一个制表位是8个字符（64字节） 8-5=3,\t是剩余没填满的位置
print('helloooo\to')

print('老师说：\'好好学习，天天向上\'')
print('老师说：\"好好学习，天天向上\"')

#原字符，使转义字符失效的符号r/R
print(r'北\n京\n欢\n迎\n你')
print(R'北\n京\n欢\n迎\n你')