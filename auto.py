from selenium import webdriver
import time
browser = webdriver.Chrome()
# 开始请求
browser.get('https://test-saas.01zhuanche.com')
time.sleep(2)
browser.find_element_by_xpath("//input[@class='user_name_pass']").send_keys('admin')
time.sleep(2)
browser.find_element_by_xpath("//input[@type='password']").send_keys('111111')
time.sleep(2)
browser.find_element_by_xpath("//input[@class='user_code el-fl']").send_keys('111111')
time.sleep(2)
browser.find_element_by_xpath("//button[@class='login_submit']").click()
time.sleep(2)
