# import sys;x='runoob';sys.stdout.write(x+'\n')

# counter=100 #整型变量
# miles =1000.0 #浮点型变量
# name="runoob"#字符串
# print(counter,'\n',miles,'\n',name)

# a,b,c=100,1000.0,'runoob'
# print(a,'\n',b,'\n',c)

# a,b,c,d,=20,5.5,True,4+3j
# # print(type(a),'\n',type(b),'\n',type(c),'\n',type(d))

# a='fdkfdshk'
# print(a[:6]) #显示字符串的前6个
# print(a[6:]) #显示字符串的从第7个开始到最后

# str = 'Runoob'
#
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + "TEST")  # 连接字符串

# list=['abcd',786,2.223,'runoob',70.2]
# a=[123,'runoob']
#
# print(list)     #输出完整列表
# print(list[0])  #输出列表第一个元素
# print(list[1:3]) #从第二个开始输出到第三个元素
# print(list[2:])  #输出从第三个元素开始的所有元素
# print(list+a) #链接列表
# print(a*2)    #输出两次列表


# tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
# a=(123,'runoob')
# print(tuple)        #输出完整的元组
# print(tuple[0])      #输出元组的第一个元素
# print(tuple[1:3])    #输出从第二个元素开始到第三个元素
# print(tuple[2:])     #输出从第三个元素开始的所有元素
# print(a*2)
# print(tuple+a)

# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(b)
#
# print(a - b)  # a和b的差集
#
# print(a | b)  # a和b的并集
#
# print(a & b)  # a和b的交集
#
# print(a ^ b)  # a和b中不同时存在的元


# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
#
# tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
#
# print(dict['one'])  # 输出键为 'one' 的值
# print(dict[2])  # 输出键为 2 的值
# print(tinydict)  # 输出完整的字典
# print(tinydict.keys())  # 输出所有键

#字典
# tinydict = {'name': 'runoob','code':1,'site': 'www.runoob.com'}
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值

#bug
# a=input('请输入（空格分开）：')
# b=a.split(',')
# b[0]=int(b[0])
# b[1]=int(b[1])
# b[2]=int(b[2])
# b.sort()
# if a1+a2>a3:
#     print(a1,a2,a3)
#     if a1**2+a2**2==a3**2:
#         print('直角')
#     elif a1**2+a2**2<a3**2:
#         print('钝角')
#     else:
#         print('锐角')
# else:
#     print('不能构成三角形')

# a='hello %s,我今年%d岁'
# print(a%('小红',23.2))
#
#
# a=[2,[12,54,45],8,5]
# import copy
# b=copy.deepcopy(a)
# print()




#List列表
  #可变的； 支持索引和切片；

# a=[312,'sa',456]
# print(a[1][1])

####list列表中的函数
# a=[2,'qwe',2,5]

# a.append(元素)  #将括号内的元素添加到列表a中
# print(a)

# a.remove(元素)      #删除列表a中的元素
# print(a)

# a.pop(2)      #删除下标号所在的元素
# print(a)

# a.insert(下标号，元素)  #第一个是下标的位置，第2个市添加的元素
# print(a)

#变量=变量.count(元素) 统计该元素在列表中的个数
# print(a.count(5))
# b=a.count(2)
# print(b)

#变量=变量.index(元素)获取元素的下标值
# print(a.index(2))
# # b=a.index(5)
# # print(b)

#变量.reverse() 反转列表
# a.reverse()
# print(a)

#变量.sort()  排序   默认是升序，数据类型必须一致
# a=[456,312,4768,123]
# a.sort()
# print(a)

# a.sort(reverse=True)#倒序排列
# print(a)



###元组tuple
          ##以小括号标识，逗号隔开
          ##不可变；支持索引和切片
          ##只有一
######元组只有一个元素时后面必须加，

# b=(123)
# print(a.count(123)) #计算在元组的个数
# print(a.index(123))   #获取某元素在元组中的下标位置




# a = [123,14543,[1234,45],43]
# b=a.copy()
# a[2].append(2)
# print(a)
# print(b)




#字符串
# a=True
# print(a)

# ad='abAaKJkf'
# print(ad.upper())   #将小写转化成大写

# print(ad.lower())   #将大写转化成小写

#print(ad.capitalize()) #将字符串中的首字母大写

#print(ad.swapcase())     #将字符串中大写变小写，小写变大写

#print(ad.lstrip())     #去掉字符串左边的空格  #

#print(ad.lstrip())         #去掉字符串中右边的空格

#print(ad.strip())       #去掉字符串中两边的空格

