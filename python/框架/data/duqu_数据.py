#!/usr/bin/env python
#-*- coding:utf-8
import xlrd
import unittest
# def duqu():
#     def tes_数据(self):
#         shuju = []
#         f = xlrd.open_workbook('ceshi1.xlsx')
#         sheet = f.sheets()[0]
#         num = sheet.nrows
#         for i in range(1,num):
#             aaa= sheet.row_values(i)
#             shuju.append(aaa)
#         return shuju

# class 学校(unittest.TestCase):
def tes_数据():
    shuju = []
    f = xlrd.open_workbook('ceshi2.xls')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1,num):
        aaa= sheet.row_values(i)
        shuju.append(aaa)
    print(shuju)
    return shuju
tes_数据()
