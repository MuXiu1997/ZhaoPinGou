from builtins import NotImplementedError

from api.base_api import BaseAPI


class FolderResumeListAPI(BaseAPI):
    api = '/api/load_candidate_info_list_all'
    payload = dict(
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

    def __init__(self, folder_id, page_on=None):
        self.payload.update({'folderId': folder_id})
        if page_on is not None:
            self.payload.update({'pageNo': page_on})
        super().__init__()

    def handler(self):
        raise NotImplementedError


class FolderResumeListTotalAPI(FolderResumeListAPI):
    def handler(self):
        return self.data.get('total')


class FolderResumeListWareHouseAPI(FolderResumeListAPI):
    def handler(self):
        return self.data.get('warehouseList')


def get_folder_resume_list(token, folder_id):
    t = FolderResumeListTotalAPI(folder_id)
    t.run(token)
    total = t.handler()
    wh = FolderResumeListWareHouseAPI(folder_id, total)
    wh.run(token)
    return wh.handler()
