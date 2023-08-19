#break,continue and pass
# and Comprehension--- list com and dict com

# break statement

# li = [45,90,42,78,65,12,98]
#
# for i in li:
#     if i == 45:
#         break
#     print(i)

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

#continue - skip
# li = [12,54,35,67,88,24,68,90,21,23,22]
#
# for i in li:
#     if i%2==0:
#         continue
#     print(i)

#pass

# for i in range(1,10):
#     pass
# if 24%2==0:
#     pass
# while 10>0:
# def func():
# class A:


#Comprehension:-
#list and dictionary


#range between 1 to 20, add all the even number in a list
# li = []
# for i in range(1,21):
#     if i%2==0:
#         li.append(i)
# print(li)


'''
var = [result for var in collection condition]

'''

# var = [i for i in range(1,21) if i%2==0]
# print(var)


# li = [56,'you','we',90,'rty','34',78,23]
#
# str_li = []
# for i in li:
#     if type(i)==str:
#         str_li .append(i)
# print(str_li)
#
# var = [i for i in li if type(i)==str]
# print(var)


# di = {'Name':'Krishna','Age':26,'Subject':['Python','Java','Mojo','R']}
# lis = []
# for k,v in di.items():
#     if k == 'Subject':
#         for data in v:
#             if data =='Python' or data == 'Mojo':
#                 lis.append(data)
# print(lis)
# print(di.get('Subject'))
# li = []
# for i in di.get('Subject'):
#     if i == 'Python'or i =='Mojo':
#         li.append(i)
# print(li)
#
# var = [i for i in di['Subject'] if i=='Python' or i=='Mojo']
# print(var)

di = [
    {'Name':'Gupta','Age':26,'Subject':['Python','R','Golag']},
    {'Name':'Rajesh','Age':28,'Subject':['C++','R','Mojo']},
    {'Name':'Manas','Age':23,'Subject':['Python','R','Golag']},
    {'Name':'Ami','Age':29,'Subject':['C','R','Curl']},
    {'Name':'Sankar','Age':27,'Subject':['Python','R','.Net']}
]

# li = []
# for i in di:
#     for k,v in i.items():
#         if k=='Subject':
#             for j in v:
#                 if j =='Python':
#                     li.append(i.get('Name'))
#
# print(li)
# li = []
# for i in di:
#     if 'Python' in i['Subject']:
#         li.append(i['Name'])
# print(li)

var = [i['Name'] for i in di if 'Python' in i['Subject']]

print(var)


------- --- math ---  server --- data