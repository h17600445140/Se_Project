# class one(object):
#     a = 1
#     __b = 2
#
#     def __init__(self):
#         print("this is one")
#
# class two(one):
#     a = 2
#
#     def __init__(self):
#         one.__init__(self)
#         print("this is two")
#
#     def print(self):
#         print("___")
#         print(self.a)
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
#     # a = one()
#     # print(a._a)
#     # print(a._one__b)
#
#     a = one()
#     print(a.a)
#
#     b = two()
#     print(b.a)
from time import sleep

from selenium import webdriver

from PageClass.loginPageClass.publicLoginPage import PublicLoginPage
from PageClass.publicIndexPageClass.groupManagementPageClass import ManagementPageClass

driver = webdriver.Chrome()

L = PublicLoginPage(driver)
M = ManagementPageClass(driver)

L.goto_publicloginpage("http://fsscysc.csztessc.com.cn:8085/public")
sleep(1)
L.input_account("admin")
L.input_password("zfs123456")
sleep(1)
L.click_loginbutton()
sleep(1)
L.get_into()
sleep(1)

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

