#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import  pymysql
# import  xlwt
#
#
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

###
# import xlrd
# f=xlrd.open_workbook('text.xls')
# # print(f.sheet_names())
# sheet=f.sheets()[0]
# # a=sheet.nrows
# a=sheet.row_values(0)##打印表格的第一行以list的类型打印出来的
#
# b=sheet.col_values(1)
#
# print(sheet.cell(0,1).value)

#######库导表
import pymysql
import xlwt
f=xlwt.Workbook(encoding='utf-8')
sheet=f.add_sheet('sheet1')
sheet.write(0,0,'姓名')
f.save('qwer.xls')
# sjk=pymysql.connect(host='192.168.0.60',port=3306,user='root',password='123456',charset='utf8')
# msjk=sjk.cursor()
# msjk.execute('use test;')
# msjk.execute('desc stu;')
# a=msjk.fetchall()
# # print(a[0])
# for i,j  in enumerate(a):
#     b=a[i]
#     # print(b)
#     for x in range(1):
#         # print(i)
#         # print(b[x])
#         sheet.write(0,i,b[x])


# print(msjk.fetchall())

# a='123'
# bb=0
# for i,j in enumerate(a[::-1]):
#     bb+=int(j)*10**i
# print(bb)

# a = input('>>')
# b = a.split(',')
# c = []
# for i in b:
#     if int(i) not in c:
#         c.append(int(i))
# print(c)
# print(type(c[0]))

