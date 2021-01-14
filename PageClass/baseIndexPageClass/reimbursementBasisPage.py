# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PageClass.basePage import BasePage
from Util import logger



class ReimbursementBasisPage(BasePage):

    _reimbursementBasis = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[5]/div/span')
    _businessType = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[5]/ul/li[2]/span')
    _billConfig = (By.XPATH, '//*[@id="app"]/section/section/aside/div/div[2]/div[1]/div/ul/li[5]/ul/li[5]/span')

    def open_reimbursementBasis(self):
        self.click(*self._reimbursementBasis)

    def getReimbursementBasis(self):
        return self._reimbursementBasis

    def open_businessType(self):
        self.click(*self._businessType)

    def open_billConfig(self):
        self.click(*self._billConfig)

    def __init__(self, driver):
        BasePage.__init__(self, driver)



class BusinessTypePage(ReimbursementBasisPage):

    _filterBox = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[1]/input')
    _businessOpen = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/span[1]')

    _totalBusinessType = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/span[2]/span')
    _businessTypeBig = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/span[2]/span')

    _addBusinessCategoryBigButton = (By.XPATH, '//*[@id="pane-default"]/div/button/span')

    _businessTypeCodeBox = (By.ID, 'form_code')
    _businessTypeNameCBox = (By.ID, 'form_name_zh-CN')
    _businessTypeNameEBox = (By.ID, 'form_name_en-US')
    _businessTypeNumBox = (By.ID, 'form_orderNum')
    _icon = (By.XPATH, '//*[@id="form"]/div[5]/div/div/div/div/div/div/input')
    _appDisplayOrNot = (By.ID, 'form_appShow')
    _appDisplayNameCBox = (By.ID, 'form_appName_zh-CN')
    _appDisplayNameEBox = (By.ID, 'form_appName_en-US')
    _auditPointsCBox = (By.ID, 'form_auditPoints_zh-CN')
    _auditPointsEBox = (By.ID, 'form_auditPoints_en-US')
    _remarkCBox = (By.ID, 'form_remark_zh-CN')
    _remarkEBox = (By.ID, 'form_remark_en-US')
    _attribute  = (By.ID, 'form_attribute')
    _statisticalDimension = (By.ID, 'form_statisticalDimensionId')

    _cancelButton = (By.XPATH, '//*[@id="form"]/div[15]/div/button[1]/span')
    _submitButton = (By.XPATH, '//*[@id="form"]/div[15]/div/button[2]/span')

    _editButton = (By.XPATH, '//*[@id="pane-default"]/div[1]/button[2]/span')
    _deleteButton = (By.XPATH, '//*[@id="pane-default"]/div[1]/span/button/span')
    _deleteSubmitButton = (By.XPATH, '//body/div[2]/div/button[2]')

    def __init__(self, driver):
        ReimbursementBasisPage.__init__(self, driver)

    def input_filterBox(self, text):
        self.clear(*self._filterBox)
        self.send_text(text, *self._filterBox)

    def click_businessOpen(self):
        self.click(*self._businessOpen)

    def click_totalBusinessType(self):
        self.click(*self._totalBusinessType)

    def getTotalBusinessType(self):
        return self._totalBusinessType

    def click_businessTypeBig(self):
        self.click(*self._businessTypeBig)

    def getBusinessTypeBig(self):
        return self._businessTypeBig

    def click_addBusinessCategoryBigButton(self):
        self.click(*self._addBusinessCategoryBigButton)

    def input_businessTypeCodeBox(self, text):
        self.clear(*self._businessTypeCodeBox)
        self.send_text(text, *self._businessTypeCodeBox)

    def input_businessTypeNameCBox(self, text):
        self.clear(*self._businessTypeNameCBox)
        self.send_text(text, *self._businessTypeNameCBox)

    def input_businessTypeNameEBox(self, text):
        self.clear(*self._businessTypeNameEBox)
        self.send_text(text, *self._businessTypeNameEBox)

    def input_businessTypeNumBox(self, text):
        self.clear(*self._businessTypeNumBox)
        self.send_text(text, *self._businessTypeNumBox)

    def icon(self):
        pass

    def appDisplayOrNot(self):
        pass

    def input_appDisplayNameCBox(self, text):
        self.clear(*self._appDisplayNameCBox)
        self.send_text(text, *self._appDisplayNameCBox)

    def input_appDisplayNameEBox(self, text):
        self.clear(*self._appDisplayNameEBox)
        self.send_text(text, *self._appDisplayNameEBox)

    def input_auditPointsCBox(self, text):
        self.clear(*self._auditPointsCBox)
        self.send_text(text, *self._auditPointsCBox)

    def input_auditPointsEBox(self, text):
        self.clear(*self._auditPointsEBox)
        self.send_text(text, *self._auditPointsEBox)

    def input_remarkCBox(self, text):
        self.clear(*self._remarkCBox)
        self.send_text(text, *self._remarkCBox)

    def input_remarkEBox(self, text):
        self.clear(*self._remarkEBox)
        self.send_text(text, *self._remarkEBox)

    def click_submitButton(self):
        self.click(*self._submitButton)

    def click_deleteButton(self):
        self.click(*self._deleteButton)

    def click_deleteSubmitButton(self):
        self.click(*self._deleteSubmitButton)

    def click_editButton(self):
        self.click(*self._editButton)



