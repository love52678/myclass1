#-*-coding:utf-8-*-
#  a = int(input('please input num1'))
# b = int(input('please input num2'))
# area = 3.14*a*a
# if area>20:
#     print 'This is a big cicle!'
# else:
#     print 'This is a small cicle.'
#
#
# def are(a,b):
#     if isinstance(b,float) and isinstance(a,float):
#         area = a*b
#         return area
#     else:
#         print 'a,b is not a float num.'
# area = are(2.2,4.0)
# print area
# print isinstance(2,int)
#
# class Animal():
#     def __init__(self):
#         print 'aaa'
# a = Animal()

# class Person():
#     def __init__(self,name):
#         self.name = name
#     def eat(self,food):
#         print 'I like eta {}'.format(food)
#     def drink(self,drink):
#         print 'I like drink {}'.format(drink)
#     def love(self,liker):
#         print 'I love the {}'.format(liker)
#
# person = Person('Jone')
# person.eat('noodle')
# person.drink('water')
# person.love('world')

# class Father():
#     def __init__(self):
#         pass
#     def do(self):
#         print 'I like read book'
#
# class Son(Father):
#     def do(self):
#          print 'I am a'
# class Son1(Son):
#     a = 12#静态属性
#     @classmethod#类方法
#     def do(self):
#         print 'I am b'
#         print self.a
#
# class Son2(Son1):
#     pass
#     @staticmethod#静态方法
#     def do(self):
#         print 'I am c'
#
# son = Son2()
# son.do()
#
# class Animal():
#     def __init__(self,name):
#         self.name = name
#     @classmethod#类方法
#     def walk(cls):
#         print 'I can walk.'
#         print cls
#     @staticmethod#静态方法
#     def work(work):
#         print 'My work is {}'.format(work)
#     def yelp(self):#普通方法
#         print '喵呜'
#         print self
# '''
# 类方法跟普通方法自带参数，例如self，静态方法没有自带参数
# 类方法跟静态方法都可以使用类或者对象调用
# 普通方法只能用对象调用
# '''
# dog = Animal('xiaohei')
# dog.work('eat')
# Animal.work('ee')
# dog.walk()
# Animal.walk()
# dog.yelp()
file = open('E:\python_script\Class\project\myclass1\my_class\README.md','r',1)
print file
try:
    print a
    file.write('rtert')
    a = 2/0
    print a
except NameError:
    print 'NameError'
except IOError:
    print 'you have not write session'
except ZeroDivisionError:
    print 'integer division or modulo by zero'






