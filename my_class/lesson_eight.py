# coding=utf-8
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
# b = webdriver.Chrome()
# b.get("https://www.baidu.com/")
# ele=b.find_element_by_xpath('//*[@id="kw"]')
# ele.clear()
# ele.send_keys("python")
# sleep(3)
# e = b.find_element_by_xpath('//*[@id="su"]')
# sleep(3)
# print e.text
# b.quit()

# sleep(2)
# try:
#     b.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
#     b.save_screenshot('a.png')
# except:
#     print '网页没找到'

# d = webdriver.Chrome()
# d.get('http://www.baidu.com')
# print d.current_url
# d.get('http://sougou.com')
# print d.current_url
# d.back()
# sleep(5)
# print d.current_url
# sleep(5)
# d.forward()
# print d.current_url
# sleep(5)
# d.quit()
d = webdriver.Chrome()
d.get('http://www.baidu.com')
# try:
# d.find_element_by_css_selector('#kw').send_keys('python')
e = d.find_element_by_xpath('//form').find_element_by_xpath('span/input')
e.send_keys('python')

# except:
sleep(5)
d.quit()

