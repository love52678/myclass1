# -*- coding:utf-8 -*-
# coding=utf-8
import unittest
import HTMLTestRunner

# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         try:
#             self.assertEqual('foo'.upper(),'FOo')
#         except:
#             print "this test_upper is failure"
#     def test_isupper(self):
#         self.assertFalse('Foo'.isupper())
#     def test_split(self):
#         mystr = 'hello world'
#         self.assertEqual(mystr.split(),['hello','world'])
#
#     if __name__ == '__main__':
#         unittest.main

# class TestMethods(unittest.TestCase):
#     def setUp(self):
#         print 'init ny setUp'
#
#     def tearDown(self):
#         print 'end by tearDown'
#
#     def test_1upper(self):
#         self.assertEqual('foo'.upper(),'FOO')
#
#     def test_2isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_3split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(),['hello','world'])
#
# if __name__ == '__main__':
#     test_cases = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
#     test_suit = unittest.TestSuite()
#     test_suit.addTests(test_cases)
#     test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
#
#     print 'testsRun:{}'.format(test_result.testRun)
#     print 'failures:{}'.format(len(test_result.failures))
#     print 'errors:{}'.format(len(test_result.errors))

class testadd(unittest.TestCase):
    def setUp(self):
        pass

    def test_add1(self):
        self.assertEqual(2+3+5,10)

    def test_add2(self):
        self.assertEqual(0+8+7,15)
    def tearDown(self):
        pass

def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(testadd('test_add1'))
    suiteTest.addTest(testadd('test_add2'))
    return suiteTest
if __name__ == '__main__':
    fp = file('D:\\pysult.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title=u'测试报告标题',description=u'描述')
    runner.run(suite())
    fp.close()
