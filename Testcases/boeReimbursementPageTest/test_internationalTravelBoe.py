# -*- coding:utf-8 -*-
from time import sleep

from PageClass.boeReimbursementPageClass.internationalTravelBoePage import InternationalTravelBoePage
from Testcases.common.boeBusinessApprove import BusinessApprove
from Testcases.common.boeSharingCenterApprove import SharingCenterApprove
from Testcases.common.loginDepend import LoginDepend
from Util import logger
from decimal import Decimal



class TestInternationalTravelBoe():

    boeNum = globals()

    def setup_class(self):
        self.login = LoginDepend('easHost', 'user')
        self.internationalTravelBoePage = InternationalTravelBoePage(self.login.driver)

    def teardown_class(self):
        # self.internationalTravelBoePage.driver.quit()
        pass

    def test_internationalTravel(self):
        sleep(1)
        self.internationalTravelBoePage.open_boeReimburse()
        sleep(1)
        self.internationalTravelBoePage.open_boe('差旅报账单（国际）', '差旅')

        sleep(1)
        # 切换窗口
        logger.info("当前窗口为：{}".format(self.internationalTravelBoePage.getCurrentWindowHandle()))
        logger.info("所有窗口为：{}".format(self.internationalTravelBoePage.getWindowHandles()))
        windowsList = self.internationalTravelBoePage.getWindowHandles()
        self.internationalTravelBoePage.switchToWin(windowsList[1])
        logger.info("当前窗口为：{}".format(self.internationalTravelBoePage.getCurrentWindowHandle()))

        sleep(1)
        global boeNum
        boeNum = self.internationalTravelBoePage.getBoeNum()
        logger.info("当前提单单据号为：{}".format(boeNum))

        self.internationalTravelBoePage.input_operationType('差旅')
        self.internationalTravelBoePage.input_boeAbstract('测试差旅报账单（国际）')

        # 费用归属区

        self.internationalTravelBoePage.selectDepartment('AD', 'A部门')

        self.internationalTravelBoePage.input_projectId('hc项目1')

        # 城市间交通费
        sleep(1)
        self.internationalTravelBoePage.click_cityTrafficExpenseAddButton()

        self.internationalTravelBoePage.select_isDomesticItineraryTraffic('是')

        self.internationalTravelBoePage.input_operationSubTypeIdTraffic('差旅交通')

        self.internationalTravelBoePage.select_travelerEmpIdTraffic()

        self.internationalTravelBoePage.input_beginDateStrTraffic('15')

        self.internationalTravelBoePage.input_fromCityTraffic('长沙')

        sleep(1)
        self.internationalTravelBoePage.input_toCityTraffic('北京')

        sleep(1)
        self.internationalTravelBoePage.select_transportationTraffic('二等座（高铁/动车）')

        self.internationalTravelBoePage.select_useCurrencyCodeTraffic('CNY')

        self.internationalTravelBoePage.input_useCurrencyAmountTraffic('100.10')

        self.internationalTravelBoePage.input_rateValueTraffic('1.11')

        self.internationalTravelBoePage.input_totalPriceTraffic('10.10')

        self.internationalTravelBoePage.input_fuelSurchargeTraffic('10.00')

        # 住宿

        self.internationalTravelBoePage.click_hotelExpenseAddButton()

        self.internationalTravelBoePage.input_operationSubTypeIdHotel('差旅住宿')

        self.internationalTravelBoePage.input_beginDateStrHotel('15')

        self.internationalTravelBoePage.input_endDateStrHotel('20')

        self.internationalTravelBoePage.input_sitePlaceHotel('北京')

        sleep(1)
        self.internationalTravelBoePage.input_hotelDayHotel('5')

        self.internationalTravelBoePage.select_useCurrencyCodeHotel('CNY')

        self.internationalTravelBoePage.input_useCurrencyAmountHotel('500.50')

        self.internationalTravelBoePage.input_rateValueHotel('1.11')

        # 补贴

        self.internationalTravelBoePage.input_operationSubTypeIdSubsidy('差旅补贴')

        self.internationalTravelBoePage.input_subsidyDaySubsidy('5')

        self.internationalTravelBoePage.input_sitePlaceSubsidy('北京')

        sleep(1)
        self.internationalTravelBoePage.select_useCurrencyCodeSubsidy('CNY ')

        self.internationalTravelBoePage.input_useCurrencyAmountSubsidy('500.55')

        self.internationalTravelBoePage.input_rateValueSubsidy('1.11')

        # 其他

        self.internationalTravelBoePage.input_operationSubTypeIdOther('差旅其他')

        self.internationalTravelBoePage.select_useCurrencyCodeOther('CNY')

        self.internationalTravelBoePage.input_useCurrencyAmountOther('500.55')

        self.internationalTravelBoePage.input_rateValueOther('1.11')

        self.internationalTravelBoePage.input_remarkOther('测试')

        # 总金额
        totalAmountTraffic = self.internationalTravelBoePage.get_totalAmountTraffic()
        logger.info("城市间交通费报账金额为：{}".format(totalAmountTraffic))
        totalAmountHotel = self.internationalTravelBoePage.get_totalAmountHotel()
        logger.info("住宿费报账金额为：{}".format(totalAmountHotel))
        totalAmountSubsidy = self.internationalTravelBoePage.get_totalAmountSubsidy()
        logger.info("补贴金额为：{}".format(totalAmountSubsidy))
        totalAmountOther = self.internationalTravelBoePage.get_totalAmountOther()
        logger.info("其他金额为：{}".format(totalAmountOther))
        totalAmount = Decimal(totalAmountTraffic) + Decimal(totalAmountHotel) + Decimal(totalAmountSubsidy) + Decimal(totalAmountOther)
        logger.info('总金额为：{}'.format(str(totalAmount)))
        self.internationalTravelBoePage.input_expenseAmount(str(totalAmount))

        # 支付区

        self.internationalTravelBoePage.input_paymentAmount(str(totalAmount))

        self.internationalTravelBoePage.input_paymentMemo('测试')

        sleep(1)
        self.internationalTravelBoePage.click_boeSubmitButton()
        sleep(3)
        self.internationalTravelBoePage.click_close()

        logger.info("单据流程结束")
        windowsList = self.internationalTravelBoePage.getWindowHandles()
        self.internationalTravelBoePage.switchToWin(windowsList[0])

    def test_businessApprove(self):
        global boeNum
        self.businessApprove = BusinessApprove(boeNum)
        content = self.businessApprove.boeBusinessApprove()

        assert content == '审批成功'

    def test_sharingCenterApprove(self):
        global boeNum
        self.sharingCenterApprove = SharingCenterApprove(boeNum)
        self.sharingCenterApprove.sharingCenterApproveChuShen()
        self.sharingCenterApprove.sharingCenterApproveFuShen()















