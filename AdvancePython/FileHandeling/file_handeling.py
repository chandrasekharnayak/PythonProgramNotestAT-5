# ''' 2 types
# 1.Text File(.text,.csv,.xlsx,.ppt)
# 2.Binary File(image,audio,video)
#
# '''
#
# '''
# syntax:- How to open a file
#
# var = open('file_path','mode')
# r,w,a ---
#
# read:- read a file only, nothing change in file. if file is not avialable in mentioned path it's showing
# error(FileNotFoundError)
# 4 methods in read:-
#
# read()
# read(n)
# readline()
# readlines()
#
#
# ,write:- open an existing file for write or change operation.If he file already contains some data then it
# will be overrideen, if the specified is not avialable then this mode will create that file first.
#
# write and writelines
# ,append:- open an existing file for write or change operation.If he file already contains some data then it
# will be write new data after old, if the specified is not avialable then this mode will create that file first.
# '''
# # file_1 = open('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\class_1_2_python_introduction.txt','r')
# # data = file_1.read()
# # print(data)
#
# #read(n)
#
# # file_1 = open('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\class_1_2_python_introduction.txt','r')
# # data = file_1.read(5)
# # print(data)
#
# #readline()
# # file_1 = open('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\class_1_2_python_introduction.txt','r')
# # data1 = file_1.readline()
# # print(data1)
# # data2 = file_1.readline()
# # print(data2)
# # data3 = file_1.readline()
# # print(data3)
# # data3 = file_1.readline()
# # print(data3)
# # data4 = file_1.readline()
# # print(data4)
#
# #readlines():-
#
# # file_1 = open('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\class_1_2_python_introduction.txt','r')
# # data1 = file_1.readlines()
# # print(data1)
#
# # Special Char/Escape Char
# '''
# \n :- New Line
# \t :- Horizontal Tab
# \r :- return
# \b :- back space
# \v :- vertical tab
# '''
#
#
# #Write:-
#
# # var = open('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\\testing_a_file_qwerty.txt','w')
# # var.write('sdbgehfvujdhvjkwhvjkchwejkchwejkchejkwc')
#
# # var = open('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\\testing_a_file_qwerty.txt','a')
# # var.write('\nhjkchwdjkcvnhwecvjkwenwjkcbwdjk\njhgcvwdjhbvwehcbvhew')
#
# #close the file
#
# # file_1 = open('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\class_1_2_python_introduction.txt','r')
# # data1 = file_1.readlines()
# # # print(data1)
# # file_1.close()
# # print(file_1.closed)
# #
# # #Variours properties of file object.
# #
# # #name
# # print(file_1.name)
# # #mode
# # print(file_1.mode)
# # #readable
# # # print(file_1.readable())
# # #writable
# # print(file_1.writable())
# # #closed
# # print(file_1.closed)
#
# #-------------------------------- With Statement------------------------------
#
# # with open('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\class_1_2_python_introduction.txt','r') as var:
# #     data = var.readlines()
# #     print(data)
# #     print(var.closed)
# #
# # print(var.closed)
#
# # How to handel CSV file :- Comma Separated Value
# import csv
# # print(dir(csv))  # writer ,reader
#
#
# # with open('C:\\Users\chand\PycharmProjects\PythonAutomationAllBatch\TREENETRA_AT_5\BasicPython\AdvancePython\FileHandeling\\treenetra_at_5_data.csv','w',newline='') as var:
# #     w = csv.writer(var) # returns csv writer object  writerow writerows
# #     w.writerow(['ENO','ENAME','ESALARY','EADDRESS'])
# #     n = int(input('Enter number of employees'))
# #     for i in range(n):
# #         eno = int(input('Enter Employee Number:-'))
# #         ename = input('Enter Employee Name:-')
# #         esalary = int(input('Enter Employee Salary:-'))
# #         eaddress = input('Enter Employee address:-')
# #         w.writerow([eno,ename,esalary,eaddress])
#
#
# #read csv file data
#
# # import csv
# # with open('C:\\Users\chand\PycharmProjects\PythonAutomationAllBatch\TREENETRA_AT_5\BasicPython\AdvancePython\FileHandeling\\treenetra_at_5_data.csv','r') as var:
# #     data = csv.reader(var)
# #     sort_data = list(data)
# #     # print(sort_dat)
# #     for i in sort_data:
# #         for j in i:
# #             print(j)
#
# #Zipping and Unzipping:-
# #---------------------
# # ZIP_DEFLATED :- Zip
# # ZipFile      :- Access to zip and unzip
# # ZIP_STORED :-- UnZip
#
# #To create Zip File:-
# '''
# var = ZipFile('new_zip_file_name','w','ZIP_DEFLATED')
#
# '''
# # from zipfile import *
# # #
# # file_1 = ZipFile('D:\\new.zip','w',ZIP_DEFLATED)
# # file_1.write('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\class_1_2_python_introduction.txt')
#
# #Unzipping:-
# '''
# var = ZipFile('zip_file_name.zip','r',ZIP_STORED)
# '''
# # from zipfile import *
# #
# # var = ZipFile('D:\\new.zip','r',ZIP_STORED)
# # names = var.namelist()
# # for name in names:
# #     s = 'D://'+name
# #     f1 = open(s,'r')
# #     print(f1.read())
# #     print()
#
# #------------------------------ binary file handeling---------------------------------------------------
#
# # var_1 = open('C:\\Users\chand\OneDrive\Pictures\Signatutre_Chandra_Sekhar.jpg','rb')
# # data1 = var_1.read()
# # # print(data1)
# #
# # var_2 = open('C:\\Users\chand\OneDrive\Pictures\Savya Chair invoice.png','wb')
# # var_2.write(data1)
#
#
# # var = open('D:\TREENETRA\Treenetra_class_notes\TREENETRA_AT-5\class_3_reserved_words.txt','r')
# # data = var.readlines()
# # print(data)
# # var.closed
#
# # import csv
# #
# # with open('D:\\t5.csv','w',newline='') as var:
# #     write = csv.writer(var)
# #     write.writerow(['Ename','Esalary','Edesignation'])
# #     n = int(input('Enter how much data wabts:-'))
# #
# #     for i in range(n):
# #         ename = input('Enter your name:-')
# #         esalary = int(input('Enter your salary'))
# #         edesing = input('Enter your dsign:-')
# #         write.writerow([ename,esalary,edesing])
#
#
# # import openpyxl
# #
# # workbook = openpyxl.Workbook()
# # sheet = workbook.active
# # sheet['A1'] = 'EName'
# # sheet['B1'] = 'Esalary'
# # sheet['C1'] = 'EDesign'
# #
# # sheet['A2'] = 'Gupta'
# # sheet['B2'] = '78000'
# # sheet['C2'] = 'QA'
# #
# # sheet['A3'] = 'Ruchira'
# # sheet['B3'] = '79000'
# # sheet['C3'] = 'QA'
# #
# # workbook.save('data.xlsx')
#
#
# var = open('D:\\TREENETRA\\Treenetra_class_notes\\at_6_file_handeling.csv','w')


# --------------------ZIP and Unzip---------------------
import zipfile

var = zipfile.ZipFile('new_zip_6','w',zipfile.ZIP_DEFLATED) # zip a file with name
var.write('D:\\TREENETRA\\Treenetra_class_notes\\cs_nayak.jpg')














