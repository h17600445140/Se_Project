# -*- coding:utf-8 -*-
from time import sleep

from PageClass.fscIndexPageClass.paymentCenterPageClass.billExchangePage import BillExchangePage
from Testcases.common.loginDepend import LoginDepend
from Util import record


class TestBillExchangePage():


    def setup_class(self):
        self.login = LoginDepend('fscHost', 'user')
        self.billExchangePage = BillExchangePage(self.login.driver)

    def teardown_class(self):
        self.billExchangePage.driver.quit()

    def test_addReceivableExchangeBill(self):

        self.billExchangePage.gotoBillExchangePage()

        self.billExchangePage.selectLe('UIHSZT')

        postalOrder1 = self.billExchangePage.addReceivableExchangeBill()

        record.writeDataToRecord({"postalOrder1": postalOrder1}, type='postalOrderData')

        sleep(3)

        postalOrder2 = self.billExchangePage.addReceivableExchangeBill()

        record.writeDataToRecord({"postalOrder2": postalOrder2}, type='postalOrderData')

        sleep(3)

