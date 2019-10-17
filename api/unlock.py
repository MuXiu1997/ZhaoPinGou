from api.base_api import BaseApi

API = '/api/zpg_charge_example_unlock_new'

SUCCESS = '您已成功解锁该简历'
UNLOCK = '贵公司已经解锁过该简历，请刷新页面查阅简历'


def unlock_resume(token, resume_id, folder_id):
    payload = {'clientType': 2, 'notes': '', 'clientNo': '', 'jobId': 0, 'userToken': token, 'htmlCode': resume_id,
               'mFolderId': folder_id}

    api = BaseApi(api=API, payload=payload, token=token)

    def handler(data):
        account = data.get('account')
        message = data.get('message')
        if account is None and message == UNLOCK:
            return False, -1, -1
        balance = account.get('sum_balance')
        free_count = account.get('sum_free_count')
        result = message == SUCCESS
        return result, balance, free_count

    api.add_handler(handler)
    return api.run()
