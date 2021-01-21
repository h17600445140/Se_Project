# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.basePage import BasePage
from Util import logger



class EasIndexPage(BasePage):

    # 事项申请
    _boeApply = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[1]/div/div')
    # 费用报销
    _boeReimburse = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[2]/div/div')
    # 借款还款
    _boeBorrow = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[3]/div/div')
    # 我的发票
    _menuMyInvoice = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[2]/div[5]/div/div')

    _myWaitApprove = (By.ID, 'tab-waitApprovel')
    _myBoeList = (By.ID, 'tab-myBoeList')

    _moreButton = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[4]/div[2]')
    _boeNo = (By.ID, 'undefined_boeNo')
    _boeNoSelectButton = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[1]/form/div[8]/div/button[1]')
    _boeNoSelectResult = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[3]/div/div[3]/table/tbody/tr')
    _boeBusinessApprove = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr/td[12]/div/button[1]')
    _boeBusinessRefuse = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr/td[12]/div/button[2]')
    _boeBusinessTipCancel = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
    _boeBusinessTipConfirm = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]')


    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def open_boe(self, boeType, boeName):
        logger.info("单据类型为：{} ,单据业务类型为: {}".format(boeType, boeName))
        flag = False
        for i in range(len(self.find_elements(*(By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div')))):
            if flag == True:
                break
            if self.get_elementText(*(By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[{}]/div[1]/span'.format(i+1))) == boeType:
                for j in range(len(self.find_elements(*(By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[{}]/div[2]/div'.format(i+1))))):
                    if self.get_elementText(*(By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[{}]/div[2]/div[{}]/div[2]'.format(i+1, j+1))) == boeName:
                        self.moveToclick(*(By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[3]/div[3]/div/div[2]/div[{}]/div[2]/div[{}]'.format(i+1, j+1)))
                        flag = True
                        break
                    else:
                        pass
            else:
                pass
        logger.info("是否正常打开单据: {}".format(flag))
        if flag != True:
            logger.error('Exception: Don\'t find Boe, please check config')
            raise Exception('Don\'t find Boe, please check config')

    def open_boeApply(self):
        self.click(*self._boeApply)

    def open_boeReimburse(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeReimburse))
        self.click(*self._boeReimburse)

    def open_boeBorrow(self):
        self.click(*self._boeBorrow)

    def open_menuMyInvoice(self):
        self.click(*self._menuMyInvoice)


    def click_myBoeList(self):
        self.click(*self._myBoeList)

    def click_myWaitApprove(self):
        self.click(*self._myWaitApprove)

    def click_moreButton(self):
        self.click(*self._moreButton)

    def input_boeNo(self, text):
        self.send_text(text, *self._boeNo)

    def getBoeNo(self):
        return self._boeNo

    def click_boeNoSelectButton(self):
        self.click(*self._boeNoSelectButton)

    def selectResultIsOrNot(self):
        try:
            self.find_element(self._boeNoSelectResult)
        except:
            logger.info("单据不存在")
            return False
        else:
            logger.info("单据存在")
            return True

    def click_boeBusinessApprove(self):
        self.click(*self._boeBusinessApprove)

    def click_boeBusinessTipConfirm(self):
        self.click(*self._boeBusinessTipConfirm)
