##接口测试：发送请求，验证响应是否符合需求的过程。
##postman\jmter


##python代码测试接口

##requests 发送http请求    assert断言处理


# import requests
# import json
# import unittest###unittest：是python自带单元测试自动化测试框架
#unittest.TestCase:用来做用例管理的，主要管理测试用例的
#unittest.TestSuit：测试套件,将多个测试用例集合在一起
#unittest.TestLoader:测试载入：将测试用例加载到测试套件中
#unittest.TestRunner：执行测试用例
##检验返回的结果的方法俗称断言


# class xuexiao():
#         def test_1(self):
#             url='http://testsupport-be.haofenshu.com/v1/schools/infos'
#             querystring = {"filterInput":"北京"}
#             headers = {'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#             response = requests.get(url=url,headers=headers,params=querystring)
#             html=response.json()
#             print(html['msg'])
#             # json.loads()
#             assert html['code']==0  ##断言 是否与预期结果字段值相等
# a=xuexiao()
# a.test_1()



        # def test_xue():
# class 学校(unittest.TestCase):
#     def setUp(self):    #setUp作用：初始化测试环境,保证每一个用例都在相同环境下执行；  是在每次执行测试用例之前执行
#         print(123)
#     def tearDown(self):  #tearDown作用：清理环境的；  每一次用例执行之后再去执行
#         print(456)
#     def test_3(self):   ###这个函数就是用例；函数名必须以test开头
#         print('a')
#     def test_2(self):
#         print('b')
# unittest.main()###main:会自动获取用例中的test之后执行顺序是：按照test后面第一个字符在ASCII从小到大执行


# import requests
# import unittest
# import HTMLTestRunne
# import HTMLTestRunnertest
# import time
# import  xlrd

# import requests
# import unittest
# class Cesi(unittest.TestCase):
#     # def setUp(self,):
#     #     url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#     def test_one(self,abc):
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         querystring = {"filterInput": "北京"}
#         headers = {'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#         response = requests.get(url=url,headers=headers,params=querystring)
#         html=response.json()
#         assert abc['code'] == 0
# unittest.main()
# import  unittest
# class 学校(unittest.TestCase):
    # def setUp(self):    #setUp作用：初始化测试环境,保证每一个用例都在相同环境下执行；  是在每次执行测试用例之前执行
    #     print(123)
    # def tearDown(self):  #tearDown作用：清理环境的；  每一次用例执行之后再去执行
    #     print(456)
#     def test_3(self):   ###这个函数就是用例；函数名必须以test开头
#         self.assertEqual('a','a1')
#     def test_2(self):
#         self.assertNotEqual('a','b')
# unittest.main()###m








####接口测试


# class Ces():
#     def test_on(self,a):
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         querystring = {"filterInput": "{}".format(a)}
#         headers = {'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#         response = requests.get(url=url,headers=headers,params=querystring)
#         html=response.json()
#         return  html
# class Aa(unittest.TestCase):
#     def test_one(self):
#         html=Ces().test_on('北京')
#         self.assertEqual(html['code'],0)
#         self.assertEqual(html['data'][0]['schoolName'],'北京七中')
#     def test_two(self):
#         html=Ces().test_on('abc')
#         self.assertNotEqual(html['code'],0)


# if __name__ == '__main__':
# unittest.main()

#生成测试报告 先创建一个测试套件
# suit=unittest.TestSuite()
#添加测试用例  将测试用例添加到测试套件中
# suit.addTest(Aa('test_one'))
# suit.addTest(Aa('test_two'))

# suit.addTest(unittest.makeSuite(Aa))##将整个类中所有的测试添加到测试套件中
# now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
# f=open('abcde.html','wb')
# runner=HTMLTestRunnertest.HTMLTestRunner(tester='孙永歌',
#                                          description='测试结果如下：',
#                                          title='好分数报告',
#                                          stream=f,)
# runner.run(suit)
# f.close()



import requests
import unittest
import HTMLTestRunne
import 框架.report.HTMLTestRunnertest
import time
import  xlrd
k=框架.report.HTMLTestRunnertest
# class Aa(unittest.TestCase):
#     def tes_shuju(selt):
#         shuju = []
#         f= xlrd.open_workbook('ceshi1.xls')
#         sheet = f.sheets()[0]
#         num=sheet.nrows
#         for i in range(1,num):
#             aaa = sheet.row_values(i)
#             shuju.append(aaa)   ###shuju=['北京', 0.0, 800.0]
#         return shuju
# a=Aa().tes_shuju()
# print(a)
#     def test_on(self,a):
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         querystring = {"filterInput": "{}".format(a)}
#         headers = {'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#         response = requests.get(url=url,headers=headers,params=querystring)
#         html=response.json()
#         return  html
# a=Aa().test_on('北京')
# print(a)
#     def test_one(self):
#         shuju=self.tes_shuju()
#         html=self.test_on(shuju[0][0])
#         self.assertEqual(html['code'],shuju[0][1])
#         self.assertIn(len(html['data']),range(shuju[0][2]))
#     def test_two(self):
#         shuju=self.tes_shuju()
#         html=self.test_on(shuju[1][0])
#         self.assertNotEqual(html['code'],shuju[1][1])
#         self.assertEqual(len(html['data']),int(shuju[1][2]))
        # self.assertEqual(len(html['data']), int(shuju[2][2]))
