'''
Collectional Interation---- for loop
Conditional Interation---- while loop

'''
# for :- if we want iterate a collection, means if you want work with element in a collection. then you can go
#         for for loop.not

# synatx:-
'''
for var in collection_name:
    statement
'''

# li = [90,89,76,54,901]
#
# for var in li:
#     print(var)

# li = [8900,7800,6700,5600,4500,3400,2300,1200]
#
# for var in li:
#     print(var+500)

#Checl even or odd
# li = [78,90,51,31,45,64,90,87,65]
# even_li = []
#
# for var in li:
#     if var%2==0:
#         print(var,True)
#     else:
#         print(var,False)

#
# li = [78,90,51,31,45,64,90,87,65]
# even_li = []
# odd_li = []
#
# for var in li:
#     if var%2==0:
#         even_li.append(var)
#     else:
#         odd_li.append(var)
#
# print(even_li)
# print(odd_li)


#write loop, check the number is pallibdrom or not then add is a set

# li = [909,8798,454,788,676,123,124,121]
#
# pallidrom_set = set()
#
# for var in li:
#     if str(var) == str(var)[::-1]:
#         pallidrom_set.add(var)
# print(pallidrom_set)


#range

# range(9) # 0,8
# range(1,9)#1,8

# for var in range(1,51):
#     if var%2 ==0:
#         print(var)

# li = [89,78,567,67]
#
# for var in li:
#     statement

#string -- for

# s = 'Bhubaneswar to Banglore'
# li = []
# for i in s:
#     li.append(i)
# print(li)

#dict -- for

# di = {'Name':'Lipu','Age':26,'Salary':78000}
#
# # for var1,var2 in dictionary.items
#
# for key,value in di.items():
#     print(key, value)

#--------------------------------------------------------
# List inside a list
# li =[
#         [2,4,6,10,12],
#         [3,6,9,12,15],
#         [4,8,12,16,20]
#     ]
#
# #Nested for in Nested list
#
# for var in li:
#     for var2 in var:
#         print(var2)



# li = [
#     (78,90,56),
#     (90,92,95),
#     (67,89,45),
#     (),()
# ]
#
# for var in li:#(90,92,95)
#     for var2 in var:#95
#         print(var2)
#


#2.list inside a dictionary
# li = [
#     {'Name':'Ruchira','Age':27,'Salary':92000},
#     {'Name':'Umesh','Age':29,'Salary':98000},
#     {'Name':'Gupta','Age':26,'Salary':140000}
# ]
#
# for jaga in li: #i={'Name':'Gupta','Age':26,'Salary':140000}
#     for k,v in jaga.items():
#         print(k,v)

##dictionary inside a dictionary
# li = {
#         1:{'Name':'Ruchira','Age':27,'Salary':92000},
#         2:{'Name':'Umesh','Age':29,'Salary':98000},
#        3: {'Name':'Gupta','Age':26,'Salary':140000}
#
# }
#
# for k,v in li.items():
#     for k1,v1 in v.items():
#         print(k1,v1)


# List inside a list
#list inside a dictionary
#dictionary inside a dictionary


#---------------------------------------------------------------------------

# li_1 = [1,2,3,4,5]
# li_2  = [1,6,3,9,5]
#
# result = [1,8,3]
# #output :- [1,8,3,13,5]
#
# for i in range(len(li_1)): #range(5) -- 0,4  i = 4
#     if len(li_1) == len(li_2):
#         if li_1[i] != li_2[i]: #li_1[1] != li_2[1]
#             result.append(li_1[i]+li_2[i])
#         else:
#             result.append(li_1[i])
# print(result)

# li_1 = [10,'Sankrit','Biology',20]
# li_2 = [20,'google','apple','30']

# output = [30,'Sankritgoogle','Biologyapple']

# result = []
# for i in range(len(li_1)):
#     if len(li_1) == len(li_2):
#         if type(li_1[i]) == type(li_2[i]):
#             result.append(li_1[i]+li_2[i])
#
# print(result)


#----------------- while loop----------------------------

'''
syntax:-

while condition:
    syntax

'''
#
# while True:
#     print('a')

#print 1 to 10 use in while loop


# num = 1
#
# while num<=10:
#     print(num)
#     num = num+1


# print reverse a number without str function

# num = 1234
# reverse_num = 0 #4321
# while num >0:
#     last_digit = num%10 # 2
#     reverse_num = (reverse_num*10)+last_digit
#     num = num//10
# print(reverse_num)


# print(1234//10)

# print even number with help of while in python 1 to 20.r
# num = 1
# while num >0 and num<=20:
#     if num%2==0:
#         print(num)
#     num = num+1

#print  div by 3and div by 5 , 1 to 30 help of while loop.

# num = 1
#
# while num>0 and num<=30:
#     if num%3==0 and num%5==0:
#         print(num)
#     num = num+1
