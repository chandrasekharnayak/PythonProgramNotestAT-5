# def function_name():
#     logic/statement
#
# function_name()

# def wish(name):
#     print('Hi',name,'Good morning')
#
# wish('Prakash')

# def add_sub(a,b):
#     add = a+b
#     sub = a-b
#     return add,sub
#
# print(add_sub(10,20))
# print(add_sub(89,67))

#Types of arguments

# def function_name(para1,para2): #formal argument = parameter
# #     statemnet
# #
# # function_name(arg1,arg2) #acutal arguments = arguments
# #
# # 1.Positional Arguments
# # 2.Keyword Arguments
# # 3.Default Arguments
# # 4.Variable length of Arguments


#Positional Arguments

# def sub(a,b):
#     sub = a-b
#     return sub
#
# print(sub(10,20))
# print(sub(20,10))


#Keyword Arguments
# def std_data(name,age,classs,sec):
#     return name,age,classs,sec
#
# print(std_data('Rohit',sec='A',age=15,classs='10th'))

#Default Arguments:-
# def wish(name='bhaiya'):
#     print('hi',name,'good morning')
#
# wish('Gourav Bhaiya')
# wish('Suresh Bhaiya')
# wish()


#Variable length of arguments

# def func(*args):
#     # total = 0
#     # for i in args:
#     #     total = total + i
#     # return total
#     even_num = []
#     for i in args:
#         if i%2==0:
#             even_num.append(i)
#     return even_num
# print(func(10,89,67,56,34,78,65,900,987))


#keyword variable length of arguments

# def dict_data(**kwargs):
#     for k,v in kwargs.items():
#        if k =='Lang':
#            for i in v:
#                if i =='Python':
#                    print(i)
#
# dict_data(Name='Ruchira',Dept='QA',Salary= '89k',Lang= ['Python','Java','C+'])


#Types of variable

# g = 30  # global variable
# print(g)
# def paresh(a,b):
#     global l
#     l = 40
#     add = a+b+g+l
#     return add
#
# print(paresh(10,20))
# print(l)




# write a python function, for fetch the highest number in a list?

# def list_max(li):
#     max_num = max(li)
#     return max_num
#
# l = [89,78,67,90,45,987,678,56,123349999]
# print(list_max(l))
#
# # write a function , check which number biggest number in two?
#
# def number(a,b):
#     if a>b:
#         return a
#     else:
#         return b




#Nested Function

# def outer():
#     print('Outer function started')
#     def inner():
#         print('Inner function started')
#     inner()
#     print('Inner End')
# outer()


# def biggest_num(li):
#     max_num = max(li)
#     def add_new(max_num,new_num):
#         addition = max_num+new_num
#         return addition
#     print(add_new(max_num,30))
#     return max_num
# l = [90,78,67,56,98,78,99]
# print(biggest_num(l))




# Nested Function:
#
# write nestedted function, if number even then add him a new number or if it is odd then sub with a new number

# def even_odd(num):
#     if num%2==0:
#         def even_add(num,new_num):
#             add = num+new_num
#             return add
#         print(even_add(num,30))
#     else:
#         def odd_sub(num,new_num):
#             sub = num-new_num
#             return sub
#         print(odd_sub(num,30))
# even_odd(79)


#Decorater

# def decore(cal):
#     def inner(a,b):
#         mul = a*b
#         div = a/b
#         print(mul,div)
#         cal(a,b)
#     return inner
# #
# @decore
# def cal(a,b):
#     add = a+b
#     sub = a-b
#     print(add,sub)
#
# cal(10,20)

#write decorator function for pallifrom and check it's even or odd?

# def singdha(add,sub):
#     result = add+sub
#     result1 = add-sub
#     return result,result1
#
#
# print(singdha(34,90))
# print(singdha(78,96))

# Generator
# l = [90,89,78,67,56]
# def gen(li):
#     for i in li:
#         yield i
#
# var = gen(l)
# print(next(var)+10)
# print(next(var)+20)
# print(next(var)+30)
# print(next(var))
# print(next(var))
# d  = {'Name':'Rohan','Age':21,'Subject':['History','Chem','Math']}



#write a genertor ,who return a diction value of list

# d  = {'Name':'Rohan','Age':21,'Subject':['History','Chem','Math']}
#
# def gen(di):
#     for k,v in di.items():
#         if k=='Subject':
#             for i in v:
#                 yield i
#
# var = gen(d)
# print(next(var))
# print(next(var))
# print(next(var))

#Anonymous:- lambda fucntion
'''
syntax:-

var = lambda parameter:logic

def function_name(parameters):
    logic

function_name(arg)
'''

# var = lambda a,b:a+b
#
# print(var(10,20))

# var = lambda a:a%2==0
# print(var(21))

#write lambda fuction check in string 'i' is there or not.

# var = lambda s: 'i' in s
# print(var('rohan'))

#write lambda function check the list 2nd element even or not.

# var = lambda li: li[1]%2==0
# print(var([67,80,76,56]))

#write lambda fucntion check dictionary values are same or not. -----

# Some Python important inbuild fucntions

#filter , map , reduce

'''
Syntax:-

var = filter(function,collection)

'''

# def true_false(a):
#     if a%2==0:
#         return True
#     else:
#         return False
#
# li = [78,67,56,45,34,31,90,89,70,65]
#
# var = list(filter(true_false,li))
# print(var)
#
# var1 = list(filter(lambda a:a%2==0,li))
# print(var1)


#map

# li = [67,90,87,68,45,23,15]
#
# #map(function_name,collection_name)
#
# def list_eleement(a):
#     return a+(5/100)
#
# # print(list_eleement(li))
# var = list(map(list_eleement,li))
# print(var)


#Reduce
from functools import reduce

#reduce(fucnction_name,collection)
li = [78,90,786,57,908,567,543]
var = reduce(lambda a,b:a+b,li)
print(var)




