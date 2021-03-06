# -*- coding:utf-8 -*-
from time import sleep
import pytest
import allure

from PageClass.cmsIndexPageClass.contractExaminePage import ContractExaminePage
from Testcases.common.loginDepend import LoginDepend
from Util import logger, record


contractData = [
    {
        'contractName': record.readDataFromRecord(type='contractData')['frameworkContractName'],
        'contractCode': record.readDataFromRecord(type='contractData')['frameworkContractCode']
    },
    {
        'contractName': record.readDataFromRecord(type='contractData')['noFrameworkContractName'],
        'contractCode': record.readDataFromRecord(type='contractData')['noFrameworkContractCode']
    }
]


@allure.feature("合同复核流程")
class TestContractExaminePage(object):

    def setup_class(self):
        self.login = LoginDepend('cmsHost', 'user')
        self.contractExaminePage = ContractExaminePage(self.login.driver)

    def teardown_class(self):
        self.contractExaminePage.driver.quit()

    @allure.story("合同复核流程")
    @allure.step("合同复核操作步骤")
    @allure.severity("blocker")
    @pytest.mark.parametrize('contractDataDict', contractData)
    def test_contractExamine(self, contractDataDict):

        logger.info(" ----- 合同复核流程开始 ----- ")

        with allure.step("打开合同管理合同复核页面"):
            self.contractExaminePage.getIntoPage('合同复核')

        with allure.step("合同录入页面输入查询条件合同名称"):
            self.contractExaminePage.input_contractNameQuery(contractDataDict['contractName'])

        with allure.step("合同录入页面输入查询条件合同编码"):
            self.contractExaminePage.input_contractCodeQuery(contractDataDict['contractCode'])

        with allure.step("合同录入页面点击查询按钮"):
            self.contractExaminePage.click_selectButton()

        sleep(1)

        with allure.step("断言查询结果是否为将要进行复核的合同"):
            assert self.contractExaminePage.getResultContractCode() == contractDataDict['contractCode']

        with allure.step("断言查询结果, 合同状态是否正确"):
            assert self.contractExaminePage.getResultContractStatus() == '待复核'

        with allure.step("对查询结果点击同意"):
            self.contractExaminePage.click_agreeButton()

        with allure.step("及逆行确定操作"):
            self.contractExaminePage.click_confirmButoon()

        with allure.step("断言是否操作成功"):
            assert self.contractExaminePage.getToastBoxText() == '审核成功'


        with allure.step("点击我已复核Tab页面"):
            self.contractExaminePage.click_contractReviewedTab()

        with allure.step("我已复核界面输入合同名称"):
            self.contractExaminePage.input_contractNameQuery(contractDataDict['contractName'])

        with allure.step("我已复核界面输入合同编码"):
            self.contractExaminePage.input_contractCodeQuery(contractDataDict['contractCode'])

        with allure.step("我已复核界面点击查询按钮"):
            self.contractExaminePage.click_selectButton()

        with allure.step("断言查询结果是否为已经复核通过的合同"):
            assert self.contractExaminePage.getResultContractCode() == contractDataDict['contractCode']

        with allure.step("断言查询结果, 合同状态是否正确"):
            assert self.contractExaminePage.getResultContractStatus() == '执行中'

        with allure.step("回到首页"):
            self.contractExaminePage.backToHomePage()
            self.contractExaminePage.closeCurrentWindows()


        with allure.step("进入我的合同界面"):
            self.contractExaminePage.click_more()

        with allure.step("我的合同界面输入合同名称"):
            self.contractExaminePage.input_contractNameQuery(contractDataDict['contractName'])

        with allure.step("我的合同界面输入合同编码"):
            self.contractExaminePage.input_contractCodeQuery(contractDataDict['contractCode'])

        with allure.step("我的合同界面点击查询按钮"):
            self.contractExaminePage.click_selectButton()

        with allure.step("断言查询结果是否为已经复核通过的合同"):
            assert self.contractExaminePage.getResultContractCodeMorePage() == contractDataDict['contractCode']

        with allure.step("断言查询结果, 合同状态是否正确"):
            assert self.contractExaminePage.getResultContractStatusMorePage() == '执行中'

        with allure.step("回到首页"):
            self.contractExaminePage.backToHomePage()
            self.contractExaminePage.closeCurrentWindows()




