import requests

from log import logger, error_handler
from setting import BASE_URL, HEADERS
from utils import create_timestamp_querystring

API = "/api/security_login"


class Token(object):
    def __init__(self, username, password, session=None):
        self.__username = username
        self.__password = password
        self.__session = session or requests.session()
        self.__token = None
        self.get()

    def get(self):
        payload = {'clientType': 2}
        payload.update(dict(userName=self.__username, password=self.__password))
        response = self.__session.request(method='POST', url=BASE_URL + API, headers=HEADERS, data=payload,
                                          params=create_timestamp_querystring())
        try:
            data = response.json()
            user_token = data.get('user').get('user_token')
            logger.info('自动登录成功')
            self.__token = user_token
        except Exception as e:
            error_handler(e)

    def export(self):
        return self.__token, self.__session
