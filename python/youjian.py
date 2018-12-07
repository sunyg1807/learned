#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import 语句    导入其他文件的数据    import 文件名
# from 文件名 import 函数名   只导入了文件中的某个函数

# import hanshu   # 将hanshu文件中所有的代码导入本文件
# from hanshu import *
# yinshu()
# shiliu(100)
# from hon import  zifu
# import hon
# hon.zifu('12 45 312')
# zifu('213 5 4 ')
class Aaa():
    def zhishu(self,x):
        sum=0
        for i in range(2,x):
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                sum=sum+i
        print(sum)
        return sum
    # 质数之和(10)
    def aaa(self,sum):
        print(sum)
aa=Aaa()
bb=aa.zhishu(100)
aa.aaa(bb)