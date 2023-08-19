# # 1991 -- 1.0v -- pops
# # 2000 -- 2.0v -- pops(idology and syntax)+  oops(rules) --- family concept
# #
# # Parent and child
# # Hum sath sath hai -- Nayak --
# #
# # class
# #     def bapa function,
# #     def mummy fucntion,
# #     def fist son func ------ \
#
# # what is oops?
# #
# # class Nayak:
# #
# #     def grandfather(self):
# #
# #         def bapa(self):
# #
# #         def bou(self):
# #
# #         def krishna(self):
# #
# #         def chiku(self):
# #
# #         def chicki(self):
# #
# #     def grandfather2(self):
# #
# #         def rahul()
# #         def
# #
# # Nayak.grandfather.bapa()
# # Nayak.grandfather2.rahul
#
#
# # what is a class?
# # class -- blueprint, plan , precondtions
# #
# #
# # class Car
# #
# #     def stering
# #
# #     def accelator
# #
# #     def break
# #
# #     def cluse
# #
# #
# # class Bike:
# #
#
#
# # Synatx:-
#
# # class ClassName:
# #     '''Doc String'''
# #
# #     # Methods and Varibales
# #     #Instance Method, Class Method and Static Method
# #     #Instance Variable, class Variable, and local variable
#
#
# # class Student:
# #
# #     def name(self,name):
# #         print('Hi',name,'morning')
# #
# # #object Reference --- variable
# #
# # obj = Student()
# # obj2 = Student()
# # obj.name('Rabi')
# # obj2.name('Sankar')
#
#
# # a = 'Rabi'
# # print(type(a))
#
#
# # write class and declare function for even and odd?
#
# # class Math:
# #
# #     def even_or_odd(self,num):
# #         if num%2 ==0:
# #             return True
# #         else:
# #             return False
# #
# #
# # obj = Math()
# #
# # print(obj.even_or_odd(11))
#
# #What is constructor
#
# #
# # class Student:
# #     '''This class was written for Student Information'''
# #
# #     def __init__(self,name,sec,sub):  # constructor
# #         self.name = name
# #         self.sec = sec
# #         self.sub = sub
# #
# #     def salary(self,sal):
# #         self.sal = sal
# #
# #
# # obj = Student('Rabi','B','Python')
# # obj.salary(100000)
# # print(obj.__dict__)
#
# #Instance Method:- # Instance Variable
#
# #Instance Variable
#  # inside constructor by using self keyword
#  #inside instance method bt using self keyword
#  #outside of the class using obj_referebce
#
# # class Employee:
# #
# #     def __init__(self,id,name,age): # constrctor
# #         self.id  = id  # 101
# #         self.name = name # 'Ammi
# #         self.age = age
# #
# #
# #     def employee_salary(self,salary):  # instance method
# #         self.salary = salary          # instance variable
# #         print(f'hi my id is {self.id} and name :- {self.name} , age is {self.age} and salary {self.salary}')
# #
# #
# # obj = Employee(101,'Ammi',30)
# # obj.dept = 'IT :- QA'
# # obj.HR = 'Hema malini'
# # obj.employee_salary(100000)
# # print(obj.__dict__)
#
# #write a bank atm machine program
# #bank account number, holder name, avilable balance balance --- primary
# # deposite amount :-  output :- deposite amount and avilable amount\
# #writhdraw amount :- withdrwa amount and avialable amount
#
# # pin number
#
# #
# # class BankAtmMachine:
# #
# #     pin_number  = int(input('Enter your pin:-'))
# #
# #
# #     def __init__(self,account_number,acct_holder_name,avl_balance,pin_number_func):
# #         self.account_number = account_number
# #         self.acct_holder_name = acct_holder_name
# #         self.avl_balance = avl_balance
# #         self.pin_number_func = pin_number_func
# #
# #
# #     def deposite_amount(self,deposite):
# #         if BankAtmMachine.pin_number == self.pin_number_func:
# #             self.deposite = deposite
# #             self.avl_balance = self.avl_balance + self.deposite
# #             print(f'deposite amount is :- {self.deposite} and avl balance is :- {self.avl_balance}')
# #         else:
# #             print('Wrong Pin')
# #
# #
# #
# #     def withdraw_amount(self,withdraw):
# #         if BankAtmMachine.pin_number == self.pin_number_func:
# #             self.withdraw = withdraw
# #             self.avl_balance = self.avl_balance - self.withdraw
# #             print(f'withdrwa amount is :- {self.withdraw} and avl balance is :- {self.avl_balance}')
# #
# #     def bank_details(self):
# #         if BankAtmMachine.pin_number == self.pin_number_func:
# #             print(f'Account Holder Name:-{self.acct_holder_name}')
# #             print(f'Account Number:-{self.account_number}')
# #             print(f'Account Balance:-{self.avl_balance}')
# #
# # obj = BankAtmMachine(1012345678,'Rabi Narayan',90000,1234)
# # obj.bank_details()
# # obj.deposite_amount(10000)
# # obj.withdraw_amount(5000)
#
# '''
# You have Bus and You are a conductor:-
# Bus :- Dolphin
# star :- Bhubaneswar
# stop :- Pune
# avl :- 60'
# seat price - 700
# cancel fees - 150
#
# Friday M:- 15 seat book -- avl--?
# Friday E :- 10 seat Book--- avl?
# Satuday M:- 7 seat cancel avl?
# Satuday E :- 11 book avl?
# Sunday M :- 6 Cancel avl ?
#
# Sunday E :- out :- how many seat booked, how many seat avl and total earning amount..?
# '''
#
# # class BusDolphin:
# #
# #     def __init__(self,bus_name,start_point,stop_point,avl_seat,seat_price,seat_cancel_price):
# #         self.bus_name = bus_name
# #         self.start_point = start_point
# #         self.stop_point = stop_point
# #         self.avl_seat =avl_seat
# #         self.seat_price = seat_price
# #         self.seat_cancel_price = seat_cancel_price
# #
# #     def friday_data(self):
# #         seat_book_fm  = int(input('Enter friday morning book tickt:-'))
# #         seat_book_fe = int(input('Enter friday evening book ticket:-'))
# #
# #         def friday_morning(seat_book_fm):
# #
# #             global friday_mrng_avl_seat
# #             friday_mrng_avl_seat = self.avl_seat-seat_book_fm
# #             print('Friday Morning seat book:-', seat_book_fm)
# #             print('friday morning avl seat:-',friday_mrng_avl_seat)
# #
# #         def friday_evening(seat_book_fe):
# #             global friday_eveng_avl_seat
# #             friday_eveng_avl_seat = friday_mrng_avl_seat - seat_book_fe
# #             print('Friday Eveing seat book:-', seat_book_fe)
# #             print('friday evening avl seat:-',friday_eveng_avl_seat)
# #
# #         return friday_morning(seat_book_fm),friday_evening(seat_book_fe)
# #
# #
# #     def saturday_data(self):
# #         seat_cancel_sm = int(input('Enter saturday morning cancel tickt:-'))
# #         seat_book_se = int(input('Enter saturday evening book ticket:-'))
# #
# #         def saturday_morning(seat_cancel_sm):
# #             global saturday_morning_avl_seat
# #             saturday_morning_avl_seat = friday_eveng_avl_seat + seat_cancel_sm
# #             print('Saturday Morning seat Cancel:-', seat_cancel_sm)
# #             print('Satuday Morning avl seat:-', saturday_morning_avl_seat)
# #
# #
# #         def saturday_evening(seat_book_se):
# #             global saturday_eveng_avl_seat
# #             saturday_eveng_avl_seat = saturday_morning_avl_seat - seat_book_se
# #             print('Saturday Eveing seat book:-', seat_book_se)
# #             print('Saturday evening avl seat:-', saturday_eveng_avl_seat)
# #
# #         return saturday_morning(seat_cancel_sm),saturday_evening(seat_book_se)
# #
# #
# #     def sunday_data(self):
# #         seat_cancel_sm = int(input('Enter sunday morning cancel tickt:-'))
# #
# #         def sunday_morning(seat_cancel_sum):
# #             global sunday_mrng_avl_seat
# #             sunday_mrng_avl_seat  = saturday_eveng_avl_seat + seat_cancel_sum
# #             print('Sunday Morning seat Cancel:-', seat_cancel_sum)
# #             print('Last  avl seat:-', sunday_mrng_avl_seat)
# #         return sunday_morning(seat_cancel_sm)
# #
# #     def final_count(self):
# #         booked_seat = self.avl_seat - sunday_mrng_avl_seat
# #         print('final book ticket:-',booked_seat)
# #
# # obj = BusDolphin('Dolphin','BBSR','PUNE',60,700,150)
# # print(obj.__dict__)
# # obj.friday_data()
# # obj.saturday_data()
# # obj.sunday_data()
# # obj.final_count()
#
# #How delete instance variable
#     #with the heelp self and with the help of object reference
#     # del
#
# # class Employee:
# #
# #     def __init__(self,name,age,salary):
# #         self.name = name
# #         self.age = age
# #         self.salary = salary
# #
# #     def data(self):
# #         del self.salary
# #
# # obj = Employee('Abhi','67',9088754676)
# # del obj.age
# # obj.data()
# # print(obj.__dict__)
#
#
# #class method and class variable
#
# # class Emp:
# #
# #     a = 10 #class variable
# #
# #     def data(self):
# #         print(Emp.a)
# #         print('Ok')
# #
# #     def data_2(self):
# #         print(Emp.a)
# #         print('OK_2')
# #
# # obj = Emp()
# # # obj.data()
# # # obj.data_2()
# # print(obj.a)
#
#
# #Create a class method
#
# # class Emp:
# #
# #     a = 10
# #     b = 20
# #
# #     @classmethod
# #     def aceess(cls): # class method
# #         result = cls.a +cls.b
# #         return result
# #
# # obj = Emp()
# # print(obj.aceess())
#
# #
#
# # write a program , declare a common integer list variable and sort it
#
# class SortList:
#
#     a = [89,90,67,54,34,98,123,46,87,62,91,11]#0,11
#
#     @classmethod
#     def bubble_sort(cls):
#         for i in range(len(cls.a)): # i 3
#             for j in range(0,len(cls.a)-i-1): #j 2,9
#                 if cls.a[j]>cls.a[j+1]:
#                     cls.a[j],cls.a[j+1] = cls.a[j+1],cls.a[j]
#
#
#         print(cls.a)
#
#
#
#
# obj = SortList()
# obj.bubble_sort()
#


