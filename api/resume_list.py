from api.base_api import BaseAPI


class ResumeListAPI(BaseAPI):
    api = '/api/find_warehouse_by_position_new'
    payload = dict(
        pageSize=0,
        pageNo=25,
        keyStr='',
        companyName='',
        schoolName='',
        keyStrPostion='',
        postionStr='',
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
        isMember=0,
        hopeAdressStr='',
        cityId=-1,
        updateTime='',
        tradeId='',
        startDegreesName='',
        endDegreesName='',
        tradeNameStr='',
        regionName='',
        isC=1,
        is211_985_school=0,
        clientNo='',
        clientType=2
    )

    def __init__(self, query=None):
        if query is None:
            query = dict()
        self.payload.update(query)
        super().__init__()

    def handler(self):
        return self.data.get('warehouseList'), self.data.get('resumeStr')


def get_resume_list(token, query=None):
    rl = ResumeListAPI(query)
    rl.run(token)
    return rl.handler()


def get_resume_id(resume):
    return resume.get('resumeHtmlId')
