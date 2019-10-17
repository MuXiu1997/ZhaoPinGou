from api.base_api import BaseApi

API = '/api/find_warehouse_position_isRead_by_IdStr'


def get_resume_list_is_purchase(token, resume_str):
    payload = {'clientNo': '', 'clientType': 2, 'resumeStr': resume_str}
    api = BaseApi(api=API, payload=payload, token=token)

    def handler(data):
        return data.get('ResumeHtmlIsReadList')

    api.add_handler(handler)
    return api.run()


def get_resume_id_is_purchase(resume):
    return resume.get('htmlId')