#Static Method and local variable

#Cls Var:- constrcutor,instance methid and static method using ClassName
        # :- Outside of class using object reference
        #In classmethod using cls variable


# class Employee:
#
#     a = 10# class variable == global variable
#     @staticmethod
#     def cal(x,y):
#         b = 90 #local var
#         sum = Employee.a+x+y+b
#         return sum
#
#
#
# obj = Employee()
# print(obj.cal(10,20))


# class Employee:
#
#     def cal(self,a,b):
#         self.a = a
#         self.b = b
#         print(self.a*self.b)
#
#     def sub(self):
#         print(self.b)
#
#     @staticmethod
#     def qwe(a,b):
#         print(b)
#
#     @staticmethod
#     def xyz():
#         print(b)
#
# obj = Employee()
# obj.cal(10,20)
# obj.sub()
# obj.xyz()213

#Inheritance

# Royal Enfield:-   Bullet 350   - key feature - 350cc,2l,2500rmp(Parent)
#
# Royal Enfield :-   Classic 350 -- body --350cc,2l,2500rmp(Child )--little bit change(parent)
#
# Royal Enfield :-   Classic 350 New -- body ----350cc,2l,2000rmp(child)

'''
single (1 single parent class clalled single child class)
multiple
mutilevel
Hyrechical

'''

