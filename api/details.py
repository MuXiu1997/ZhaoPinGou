import re

from lxml import etree

from api.base_api import BaseApi
from log import logger

API = '/api/warehouse_share_info'

GENDER = ('男', '女')


def parse_major(json_html):
    try:
        html_elem = etree.HTML(json_html)
        div_elem = html_elem.xpath('//dd/div[@class="experience"]')[0]
        _major = div_elem.xpath('./p/span/text()')
        for degrees_name in ['本科', '硕士', '博士', '大专']:
            if degrees_name in _major:
                _major.remove(degrees_name)
        major = ''.join(_major)
        return major
    except Exception as e:
        logger.error(e)
        return ''


def process(data):
    resume = data.get('resumeHtml')
    json_html = data.get('jsonHtml')

    info = dict(
        专业=parse_major(json_html),
        姓名=resume.get('name'),
        学历=resume.get('degreesName'),
        学校=resume.get('universityName'),
        年龄=resume.get('age'),
        性别=GENDER[resume.get('gender')],
        意向岗位=resume.get('hopePosition'),
        所在城市=resume.get('hopeAddress'),
        电话=resume.get('mobile'),
        邮箱=resume.get('email'),
    )
    return info


def get_share_id(share_url):
    r = re.compile(r'.*?\?id=(.*)')
    share_id = r.search(share_url).group(1)
    return share_id


def get_info(token, share_url):
    share_id = get_share_id(share_url)
    payload = {'htmlId': share_id}
    api = BaseApi(api=API, payload=payload, token=token)

    def handler(data):
        info = process(data)
        return info

    api.add_handler(handler)
    return api.run()