class BillConfigPage(ReimbursementBasisPage):

    _billName = (By.ID, 'undefined_keyword')

    _selectButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div/div[1]/form/div[2]/div/button[1]/span')
    _resetButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div/div[1]/form/div[2]/div/button[2]/span')

    # 业务类型
    _businessTypeButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div/div[3]/div/div[3]/table/tbody/tr/td[14]/div/button/span')
    _businessInputBox = (By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/input')
    _selectAllBox = (By.XPATH, '/html/body/div[3]/div/div[2]/label/span[1]/span')
    _selectFirstBox = (By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/label/span[1]')
    _businessTypeCloseButton = (By.XPATH, '/html/body/div[3]/div/div[3]/span/button[1]/span')
    _businessTypeConfirmButton = (By.XPATH, '/html/body/div[3]/div/div[3]/span/button[2]/span')

    # 凭证类型
    _voucherTypeButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div/div[3]/div/div[3]/table/tbody/tr/td[13]/div/button/span')
    _voucherAddButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[2]/div/div[2]/div/div[1]/button')
    _voucherSubmit = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[2]/div/div[3]/span/button[2]')

    _accountingEntity = (By.ID, 'form_leId')
    _accountingEntityCode = (By.ID, 'undefined_CODE')
    _accountingEntityName = (By.ID, 'undefined_NAME')
    _accountingEntitySelectButton = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/form/div[3]/div/button[1]')
    _accountingEntityFirstOption = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr')
    _accountingEntitySubmit = (By.XPATH, '/html/body/div[4]/div/div[3]/span/button[2]/span')

    _vendorType = (By.ID, 'form_vendorType')
    _vendorTypeStaff = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
    _vendorTypeSupplier = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
    _vendorTypeCustomer = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[3]/span')

    _voucherCategory = (By.ID, 'form_voucherCategory')
    _voucherYingFu = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
    _voucherShiFu = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[2]/span')
    _voucherTuiPiao = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[3]/span')
    _voucherFuKuan = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[4]/span')
    _voucherYuFu = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[5]/span')

    _voucherType = (By.ID, 'form_voucherType')
    _voucherTypeYingShouZhangKuan = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[1]/span')
    _voucherTypeYingFuZhangKuan = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[2]/span')
    _voucherTypeZiChanGuoZhang = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[3]/span')
    _voucherTypeYuanBaoPingZheng = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[4]/span')
    _voucherTypeYuFu = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[5]/span')

    _createNode = (By.ID, 'form_createNode')
    _createNodeCaiWuChuShen = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[1]/span')
    _createNodeShenHeWanCheng = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[2]/span')
    _createNodeFuKuanChengGong = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[3]/span')

    _importNode = (By.ID, 'form_importNode')
    _importNodeCaiWuChuShen = (By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul/li[1]/span')
    _importNodeFuKuanWancheng = (By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul/li[2]/span')
    _importNodeShenHeWanCheng = (By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul/li[3]/span')

    _whetherMerge = (By.ID, 'form_whetherMerge')
    _whetherMergeNo = (By.XPATH, '/html/body/div[9]/div[1]/div[1]/ul/li[1]/span')
    _whetherMergeIs = (By.XPATH, '/html/body/div[9]/div[1]/div[1]/ul/li[2]/span')

    _voucherAddSubmit = (By.XPATH, '//*[@id="form"]/div[8]/div/button[2]')

    # 编辑
    _billEditButton = (By.XPATH, '//*[@id="app"]/section/section/section/main/div/div/div[1]/div/div[3]/div/div[5]/div[2]/table/tbody/tr/td[18]/div/button[1]/span')
    _billWhetherToStandardControlButton = (By.XPATH, '//*[@id="form"]/div[10]/div/div/div')
    _billWhetherToPayButton = (By.XPATH, '//*[@id="form"]/div[11]/div/div/div')
    _billWhetherToAPPSubmitBill = (By.XPATH, '//*[@id="form"]/div[12]/div/div/div')
    _billWhetherToGenerateVoucher = (By.XPATH, '//*[@id="form"]/div[13]/div/div/div')
    _billWhetherToStatistics = (By.XPATH, '//*[@id="form"]/div[14]/div/div/div')
    _billWhetherToEnableBillImageArea = (By.XPATH, '//*[@id="form"]/div[15]/div/div/div')
    _billWhetherToEnableOCR = (By.XPATH, '//*[@id="form"]/div[16]/div/div/div')
    _billCloseButton = (By.XPATH, '//*[@id="form"]/div[20]/div/button[1]/span')
    _billSubmitButton = (By.XPATH, '//*[@id="form"]/div[20]/div/button[2]/span')

    def __init__(self, driver):
        ReimbursementBasisPage.__init__(self, driver)

    # —————————— 业务类型 ——————————

    def input_billName(self, text):
        self.clear(*self._billName)
        self.send_text(text, *self._billName)

    def click_selectButton(self):
        self.click(*self._selectButton)

    def click_resetButton(self):
        self.click(*self._resetButton)

    def click_businessTypeButton(self):
        self.click(*self._businessTypeButton)

    def input_businessInputBox(self, text):
        self.clear(*self._businessInputBox)
        self.send_text(text, *self._businessInputBox)

    def click_selectAllBox(self):
        self.click(*self._selectAllBox)

    def click_selectFirstBox(self):
        self.click(*self._selectFirstBox)

    def getSelectFirstBox(self):
        return self._selectFirstBox

    def click_businessTypeCloseButton(self):
        self.click(*self._businessTypeCloseButton)

    def click_businessTypeConfirmButton(self):
        self.click(*self._businessTypeConfirmButton)

    # —————————— 凭证类型 ——————————

    def click_voucherTypeButton(self):
        self.click(*self._voucherTypeButton)

    def click_voucherAddButton(self):
        self.click(*self._voucherAddButton)

    def click_voucherSubmit(self):
        self.click(*self._voucherSubmit)

    def accountingEntitySelect(self, text):
        self.click(*self._accountingEntity)
        self.send_text(text, *self._accountingEntityName)
        self.click(*self._accountingEntitySelectButton)
        self.click(*self._accountingEntityFirstOption)
        self.click(*self._accountingEntitySubmit)

    def vendorTypeSelect(self, text):
        self.click(*self._vendorType)
        if text == "员工":
            self.moveToclick(*self._vendorTypeStaff)
        elif text == "供应商":
            self.moveToclick(*self._vendorTypeSupplier)
        elif text == "客户":
            self.moveToclick(*self._vendorTypeCustomer)

    def voucherCategorySelect(self, text):
        self.click(*self._voucherCategory)
        if text == "应付凭证":
            self.moveToclick(*self._voucherYingFu)
        elif text == "实付凭证":
            self.moveToclick(*self._voucherShiFu)
        elif text == "退票凭证":
            self.moveToclick(*self._voucherTuiPiao)
        elif text == "付款凭证":
            self.moveToclick(*self._voucherFuKuan)
        elif text == "预付凭证":
            self.moveToclick(*self._voucherYuFu)

    def voucherTypeSelect(self, text):
        self.click(*self._voucherType)
        if text == "应收账款":
            self.moveToclick(*self._voucherTypeYingShouZhangKuan)
        elif text == "应付账款":
            self.moveToclick(*self._voucherTypeYingFuZhangKuan)
        elif text == "资产过账":
            self.moveToclick(*self._voucherTypeZiChanGuoZhang)
        elif text == "员报凭证":
            self.moveToclick(*self._voucherTypeYuanBaoPingZheng)
        elif text == "预付":
            self.moveToclick(*self._voucherTypeYuFu)

    def createNodeSelect(self, text):
        self.click(*self._createNode)
        if text == "财务初审":
            self.moveToclick(*self._createNodeCaiWuChuShen)
        elif text == "审核完成":
            self.moveToclick(*self._createNodeShenHeWanCheng)
        elif text == "付款成功":
            self.moveToclick(*self._createNodeFuKuanChengGong)

    def importNodeSelect(self, text):
        self.click(*self._importNode)
        if text == "财务初审":
            self.moveToclick(*self._importNodeCaiWuChuShen)
        elif text == "付款完成":
            self.moveToclick(*self._importNodeFuKuanWancheng)
        elif text == "审核完成":
            self.moveToclick(*self._importNodeShenHeWanCheng)

    def whetherMergeSelect(self, text):
        self.click(*self._whetherMerge)
        if text == "否":
            self.moveToclick(*self._whetherMergeNo)
        elif text == "是":
            self.moveToclick(*self._whetherMergeIs)

    def click_voucherAddSubmit(self):
        self.click(*self._voucherAddSubmit)


    # —————————— 单据编辑 ——————————

    def click_billEditButton(self):
        self.click(*self._billEditButton)

    def click_billWhetherToStandardControlButton(self):
        self.click(*self._billWhetherToStandardControlButton)

    def getBillWhetherToStandardControlButton(self):
        return self._billWhetherToStandardControlButton

    def click_billWhetherToPayButton(self):
        self.click(*self._billWhetherToPayButton)

    def getBillWhetherToPayButton(self):
        return self._billWhetherToPayButton

    def click_billWhetherToAPPSubmitBill(self):
        self.click(*self._billWhetherToAPPSubmitBill)

    def getBillWhetherToAPPSubmitBill(self):
        return self._billWhetherToAPPSubmitBill

    def click_billWhetherToGenerateVoucher(self):
        self.click(*self._billWhetherToGenerateVoucher)

    def getBillWhetherToGenerateVoucher(self):
        return self._billWhetherToGenerateVoucher

    def click_billWhetherToStatistics(self):
        self.click(*self._billWhetherToStatistics)

    def getBillWhetherToStatistics(self):
        return self._billWhetherToStatistics

    def click_billWhetherToEnableBillImageArea(self):
        self.click(*self._billWhetherToEnableBillImageArea)

    def getBillWhetherToEnableBillImageArea(self):
        return self._billWhetherToEnableBillImageArea

    def click_billWhetherToEnableOCR(self):
        self.click(*self._billWhetherToEnableOCR)

    def getBillWhetherToEnableOCR(self):
        return self._billWhetherToEnableOCR

    def click_billCloseButton(self):
        self.click(*self._billCloseButton)

    def click_billSubmitButton(self):
        self.click(*self._billSubmitButton)







