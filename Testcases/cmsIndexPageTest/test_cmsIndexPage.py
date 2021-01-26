# -*- coding:utf-8 -*-
from PageClass.cmsIndexPageClass.cmsIndexPage import CmsIndexPage
from Testcases.common.loginDepend import LoginDepend


class TestCmsIndexPage(object):

    def setup_class(self):
        self.publicLogin = LoginDepend('cmsHost', 'user')
        self.cmsIndexPage = CmsIndexPage(self.publicLogin.driver)

    def teardown_class(self):
        # self.cmsIndexPage.driver.quit()
        pass

    def test_cmsIndex(self):
        pass
