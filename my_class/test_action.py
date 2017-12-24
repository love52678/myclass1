from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import HTMLTestRunner
import time
class ContextcClick:
    def setUp(self):
        pass
    def test_context_click(self):
        driver = webdriver.Chrome()
        # b = driver.get('https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xbe74b16700011697&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=7&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&inputT=1980&rsv_sug4=2968&rsv_sug=2')
        # time.sleep(3)
        # menu = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div').click()
# time.sleep(3)
# ActionChains(driver).click_and_hold(menu).perform()
# t = driver.find_element_by_class_name('c-icon c-icon-triangle-down')
# time.sleep(3)
# ActionChains(driver).click_and_hold(t).perform()
# driver.quit()
        driver.get('https://www.baidu.com/')
        time.sleep(3)
        b = driver.find_element_by_id('su')
        ActionChains(driver).context_click(b).perform()

    def tearDown(self):
        pass



# timepic=time.strftime("%Y-%m-%d-%H_%M_%S")
# dr1=webdriver.Chrome()
# dr1.get("https://shanghai.anjuke.com/")
# dr1.implicitly_wait(5)
# dr1.execute_script('var q=document.documentElement.scrollTop=10000')
# dr1.save_screenshot("D:/345/"+timepic+".png")
# time.sleep(10)
# dr1.quit()



