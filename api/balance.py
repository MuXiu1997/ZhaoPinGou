from api.base_api import BaseApi

API = '/api/user_information'


def get_balance(token):
    payload = {'clientType': 2, 'isAjax': 1}
    api = BaseApi(api=API, payload=payload, token=token)

    def handler(data):
        balance = data.get('account').get('sum_balance')
        free_count = data.get('account').get('sum_free_count')
        return balance, free_count

    api.add_handler(handler)
    return api.run()
