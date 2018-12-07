#!/usr/bin/env python
#-*- doding=:utf-8
# import unittest
# import requests
import  框架.data.duqu_数据
import 框架.config.学校_接口
b=框架.config.学校_接口
b.tess(123)

a=框架.data.duqu_数据
a.tes_数据()


# class 学校(unittest.TestCase):
#     def test_1(self):
#         shuju = a.tes_数据()
#         html = b.tess(shuju[0][0])
#         self.assertEqual(html['code'], shuju[0][1])
#         self.assertIn(len(html['data']), range(int(shuju[0][2])))

#
#     def test_2(self):
#         shuju = a.tes_数据()
#         html = b.tess(shuju[1][0])
#         self.assertEqual(html['code'], int(shuju[1][1]))
#         self.assertEqual(len(html['data']), int(shuju[1][2]))
#
#
#     def test_3(self):
#         shuju = a.tes_数据()
#         html = b.tess(shuju[2][0])
#         self.assertEqual(html['code'], int(shuju[2][1]))
#         self.assertEqual(len(html['data']), int(shuju[2][2]))













































# from 框架.config.学校_接口 import 学校_查询
# from 框架.data.duqu_数据 import duqu
#
#
# class 学校(unittest.TestCase):
#     tes_学校=学校_查询.学校_考试快查()
#     shuju=duqu()
#     def test_1(self):
#
#         # shuju = self.tes_数据()
#         html = self.tes_学校(self.shuju[0][0])
#         self.assertEqual(html['code'], int(self.huju[0][1]))
#         self.assertIn(len(html['data']), range(int(self.shuju[0][2])))
#
#
#     def test_2(self):
#         # shuju = self.tes_数据()
#         html = self.tes(self.shuju[1][0])
#         self.assertEqual(html['code'], int(self.shuju[1][1]))
#         self.assertEqual(len(html['data']), int(self.huju[1][2]))
#
#
#     def test_3(self):
#         # shuju = self.tes_数据()
#         html = self.tes(self.shuju[2][0])
#         self.assertEqual(html['code'], int(self.shuju[2][1]))
#         self.assertEqual(len(html['data']), int(self.shuju[2][2]))