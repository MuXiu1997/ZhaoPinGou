from api.base_api import BaseAPI


class DetailsAPI(BaseAPI):
    api = '/api/zpg_find_resume_html_details'

    def __init__(self, resume_id):
        self.payload = {'resumeHtmlId': resume_id, 'keyStr': '', 'keyPositionName': '', 'tradeId': '', 'postionStr': '',
                        'jobId': 0, 'companyName': '', 'schoolName': '', 'clientNo': '', 'clientType': '2', }
        super().__init__()

    def handler(self):
        raise NotImplementedError
        # is_purchase = self.data.get('isPurchase') == 1
        # share_url = self.data.get('shareUrl')
        # return is_purchase, share_url


class DetailsIsPurchase(DetailsAPI):
    def handler(self):
        is_purchase = self.data.get('isPurchase') == 1
        return is_purchase


def get_resume_is_purchase(token, resume_id):
    su = DetailsIsPurchase(resume_id)
    su.run(token)
    return su.handler()
