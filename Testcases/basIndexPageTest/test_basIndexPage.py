# -*- coding:utf-8 -*-
from time import sleep

from PageClass.basIndexPageClass.basIndexPage import BasIndexPage
from Testcases.common.loginDepend import LoginDepend



class TestBasIndexPage():

    def setup_class(self):
        self.publicLogin = LoginDepend('basHost', 'user')
        self.cmsIndexPage = BasIndexPage(self.publicLogin.driver)

    def teardown_class(self):
        # self.cmsIndexPage.driver.quit()
        pass

    def test_cmsIndex(self):

        self.cmsIndexPage.selectTabType('采购付款')

        self.cmsIndexPage.boeRntry('成本暂估(新)')

        # sleep(2)
        # self.cmsIndexPage.click_myDraft()
        #
        # sleep(2)
        # self.cmsIndexPage.click_waitDeal()
        #
        # sleep(2)
        # self.cmsIndexPage.click_payFailed()
        #
        # sleep(2)
        # self.cmsIndexPage.click_myBill()
        #
        # sleep(2)
        # self.cmsIndexPage.click_more()
        #
        # sleep(2)
        # self.cmsIndexPage.input_boeNumQuery('123456789')
        #
        # sleep(2)
        # self.cmsIndexPage.click_queryButton()
        #
        # sleep(2)
        # self.cmsIndexPage.backToHomePage()

