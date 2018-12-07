# import pymysql
# import os
# abc=pymysql.connect(host='192.168.0.60',port=3306,user='root',password='123456')
# aaa=abc.cursor()
# aaa.execute('show databases;')
# print(aaa.fetchall())
# aaa.execute('use test;')
# aaa.execute('show tables;')
# # aaa.execute('select * from stu ;')
# print(aaa.fetchall())



# for j in a:
#     print(j)
# bsjk.execute('use test;')
# bsjk.execute('show tables;')
# print(bsjk.fetchll())
# bsjk.execute('create table stu10(name char(10),math int(10),enlish int(10))')
# print(bsjk.fetchall())
# bsjk.execute('insert into stu1 values("小红",133,100)')
# bsjk.execute('desc stu1')
# print(bsjk.fetchall())
#     print(a)
#
#
# import mysql.connector
# mydb=mysql.connector.connect(host='192.168.0.61',user='root',password='123456')
# mycursor=mydb.cursor()
# mycursor.execute('show databases')
# for x in mycursor:
#     print(x)k.

# f = open(r'./wenjia/k.txt','a',encoding='utf8')
# f.write('{}'.format(a))
# f.close







###数据库导入文件
# import os
# import pymysql
# def kudaowen():
#     f = open(r'../wenjia/a.txt','w',encoding='utf8')
#     asjk=pymysql.connect(host='192.168.0.60',port=3306,user='root',password ='123456')
#     bsjk=asjk.cursor()
#     bsjk.execute('use test;')
#     bsjk.execute('desc stu;')
#     b=bsjk.fetchall()
#     for h,n in enumerate(b):
#         c=b[h]
#         for k in range(1):
#             f.write('{} {}'.format(c[k], ' '))
#     f.write('\n')
#     for i in range(1,6):
#         bsjk.execute('select * from stu where num ={} ;'.format(i))
#         a=bsjk.fetchall()
#         for x,y in enumerate(a):
#             a=a[x]
#             for  j,h in enumerate(a):
#                 f.write('{} {}'.format(a[j],'  '))
#             f.write('\n')
# kudaowen()



###文件导入数据库
# import os
# import pymysql
# msjk=pymysql.connect(host='192.168.0.29',port=3306,user='root',password='123456')
# k=msjk.cursor()
# k.execute('use python;')
# f = open(r'./wenjia/k.txt','r',encoding='utf8')
# a=f.readline()
# a=a.split('  ')
# k.execute('create table stu15({} int(10),{} char(30),{} char(10),{} char(10),{} date);'.format(a[0],a[1],a[2],a[3],a[4]))
# for i in range(5):
#     a = f.readline()
#     a = a.split('  ')
#     # if a[5]==None:
#     #     k.execute('insert into stu15 values("{}","{}","{}","{}","0000-00-00");'.format(a[0], a[1], a[2], a[3]))
#     #     break
#     k.execute('insert into stu15 values("{}","{}","{}","{}","{}");'.format(a[0],a[1],a[2],a[3],a[4]))
#

####文件写入excle表格
# import  xlwt
#
#
# f=open(r'./wenjia/b.txt','r',encoding='utf-8')
# a=f.readlines()
# w=xlwt.Workbook(encoding='utf')
# sheet=w.add_sheet('sheet1')
# # shee=w.add_sheet('sheet2')
# b=len(a)
# f.seek(0)
# for i in range(b):
#     c=f.readline()
#     sheet.write(i,1,c)
# for j in range(b):
#     sheet.write(j,0,j)
# w.save('text.xls')
# f.close()


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import  pymysql
# import  xlwt
# #
# #
# f=open(r'./wenjia/k.txt','r',encoding='utf-8')
# a=f.readlines()
# w=xlwt.Workbook(encoding='utf')
# sheet=w.add_sheet('sheet1')
# # shee=w.add_sheet('sheet2')
# b=len(a)
# f.seek(0)
# for i in range(b):
#     c = f.readline()
#     c=c.split('  ')
#     # print(c[0])
#     for j in range(b):
#         sheet.write(i,j,c[j])
# # # for j in range(b):
# # #     sheet.write(j,0,j)
# w.save('text.xls')
# f.close()

import  pymysql
abc=pymysql.connect(host='192.168.0.60',
                port=3306,
                user='root',
                password='123456',
                charset='utf8')
aaa=abc.cursor()
aaa.execute('show databases;')
print(aaa.fetchall())

