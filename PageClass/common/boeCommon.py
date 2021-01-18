# -*- coding:utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PageClass.basePage import BasePage



class BoeCommen(BasePage):

    _boeNum = (By.XPATH, '//*[@id="top"]/span[3]')

    # 单据保存、提交
    _boeSaveButton = (By.ID, 'save')
    _boeSubmitButton = (By.ID, 'submit')


    _printCover = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[1]')
    _viewBoe = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[2]')
    _copyBoe = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[3]')
    _continueBoe = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[4]')
    _close = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div[2]/div/div[2]/button[5]')


    _accountMessage = (By.ID, 'tab-accounting')
    _approveButton = (By.XPATH, '//*[@id="pane-accounting"]/div/div[1]/div[1]/div/div/div[1]/div[2]/div[4]/button[1]')
    _approveButton1 = (By.XPATH, '//*[@id="pane-accounting"]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[4]/button[1]')


    # —————————— 主表区 ——————————
    # 申请人
    _employeeId = (By.ID, 'boeHeader.0.employeeId')
    # 业务类型
    _operationTypeId = (By.ID, 'boeHeader.0.operationTypeId')
    # 纸质附件
    _paperAccessories = (By.ID, 'boeHeader.0.paperAccessories')
    # 借款币种
    _paymentCurrency = (By.ID, 'boeHeader.0.paymentCurrency')
    # 备注
    _boeAbstract = (By.ID, 'boeHeader.0.boeAbstract')

    # —————————— 支付区 ——————————
    # 支付方式
    _paymentModeCode = (By.ID, 'zfsBoePayments.0.paymentModeCode')
    # 收款账户
    _vendorId = (By.ID, 'zfsBoePayments.0.vendorId')
    # 支付金额
    _paymentAmount = (By.ID, 'zfsBoePayments.0.paymentAmount')
    # 付款用途
    _paymentMemo = (By.ID, 'zfsBoePayments.0.paymentMemo')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def getBoeNum(self):
        return self.get_elementText(*self._boeNum)

    def click_boeSubmitButton(self):
        self.click(*self._boeSubmitButton)

    def click_printCover(self):
        self.click(*self._printCover)

    def click_viewBoe(self):
        self.click(*self._viewBoe)

    def click_copyBoe(self):
        self.click(*self._copyBoe)

    def click_continueBoe(self):
        self.click(*self._continueBoe)

    def click_close(self):
        self.click(*self._close)

    def click_accountMessage(self):
        self.click(*self._accountMessage)

    def click_approveButton(self):
        try:
            self.click(*self._approveButton)
        except:
            self.click(*self._approveButton1)

    # —————————— 操作主表区 ——————————

    def input_operationType(self, text):
        self.clear(*self._operationTypeId)
        self.send_text(text, *self._operationTypeId)

    def input_boeAbstract(self, text):
        self.clear(*self._boeAbstract)
        self.send_text(text, *self._boeAbstract)

    # ——————————————————————————————

    # —————————— 操作支付区 ——————————

    def input_paymentAmount(self, text):
        self.click(*self._paymentAmount)
        element = self.find_element(*self._paymentAmount)
        ActionChains(self.driver).send_keys_to_element(element, Keys.BACKSPACE).perform()
        ActionChains(self.driver).send_keys_to_element(element, text).perform()

    def input_paymentMemo(self, text):
        self.clear(*self._boeAbstract)
        self.send_text(text, *self._paymentMemo)

    # ——————————————————————————————