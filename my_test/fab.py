#-*- coding:utf-8 -*-
#斐波那契函数

def add(a,*b):
    t = 0
    for i in b:
        t += i;
    sum = a+t
    return sum
num = add(1,2,3,4)
print num
