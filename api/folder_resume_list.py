from api.base_api import BaseApi

API = '/api/load_candidate_info_list_all'


def base_payload():
    return dict(
        pageSize=0,
        pageNo=1,
        keyStr='',
        keyType=-1,
        keyStrPostion='',
        key='',
        startDegrees=-1,
        endDegress=-1,
        startAge=0,
        endAge=0,
        gender=-1,
        region='',
        timeType=-1,
        startWorkYear=-1,
        endWorkYear=-1,
        beginTime='',
        endTime='',
        hopeAdressStr='',
        cityId=-1,
        child_user_id=-1,
        clientNo='',
        clientType=2
    )


def get_folder_resume_list(token, folder_id):
    payload = base_payload()
    payload.update({'folderId': folder_id})
    api = BaseApi(api=API, payload=payload, token=token)

    def handler(data):
        return data.get('total')

    api.add_handler(handler)
    total = api.run()

    payload.update({'pageNo': total})
    _api = BaseApi(api=API, payload=payload, token=token)

    def _handler(data):
        return data.get('warehouseList')

    _api.add_handler(_handler)

    return _api.run()
