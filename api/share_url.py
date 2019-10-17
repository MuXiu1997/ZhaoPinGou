from api.base_api import BaseApi

API = '/api/zpg_find_resume_html_details'


def get_share_url(token, resume_id):
    payload = {'resumeHtmlId': resume_id, 'keyStr': '', 'keyPositionName': '', 'tradeId': '', 'postionStr': '',
               'jobId': 0, 'companyName': '', 'schoolName': '', 'clientNo': '', 'clientType': '2', }

    api = BaseApi(api=API, payload=payload, token=token)

    def handler(data):
        is_purchase = data.get('isPurchase') == 1
        share_url = data.get('shareUrl')
        return is_purchase, share_url

    api.add_handler(handler)
    return api.run()
