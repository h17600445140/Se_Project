# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageClass.easIndexPageClass.easIndexPage import EasIndexPage
from Testcases.common.loginDepend import LoginDepend
from Util import logger


class BusinessApprove():

    def __init__(self, boeNum):
        self.boeNum = boeNum
        self.login = LoginDepend('easHost', 'leader')
        self._easIndexPage = EasIndexPage(self.login.driver)

    def boeBusinessApprove(self):
        try:

            self._easIndexPage.click_myWaitApprove()
            self._easIndexPage.click_moreButton()

            self._easIndexPage.input_boeNo(self.boeNum)
            self._easIndexPage.click_boeNoSelectButton()

            status = self._easIndexPage.selectResultIsOrNotBusiness(self.boeNum)
            if status == True:
                pass
            else:
                logger.error("boeNum do not exist")
                raise Exception("boeNum do not exist")

            self._easIndexPage.click_boeBusinessApprove()
            self._easIndexPage.click_boeBusinessTipConfirm()

            if self._easIndexPage.getToastBoxText() == '操作成功':
                content = '审批成功'
                logger.info("审批状态为：{}".format(content))
                self.login.driver.quit()
                return content
            else:
                content = '审批失败'
                logger.info("审批状态为：{}".format(content))
                self.login.driver.quit()
                return content

        except Exception as e:
            logger.error("业务审批出现异常，异常信息为：{}".format(type(e)))
            self.login.driver.quit()
