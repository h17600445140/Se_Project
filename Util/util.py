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


# 生成随机字符串
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


# 加载 Data 目录下json数据
# ----- old version -----[(param1,param2,param3),(param11,param22,param33)]
# def get_jsontestdata(path) -> list:
#     with open(path, encoding='UTF-8') as f:
#         data = json.load(f)
#     values = [value for value in data.values()]
#     case_name = data.get("casename")
#     new_list = [i for i in zip(*values)]
#     return new_list,case_name
# ----- new version -----
def get_jsontestdata(path,suitename) -> (dict,list):
    with open(path, encoding='UTF-8') as f:
        data = json.load(f)
        casename = [data[suitename][i]["casename"] for i in range(len(data[suitename]))]
    return data[suitename],casename

def get_ymltestdata(path,suitename) -> (dict,list):
    with open(path, 'r', encoding='utf-8') as f:
        cfg = f.read()
    data = yaml.load(cfg, Loader=yaml.FullLoader)
    casename = [data[suitename][i]["casename"] for i in range(len(data[suitename]))]
    return data[suitename],casename

# 获取 data_path
def get_datapath(path) -> str:
    a = path.split('Testcases')
    b = a[1].split('Test')
    data_path = a[0] + 'Data' + b[0] + 'Data' + b[0] + 'Data.json'
    return data_path

def get_ymldatapath(path) -> str:
    a = path.split('Testcases')
    b = a[1].split('Test')
    data_path = a[0] + 'Data' + b[0] + 'Data' + b[0] + 'Data.yml'
    return data_path


# 获取url文件
def get_urldict() -> dict:
    path = os.path.dirname(os.path.dirname(__file__))
    yamlPath = os.sep.join([path, 'Config', 'test', 'testUrl_config.yml'])
    with open(yamlPath, 'r', encoding='utf-8') as f:
        cfg = f.read()
    d = yaml.load(cfg, Loader=yaml.FullLoader)
    # print(d)    # {'url': {'host': 'http://fsscysc.csztessc.com.cn:8085/'}}
    return d


# 获取图片路径
def get_picture_path(state,time) -> str:
    if state == 'success':
        code = 'success_picture'
    else:
        code = 'wrong_picture'
    path = os.path.dirname(os.path.dirname(__file__))
    picture_path = os.sep.join([path, 'Image', code, time]) + ".png"
    return picture_path



