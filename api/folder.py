from api.base_api import BaseAPI
from utils import get_date_str


class AddFolderAPI(BaseAPI):
    api = '/api/add_candidate_folder'

    def __init__(self, folder_name):
        self.payload = {'clientNo': '', 'clientType': 2, 'folderName': folder_name}
        self.folder_name = folder_name
        super().__init__()

    def handler(self):
        return self.data.get('folderData').get('id'), self.folder_name


class FolderListAPI(BaseAPI):
    api = '/api/get_candidate_folder_list'
    payload = {'clientNo': '', 'clientType': 2, 'type': 1, 'keyStr': ''}

    def handler(self):
        return self.data.get('dataList')


def add_folder(token, folder_name):
    af = AddFolderAPI(folder_name)
    af.run(token)
    return af.handler()


def get_folder_id(token):
    folder_name = get_date_str()
    folder_id = folder_exist(token, folder_name)
    if folder_id:
        return folder_id, folder_name
    return add_folder(token, folder_name)


def folder_exist(token, folder_name):
    fl = FolderListAPI()
    fl.run(token)
    folder_list = fl.handler()
    for folder in folder_list:
        if folder.get('folder_name') == folder_name:
            return folder.get('id')
    return 0
