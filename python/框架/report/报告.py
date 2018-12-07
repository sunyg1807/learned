
import unittest
import time
import 框架.report.HTMLTestRunnertest
import 框架.test.test_学校
a=框架.report.HTMLTestRunnertest

def 好分数():
    c=框架.test.test_学校
    # c.学校()
    suit=unittest.TestSuite()
                            # 添加测试用例  将测试用例添加到测试套件中
                            # suit.addTest(学校('test_1'))
                            # suit.addTest(学校('test_2'))
    suit.addTest(unittest.makeSuite(c.学校))
    now = time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f = open('abc.html','wb')
    runner = a.HTMLTestRunnertest.HTMLTestRunner(tester='孙永歌',
                                               description='测试结果如下',
                                               title='好分数测试报告',
                                               stream=f)
    runner.run(suit)
    f.close()
    # return runner.run(suit)
# 好分数()