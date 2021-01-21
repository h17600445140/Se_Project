from time import sleep

from PageClass.easIndexPageClass.easMyInvoicePage import EasMyInvoiceIndexPage
from Util import logger



# 火车票
class trainTickets():

    def __init__(self, driver, invoiceType):
        self._easMyInvoiceIndexPage = EasMyInvoiceIndexPage(driver)
        self.invoiceType = invoiceType

    def getTickets(self, date, personType, personName, fromCity, toCity, siteType, ticketFee, isReplace):
        year, month, day = date.split('-')[0], date.split('-')[1], date.split('-')[2]

        self._easMyInvoiceIndexPage.open_addInvoiceWindow(self.invoiceType)
        try:
            self._easMyInvoiceIndexPage.select_itemtripDate(year, month, day)
        except Exception as e:
            logger.error("出现异常，异常信息为：{}".format(type(e)))
            self._easMyInvoiceIndexPage.open_addInvoiceWindow(self.invoiceType)
            self._easMyInvoiceIndexPage.select_itemtripDate(year, month, day)
        self._easMyInvoiceIndexPage.select_itempersonnelAttribution(personType)
        self._easMyInvoiceIndexPage.input_itempassengerName(personName)
        self._easMyInvoiceIndexPage.input_itemstartOffCityName(fromCity)
        self._easMyInvoiceIndexPage.input_itemarriveCityName(toCity)
        self._easMyInvoiceIndexPage.select_itemseatLevel(siteType)
        self._easMyInvoiceIndexPage.input_itemfee(ticketFee)
        self._easMyInvoiceIndexPage.select_itemisReplacementTicket(isReplace)
        self._easMyInvoiceIndexPage.click_invoiceSubmitButton()



class InvoiceFactory(object):

    def get_invoice(self, driver, invoiceType):

        if invoiceType == '火车票':
            return trainTickets(driver, invoiceType)

invoiceFactory = InvoiceFactory()


