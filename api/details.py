from lxml import etree

from api.base_api import BaseAPI
from log import error_handler

GENDER = ('男', '女')


class DetailsAPI(BaseAPI):
    api = '/api/zpg_find_resume_html_details'

    def __init__(self, resume_id):
        self.payload = {'resumeHtmlId': resume_id, 'keyStr': '', 'keyPositionName': '', 'tradeId': '', 'postionStr': '',
                        'jobId': 0, 'companyName': '', 'schoolName': '', 'clientNo': '', 'clientType': '2', }
        super().__init__()

    def handler(self, is_info=True):
        if is_info:
            info = process(self.data)
            return info


def process(data):
    resume = data.get('resumeHtml')
    json_html = data.get('jsonHtml')
    mobile = parse_label(json_html, '联系电话：')
    university, major = parse_university_major(json_html)
    info = dict(
        专业=major,
        姓名=resume.get('name'),
        学历=resume.get('degreesName'),
        学校=university,
        年龄=resume.get('age'),
        性别=GENDER[resume.get('gender')],
        意向岗位=parse_label(json_html, '期望职位：'),
        所在城市=parse_label(json_html, '现居地址：'),
        电话=mobile,
        邮箱=parse_label(json_html, '电子邮箱：'),
        运营商=distinguish_segments(mobile)
    )
    return info


def parse_university_major(json_html):
    try:
        html_elem = etree.HTML(json_html)
        div_elem = html_elem.xpath('//p[text()="教育经历"]/../../dd/div')[0]

        university = ''.join(div_elem.xpath('./span[2]/text()'))
        _major = div_elem.xpath('./span[position()>last()-3]/text()')
        for degrees_name in ['本科', '硕士', '博士', '大专']:
            if degrees_name in _major:
                _major.remove(degrees_name)
        major = ''.join(_major)
        return university, major
    except Exception as e:
        error_handler(e)
        return '', ''


def parse_label(json_html, label):
    text = ''
    try:
        html_elem = etree.HTML(json_html)
        text = ''.join(html_elem.xpath('//p[@class="ptxt"]/label[text()="{}"]/..//text()'.format(label)))
        text = text.replace(label, '')
    except Exception as e:
        error_handler(e)
    return text


def distinguish_segments(mobile):
    segment = ''
    if mobile[:4] in ['1700', '1701', '1702'] or mobile[:3] in ['133', '149', '153', '173', '177', '180', '181', '189',
                                                                '199']:
        segment = '电信'
    if mobile[:4] in ['1703', '1705', '1706'] or mobile[:3] in ['134', '135', '136', '137', '138', '139', '147', '150',
                                                                '151', '152', '157', '158', '159', '172', '178', '182',
                                                                '183', '184', '187', '188', '198']:
        segment = '移动'
    if mobile[:4] in ['1704', '1707', '1708', '1709'] or mobile[:3] in ['130', '131', '132', '145', '155', '156', '166',
                                                                        '171', '175', '176', '185', '186', '166']:
        segment = '联通'

    return segment


def get_info(token, resume_id):
    d = DetailsAPI(resume_id)
    d.run(token)
    return d.handler()


def read_resume(token, resume_id):
    d = DetailsAPI(resume_id)
    d.run(token)
    return d.handler(is_info=False)
