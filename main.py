# import os
# import yaml
#
# path = os.path.dirname(__file__)
# yamlPath = os.sep.join([path, 'Config', 'test', 'testUrl_config.yml'])
# # yamlPath = os.path.join(path, 'Config', 'test', 'testUrl_config.yml')
# # yamlPath = path + '/' + 'Config' + '/' + 'test' + '/' + 'testUrl_config.yml'
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


# if __name__ == '__main__':
#     print('111')

