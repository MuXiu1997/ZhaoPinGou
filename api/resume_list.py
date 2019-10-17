from api.base_api import BaseApi

API = '/api/find_warehouse_by_position_new'

payload = dict()
payload['pageSize'] = 0
payload['pageNo'] = 25
payload['keyStr'] = ''
payload['companyName'] = ''
payload['schoolName'] = ''
payload['keyStrPostion'] = ''
payload['postionStr'] = ''
payload['startDegrees'] = -1
payload['endDegress'] = -1
payload['startAge'] = 0
payload['endAge'] = 0
payload['gender'] = -1
payload['region'] = ''
payload['timeType'] = -1
payload['startWorkYear'] = -1
payload['endWorkYear'] = -1
payload['beginTime'] = ''
payload['endTime'] = ''
payload['isMember'] = 0
payload['hopeAdressStr'] = ''
payload['cityId'] = -1
payload['updateTime'] = ''
payload['tradeId'] = ''
payload['startDegreesName'] = ''
payload['endDegreesName'] = ''
payload['tradeNameStr'] = ''
payload['regionName'] = ''
payload['isC'] = 1
payload['is211_985_school'] = 0
payload['clientNo'] = ''
payload['clientType'] = 2


def get_resume_list(token, query=None):
    if query is None:
        query = dict()
    payload.update(query)
    print(payload)
    api = BaseApi(api=API, payload=payload, token=token)

    def handler(data):
        return data.get('warehouseList'), data.get('resumeStr')

    api.add_handler(handler)
    return api.run()


def get_resume_id(resume):
    return resume.get('resumeHtmlId')
