# from time import sleep
from gevent import sleep

from log import logger, error_handler
from setting import BASE_URL, HEADERS
from utils import create_timestamp_querystring


class BaseAPI(object):
    base_url = BASE_URL
    headers = HEADERS
    api = NotImplemented
    payload = {}
    method = 'POST'

    def __init__(self):
        self.response = None

    @property
    def url(self):
        return self.base_url + self.api

    def request(self, token):
        user_token, session = token.export()
        self.payload.update({'userToken': user_token})
        return session.request(url=self.url, method=self.method, data=self.payload,
                               params=create_timestamp_querystring(), verify=False)

    def handler(self):
        raise NotImplementedError

    @property
    def data(self):
        return self.response.json()

    def run(self, token):
        while True:
            response = self.request(token)
            logger.info('url: {} class: {} status: {}'.format(self.url, type(self), response.status_code))
            try:
                data = response.json()
                if data.get('message') == '您的操作频繁，请稍后刷新再试' or data.get('errorCode') == 6:
                    logger.info('系统反馈操作频繁，程序将睡眠1分钟')
                    sleep(60)
                    sleep(1)
                else:
                    self.response = response
                    return
            except Exception as e:
                error_handler(e)
                raise e
