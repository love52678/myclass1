# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest
import HTMLTestRunner
class TestOpenChrome(unittest.TestCase):
    def setUp(self):
        pass

    def test_open_chrome(self):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com/')
        sleep(2)
        e = driver.find_element_by_id('kw')
        e.clear()
        e.send_keys('python')
        t = driver.find_element_by_id('su')
        t.click()
        sleep(2)
        # a = driver.find_element_by_link_text('http://www.baidu.com/link?url=I7X7D6QJxwRA5Mh8AE5tfRB_bTTUzoTqyErSqEWAFblkoiVRw0hA7BtWFAhh5rcH').click()
        self.assertIn('python',driver.title)
        driver.close()
    def tearDown(self):
        pass

def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestOpenChrome('test_open_chrome'))
    return suiteTest
if __name__ == '__main__':
    fp = file('d:\\py.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"报告描述")
    runner.run(suite())
    fp.close()
