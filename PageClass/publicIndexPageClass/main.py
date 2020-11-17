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
from selenium.webdriver.common.by import By

from PageClass.loginPageClass.publicLoginPage import PublicLoginPage
from PageClass.publicIndexPageClass.groupManagementPageClass import ManagementPageClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

L = PublicLoginPage(driver)
M = ManagementPageClass(driver)

L.goto_publicloginpage("http://fsscysc.csztessc.com.cn:8085/public")
sleep(1)
L.input_account("hc3")
L.input_password("123456")
sleep(1)
L.click_loginbutton()
sleep(1)
L.get_into()
sleep(2)


M.open_groupManagement()
sleep(1)
M.open_management()
sleep(1)
M.clickAddButton()
sleep(1)
M.input_groupCname("测试1")
M.input_groupEname("test1")
M.input_groupCode("testhc")
M.input_maxUserRegister("10")
M.input_describeC("这是自动化测试")
M.input_describeE("this is a auto test")
M.click_confirm()

WebDriverWait(M.driver, 3).until(
    EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[2]/p'), '编码已存在'))

# '/div/p'
# '/html/body/div[2]'
#
# <div role="alert" class="el-message el-message--success" style="top: 20px; z-index: 2010;">
#     <i class="el-message__icon el-icon-success">
#     </i>
#     <p class="el-message__content">删除成功</p><!---->
# </div>

print("成功")


