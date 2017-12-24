# from selenium import webdriver
# import time
# dr = webdriver.Chrome()
# dr.get("https://www.baidu.com/")
# # dr.find_element_by_id("kw").send_keys("selenium")
# # dr.find_element_by_id("su").click()
# dr.find_element_by_id("kw").send_keys("selenium")
# time.sleep(3)
# dr.quit()
# from selenium.webdriver.common.action_chains import ActionChains

#coding=utf-8
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
b = webdriver.Chrome()
b.get("https://www.baidu.com/")
ele=b.find_element_by_xpath('//*[@id="kw"]')
ele.send_keys("python")
sleep(3)
b.find_element_by_xpath('//*[@id="su"]').click()
sleep(2)
b.find_element_by_partial_link_text(u'-甲骨文.首页-欢迎您').click()