#Base class
# class RoyalEnfieldBullet:# parent class
#
#     def __init__(self,cc,engine_capacity,rmp):
#         self.cc = cc
#         self.engine_capacity=engine_capacity
#         self.rmp = rmp
#
#     def display(self):
#         print(f'cc:-{self.cc}')
#         print(f'engine_capacity:-{self.engine_capacity}')
#         print(f'rmp:-{self.rmp}')
#
#
#
# class RoyalEnfieldClassic(RoyalEnfieldBullet):#child
#
#     def __init__(self,cc,engine_capacity,rmp,body_change):
#         super(RoyalEnfieldClassic, self).__init__(cc,engine_capacity,rmp)
#         self.body_change = body_change
#
#     def display(self):
#         print(f'cc:-{self.cc}')
#         print(f'engine_capacity:-{self.engine_capacity}')
#         print(f'rmp:-{self.rmp}')
#         print(f'body_change:-{self.body_change}')
#
# classic = RoyalEnfieldClassic('350cc','2L','2500hz/rpm','Retro Type')
# classic.display()
# print('parentis:-',RoyalEnfieldClassic.__bases__[0].__name__)




#multiple inheritance

# Base class 1
# class Parent1:
#     def method1(self):
#         print('This is method 1 from Prarent1')
#
#
# #Base class2
# class Parent2:
#     def method2(self):
#         print('This is method 2 from Prarent2')
#
#     def method3(self):
#         print('This is method 3 from Prarent2')
#
# #Derived class inheriting from both Parent1 and Parent2
# class Child(Parent1,Parent2):
#     def method3(self):
#         print('This is method 3 from child')
#
#
# obj = Child()
# obj.method1()
# obj.method2()
# obj.method3()
# #
# #wrong concept
# # obj_parent2 = Parent2()
# # obj_parent2.method1()
#
#
#
# #multi level inhheritance
#
# #base class
# class Grandparent():
#     def method1(self):
#         print('This is method1 from  Grandparent')
#
# #Derived class inheriting from Grandparent
# class Parent(Grandparent):
#
#     def method2(self):
#         print('This is method2 from  Parent')
#
# #Derived class inheriting from Parent
# class Child(Parent):
#     def method3(self):
#         print('This is method3 from  Child')
#
#
# obj = Child()
# obj.method1()
# obj.method2()
# obj.method3()

