# def function(a,b):
#     result = a+b
#     return result
#
# function(56,'uo')

#Runing time error ---------------------- Handel
#Syntax Error --------------- Error

# def func():
#     logic/statement/expression

# def function(a,b):
#     return a/b
#
# function(10,0)
# s = int(input('Enter a number:-'))
#
# ZeroDivisionError
# ValueError
# TypeError
# FileNotFoundError
# NameError
# IndexError
# KeyError

# try:
#     Risky Code
# except:
#     handeling block exception
# finally:
#     Relax Block
# try:
#     a = int(input('Enter a value:-'))
#     b =  int(input('Enter a value:-'))
#     print(a/b)
#
# except ZeroDivisionError:
#     print("P/Q Don't use Zero in Q")

#Syntax:-

# try:
#     Risky Code
#
# except ErrorName:
#     Handel the Error
#
# finally:
#     No Risky Code

# try:
#     a = eval(input('Enter a first number:-'))
#     b = eval(input('Enter a second number:-'))
#
#     result = a/b
#
# except ZeroDivisionError as msg:
#     if b == 0:
#         b = eval(input('Please provide a non zero number:-'))
#         result = a/b
#         print(result)
#
# except TypeError as msg:
#     b = eval(input('Please provide a int number only'))
#     result = a/b
#     print(result)
#
# except ValueError as msg:
#     print(msg,'Plz put your value correctly')
#
# except Exception as msg:
#     print(msg)



# try:
#     a = eval(input('Enter a first number:-'))
#     b = eval(input('Enter a second number:-'))
#
#     result = a/b
#
# except (ZeroDivisionError,TypeError,ValueError) as msg:
#     print(msg)
# except Exception as msg:
#     print(msg)







#handel exception for FileNotFoundError.

# file_name = input('Enter your file name:-')

# try:
#     var = open(file_name,'r')
#     data = var.read()
#     print(data)
#
# except FileNotFoundError as msg:
#     print(msg)
#     file_name = input('Enter your file name agin perivous one is wrong:-')
#     var = open(file_name, 'r')
#     data = var.read()
#     print(data)

try:
    file_name_from_user = input('Enter your file name:-')
    def handel_a_file(file_name):
        with open(file_name,'r') as var:
            data = var.read()
            return data

    print(handel_a_file(file_name_from_user))

except FileNotFoundError as msg:
    print(msg)
    file_name_from_user = input('Enter your file name:-')
    print(handel_a_file(file_name_from_user))

finally:
    file_name_from_user = input('Enter your file name:-')
    var = open(file_name_from_user,'w')
    var.write('Gopal')


