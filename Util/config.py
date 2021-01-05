import os


class Config():

    def __init__(self):
        pass

    # 配置文件路径
    @classmethod
    def configPath(cls):
        return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"Config")


Config = Config()
