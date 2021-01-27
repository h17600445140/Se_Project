# -*- coding:utf-8 -*-

"""

author      :   huangchao
fileName    :   dateConvert.py

"""


class DateConvert():

    January = '一月'
    February = '二月'
    March = '三月'
    April = '四月'
    May = '五月'
    June = '六月'
    July = '七月'
    August = '八月'
    September = '九月'
    October = '十月'
    November = '十一月'
    December = '十二月'

    @classmethod
    def dateConvert(self, num):

        if num == '1':
            return self.January
        elif num == '2':
            return self.February
        elif num == '3':
            return self.March
        elif num == '4':
            return self.April
        elif num == '5':
            return self.May
        elif num == '6':
            return self.June
        elif num == '7':
            return self.July
        elif num == '8':
            return self.August
        elif num == '9':
            return self.September
        elif num == '10':
            return self.October
        elif num == '11':
            return self.November
        elif num == '12':
            return self.December
        else:
            raise Exception("There is no such month, please enter the correct value")


dateConvert = DateConvert()
