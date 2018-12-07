# 16:22:00
# 小仙女 2018/11/18 16:22:00
# import requests
# import re
# class Doutu(object):
#     def qingqiu(self,page):
#         #输入网址
#         url='https://www.doutula.com/article/list/?page={}'.format(page)
#         #模仿浏览器（反爬）
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#         response=requests.get(url=url,headers=head)   #发送请求
#         html=response.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         patt=re.compile(r'https://www.doutula.com/article/detail/[0-9]{7}')  #过滤的条件    第一次筛选
#         itmes=patt.findall(abc)    #筛选出来的内容
#
#         tupian=[]
#         for i in itmes:   #在第一次筛选的基础上
#             head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#             response= requests.get(url=i, headers=head)  #发送请求
#             html2= response.content.decode('utf-8')  #显示内容
#             patt1 = re.compile(r'<img src="https://(.*?)" alt')   #第二次筛选
#             itmes2=patt1.findall(html2)    #第二次筛选出来的内容
#             for j in itmes2:
#                 tupian.append(j)
#                 # print(tupian)
#         return tupian
#     #保存图片
#     def save(self,tupian):
#         for j,k in enumerate(tupian):
#             k = 'https://' + k
#             # print(k)
#             rese=requests.get(url=k)
#
#             html2=rese.content
#             with open(r'E:\图片\{}.jpg'.format(j),'wb') as f:
#                 f.write(html2)
# a=Doutu()
# b=a.qingqiu(2)
# c=a.guolv(b)
# a.save(c)

import requests

import re
class Doutu(object):
    def qingqiu(self,page):
        #输入网址
        url='https://www.doutula.com/article/list/?page={}'.format(page)
        #模仿浏览器（反爬）
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        response=requests.get(url=url,headers=head)   #发送请求
        html=response.content.decode('utf-8')
        return html
    def guolv(self,abc):
        patt=re.compile(r'https://www.doutula.com/article/detail/[0-9]{7}')  #过滤的条件    第一次筛选
        itmes=patt.findall(abc)    #筛选出来的内容

        tupian=[]
        for i in itmes:   #在第一次筛选的基础上
            head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
            response= requests.get(url=i, headers=head)  #发送请求
            html2= response.content.decode('utf-8')  #显示内容
            patt1 = re.compile(r'<img src="https://(.*?)" alt')   #第二次筛选
            itmes2=patt1.findall(html2)    #第二次筛选出来的内容
            for j in itmes2:
                tupian.append(j)
                # print(tupian)
        return tupian
    #保存图片
    def save(self,tupian):
        for j,k in enumerate(tupian):
            k = 'https://' + k
            # print(k)
            rese=requests.get(url=k)

            html2=rese.content
            with open(r'E:\图片\{}.jpg'.format(j),'wb') as f:
                f.write(html2)
a=Doutu()
b=a.qingqiu(2)
c=a.guolv(b)
a.save(c)

