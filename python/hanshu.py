# def a():
#     print('hfello')
# a()

# def a(wi,he):
# #     return w*h
# # def print_welcome(name):
# #     print("welcome",name)
# #
# # print_welcome('runoob')
# # w=4
# # h=5
# # print('wi=',w,'he=',h,a(w,h))

# a=['d','fe',3,'fe','x']
# print(a.index('x'))

# vec=[2,4,6]
# b=[3*x for x in vec]

# b=[3*y for y in vec if y > 3]


# vec1=[4,3,-9]
# b=[x*y for x in vec for y in vec1]

# print(b)

# import  random
# # print(random.randint(0,9))


# for i in range(1,10):
#     for j in range(1,i+1):
#         a='{}*{}=={}'.format(j,i,j*i)
#         print(a,'\t',end="")
#     print()
#函数
#一个简单的函数
# def hello():
#     print('hello world')
# hello()
##第二个简单的函数
# def 面积(height,width):
#     return width*height
# def print_welcome(name):
#     print('welcome',name)
# print_welcome('函数')
# w=4
# h=3
# print('width=',4,'height=',3,'面积=',面积(3,4))


#函数的传参()
######必须参数
# def jiujiu(x):
#     for i in range(1,x):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(i,j,i*j),end='\t')
#         print()
# jiujiu(8)

####默认参数
# def 质数之和(x=100):
#     sum=0
#     for i in range(2,x):
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             sum=sum+i
#     print(sum)
# 质数之和(10)


###可变长函数 #加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# def printinfo(*vartuple):
#     # "打印任何传入的参数"
#     print("输出: ")
#     # print(arg1)
#     print(vartuple)
#
#
# # 调用printinfo 函数
# printinfo(70, 60, 50)

###可变长函数 ###加了两个星号 ** 的参数会以字典的形式导入。
# def printinfo(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
#
#
# # 调用printinfo 函数
# printinfo(1, a=2, b=3)


###reture  作用1，将函数中的数值赋值给调用者  2，函数的结束标志函数   0

#冒泡函数
# def maopao(*a):
#     a=list(a)
#     # a=a.split()
#     b=len(a)
#     for i in range(b):
#         for j in range(i+1,b):
#             if int(a[i])>int(a[j]):
#              a[i],a[j]=a[j],a[i]
#     print(a)
# maopao(13,32,3.6233,121)

#选择排序法函数
# def xuanze(*a):
    # a=input('>>>')
    # b=a.split()
    # b=list(a)
    # c=len(b)
    # for i in range(c):
    #     for j in range(i+1,c):
    #         if int(b[j])>int(b[i]):
    #             b[i],b[j]=b[j],b[i]
    #     # print(b)
    # print(b[::-1])
# xuanze()
# xuanze(45,51,5,6)

##质数之和
# def  zhishu(a):
#     sum=0
#     for i in range(2,a):
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             sum=sum+i
#     print(sum)
# zhishu(10)

##阶乘函数
# def jiecheng(a):
#     sum=0
#     num=1
#     # b=input('请输入一个整数：')
#     # a=int(b)
#     for i in range(1,a+1):
#         num=num*i
#         sum=sum+num
#     print(sum)
# jiecheng(4)

##九九乘法表函数


##水仙花数
# def huashu():
#     for i in range(100,1000):
#         a=i//100
#         b=i%10
#         c=i//10%10
#         d=a**3+b**3+c**3
#         if d==i:
#         # print(a)
#             print(i)
# huashu()


##选商品
# def xuanshangpin(*a):
#     # a=['电脑','手机','ipad']
#     for i,j in enumerate(a):
#         print(i+1,j)
#     b=int(input('请输入商品号:'))
#     print(a[b - 1])
# xuanshangpin('电脑','手机','笔记本')

#平均值
# while True:
#     def pinjunzhi(*a):
#         # if a == 'exit':
#         #     break
#         a=list(a)
#         sum=0
#         b=len(a)
#         for i,j in enumerate(a):
#             sum=sum+int(a[i])
#         c=sum/b
#         print(c)
    # for x in range(b):
    #     if int(a[x]) < c:
    #         print(c)

# def pinjunzhi():
#     while True:
#         a=input('>>>')
#         b=a.split()
#         c=0;y=len(b)
#         d=0
#         x=''
#         if a=='exit':
#             break
#         for i,j in enumerate(b):
#             c=c+int(b[i])
#             d=d+1
#             e=c/d
#         print('平均值：',e)
#         for x in b:
#             if int(x)<e:
#                 print('小于品均值的：',x)
# pinjunzhi()


# def shiliu(a):
#     c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
#     b=''
#     while True:
#         x=a%16
#         a=a//16
#         b=b+c[x]
#         if a==0:
#             break
#     print(b[::-1])




####是否是回文
# def huiwen(*a):
#     #a=input('>>>')
#     b=a[::-1]
#     if a==b:
#         print('是回文')
#     else:
#         print('不是回文')
# huiwen('a','s',2,'s','a')




#######最大的放在前面，最小的放在后面。
# def zuida(*a):
#     a=list(a)
#     a.sort()
#     print(a[::-1])
#
# zuida(45,12,1,52,5,584,4,98594,12,52)

###1000内的一个数的因数和加起来等于本身的数
# def yinshu():
#     for i in range(2,1000):
#         sum = 0
#         for j in range(1,i):
#             if i % j == 0:
#                 sum=sum+j
#         if sum == i:
#             print(i)

####打印第一大第二大的数
# def fir(*a):
# #     a=list(a)
# #     a.sort()
# #     b=a.count(a[-1])
# #     # for i in range(b):
# #     print(a[-1],'\t最大的的个数：',b)
# #     # for j in range(1):
# #     print(a[-b-1])
# # fir(52,4,5,584,1,586,666,666,666,586,586)


##任意三个数字组成不同的数
# def renyi(*a):
#     # a=input('>>>')
#     # b=a.split()
#     b=list(a)
#     c=[]
#     for i in b:
#         for j in b:
#             for h in b:
#                 if (i != j) and (i != h) and (j != h):
#                     print(i,j,h)
#                     c.append(int(i)*100+int(j)*10+int(h))
#     print(c)
# a=[215,5,45]
#####爬虫
# import os
# # a=os.popen('ping 192.168.0.1')
# # print(a.read())
#
#
# # os.chdir(r'D:\程序')
#
# # os.mkdir(r'sun')
# # os.chdir(r'D:\程序\sun')
# #
# # print(os.getcwd())
#
# # print(os.listdir(r'D:\程序'))
# # print(os.path.split(r'D:\py.dem'))
#
import requests
# import re
# class Qiushi(object):
#     def qingqiu(self,page):
#         url ='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         #发送请求
#         response = requests.get(url=url)
#         #读取结果的方式   1义字符串的方式读取 2以字节码的方式读取
#         # print(response.text)   #  字符串
#         html=response.content.decode('utf-8')   #字节码
#         # print(html)
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         patt = re.compile('<div class="content">(.*?)</div>', re.S)
#         items = patt.findall(abc)
#         print(items)
#         for i in items:
#             i=i.replace('<span>','')
#             i=i.replace('</span>','')
#             i=i.replace('<br/>','')
#             i=i.strip()
#             shuju.append(i)
#         return shuju
#     def save(self,shuju):
#         with open('a.txt','w',encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i+'\n')
# qiushi = Qiushi()
# jieguo=qiushi.qingqiu(1)
# shuju=qiushi.guolv(jieguo)
# qiushi.save(shuju)


# import re
# a='qwe123qwe'
# b=re.compile('qwe.*?qwe')
# c=b.findall(a)
# print(c)


