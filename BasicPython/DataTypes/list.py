'''
var = [12,9+9j,67.90,12]
'''
#append.insert,extend,pop,remove,reverse,sort,index,count,clear,copy

li = [67,90,679,87]
li.append(12)
print(li)

li1 = [67,90,679,87]
li1.insert(1,12)
print(li1)

li3 = ['A','B']
li4 = ['C','D']

li3.extend(li4)
print(li4)

li5 = [67,90,679,87,90]
li5.remove(90)
print(li5)

a = [78,90,54]
b = a.copy()
print(b)


s = [78,90]
s1 = [[56,90,21]]