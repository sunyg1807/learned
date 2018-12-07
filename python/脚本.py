###质数之和
# sum=0
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         sum=sum+i
# print(sum)


####阶乘之和
# sum=0
# num=1
# b=input('请输入一个整数：')
# a=int(b)
# for i in range(1,a+1):
#     num=num*i
#     sum=sum+num
# print(sum)



###九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()

###质数之和
# sum=0
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         sum=sum+i
# print(sum)


###水仙花数
# for i in range(100,1000):
# #     a=i//100
# #     b=i%10
# #     c=i//10%10
# #     d=a**3+b**3+c**3
# #     if d==i:
# #         # print(a)
# #         print(i)

##用编号选商品
# a=['电脑','手机','ipad']
# for i,j in enumerate(a):
#     print(i+1,j)
# b=int(input('请输入商品号:'))
# print(a[b-1])

#判断三角形
# a=input('请输入三边长（空格为分割）：')
# b=a.split()
# b[0]=int(b[0])
# b[1]=int(b[1])
# b[2]=int(b[2])
# b.sort()
# # print(type(b),b)
# a1=b[0]
# a2=b[1]
# a3=b[2]
# # print(a1,a2,a3)
# if a1+a2>a3:
#     if a1**2 + a2**2 == a3**2:
#         print('直角三角形')
#     elif a1**2+a2**2<a3**2 :
#         print('钝角三角形')
#     else :
#  print('锐角三角形')

##冒泡排序法
# a=input('>>>')
# c=a.split()
# b=len(c)
# print(b)
# for i in range(0,b):
#     for j in range(1,i+1):
#         if int(c[i])>int(c[j]):
#             c[i],c[j]=c[j],c[i]
#             # print(a[::])
# print(c)


#选择排序法
# a=input('>>>')
# b=a.split()
# c=len(b)
# for i in range(c):
#     for j in range(i+1,c):
#         if int(b[j])>int(b[i]):
#             b[i],b[j]=b[j],b[i]
#         print(b)
# print(b[::-1])



###一组数字，求平均值并且打印出比平均值小的数字，输入exit退出
# while True:
#     a=input('>>>')
#     b=a.split()
#     c=0;y=len(b)
#     d=0
#     x=''
#     if a=='exit':
#         break
#     for i,j in enumerate(b):
#         c=c+int(b[i])
#         d=d+1
#         e=c/d
#     print('平均值：',e)
#     for x in b:
#         if int(x)<e:
#             print('小于品均值的：',x)


# a=[223,432,213,645,2321]
# b=a.index(max(a))
# c=a.index(min(a))
# a[b],a[0]=a[0],a[b]
# a[c],a[-1]=a[-1],a[c]
# print(a)
#
# a=[12,32,11,43,23,67]
# b=a.copy()
# b.sort()
# c=a.index(b[0])
# d=a.index(b[-1])
# a[d],a[0]=a[0],a[d]
# a[c],a[-1]=a[-1],a[c]
# print(a)



##去重排序法
# a=input('请输入一组数：')
# b=a.split()
# c=len(b)
# for i,j in enumerate(b):
#     # for x,y in enumerate(b):
#     if int(b[i])==int(b[i+1]):
#         c=b.pop(i)
#         print(c)

# a=input('请输入一组数:')
# b =a.split()
# # print(type(a))
# c=[]
# for i in b:
#     if i not in c:
#         c.append(i)
# print(c)



##十进制转十六进制
# a=int(input('输入数字：'))
# c=hex(a)
# print(c)



# a=int(input('输入数字：'))
# c=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b=''
# while True
#     a=a//16:
#     x=a%16
#     b+=c[x]
#     if a==0:
#         break
# print(b[::-1])


###字符串变成数字
# a=input('请输入数字：')
# a=a.split()
# for i in a:
#     print(i)
# print(type(i))


# a=input('请输入：')
# for i,j in enumerate(a):
#     for x in range(0,10):
#         if a[i]==str(x):
#             print(x,end="")
#     if j==str(' '):
#             print('\t',end='')
#             print(type(x))


