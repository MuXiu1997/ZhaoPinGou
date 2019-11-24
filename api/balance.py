from api.base_api import BaseAPI


class BalanceAPI(BaseAPI):
    api = '/api/user_information'
    payload = {'clientType': 2, 'isAjax': 1}

    def handler(self):
        balance = self.data.get('account').get('sum_balance')
        free_count = self.data.get('account').get('sum_free_count')
        return balance, free_count


def get_balance(token):
    b = BalanceAPI()
    b.run(token)
    return b.handler()
