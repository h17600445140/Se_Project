# -*- coding:utf-8 -*-
# import os
# import yaml
#
# path = os.path.dirname(__file__)
# yamlPath = os.sep.join([path, 'Config', 'test', 'UrlConfig.yml'])
# # yamlPath = os.path.join(path, 'Config', 'test', 'UrlConfig.yml')
# # yamlPath = path + '/' + 'Config' + '/' + 'test' + '/' + 'UrlConfig.yml'
# print(yamlPath)
#
# # open方法打开直接读出来
# with open(yamlPath, 'r', encoding='utf-8') as f:
#     cfg = f.read()
#     print(type(cfg))  # 读出来是字符串
#     print(cfg)
#
# d = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
# print(d)
# print(type(d))


# login_data = [
#     ('hctest', '123456', '账号密码不匹配'),
#     ('admin', 'zfs123456', '登陆成功')
# ]

# dict = {
#     "username": ["hcest", 'admin'],
#     "password": ["123456", "zfs123456"],
#     "casename": ["账号密码不匹配", "登陆成功"]
# }

# import json
# path = "D:\Pycharm\自动化\SeleniumAutoProject\Data\loginPageData\loginPageData.json"
# with open(path, encoding='UTF-8') as f:
#     data = json.load(f)
# list = [data[key] for key in data.keys()]
# new_list = [i for i in zip(*list)]
# print(new_list)

# def trans(l):
#     a = [[] for i in l[0]]
#     print(a)
#     for i in l:
#         for j in range(len(i)):
#             a[j].append(i[j])
#     return a
# print(trans(list))
from multiprocessing import Pool


def hhh(i):
    return i * 2


if __name__ == '__main__':
    pool = Pool(processes=2)
    hh = pool.map(hhh, [1, 2, 3, 4, 5, 6, 7, 8])
    print(hh)



