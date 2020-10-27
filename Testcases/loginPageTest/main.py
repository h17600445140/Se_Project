import os

# from Util.util import get_jsontestdata, get_datapath


# path = os.path.dirname(__file__)
# print(path)

# 测试打印出
# D:/Pycharm/自动化/SeleniumAutoProject/Testcases/loginPageTest
# conftest
# D:\Pycharm\自动化\SeleniumAutoProject\Testcases\loginPageTest
# 加载dataoath,传入当前test文件的工作路径

# path = get_datapath("D:\Pycharm\自动化\SeleniumAutoProject\Testcases\loginPageTest")
# print(path)


def get_datapath(path):
    a = path.split('Testcases')
    b = a[1].split('Test')
    data_path = a[0] + 'Data' + b[0] + 'Data' + b[0] + 'Data.json'
    return data_path