# obj_parent = Parent()
# obj_parent.method1()


#Write multiple inheritance on a file sharing part

# class File1:
#
#     def open_file1(self):
#         var = open('D:\TREENETRA\Treenetra_class_notes\Treenetra_AT-3\class_1_fundamental_of_python.txt','r')
#         data = var.read()
#         print(data)
#
# class File2(File1):
#
#     def open_file2(self):
#         var = open('D:\TREENETRA\Treenetra_class_notes\Treenetra_AT-3\class_2_features_of_python.txt', 'r')
#         data = var.read()
#         print(data)
#
#
# class File3(File2):
#
#     def open_file3(self):
#         var = open('D:\TREENETRA\Treenetra_class_notes\Treenetra_AT-3\class_3_identifiers.txt', 'r')
#         data = var.read()
#         print(data)
#
# obj3 = File3()
# obj3.open_file1()

#Hierachical

#Base Class
class Fruits:

    def __init__(self,verity):
        self.verity = verity

    def taste(self):
        pass


#child class1
#
# class Mango(Fruits):
#     def taste(self):
#         return 'Awsome'
#
# #child class2
#
# class Orange(Fruits):
#     def taste(self):
#         return 'Mast'
#
# #child class1
#
# class Banana(Fruits):
#     def taste(self):
#         return 'Ok Type'
#
#
# #usage
#
# if __name__ == '__main__': # special construct
#     mango = Mango('banarasi')
#     orange = Orange('Santra')
#     banana = Banana('Singapuri')
#
#     print(mango.verity)
#     print(mango.taste())
#
#     print(orange.verity)
#     print(orange.taste())
#
#     print(banana.verity)
#     print(banana.taste())
#
# print(dir(int))

# Basic:-
#
# 1. Python Intro
# 2.Python Feature
# 3.Where we can use
# 4.Not use area
#
# 6.Indetifies
# 7.Keyword
#
# 8.Datatype
# 9.Data structure(int,float,bool,complex,string,list,tuple,set,fzset,bytes,bytearray,range
#                  dict,None)
#
# 10.Operator
#
# 11.Input and Output Satatemment
#
# 12.Flow Control(Condition,Transfer,Interative) :- Terranary operotor
#
#
# Advance:-unzip,nested fucn,lambda,decorator,shallow and deep
#
# Function(Types arguments, fucntion define, parameter,types variable,nested fucn,lambda,filter,map.reduce
# decorator,genertor)
#
# File Handeling(open,r,w,a,with,zip,unzip)
#
# exception handleing(type handleing,try,except,finally)
#
# module and packages
#
# oops(class,type of method, types variables, inhheritance, constructor,del)
#
#
# #Database Connection 90mints
# #Regular expression-- selenium with API 2
# #logging - warning- seenium 2
#
# #Selenium -
# #Pytest - jenkins and docker
# #Manual Testing - jira and agile
#
#
# GIT
# MongoDB
# AWS-EC2
#














