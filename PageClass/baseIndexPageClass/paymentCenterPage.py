# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageClass.basePage import BasePage



class PaymentCenterPage(BasePage):

    _paymentCenter = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[7]/div/span')
    _companyAccount = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[7]/ul/li[2]/span')
    _payMethod = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[7]/ul/li[3]/span')

    _addButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[2]/button[1]/span')
    _deleteButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[2]/button[2]/span')
    _enableButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[2]/button[3]/span')
    _disableButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[2]/button[4]/span')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def open_paymentCenter(self):
        self.click(*self._paymentCenter)

    def getPaymentCenter(self):
        return self._paymentCenter

    def open_companyAccount(self):
        self.click(*self._companyAccount)

    def open_payMethod(self):
        self.click(*self._payMethod)

    def click_addButton(self):
        self.click(*self._addButton)

    def click_deleteButton(self):
        self.click(*self._deleteButton)

    def click_enableButton(self):
        self.click(*self._enableButton)

    def click_disableButton(self):
        self.click(*self._disableButton)

class CompanyAccountPage(PaymentCenterPage):

    _selectCode = (By.ID, 'undefined_code')
    _selectButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[1]/form/div[8]/div/button[1]')
    _selectResult = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[3]/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span')

    # 编辑
    _editButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr/td[17]/div/button[1]/span')

    # 分配
    _distributeButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr/td[17]/div/button[2]/span')

    # 新增页面 -> 优先级
    _priorityInput = (By.XPATH, '//*[@id="form_bankLevel"]/div/input')
    # 新增页面 -> 核算主体
    _accountingEntity = (By.ID, 'form_fuId')
    _accountingEntityCode = (By.ID, 'undefined_CODE')
    _accountingEntityName = (By.ID, 'undefined_NAME')
    _accountingEntitySelectButton = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/form/div[3]/div/button[1]')
    _accountingEntityFirstOption = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr')
    _accountingEntitySubmitButton = (By.XPATH, '/html/body/div[3]/div/div[3]/span/button[2]')
    # 新增页面 -> 编码
    _code = (By.ID, 'form_code')
    # # 新增页面 -> 开户行
    _subBank = (By.ID, 'form_subBank')
    _subBankName = (By.ID, 'undefined_BANK_NAME')
    _subBankHardOfficeName = (By.ID, 'undefined_BANK_HEAD_OFFICE')
    _subBankUnitedCode = (By.ID, 'undefined_UNITED_CODE')
    _subBankSelectButton = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/form/div[4]/div/button[1]')
    _subBankFirstOption = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr')
    _subBankSubmitButton = (By.XPATH, '/html/body/div[3]/div/div[3]/span/button[2]')
    # 新增页面 -> 账户名称
    _bankAccountName = (By.ID, 'form_bankAccountName')
    # 新增页面 -> 银行账号
    _bankAccountNum = (By.ID, 'form_bankAccountNum')
    # 新增页面 -> 收款付款
    _collectionType = (By.ID, 'form_collectionType')
    _collectionTypeShouKuan = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
    _collectionTypeFuKuan = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
    _collectionTypeShouFuKuan = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[3]/span')
    # 新增页面 -> 币种
    _currencyId = (By.ID, 'form_currencyId')
    _currencyCode = (By.ID, 'undefined_CURRENCY_CODE')
    _currencyName = (By.ID, 'undefined_NAME')
    _currencyIdSelectButton = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/form/div[3]/div/button[1]')
    _currencyIdFirstOption = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span/span')
    _currencyIdSubmitButton = (By.XPATH, '/html/body/div[4]/div/div[3]/span/button[2]/span')
    # 新增页面 -> 银行科目
    _accountId = (By.ID, 'form_accountId')
    # 新增页面 -> 票据科目
    _ticketId = (By.ID, 'form_ticketId')
    # 新增页面 -> 账户类型
    _bankAccountType = (By.ID, 'form_bankAccountType')
    _bankAccountTypeJiBenAccount = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
    _bankAccountTypeYiBanAccount = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
    _bankAccountTypeNongWangAccount = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[3]/span')
    # 新增页面 -> 是否直联账户
    _isConnAccount = (By.ID, 'form_isConnAccount')
    # 新增页面 -> 是否直联票据
    _isConnTicket = (By.ID, 'form_isConnTicket')
    # 新增页面 -> 提交按钮
    _addEditSubmit = (By.XPATH, '//*[@id="form"]/div[14]/div/button[2]/span')

    def __init__(self, driver):
        PaymentCenterPage.__init__(self, driver)

    def input_selectCode(self, text):
        self.clear(*self._selectCode)
        self.send_text(text, *self._selectCode)

    def click_selectButton(self):
        self.click(*self._selectButton)

    def click_editButton(self):
        self.click(*self._editButton)

    def input_priorityInput(self, text):
        self.clear(*self._priorityInput)
        self.send_text(text, *self._priorityInput)

    # 核算主体
    def accountingEntitySelect(self, text):
        self.click(*self._accountingEntity)
        self.send_text(text, *self._accountingEntityName)
        self.click(*self._accountingEntitySelectButton)
        self.click(*self._accountingEntityFirstOption)
        self.click(*self._accountingEntitySubmitButton)

    def input_code(self, text):
        self.clear(*self._code)
        self.send_text(text, *self._code)

    # 开户行
    def subBankSelect(self, bankName, bankHardOfficeName, bankUnitedCode):
        self.click(*self._subBank)
        self.send_text(bankName, *self._subBankName)
        self.send_text(bankHardOfficeName, *self._subBankHardOfficeName)
        self.send_text(bankUnitedCode, *self._subBankUnitedCode)
        self.click(*self._subBankSelectButton)
        self.click(*self._subBankFirstOption)
        self.click(*self._subBankSubmitButton)

    def input_bankAccountName(self, text):
        self.clear(*self._bankAccountName)
        self.send_text(text, *self._bankAccountName)

    def input_bankAccountNum(self, text):
        self.clear(*self._bankAccountNum)
        self.send_text(text, *self._bankAccountNum)

    def collectionTypeSelect(self, text):
        self.click(*self._collectionType)
        if text == "收款":
            self.moveToclick(*self._collectionTypeShouKuan)
        elif text == "付款":
            self.moveToclick(*self._collectionTypeFuKuan)
        elif text == "收付款":
            self.moveToclick(*self._collectionTypeShouFuKuan)

    # 币种
    def currencyIdSelect(self, text):
        self.click(*self._currencyId)
        self.send_text(text, *self._currencyCode)
        self.click(*self._currencyIdSelectButton)
        self.click(*self._currencyIdFirstOption)
        self.click(*self._currencyIdSubmitButton)

    def bankAccountTypeSelect(self, text):
        self.click(*self._bankAccountType)
        if text == "基本账户":
            self.moveToclick(*self._bankAccountTypeJiBenAccount)
        elif text == "一般账户":
            self.moveToclick(*self._bankAccountTypeYiBanAccount)
        elif text == "农网专户":
            self.moveToclick(*self._bankAccountTypeNongWangAccount)

    def click_addEditSubmit(self):
        self.click(*self._addEditSubmit)

