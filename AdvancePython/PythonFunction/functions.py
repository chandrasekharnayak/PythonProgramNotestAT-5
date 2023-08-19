# def add(a,b):
#     c = a+b
#     return c
#
# print(add(10,20))
#
# print(add(80,70))
#
# print(add(67978,13123))

#                                       Functions:-
#                                       ---------
# If a group statements is repeatadly required then it's not recommended to write these statements everytime separetly, We have to define these statements as a single unit and we call that unit any number of times based on our
# requirement without rewriting the code. These single unit is called Function.
#
#
# Adv:- Reusabilty,Time consume, Length of code Reduce
#
# There are 2 types of Function in Python

#Inbuild function and User Define Function

'''
syntax:-

def fucntion_name():
    statement/expression/logic
    return data
'''

# def wish():
#     return 'Good morning'
#
# print(wish())
# print(wish())

#Parameter Concept

# def name_wish(name): #parameter
#     wish_plz = name+' Good morning'
#     return wish_plz
#
# print(name_wish('Gupta')) #argument

# def even_odd(num):
#     if num%2==0:
#         return 'even'
#     else:
#         return 'odd'
#
# print(even_odd(10))
# print(even_odd(13))

# def is_pllindrom(num):
#     if str(num) == str(num)[::-1]:
#         return 'Pallindrom'
#
#     else:/
#         return 'Not a Pllindrom'
#
# print(is_pllindrom(121))
# print(is_pllindrom(123))

#Types of Parametergument/Argument:-

'''
1.Positial Paratmeter/Argument
2. Keyword
3.Default 
4.Variable length 

'''

# def func_name(parameter):  # formal argument
#     statement
#
# fucn_name(78) # acutal argument


#Positional Argument:-

# def sub(a,b):
#     c = a-b
#     return c
# rning
# print(sub(20,))


# #keyword arguments
# def wish(wish,name,work):
#     print('Hi',wish,name,work)
#
# wish(work = 'yes am working today',wish = 'Good Morning',name = 'krishna',)
#


#default Arguments:-

# def wish(name='Uncle'):
#     print('Hi',name,'Good morning')
#
# wish()

#Variable length of arguments:-

# def sum(*args):
#     var = 0
#     for i in args:
#         var = var+i
#     print(var)
#
# sum(7,8,68,79,54,989,78,65,7876,764,89765,789654)

# def is_pallindrom(*num):
#     di = {}
#     for i in num:
#         if str(i)==str(i)[::-1]:
#             ans = "Pallindrom"
#             di.setdefault(i,ans)
#         else:
#             ans = 'Not Pallindrom'
#             di.setdefault(i,ans)
#     return di
#
# print(is_pallindrom(78,121,898,765,234,555))


# # I want variable length of argument of same length of list
#
# [78,90,76,56],[89,90,76,45],[89,90,78,67]
# index addition :-
# [3423,270,]
#
# var = [[12,89,90,56],[78,56,34,90],[223,89,43,21,85],[12,91,15,61]]
#
# li = [sum(i) for i in zip(*var)]
# print(li)


# var = [[12,89,90,56],[78,56,34,90],[223,89,43,21],[12,91,15,61]]
# output_list = []
#
# list_length = len(var[0])
#
# for i in range(list_length):#i0,1,2,3
#     current_sum = 0
#     for j in var:#j = 1st
#         current_sum = j[i]+current_sum
#
#     output_list.append(current_sum)
# print(output_list)


def var_length(*var):
    output_list = []

    list_length = len(var[0])

    for i in range(list_length):  # i0,1,2,3
        current_sum = 0
        for j in var:  # j = 1st
            current_sum = j[i] + current_sum

        output_list.append(current_sum)
    return output_list

print(var_length([78,90,76,56],[89,90,76,45],[89,90,78,67]))


