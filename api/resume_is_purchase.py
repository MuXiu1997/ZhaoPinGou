from api.base_api import BaseAPI


class ResumeListIsPurchaseAPI(BaseAPI):
    api = '/api/find_warehouse_position_isRead_by_IdStr'

    def __init__(self, resume_str):
        self.payload = {'clientNo': '', 'clientType': 2, 'resumeStr': resume_str}
        super().__init__()

    def handler(self):
        return self.data.get('ResumeHtmlIsReadList')


def get_resume_list_is_purchase(token, resume_str):
    rl = ResumeListIsPurchaseAPI(resume_str)
    rl.run(token)
    return rl.handler()


def get_resume_id_is_purchase(resume):
    return resume.get('htmlId')
