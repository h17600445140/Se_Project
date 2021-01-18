# -*- coding:utf-8 -*-
# class one(object):
#     __a = 1
#     __b = 2
#
#     def __init__(self):
#         print("this is one")
#
# class two(one):
#
#     def __init__(self):
#         one.__init__(self)
#         print("this is two")
#
#     def print(self):
#         print("___")
#         print(self.__a)
#
# class three(two):
#
#     def __init__(self):
#         two.__init__(self)
#         print("this is three")
#
#     def print1(self):
#         print(self.a)
#
# if __name__ == '__main__':
#     a = one()
#     print(a._one__a)
#     print(a._one__b)
#
#     # a = one()
#     # print(a._a)
#     #
#     b = two()
#     print(b._one__a)

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PageClass.loginPageClass.publicLoginPage import PublicLoginPage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.publicIndexPageClass.groupManagementPage import RolePage

driver = webdriver.Chrome()

L = PublicLoginPage(driver)
R = RolePage(L.driver)

L.goto_publicloginpage("http://fsscysc.csztessc.com.cn:8085/public")
sleep(1)
L.input_account("hc3")
L.input_password("123456")
sleep(1)
L.click_loginbutton()
sleep(1)
L.get_into()
sleep(2)
R.open_groupManagement()
sleep(1)
R.open_role()
# R.clickAddButton()

R.send_text('huangchao', *(By.ID, 'undefined_name'))
sleep(1)
R.click(*(By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[1]/form/div[4]/div/button[1]/span'))
sleep(2)

R.click(*(By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[3]/div/div[3]/table/tbody/tr/td[9]/div/button/span'))
sleep(2)


print(R.find_element(*(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div')))
print(len(R.find_element(*(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div')).find_elements(*(By.CLASS_NAME, 'el-checkbox__inner'))))
print(type(R.find_element(*(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div')).find_elements(*(By.CLASS_NAME, 'el-checkbox__inner'))))

oList = R.find_element(*(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div')).find_elements(*(By.CLASS_NAME, 'el-checkbox__inner'))

for i in range(len(oList)):
    oList[i].click()

print("成功")


