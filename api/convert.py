from api.base_api import BaseApi

API = '/api/update_member_convert'


def convert_balance(token):
    payload = {'memberBalance': 50, 'number': 1, 'clientType': 2}

    api = BaseApi(api=API, payload=payload, token=token)

    def handler(data):
        code = data.get('errorCode')
        if code == 1:
            return True
        return False

    api.add_handler(handler)
    return api.run()