# a=input('<<<')
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for h in range(10):
#         if str(h)==j:
#             s+=h*10**i
# print(s)
# print(type(s))



##三次猜数字
# import random
# a=random.randrange(2,8)
# c=0
# while True:
#     c=c+1
#     b=input('三次猜从2到8的数字:')
#     b=int(b)
#     if a==b:
#         print('恭喜，猜对啦')
#         break
#     if a<b:
#         print('大了')
#     if a>b:
#         print('小了')
#     if c==1:
#         print('还有2次机会')
#     if c==2:
#         print('还剩一次机会')
#     if c==3:
#         print('笨')
#         break


# import random
# a=random.randrange(1,10)
# for i in range(1,4):
#     c=3-i
#     b=int(input('三次猜数字，请输入一个1到9的数字：'))
#     if a==b:
#         print('恭喜你，答对啦')
#         break
#     elif a<b:
#         print('大了')
#         print('还有{}次机会'.format(c))
#     elif a>b:
#         print('小了')
#         print('还有{}次机会'.format(c))
#     elif c==0:
#         print('ben')
#         break

##判断是否为回文字符串

# a=input('请输入：')
# b=a[::-1]
# if a == b:
#     print('是回文字符串')
# else:
#     print('不是回文字符串')

# a=input('请输入：')
# b=len(a)
# c=b//2
# for i in range(c):
#     if a[i] != a[-i-1]:
#         print('不是')
#         break
# else:
#     print('是的')

#把最大的放在前面，最小的放在后面
#bug
# a=input('请输入：')
# a=a.split()
# b=max(a)
# c=min(a)
# x=a.count(b)
# y=a.count(c)
# # print(type(a),a,y,x)
# if x==1:
#     a[0]=b
# else:
#     for i in range(x):
#         a[i]=b
# if y==1:
#     a[-1]=c
# else:
#     for j in range(y):
#         a[-j-1]=c
# print(a)


# a=input('输入一组数字：')
# a=a.split()
# d=len(a)
# b=[]
# for i in range(d) :
#     c=int(a[i])
#     b.append(c)
# b.sort(reverse=True)
# print(b)

##1000内一个数的因数之和加起来等于本身的数

# for i in range (1,1000):
#     sum=0
#     for j in range(1,i):
#         if i % j == 0 :
#             sum=j+sum
#     if sum==i:
#         print(sum)


#打印最大的和第二个大的数字：（注意：可以有多个最大的）
# a=[5000,3,51000,51000,51000,5000]
# a.sort()
# d=a.count(a[-1])
# f=a.count(a[-d-1])
# for i in range(0,d):
#     print(a[-1])
# for i in range(0,f):
#     print(a[-d-1])


#打印任意四个数字组成不同的三位数


# a=input('>>>')
# b=a.split()
# c=[]
# for i in b:
#     for j in b:
#         for h in b:
#             if (i != j) and (i != h) and (j != h):
#                 print(i,j,h)
#                 c.append(int(i)*100+int(j)*10+int(h))
# print(c)

# while 循环


# 函数  是具有某种功能、可重复使用的代码块
# def 函数名():
#     i = 0
#     sum=0
#     while i<100:
#         print('rtewt')
#
# 函数名()  # 调用
# def maopao(*a):
#     a=list(a)
#     # a=a.split()
#     b=len(a)
#     for i in range(b):
#         for j in range(i+1,b):
#             if int(a[i])>int(a[j]):
#              a[i],a[j]=a[j],a[i]
#     print(a)
# maopao(121,456,789)

# 1.必须参数   2.默认参数  3.可变长参数 *  **
# # def asd(a):
# #     print(a)
# # #
# asd(a=78)

# import os
# import pymysql
# asjk=pymysql.connect(host='192.168.0.29',port=3306,user='root',password ='123456')
# bsjk=asjk.cursor()
# bsjk.execute('use test;')
# # b=['num','name','sex','age','bri']
# bsjk.execute('desc stu;')
# b=bsjk.fetchall()
# for i,j in enumerate(b):
#     c=b[i]
#     for x in range(1):
#         print(c[x])