# b=ad.startswith('a')     #判断‘s'是否是变量中的元素的开始
# print(b)

# b=ad.endswith('f')         #判断‘f'是否是变量中的元素结尾
# print(b)




###字典
# a={'name':'小明','age':20,'sex':"男"}
# b={'wer':'12'}

# a.update(b)         #将字典中的b的所有元素更新到a中
# print(a)

# a['key']='value'       #添加键值对到字典a中
# print(a)

# a.pop('name')      #删除key所在的键值对
# print(a)

# a.popitem()        #默认删除最后一个键值对，因为无序的所以相当于随机删除的
# print(a)

# b=a.keys()        #获取所有的key
# print(b)

# c=a.items()     #获取所有的键值对
# print(c)

# d=a.values()     #获取所有的值
# print(d)

# a['name']='123'   #更改键的值
# print(a)






#####set 集合
     ###大括号来标识    以逗号隔开

# a={1,2,456,5}

# a.add('ewerewet')   #添加一个元素但不能添加列表，能添加元组
# print(a)

# a.pop()            #删除一个元素默认删除最后一个，因为无序所以相当于随机删除
# print(a)

# a.remove(456)       #删除集合中的元素
# print(a)


# a=input('输入成绩：')
# a=int(a)
# if 90<a and a<=100:
#     print('优秀')
# elif 80<a and a<=90:
#     print('良好')
# elif 70<a and a<=80:
#     print('良')
# elif 60<=a and a<=70:
#     print('及格')
# elif 0<=a and a<60:
#     print('不及格')
# else:
#     print('输入不合法')

# sum=0
# for i in range(101):
#     sum=sum+i
# print(sum)


# sum=0
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# for i in range(10):
#     print(i)
#     continue
# else:
#     print('123').



# for i in range(1,10):
#     for j in range(1,i+1):
#         '%d*%d'== j*i "\t"
#         b=a%(j,i)
#     '\n'
# print(b)



# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(j,i,j*i),end='')
#         # b=a.format(j,i)
#     print()


# sum=0
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         sum=sum+i
# print(sum)
#



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
#     c=0
#     d=0
#     x=''
#     if a=='exit':
#         break
#     for i,j in enumerate(b):
#         c=c+int(b[i])
#         d=d+1
#         e=c/d
#     print('平均值：',e)


# a=[223,432,213,645,2321]
# # b=a.index(max(a))
# # c=a.index(min(a))
# # a[b],a[0]=a[0],a[b]
# # a[c],a[-1]=a[-1],a[c]
# # print(a)
# #
# # a=[12,32,11,43,23,67]
# # b=a.copy()
# # b.sort()
# # c=a.index(b[0])
# # d=a.index(b[-1])
# # a[d],a[0]=a[0],a[d]
# # a[c],a[-1]=a[-1],a[c]
# # print(a)



##去重排序法
# a=input('请输入一组数：')
# b=a.split()
# for i,j in enumerate(b):
#     for x,y in enumerate(b):
#         if int(b[i])==int(b[x]):
#             c=b.pop(i)
#             print(c)

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
# while True:
#     x=a%16
#     a=a//16
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

# def zifu(a):
# # a=input('请输入：')
#     for i,j in enumerate(a):
#         for x in range(0,10):
#             if a[i]==str(x):
#                 print(x,end="")
#         if j==str(' '):
#             print('\t',end='')
#             print(type(x))
# zifu('124')

# if __name__ == '__main__':  # 判断执行的文件是否是本文件
#     print('hello')


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
#                 # print(i,j,h)
#                 c.append(int(i)*100+int(j)*10+int(h))
#             print(c)
#


# import os
# import pymysql
# asjk=pymysql.connect(host='192.168.0.53',port=3306,user='root',password ='123456')
# sjk=asjk.cursor()
# sjk.execute('use python;')
# # b=['num','name','sex','age','bri']
# for i in range(11,16):
#     sjk.execute('drop table stu{};'.format(i))
# print(sjk.fetchall())
# b=bsjk.fetchall()
# for i,j in enumerate(b):
#     c=b[i]
#     for x in range(1):
#         print(c[x])


import re
import requests
class Qiushi():
    def qingqiu(self,page):
        url ='https://www.qiushibaike.com/text/page/{}/'.format(page)
        #发送请求
        response = requests.get(url=url)
        #读取结果的方式   1义字符串的方式读取 2以字节码的方式读取
        # print(response.text)   #  字符串
        html=response.content.decode('utf-8')   #字节码
        return html
# Qiushi().qingqiu(2)
    def guolv(self):
        shuju=[]
        patt=re.compile('<div class="content"> ()')