class PayMethodPage(PaymentCenterPage):

    # 新增页面 -> 优先级
    _priorityInput = (By.XPATH, '//*[@id="form_paymentSort"]/div/input')
    # 新增页面 -> 编码
    _code = (By.ID, 'form_paymentCode')
    # 新增页面 -> 支付方式（中）
    _paymentNameC = (By.ID, 'form_paymentName_zh-CN')
    # 新增页面 -> 支付方式（En）
    _paymentNameE = (By.ID, 'form_paymentName_en-US')
    # 新增页面 -> 核算主体
    _accountingEntity = (By.ID, 'form_sysPaymentModeLeId')
    _accountingEntityCode = (By.ID, 'undefined_CODE')
    _accountingEntityName = (By.ID, 'undefined_NAME')
    _accountingEntitySelectButton = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/form/div[3]/div/button[1]')
    _accountingEntityFirstOption = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span/span')
    _accountingEntitySubmitButton = (By.XPATH, '/html/body/div[3]/div/div[3]/span/button[2]')
    # 新增页面 -> 适用单据
    _paymentModeBoe = (By.ID, 'form_sysPaymentModeBoeTypeId')
    _paymentModeBoeName = (By.ID, 'undefined_BOE_TYPE_NAME')
    _paymentModeBoeSelectButton = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[1]/form/div[2]/div/button[1]')
    _paymentModeBoeFirstOption = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span/span')
    _paymentModeBoeSubmitButton = (By.XPATH, '/html/body/div[3]/div/div[3]/span/button[2]')
    # 新增页面 -> 是否挂账
    _onAccountFlag = (By.ID, 'form_onAccountFlag')
    _onAccountFlagIs = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
    _onAccountFlagNot = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
    # 新增页面 -> 付款属性
    _transferFundFlag = (By.ID, 'form_transferFundFlag')
    _transferFundFlagBuZhiFu = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
    _transferFundFlagHuiPiao = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
    _transferFundFlagXianJin = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[3]/span')
    _transferFundFlagZhiPiao = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[4]/span')
    _transferFundFlagZhuanZhang = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[5]/span')
    # 新增页面 -> 是否直联账户
    _whetherToBankAccountFlag = (By.XPATH, '//*[@id="form"]/div[9]/div/div/div')
    # 新增页面 -> 新增按钮
    _subjectAdd = (By.XPATH, '//*[@id="form"]/div[10]/div/div[1]/button[1]')
    _subjectAccountingEntity = (By.ID, 'form_fuId')
    _subjectAccountingEntityName = (By.ID, 'undefined_FU_NAME')
    _subjectAccountingEntitySelectButton = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[1]/form/div[2]/div/button[1]')
    _subjectAccountingEntityFirstOption = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr')
    _subjectAccountingEntitySubmitButton = (By.XPATH, '/html/body/div[6]/div/div[3]/span/button[2]')
    _subjectCode = (By.ID, 'form_subjectId')
    _subjectCodeCode = (By.ID, 'undefined_ACCOUNT_CODE')
    _subjectSelectButton = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[1]/form/div[3]/div/button[1]')
    _subjectFirstOption = (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr')
    _subjectSubmitButton = (By.XPATH, '/html/body/div[6]/div/div[3]/span/button[2]')
    _subjectAddSubmit = (By.XPATH, '//*[@id="form"]/div[5]/div/button[2]')
    # 新增页面 -> 删除按钮
    _subjectDelete = (By.XPATH, '//*[@id="form"]/div[10]/div/div[1]/button[2]')
    # 新增页面 -> 提交按钮
    _paymentSubmit = (By.XPATH, '//*[@id="form"]/div[11]/div/button[2]')


    def __init__(self, driver):
        PaymentCenterPage.__init__(self, driver)

    def input_priorityInput(self, text):
        self.clear(*self._priorityInput)
        self.send_text(text, *self._priorityInput)

    def input_code(self, text):
        self.clear(*self._code)
        self.send_text(text, *self._code)

    def input_paymentNameC(self, text):
        self.clear(*self._paymentNameC)
        self.send_text(text, *self._paymentNameC)

    def input_paymentNameE(self, text):
        self.clear(*self._paymentNameE)
        self.send_text(text, *self._paymentNameE)

    def accountingEntitySelect(self, text):
        self.click(*self._accountingEntity)
        self.send_text(text, *self._accountingEntityName)
        self.click(*self._accountingEntitySelectButton)
        self.click(*self._accountingEntityFirstOption)
        self.click(*self._accountingEntitySubmitButton)

    def paymentModeBoeSelect(self, text):
        self.click(*self._paymentModeBoe)
        self.send_text(text, *self._paymentModeBoeName)
        self.click(*self._paymentModeBoeSelectButton)
        self.click(*self._paymentModeBoeFirstOption)
        self.click(*self._paymentModeBoeSubmitButton)

    def onAccountFlagSelect(self, text):
        self.click(*self._onAccountFlag)
        if text == "挂账":
            self.moveToclick(*self._onAccountFlagIs)
        elif text == "不挂账":
            self.moveToclick(*self._onAccountFlagNot)

    def transferFundFlagSelect(self, text):
        self.click(*self._transferFundFlag)
        if text == "不支付":
            self.moveToclick(*self._transferFundFlagBuZhiFu)
        elif text == "汇票":
            self.moveToclick(*self._transferFundFlagHuiPiao)
        elif text == "现金":
            self.moveToclick(*self._transferFundFlagXianJin)
        elif text == "支票":
            self.moveToclick(*self._transferFundFlagZhiPiao)
        elif text == "转账":
            self.moveToclick(*self._transferFundFlagZhuanZhang)

    def click_whetherToBankAccountFlag(self):
        self.click(*self._whetherToBankAccountFlag)

    def getWhetherToBankAccountFlag(self):
        return self._whetherToBankAccountFlag

    def whetherToBankAccountFlagSelect(self, flag):
        if flag != True:
            if 'is-checked' in self.getElementAttribute(
                    'class', *self.getWhetherToBankAccountFlag()):
                self.click_whetherToBankAccountFlag()
            else:
                pass
        else:
            if 'is-checked' in self.getElementAttribute(
                    'class', *self.getWhetherToBankAccountFlag()):
                pass
            else:
                self.click_whetherToBankAccountFlag()

    def click_subjectAdd(self):
        self.click(*self._subjectAdd)

    def subjectAccountingEntitySelect(self, text):
        self.click(*self._subjectAccountingEntity)
        self.send_text(text, *self._subjectAccountingEntityName)
        self.click(*self._subjectAccountingEntitySelectButton)
        self.click(*self._subjectAccountingEntityFirstOption)
        self.click(*self._subjectAccountingEntitySubmitButton)

    def subjectCodeSelect(self, text):
        self.click(*self._subjectCode)
        self.send_text(text, *self._subjectCodeCode)
        self.click(*self._subjectSelectButton)
        self.click(*self._subjectFirstOption)
        self.click(*self._subjectSubmitButton)

    def click_subjectAddSubmit(self):
        self.click(*self._subjectAddSubmit)

    def click_paymentSubmit(self):
        self.click(*self._paymentSubmit)



