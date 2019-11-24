from api.base_api import BaseAPI


class ConvertBalance(BaseAPI):
    api = '/api/update_member_convert'
    payload = {'memberBalance': 50, 'number': 1, 'clientType': 2}

    def handler(self):
        code = self.data.get('errorCode')
        if code == 1:
            return True
        return False


def convert_balance(token):
    cb = ConvertBalance()
    cb.run(token)
    return cb.handler()
