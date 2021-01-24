from time import sleep

from PageClass.common.boeInvoiceCommon import BoeInvoiceCommon

from Util import logger



# 火车票
class trainTickets():

    def __init__(self, driver, invoiceType, pageType):
        self._pageType = pageType
        if self._pageType == 'boeInvoicePage':
            self._oeInvoiceCommon = BoeInvoiceCommon(driver)
            self.invoiceType = invoiceType


    def getTickets(self, date, personType, personName, fromCity, toCity, siteType, ticketFee, isReplace):
        if self._pageType == 'boeInvoicePage':
            year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]

            self._oeInvoiceCommon.open_addInvoiceWindow(self.invoiceType)
            try:
                self._oeInvoiceCommon.select_itemtripDate(year, month, day)
            except Exception as e:
                logger.error("出现异常，异常信息为：{}".format(type(e)))
                self._oeInvoiceCommon.open_addInvoiceWindow(self.invoiceType)
                self._oeInvoiceCommon.select_itemtripDate(year, month, day)
            self._oeInvoiceCommon.select_itempersonnelAttribution(personType)
            self._oeInvoiceCommon.input_itempassengerName(personName)
            self._oeInvoiceCommon.input_itemstartOffCityName(fromCity)
            self._oeInvoiceCommon.input_itemarriveCityName(toCity)
            self._oeInvoiceCommon.select_itemseatLevel(siteType)
            self._oeInvoiceCommon.input_itemfee(ticketFee)
            self._oeInvoiceCommon.select_itemisReplacementTicket(isReplace)
            self._oeInvoiceCommon.click_invoiceSubmitButton()
            sleep(2)
            logger.info('新增火车票成功')



# 增值税普通发票
class VATInvoice():

    def __init__(self, driver, invoiceType, pageType):
        self._pageType = pageType
        if self._pageType == 'boeInvoicePage':
            self._boeInvoiceCommon = BoeInvoiceCommon(driver)
            self.invoiceType = invoiceType

    def getTickets(self, date, invoiceNo, invoiceCode, feeTotal, tax, checkCode):
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]
        if self._pageType == 'boeInvoicePage':
            self._boeInvoiceCommon.open_addInvoiceWindow(self.invoiceType)

            self._boeInvoiceCommon.input_invoiceNo(invoiceNo)

            self._boeInvoiceCommon.input_invoiceCode(invoiceCode)

            self._boeInvoiceCommon.selectInvoiceDate(year, month, day)

            self._boeInvoiceCommon.input_feeTotal(feeTotal)

            self._boeInvoiceCommon.input_tax(tax)

            self._boeInvoiceCommon.input_checkCode(checkCode)

            self._boeInvoiceCommon.click_invoiceSubmitButton()



class InvoiceFactory(object):

    def get_invoice(self, driver, invoiceType, pageType):

        if invoiceType == '火车票':
            return trainTickets(driver, invoiceType, pageType)

        if invoiceType == '增值税普通发票':
            return VATInvoice(driver, invoiceType, pageType)


invoiceFactory = InvoiceFactory()


