from threading import Thread
from time import time

import requests


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()  # 因为父类的初始值无法继承，需要调用下父类构造函数
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/douyakang-impr/Downloads/video' + filename, 'wb') as f:
            f.write(resp.content)
