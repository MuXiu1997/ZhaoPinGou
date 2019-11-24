from api.base_api import BaseAPI

SUCCESS = '您已成功解锁该简历'
UNLOCK = '贵公司已经解锁过该简历，请刷新页面查阅简历'


class UnlockResumeAPI(BaseAPI):
    api = '/api/zpg_charge_example_unlock_new'

    def __init__(self, resume_id, folder_id):
        self.payload = {'clientType': 2, 'notes': '', 'clientNo': '', 'jobId': 0, 'htmlCode': resume_id,
                        'mFolderId': folder_id}
        super().__init__()

    def handler(self):
        account = self.data.get('account')
        message = self.data.get('message')
        if account is None and message == UNLOCK:
            return False, -1, -1
        balance = account.get('sum_balance')
        free_count = account.get('sum_free_count')
        result = message == SUCCESS
        return result, balance, free_count


def unlock_resume(token, resume_id, folder_id):
    ur = UnlockResumeAPI(resume_id, folder_id)
    ur.run(token)
    return ur.handler()
