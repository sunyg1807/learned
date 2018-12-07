# f = open(r'F:\damo\fda.txt','rw',encoding='utf-8')
# f=open('a.txt','a',encoding='utf-8')
# f.write("i'm good")
# f.seek(0)
# print(f.read())
# import  os
# print(os.getcwd())

# f=open('a.txt','w',encoding='utf-8')
# f.write('写一个文件\n不知道内容些什么啦\n随便写点中文')
# f.flush()
# f.close()
# name=['tom\n','jim','danny','jieny']
# f.writelines(name)
# f.flush()
# f.close()

# while True:
#     f=open('course.txt',encoding='utf-8')
#     print(f.readline())


# with open(r'F:\\python\a.txt',encoding='utf8') as f:
#     for i in f:
#         print(i)

# a=open(r'F:\\python\a.txt','a',encoding='utf-8')
# a.write('追加东西\n校园歌手大赛\n')
# a.close()
# f=open(r'F:\\python\a.txt',encoding='utf8')
# f.flush()
# print(f.read())




##一字节码的方式读写追加（图片，音频，视频等都是一字节码的方式读写的，下面是的图片的例题）
# f=open(r'F:\python\a.png','rb')
# # a=f.read()
# # w=open(r'F:\python\b.png','wb')
# # w.write(a)


# a='3'
# b='4'
# try :
#     a,b=int(a),int(b)
# except :
#     print('类型错误')
# print(a+b)

# a='3'
# b=4
# try:错')
# # except:
# #     print('cu
#     print('出owu')
# print(a+b)




# f=open(r'./wenjia/a.txt','r',encoding='utf-8')
# print(f.read())
# f.close()
''

# f=open(r'.\wenjia/b.txt','a+',encoding='utf8')
# print(f.write('新追加文字'))
# print(f.read())
# f.close()
#
# def jiujiu():
# f = open(r'./wenjia/c.txt', 'w', encoding='utf8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write('{}*{}={} {}'.format(i, j, i * j,'\t'))
#     f.write('\n')
# f.close




# import pymysql

# f=open(r'./wenjia/k.txt','w',encoding='utf8')
# a=f.write()
# f.close()

# import  pysql
# msjk=pymysql.connect(host='192.168.0.58',port=3306,encoding='utf8')
# msjk=msjk.cursor()
# msjk.execute("show databases;")
# print(msjk.fetchall())


# msjk=pymysql.connect(host='192.168.0.18',port=3306,user='root',password='123456')
# msjk=msjk.cursor()
# msjk.execute('use test;')
# msjk.execute('desc stu;')
# a=msjk.fetchall()
# print(a)
# for i,j in enumerate(a):
#     a=a[i]
#     print(a)
    # for x,y in enumerate(a):
    #    print(a[x])
# print(a)


###输入文件名 统计多少行，去掉空行和注释行。
# def wenjia(a):
#     with open('{}'.format(a),'r',encoding="utf-8") as f:
#         a=f.readlines()
#         b=len(a)
#     for i in a:
#         if i=='\n':
#             b-=1
#         elif i[0]== '#':
#             b-=1
#     print(b)
# wenjia('a.txt')


