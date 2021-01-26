# -*- coding:utf-8 -*-
import allure
from PageClass.cmsIndexPageClass.contractEditPage import ContractEditPage
from Testcases.common.loginDepend import LoginDepend
from Util import logger, record


@allure.feature("新建合同流程")
class TestContractEditPage(object):


    def setup_class(self):
        self.login = LoginDepend('cmsHost', 'user')
        self.contractEditPage = ContractEditPage(self.login.driver)

    def teardown_class(self):
        # self.cmsIndexPage.driver.quit()
        pass

    @allure.story("新建合同流程")
    @allure.step("新建合同操作步骤")
    @allure.severity("blocker")
    def test_cmsIndex(self, contractEditPage_testdata):

        logger.info(" ----- 合同新建流程开始 ----- ")
        with allure.step("打开合同管理合同录入页面"):
            self.contractEditPage.getIntoPage('合同录入')
        with allure.step("输入合同名称"):
            self.contractEditPage.input_contractName(contractEditPage_testdata['contractName'])
        with allure.step("输入合同编号"):
            self.contractEditPage.input_contractCode(contractEditPage_testdata['contractCode'])
        with allure.step("选择合同类型"):
            self.contractEditPage.selectContractType(contractEditPage_testdata['contractType'])
        with allure.step("输入合同总金额"):
            self.contractEditPage.input_contractAmount(contractEditPage_testdata['contractAmount'])
        with allure.step("选择合同币种"):
            self.contractEditPage.selectCurrency(contractEditPage_testdata['currency']['currencyCode'])
        with allure.step("选择客商类型"):
            self.contractEditPage.selectVendorType(contractEditPage_testdata['vendorType'])
        with allure.step("选择客商"):
            self.contractEditPage.selectVendorName(contractEditPage_testdata['vendor']['vendorCode'])
        with allure.step("选择签订日期"):
            self.contractEditPage.input_signDate(contractEditPage_testdata['signDate'])
        with allure.step("选择合同开始时间"):
            self.contractEditPage.input_contractDataFrom(contractEditPage_testdata['contractDataFrom'])
        with allure.step("选择合同结束时间"):
            self.contractEditPage.input_contractDataTo(contractEditPage_testdata['contractDataTo'])
        with allure.step("选择报账人"):
            self.contractEditPage.selectResUser(contractEditPage_testdata['respUser']['respUserNo'])
        with allure.step("选择合同责任部门"):
            self.contractEditPage.selectDept(contractEditPage_testdata['respDept']['respDeptNo'], deptName = contractEditPage_testdata['respDept']['respDeptCode'])
        with allure.step("选择合同范围"):
            self.contractEditPage.selectContractScope(contractEditPage_testdata['contractScope'])
        with allure.step("选择是否框架合同"):
            self.contractEditPage.selectFrameworkContract(contractEditPage_testdata['frameworkContract'])
        with allure.step("是否有影像"):
            self.contractEditPage.selectHaveImage(contractEditPage_testdata['haveImage'])

        with allure.step("判断是否为框架合同"):
            if contractEditPage_testdata['frameworkContract'] == '否':

                for i in range(len(contractEditPage_testdata['paymentDetail'])):
                    with allure.step("选择款项性质"):
                        self.contractEditPage.selectPaymentType(contractEditPage_testdata['paymentDetail'][i]['paymentType'])
                    with allure.step("输入结算条件"):
                        self.contractEditPage.input_paymentCondition(contractEditPage_testdata['paymentDetail'][i]['paymentCondition'])
                    with allure.step("选择计划执行时间"):
                        self.contractEditPage.input_plansDate(contractEditPage_testdata['paymentDetail'][i]['plansDate'])
                    with allure.step("选择结算单位"):
                        self.contractEditPage.selectSettlementUnit(contractEditPage_testdata['paymentDetail'][i]['settlementUnit'])
                    with allure.step("输入结算金额"):
                        self.contractEditPage.input_settlementAmount(contractEditPage_testdata['paymentDetail'][i]['settlementAmount'])
                    with allure.step("选择控制方式"):
                        self.contractEditPage.selectPaymentCondition(contractEditPage_testdata['paymentDetail'][i]['controlType'])
                    with allure.step("选择支付方式"):
                        self.contractEditPage.selectPaymentMethod(contractEditPage_testdata['paymentDetail'][i]['paymentMethod'])

                    if i != (len(contractEditPage_testdata['paymentDetail'])-1):
                        with allure.step("点击新增按钮"):
                            self.contractEditPage.click_addPaymentPlan()

        with allure.step("点击提交按钮"):
            self.contractEditPage.click_submitButton()

            # 将合同写入记录文件
            with allure.step("记录合同,合同名称/编号为 : {} - {}".format(contractEditPage_testdata['contractName'], contractEditPage_testdata['contractCode'])):
                if contractEditPage_testdata['frameworkContract'] == '否':
                    contractDict = {'noFrameworkContractName':contractEditPage_testdata['contractName'],
                                    'noFrameworkContractCode':contractEditPage_testdata['contractCode']}
                    record.writeDataToRecord(contractDict, type='contractData')
                elif contractEditPage_testdata['frameworkContract'] == '是':
                    contractDict = {'frameworkContractName': contractEditPage_testdata['contractName'],
                                    'frameworkContractCode': contractEditPage_testdata['contractCode']}
                    record.writeDataToRecord(contractDict, type='contractData')

        with allure.step("点击确认按钮"):
            self.contractEditPage.click_confirmButoon()












