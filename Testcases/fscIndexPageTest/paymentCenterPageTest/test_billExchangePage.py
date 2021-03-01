# -*- coding:utf-8 -*-
from PageClass.fscIndexPageClass.paymentCenterPageClass.billExchangePage import BillExchangePage
from Testcases.common.loginDepend import LoginDepend



class TestBillExchangePage():


    def setup_class(self):
        self.login = LoginDepend('fscHost', 'user')
        self.billExchangePage = BillExchangePage(self.login.driver)

    def teardown_class(self):
        pass

    def test_addReceivableExchangeBill(self):

        self.billExchangePage.gotoBillExchangePage()

        self.billExchangePage.selectLe('XYTEST')

        self.billExchangePage.addReceivableExchangeBill()

