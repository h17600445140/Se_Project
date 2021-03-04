# -*- coding:utf-8 -*-
"""

author      :   huangchao
fileName    :   util.py

"""

from time import strftime, localtime, time
from Lib.ShowapiRequest import ShowapiRequest
from PIL import Image
from logging import handlers

import logging
import datetime
import json
import pickle
import random
import string
import yaml
import os

from Util import config

# 初始化logger对象
def get_logger():
    # 初始化logger对象
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    path = os.path.dirname(os.path.dirname(__file__))
    allLogPath = os.sep.join([path, 'Log', 'allLogs', 'all.log'])
    errorLogPath = os.sep.join([path, 'Log', 'errorLogs', 'error.log'])

    # 记录所有的日志
    all_handler = handlers.TimedRotatingFileHandler(allLogPath, when='midnight', interval=1, backupCount=7,atTime=datetime.time(hour=0, minute=0, second=0, microsecond=0),encoding="UTF-8")
    all_handler.setFormatter(logging.Formatter("%(levelname)s - %(asctime)s - %(message)s"))
    # 记录错误级别以上的日志
    error_handler = logging.FileHandler(errorLogPath,encoding="UTF-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter("%(levelname)s - %(asctime)s - %(pathname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    # 将 handler 添加到 logger 中
    logger.addHandler(all_handler)
    logger.addHandler(error_handler)

    return logger


# 获取验证码（需要修改）
def get_code(driver, id) -> str:
    # 获取页面截图
    t1 = strftime("%Y-%m-%d-%H-%M-%S",localtime(time()))
    path1 = os.path.dirname(os.path.dirname(__file__)) + '/screenshots'
    screenshots_name = path1 + '/' + t1 + '.png'
    driver.save_screenshot(screenshots_name)

    # 获取验证码图片位置
    ce = driver.find_element_by_id(id)
    left = (ce.location['x'])
    top = (ce.location['y'])
    right = (ce.size['width']) + left
    height = (ce.size['height']) + top

    # 获取屏幕缩放比例
    dpr = driver.execute_script('return window.devicePixelRatio')

    # 抠图
    im = Image.open(screenshots_name)
    img = im.crop((left*dpr, top*dpr, right*dpr, height*dpr))

    # 保存截取到的验证码图片
    t2 = strftime("%Y-%m-%d-%H-%M-%S",localtime(time()))
    path2 = os.path.dirname(os.path.dirname(__file__)) + '/screenshots_code'
    screenshots_code_name = path2 + '/' + t2 + '.png'
    img.save(screenshots_code_name)

    # 通过第三方接口将验证码解析为code
    r = ShowapiRequest("http://route.showapi.com/184-4", "395676", "7cbf51451565431c937fd4397adef103")
    r.addFilePara("image", screenshots_code_name)
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()['showapi_res_body']
    code = text['Result']
    return code


# 生成16位随机字符串
def gen_random_str() -> str:
    random_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return random_str


# 保存cookie
def save_cookie(driver, path) -> None:
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


# 加载cookie
def load_cookie(driver, path) -> None:
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)


# 获取图片路径
def getPicturePath(state, time) -> str:
    if state == 'success':
        code = 'success_picture'
    else:
        code = 'wrong_picture'
    picture_path = os.path.join(config.imagePath() , code, time) + ".png"
    return picture_path


# 获取当前时间
def getNowTime():
    timeNow = strftime("%Y-%m-%d %H-%M-%S", localtime(time()))
    return timeNow


# 单例模式
def singleton(cls):
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


# 写入记录文件
def writeBoeNum(path, boeNum):
    with open(path, "r", encoding="UTF-8") as f:
        Rdata = json.load(f)
    Rdata["data"].update({'boeNum': boeNum})
    data = Rdata
    with open(path, "w", encoding="UTF-8") as f:
        json.dump(data, f)

def writeInvoiceNum(path, boeNum):
    with open(path, "r", encoding="UTF-8") as f:
        Rdata = json.load(f)
    Rdata["data"].update({'invoiceNum': boeNum})
    data = Rdata
    with open(path, "w", encoding="UTF-8") as f:
        json.dump(data, f)

# 读取记录文件
def readBoeNum(path):
    with open(path, "r", encoding="UTF-8") as f:
        Rdata = json.load(f)
    return Rdata['data']['boeNum']

def readInvoiceNum(path):
    with open(path, "r", encoding="UTF-8") as f:
        Rdata = json.load(f)
    return Rdata['data']['invoiceNum']


if __name__ == '__main__':
    print(os.path.dirname(os.path.dirname(__file__)))
    print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

