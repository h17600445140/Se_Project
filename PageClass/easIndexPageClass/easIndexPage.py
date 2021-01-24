# -*- coding:utf-8 -*-
from time import sleep

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

    _boeBusinessRefuse = (By.XPATH, '//*[@id="app"]/section/main/div[2]/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr/td[12]/div/button[2]')
    _boeBusinessTipCancel = (By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def open_boe(self, boeType, boeName):
        logger.info("打开的单据类型为：{} ,选择的单据业务类型为: {}".format(boeType, boeName))

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
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeApply))
        logger.info("打开事项申请单据选择页面")
        self.click(*self._boeApply)

    def open_boeReimburse(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeReimburse))
        logger.info("打开费用报销单据选择页面")
        self.click(*self._boeReimburse)

    def open_boeBorrow(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeBorrow))
        logger.info("打开借款还款单据选择页面")
        self.click(*self._boeBorrow)

    def open_menuMyInvoice(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._menuMyInvoice))
        self.click(*self._menuMyInvoice)

    # 我的单据
    _myBoeList = (By.ID, 'tab-myBoeList')
    def click_myBoeList(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._myBoeList))
        self.click(*self._myBoeList)
        logger.info('点击我的单据')

    # 待我审批
    _myWaitApprove = (By.ID, 'tab-waitApprovel')
    def click_myWaitApprove(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._myWaitApprove))
        self.click(*self._myWaitApprove)
        logger.info('点击待我审批')

    # 更多
    _moreButton = (By.XPATH, '//*[@id="app"]/section/main/div/div/div[2]/div[4]/div[2]')
    def click_moreButton(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._moreButton))
        self.click(*self._moreButton)
        logger.info('点击更多按钮')
        self.switchWindow()

    # 单据编号
    _boeNo = (By.ID, 'undefined_boeNo')
    def getBoeNo(self):
        return self._boeNo
    def input_boeNo(self, text):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeNo))
        self.send_text(text, *self._boeNo)
        logger.info("输入查询的单据编号为：{}".format(text))

    # 查询
    def click_boeNoSelectButton(self):
        self.click_button('查询')
        logger.info("点击查询按钮")

    # 查询结果
    _boeNoSelectResult = (By.XPATH, '//*[@id="app"]//table/tbody/tr/td[2]')
    def selectResultIsOrNot(self, boeNum):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeNoSelectResult))
        if self.get_elementText(*self._boeNoSelectResult) == boeNum:
            logger.info("Success ， 查询出对应结果")
            return True
        else:
            logger.info("Fail ， 没有查询出对应结果")
            return False

    # 查询结果
    _boeNoSelectResultBusiness = (By.XPATH, '//*[@id="app"]//table/tbody/tr/td[3]')
    def selectResultIsOrNotBusiness(self, boeNum):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self._boeNoSelectResultBusiness))
        if self.get_elementText(*self._boeNoSelectResultBusiness) == boeNum:
            logger.info("Success ， 查询出对应结果")
            return True
        else:
            logger.info("Fail ， 没有查询出对应结果")
            return False

    # 同意
    _boeBusinessApprove = (By.XPATH, '//*[@id="app"]//div[5]/div[2]/table/tbody/tr/td[12]/div/button[1]')
    def  click_boeBusinessApprove(self):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self._boeBusinessApprove))
            self.click(*self._boeBusinessApprove)
            logger.info("点击审批单据同意按钮")

    # 确定
    _boeBusinessTipConfirm = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]')
    def click_boeBusinessTipConfirm(self):
        self.click_button('确定')
        logger.info("点击确定按钮")
