# -*- coding:utf-8 -*-

# 测试文件

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://fsscysc.csztessc.com.cn:8085/login")
# driver.maximize_window()
#
# driver.find_element_by_id('loginKey').send_keys('hc3')
# driver.find_element_by_id('password').send_keys('123456')
# driver.find_element_by_id('login').click()
# sleep(1)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/p[2]').click()
# sleep(2)
# print(driver.current_window_handle)
# driver.find_element_by_xpath('//*[@id="app"]/section/header/div[2]/ul/li[4]').click()
# print(driver.current_window_handle)
# print(driver.window_handles)
# win = driver.window_handles
# driver.switch_to.window(win[1])
# print(driver.current_window_handle)
# driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[3]/div/i').click()
# sleep(2)
# driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/i').click()
# sleep(2)
# print(driver.window_handles)
# print(driver.current_window_handle)
# win = driver.window_handles
# driver.switch_to.window(win[2])
# element = driver.find_element_by_id('loan.0.expenseAmount')
# element.click()
# sleep(5)
#
# ActionChains(driver).send_keys_to_element(element,Keys.BACKSPACE).perform()
# ActionChains(driver).send_keys_to_element(element,'100').perform()


driver = webdriver.Chrome()
driver.get("http://192.168.0.200/eas/myApproval")
driver.maximize_window()
driver.find_element_by_id('loginKey').send_keys('1')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('login').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div[2]/div[4]/div[2]').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/section/main/div[2]/div/div/div[1]/div/i').click()
# driver.find_element_by_id('undefined_boeNo').send_keys('123456')
element = driver.find_element_by_xpath('//*[@id="undefined_boeNo"]')
print(element)


