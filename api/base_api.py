import time

from log import logger
from setting import BASE_URL, HEADERS
from utils import create_timestamp_querystring


class BaseApi(object):
    base_url = BASE_URL

    headers = HEADERS

    def __init__(self, api, payload, token, method='POST'):
        self.url = self.base_url + api
        self.method = method
        self.payload = payload
        self.token = token
        self.handler = None

    def request(self):
        user_token, session = self.token.export()
        self.payload.update({'userToken': user_token})
        return session.request(url=self.url, method=self.method, data=self.payload,
                               params=create_timestamp_querystring())

    def add_handler(self, func):
        self.handler = func

    def run(self):
        while True:
            response = self.request()
            # logger.info(response.text)
            try:
                data = response.json()
                if data.get('message') == '您的操作频繁，请稍后刷新再试' or data.get('errorCode') == 6:
                    logger.info(data)
                    logger.info('系统反馈操作频繁，程序将睡眠1分钟')
                    time.sleep(61)
                else:
                    return self.handler(data)
            except Exception as e:
                logger.error(e)
                raise e
