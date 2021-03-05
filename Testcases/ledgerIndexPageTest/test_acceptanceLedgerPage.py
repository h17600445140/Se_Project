# -*- coding:utf-8 -*-
import datetime
import random
import string
from time import sleep

from PageClass.ledgerIndexPageClass.acceptanceLedgerPage import AcceptanceLedgerPage
from Testcases.common.loginDepend import LoginDepend
from Util import record



class TestAcceptanceLedgerPage():

    acceptanceNo = globals()

    def setup_class(self):
        self.login = LoginDepend('ledgerHost', 'user')
        self.acceptanceLedgerPage = AcceptanceLedgerPage(self.login.driver)

    def teardown_class(self):
        self.acceptanceLedgerPage.driver.quit()

    def test_addAcceptanceLedger(self):

        self.acceptanceLedgerPage.getInLedger('验收单台账')

        self.acceptanceLedgerPage.click_ledgerDetail()

        self.acceptanceLedgerPage.clickTargetButton('新增')

        global acceptanceNo

        acceptanceNo = 'UIYSD' + ''.join(random.choice(string.digits) for _ in range(5))

        self.acceptanceLedgerPage.input_acceptanceNo(acceptanceNo)

        self.acceptanceLedgerPage.input_acceptOrderNo('UIDD' + ''.join(random.choice(string.digits) for _ in range(5)))

        self.acceptanceLedgerPage.selectAcceptVendor('UI供应商')

        # self.acceptanceLedgerPage.selectAcceptContract('hc00000020', contractName='hc合同020')

        self.acceptanceLedgerPage.selectAcceptProject('UIXM', projectName='UI项目')

        self.acceptanceLedgerPage.selectAcceptReceivingUnit('UIDP', deptName='UI部门')

        # self.acceptanceLedgerPage.selectAcceptAgent('UI01', agentName='UI01')

        self.acceptanceLedgerPage.input_acceptanceDate(datetime.datetime.now().strftime("%Y-%m-%d"))

        self.acceptanceLedgerPage.click_acceptSubmitButton()

        assert self.acceptanceLedgerPage.getToastBoxText() == '保存成功'

        self.acceptanceLedgerPage.input_acceptanceNoQuery(acceptanceNo)

        self.acceptanceLedgerPage.click_acceptanceQueryButton()

        assert self.acceptanceLedgerPage.get_acceptanceNoResult() == acceptanceNo


    def test_editAcceptanceLedgerDetail(self):

        global acceptanceNo

        self.acceptanceLedgerPage.input_acceptanceNoQuery(acceptanceNo)

        self.acceptanceLedgerPage.click_acceptanceQueryButton()

        self.acceptanceLedgerPage.click_acceptanceEditButoon()

        self.acceptanceLedgerPage.click_addDetailButton()

        self.acceptanceLedgerPage.input_detailName('hcProduct')

        self.acceptanceLedgerPage.input_detailSpecification('大')

        self.acceptanceLedgerPage.input_detailUnit('个')

        self.acceptanceLedgerPage.input_detailNum('1')

        self.acceptanceLedgerPage.input_detailPrice('100.00')

        self.acceptanceLedgerPage.input_detailTaxAmount('100.00')

        self.acceptanceLedgerPage.input_detailTaxRate('0')

        self.acceptanceLedgerPage.input_detailTax('0.00')

        self.acceptanceLedgerPage.click_detailSubmit()

        assert self.acceptanceLedgerPage.getToastBoxText() == '保存成功'

        record.writeDataToRecord({'acceptanceNo':acceptanceNo}, type='acceptanceLedgerData')



