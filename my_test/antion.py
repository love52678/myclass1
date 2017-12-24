#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('http://www.maiziedu.com')
# driver.maximize_window()
sleep(5)
# ele = driver.find_element_by_link_text(u'')
ele = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/ul/li[1]')
ActionChains(driver).move_to_element(ele).perform()
sleep(5)
sub_ele = driver.find_element_by_link_text(u'机器学习')
sub_ele.click()
# driver.quit()
