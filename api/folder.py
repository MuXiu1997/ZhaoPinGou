from api.base_api import BaseApi
from utils import get_date_str

API_GET = '/api/get_candidate_folder_list'
API_ADD = '/api/add_candidate_folder'


def add_folder(token, folder_name):
    payload = {'clientNo': '', 'clientType': 2, 'folderName': folder_name}

    api = BaseApi(api=API_ADD, payload=payload, token=token)

    def handler(data):
        return data.get('folderData').get('id'), folder_name

    api.add_handler(handler)
    return api.run()


def get_folder_id(token):
    folder_name = get_date_str()
    folder_id = folder_exist(token, folder_name)
    if folder_id:
        return folder_id, folder_name
    return add_folder(token, folder_name)


def folder_exist(token, folder_name):
    payload = {'clientNo': '', 'clientType': 2, 'type': 1, 'keyStr': ''}

    api = BaseApi(api=API_GET, payload=payload, token=token)

    def handler(data):
        folder_list = data.get('dataList')

        for folder in folder_list:
            if folder.get('folder_name') == folder_name:
                return folder.get('id')
        return 0

    api.add_handler(handler)
    return api.run()