#     def test_3(self):
#         shuju=self.tes_shuju()
#         html=self.test_on(shuju[2])
#         self.assertEqual(html['code'],int(shuju[2][1]))
#         self.assertEqual(len(html['data']),int(shuju[2][2]))
#
# unittest.main()
# suit=unittest.TestSuite()
# suit.addTest(unittest.makeSuite(Aa))
# f=open('abcd.html','wb')
# runner=HTMLTestRunnertest.HTMLTestRunner(tester='孙永歌',
#                                          description='测试结果如下：',
#                                          title='好分数报告',
#                                          stream=f,)
# runner.run(suit)
# f.close()


########################################################

 # def tes_shuju(selt):
 #     shuju=[]
 #     f= xlrd.open_workbook('ceshi.xlsx')
 #     sheet=f.sheets(0)
 #     num=sheet.nrows
 #     for i in range(1,num):
 #         aaa=sheet.row_valu
 #         shuju.append(aaa)
 #         return  aaa

##########################################################







class 学校(unittest.TestCase):
    def tes_数据(self):
        shuju = []
        f = xlrd.open_workbook('ceshi1.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1,num):
            aaa= sheet.row_values(i)
            shuju.append(aaa)
        return shuju
    def tess(self,a):
        url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
        canshu = {"filterInput":"{}".format(a)}
        headers = {'Cookie':"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
        response = requests.get(url=url,headers=headers,params=canshu)
        aaaa = response.json()
        return aaaa
    def test_1(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[0][0])
                                #         print(html)
                                # 学校().test_1()
        self.assertEqual(html['code'],shuju[0][1])
        self.assertIn(len(html['data']),range(int(shuju[0][2])))
    def test_2(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[1][0])
        self.assertEqual(html['code'],int(shuju[1][1]))
        self.assertEqual(len(html['data']),int(shuju[1][2]))
    def test_3(self):
        shuju = self.tes_数据()
        html = self.tess(shuju[2][0])
        self.assertEqual(html['code'],int(shuju[2][1]))
        self.assertEqual(len(html['data']),int(shuju[2][2]))
    # def test_4(self):
    #     shuju = self.tes_数据()
    #     html = self.tess(shuju[3][0])
    #     self.assertEqual(html['code'],int(shuju[3][1]))
        # self.assertEqual(len(html['data']),int(shuju[3][2])
suit=unittest.TestSuite()
                        # 添加测试用例  将测试用例添加到测试套件中
                        # suit.addTest(学校('test_1'))
                        # suit.addTest(学校('test_2'))
suit.addTest(unittest.makeSuite(学校))
now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
f = open('abc.html','wb')
runner = k.HTMLTestRunnertest.HTMLTestRunner(tester='孙永歌',
                                           description='测试结果如下',
                                           title='好分数测试报告',
                                           stream=f)
runner.run(suit)
f.close()












##################################################################################
# class 学校(unittest.TestCase):
#     def tes_数据(self):
#         shuju = []              #创建一个空列表  用来接收表格数据
#         f = xlrd.open_workbook('ceshi1.xls')    #打开存储数据的表格
#         sheet = f.sheets()[0]      #索引获取标签页
#         num = sheet.nrows          #统计多少行
#         for i in range(1,num):
#             aaa= sheet.row_values(i)     #循环获取没行内容
#             shuju.append(aaa)        #把获取的内容添加到空列表中
#         return shuju               #把所的数据用return 返还到变量
#     def tess(self,m):
#         url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
#         canshu = {"filterInput":"{}".format(m)}
#         headers = {'Cookie':"yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA"}
#         response = requests.get(url=url,headers=headers,params=canshu)
#         aaaa = response.json()
#         return aaaa
#     def test_1(self):
#         shuju = self.tes_数据()
#         html = self.tess(shuju[0][0])     #使用数据中的第一个变量的参数
#         self.assertEqual(html['code'],shuju[0][1])    #使用数据中第一个变量的第一个预期结果
#         self.assertIn(len(html['data']),range(int(shuju[0][2])))   #使用数据中第一个变量的第二个预期结果
#     def test_2(self):
#         shuju = self.tes_数据()
#         html = self.tess(shuju[1][0])    #使用数据中的第二个变量的参数
#         self.assertEqual(html['code'],shuju[1][1])     #使用数据中第二个变量的第一个预期结果
#         self.assertEqual(len(html['data']),int(shuju[1][2]))    #使用数据中第二个变量的第二个预期结果
#     def test_3(self):
#         shuju = self.tes_数据()
#         html = self.tess(shuju[2][0])     #使用数据中的第三个变量的参数
#         self.assertEqual(html['code'],shuju[2][1])    #使用数据中第三个变量的第一个预期结果
#         self.assertEqual(len(html['data'],int(shuju[2][2])))    #使用数据中第三个变量的第二个预期结果
#     def test_4(self):
#         shuju = self.tes_数据()
#         html = self.tess(shuju[3][0])    #使用数据中的第四个变量的参数
#         self.assertEqual(html['code'],shuju[3][1])   #使用数据中第四个变量的第一个预期结果
#         self.assertEqual(len(html['data'],int(shuju[3][2])))   #使用数据中第四个变量的第二个预期结果
