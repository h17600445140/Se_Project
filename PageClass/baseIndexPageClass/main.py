from time import sleep
from selenium import webdriver
from PageClass.baseIndexPageClass.reimbursementBasisPage import ReimbursementBasisPage, BusinessTypePage
from Testcases.common.loginDepend import LoginDepend
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login = LoginDepend('baseHost', 'user')

sleep(2)
a = BusinessTypePage(login.driver)
a.open_reimbursementBasis()
a.open_businessType()

sleep(2)
a.input_filterBox("a")

print(EC.visibility_of(a.find_element(*a.getBusinessTypeBig())))

sleep(1)

print(a.elementIsDisplay(*a.getBusinessTypeBig()))


# b = a.elementExistIsOrNot(*a.getBusinessTypeBig())
# print(b)

# c = EC.element_to_be_clickable(a.find_element(*(By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]')))
# print(c)

# a.click_businessTypeBig()

# WebDriverWait(a.driver, 5).until(EC.visibility_of_element_located(a.getIntoButton()))


# sleep(2)
# sleep(1)









