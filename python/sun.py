# a=input('请输入（空格分开）：')
# b=a.split()
# b.sort()
# print(b)




#第一个python函数
# def hello() :
#    print("Hello World!")
#
# hello()


# 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值: ", mylist)
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist)

# def printme('ds'):
#     "打印任何传入的字符串"
#     print('ds')
#     return
#
#
# # 调用printme函数
# printme()


# def inter(no,sex):
#     print('编号：',no)
#     print('性别：',sex)
#     return
# inter('男',2016211418)


# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     # print(arg1)
#     for var in vartuple:
#         print(var)
#     return


# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)
#


# 可写函数说明
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
#
#
# # 调用printinfo 函数
# printinfo(70, 60, 50)


# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
#
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)


# def printinfo(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
#
#
# # 调用printinfo 函数
# def printinfo(b, a=2):
#     print('姓名：',b)
#     print(a)
#     return
# printinfo(10,12)

# for i in range(4):
#     print(i)
#     if i ==2 :
#         break
# else:
#     print('231')

# b=int(input('<<<<'))
# a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# f=''
# while True:
#     c=b%16
#     b=b//16
#     f+=a[c]
#     if b==0:
#         break
# print(f[::-1])


# sum1=0
# sum2=0
# for i in range(1,100,2):
#     sum1=sum1+i
# for j in range(2,100,2):
#     sum2=sum2+j
# sum=sum1-sum2
# print(sum)

# a='fa'
# for i,j in enumerate(a):
#     print(j)


# import random
# a=random.randrange(1,10)
# print(a)



# a=int(input('请输入：'))
# print(a)
# g=a.split()
# b=max(a)
# c=min(a)
# x=a.count(b)
# import 脚本
# # 脚本.maopao(21,23,5,2,52)


# for i in range(30):
#     f=open(r'b.txt','a',encoding='utf-8')
#     print(f.write('博文智生\n'))
# # f.write('追加三十行\n')
#     f.close()

# f=open(r'b.txt','r',encoding='utf-8')
# # print(f.read())
# # f.close()
# f=open(r'c.txt','w',encoding='utf-8')
# f.write('金明校区')
# f.close()


# def huashu():
#     for i in range(100,1000):
#         a=i//100
#         b=i%10
#         c=i//10%10
#         d=a**3+b**3+c**3
#         if d==i:
#         # print(a)
#             print(i)
#             return i
# # huashu()
# a=huashu()
# print(a)

####################################################################################################
##质素之和
# sum = 0
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         sum=sum+i
# print(sum)

##阶乘之和
# sum1=1;sum2=0
# for i in range(1,5):
#     sum1=sum1*i
#     sum2=sum2+sum1
# print(sum2)

###判断是否为三角形
# a=input('请输入三角形三边(以空格为分隔符)：')
# a=a.split(' ')
# a[0]=int(a[0])
# a[1]=int(a[1])
# a[2]=int(a[2])
# a.sort()
# # print(a)
# if a[0] + a[1]> a[2] :
#    if  a[0]**2+a[1]**2 == a[2]**2:
#        print('直角三角形')
#    elif a[0]**2+a[1]**2 >a[2]**2:
#        print('钝角三角形')
#    elif a[0]**2+a[1]**2 < a[2]**2:
#        print('锐角三角形')
# else:
#     print('不能构成三角形')


#####去重排序
# a=input("请输入：")
# a=a.split(',')
# b=len(a)
# # print(a,b)
# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# print(c)

#####判断对否是回文
# a=input("请输入（判断是否为回文）：")
# b=a[::-1]
# if a == b :
#     print("是回文")
# else:
#     print("不是回文")

#####选择排序
# a=input("请输入（以空格为分割）：")
# b=a.split(' ')
# # b=[5,6,2,3,4]
# c=len(b)
# for i in range(c):
#     for j in range(i+1,c):
#         if int(b[j]) > int(b[i]):
#             b[i],b[j]=b[j],b[i]
# print(b[::-1])


###三次猜数字
# import  random
# a=random.randrange(2,8)
# c = 0
# while True:
#     c = c + 1
#     b=input("请输入：")
#     b=int(b)
#     if a==b:
#         print("恭喜你回答正确")
#         break
#     if a > b :
#         print("小了")
#     if a<b:
#         print("大了")
#     if c== 1:
#         print('2ci')
#     if c==2:
#         print('1ci')
#     if c==3:
#         print('cai')
#         break
#

####水仙花数
# for i in range(100,1000):
#     a=i%10
#     b=i//100
#     c=i//10%10
#     d=a**3+b**3+c**3
#     if i == d:
#         print(i)


###打印列表中第一大和二大的数

# a=input('请输入(以空格为分隔符)：')
# b=a.split(' ')
# len(b)
# for i,j in enumerate(b):
#     b[i]=int(b[i])
# b.sort()
# c=max(b)
# d=b.count(c)
# if b[-1] == b[-(d+1)]:
#     print(b[-1])
# else :
#     print(b[-1],b[-(d+1)])

##不用int将字符串变成整数类型
# a=input('请输入：')
# for i in a:
#     for j in range(10):
#         if int(i)==j:
#             print(j,end='')

######################################任意4个数字，组成不相同的三位数
# a=input("输入连续4位数字：")
# b=a.split()
# c=[]
# for i in b:
#     for j in b:
#         for x in b:
#             if (i!=j) and (j!=x) and (i!=x):
#                 print(i,j,x)
#                 c.append(int(i)*100+int(j)*10+int(x))
# print(c)
# print(len(c))

###########
# a=["电脑","计算机","mp3"]
# for  i,j  in  enumerate(a):
#      print(i+1,j)
# b=int(input("请输入商品编号"))
# print(a[b-1])

# #一个有顺序的列表，随机加入一个数，加入的数在正确位置
# a=int(input('请输入一个数'))
# b=[2,3,4,8]
# for i in b:
#     if a>i:
#         b.append(a)
#         b.sort()
#         break
# print(b)
#

#####
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

########
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}+{}={}'.format(i,j,i*j),'\t',end='')
#     print()
#










# def cha():
#     f= open(r'F:\python\wenjia\b.txt','r',encoding='utf8')
#     a=f.readlines()
#     print(len(a))
# cha()
####################################
##str 字符串
# #把小写变成大写
# a='asd';b=a.upper();print(b)
# #把字符串中所有的大写变成小写
# a='FGhj';b=a.lower();print(b)
# #把字符串中首字母小写换成大写
# a='ghjklDD';b=a.capitalize();print(b)
# #把字符串中的字母大写变成小写，小写变成大写
# a='hjkJUiJk';b=a.swapcase();print(b)
# #将前一个字符替换为后一个字符
# a='ASDFAghAgja45S546hd';b=a.replace('M','A');print(b)
###判断字符串是否为startswitch()括号中的元素开始i

# a='hello %s,我今年%d';b=a%('小红',23);print(b)

###################
# a=[2,'qwer',5,2]
# # a.append(3)
#
# a.insert(3,4)
# print(a)