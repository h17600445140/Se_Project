import json
import pickle
import random
import string
from time import strftime, localtime, time

import yaml

from Lib.ShowapiRequest import ShowapiRequest
from PIL import Image
import os


# 初始化logger对象
def get_logger():
    import logging
    import logging.handlers
    import datetime

    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    # 记录所有的日志
    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # 记录错误级别以上的日志
    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    # 将 handler 添加到 logger 中
    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)

    return logger


# 获取验证码
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
def get_jsontestdata(path) -> list:
    with open(path, encoding='UTF-8') as f:
        data = json.load(f)
    values = [data[key] for key in data.keys()]
    new_list = [i for i in zip(*values)]
    return new_list

# 获取 data_path
def get_datapath(path) -> str:
    a = path.split('Testcases')
    b = a[1].split('Test')
    data_path = a[0] + 'Data' + b[0] + 'Data' + b[0] + 'Data.json'
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



