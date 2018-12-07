#requests 第三方库需要下载
#爬虫：又叫 网络蜘蛛（spider）
#模仿浏览器，根据自己制定的规则批量下载网络中的资源；

#正则表达式：匹配文件中的内容
# .匹配任意一个字符，除了换行符（后加re.S 可以匹配包括换行符在内的所有字符 re.I匹配的字符不区分大小写）

#导入正则模块  只能匹配字符串
#贪婪模式：尽可能多的去匹配最后的字符串     非贪婪模式：尽可能少的去匹配最后的字符串     带有？的是非贪婪（级别最高）；带有*是贪婪模式
# import re
# a = '''qwe123
# qweqwe456qwe'''
#将要匹配的正则编译
# b = re.compile('qwe(.*?)qwe',re.S)
#到目的字符串中去查找
# c = b.findall(a)
# print(c)
#


#模仿浏览器的模块： urllib,urllib3,requests

#匹配内容的模块： re,bs4, xpath

#爬虫分类  1，聚焦爬虫（只爬取某个网站的资源）  2，搜索爬虫（爬区整个网络中的资源）

#面向对象代码   爬虫的第一步：分析网址的变化   第二步：分析html文件过滤想要下载的资源  第三步： 保存 ，，保存的权限和格式
# import requests
# import re
#
# class Qiushi(object):
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         # 发送请求
#         response = requests.get(url=url)
# # 读取结果的方式：1,以字符串的方式读取 2,以字节码的方式读取
# #         html=response.text   #以字符串的方式读取
#         html = response.content.decode('utf-8')  #以字节码的方式读取
#         return html
#
#     def guolv(self,abc):
#         shuju=[]
#         patt=re.compile('<div class="content">(.*?)</div>',re.S)
#         items =  patt.findall(abc)
#         for i in items:
#             i = i.replace('<span>','').replace('</span>','')
#             i =i.replace('<br/>','')
#             i=i.strip()
#             print(i)
#             shuju.append(i)
#         return shuju
#
#     def save(self, shuju):
#         with open('b.txt', 'a', encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i + '\n')
#
#
# qiushi = Qiushi()
# jieguo = qiushi.qingqiu(1)
# shuju=qiushi.guolv(jieguo)
# qiushi.save(shuju)


# !/usr/bin/python3

# str = 'Runoob'
#
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + '你好')  # 连接字符串
#
# print('------------------------------')
#
# print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义'

#!/usr/bin/python3
# a={'tom','jim','mary','tom','jack','rose'}
# print(a)
# if 'rose' in a:
#     print('rose在集合中')
# else :
#     print('rose 不在集合中')
# a=set('abracadabra')
# b=set('alacazam')
# print(a)
# print(a-b)


# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b



# age = float(input("请输入你家狗狗的年龄: "))
# print("")
# if age<0:
#     print("你是再逗我吧！")
# elif age==1:
#     print("相当于14岁的人")
# elif age==2:
#     print("相当于22岁的人")
# elif age>2:
#     human=22+(age-2)*5
#     print("相当于人类的年龄：",human)
# input("点击enter键退出")

# x=5
# y=9
# print(x==y)


#猜数字游戏
# number=7
# guess=1
# print("数字猜谜游戏")
# while guess != number:
#     guess=int(input("请输入你猜的数字："))
#
#     if guess==number:
#          print("恭喜你，猜对啦")
#     elif guess < number:
#          print("数字猜小啦")
#     elif guess > number:
#          print("数字猜大了")
# import os
# print(os.getcwd())


##爬取
# import requests
# import re
# class Qiushi(object):
#     def qingqiu(self,page):
#         url ='https://www.qiushibaike.com/text/page/{}/'.format(page)
        #发送请求
        # response = requests.get(url=url)
        #读取结果的方式   1义字符串的方式读取 2以字节码的方式读取
        # print(response.text)   #  字符串
#         html=response.content.decode('utf-8')   #字节码
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         patt = re.compile('<div class="p">(.*?)</div>', re.S)
#         items = patt.findall(abc)
#         for i in items:
#             i=i.replace('<span>','')
#             i=i.replace('</span>','')
#             i=i.replace('<br/>','')
#             i=i.strip()
#             shuju.append(i)
#         return shuju
#     def save(self,shuju):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i+'\n')
# qiushi = Qiushi()
# jieguo=qiushi.qingqiu(2)
# shuju=qiushi.guolv(jieguo)
# qiushi.save(shuju)



import re
import requests
class Pacong(object):
    def qingqiu(self,page):
        url='https://www.qiushibaike.com/text/page/{}/'.format(page)
        response=requests.get(url=url)
        html=response.content.decode('utf-8')
        # html=response.text####以字符串读取
        # print(html)
        # return qingqiu()
        return html

# Pacong().qingqiu(2)
    def guolv(self,asd):
        a=[]
        patt = re.compile(r'<div class="content">(.*?)</span>',re.S)
        items=patt.findall(asd)
        return items
    def baocun(self,x):
        f=open(r'a.txt','w',encoding='utf8')
        f.write('{}'.format(x))
        f.close()
a=Pacong()
q=a.qingqiu(2)
b=a.guolv(q)
# a.baocun(b)




