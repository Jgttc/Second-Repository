# -*- coding: utf-8 -*-

luck_number=8#整型变量

my_name='小猪猪'#字符串类型的变量

print('luck_number的数据类型是：',type(luck_number))
print(my_name,'的幸运数字是：',luck_number)

#python动态修改变量的数据类型，通过不同类型的值就可以直接修改
luck_number='北京欢迎你'
print('luck_number的数据类型是：',type(luck_number))
print(my_name,'说：',luck_number)

#在python中允许多个变量指向同一个值
no=number=1024
print(no,number)
print(id(no))#id()查看对象的额内存地址
print(id(number))