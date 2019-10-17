import pandas as pd

from api import (get_resume_list, get_resume_list_is_purchase, get_resume_id_is_purchase, get_resume_id, get_share_url,
                 unlock_resume, get_city_id, get_folder_id, get_info)
from auth import Token
from log import logger
from setting import DEGREES, GENDER


# def get_query():
#     return {
#         'pageSize': 0,
#
#         'startDegrees': DEGREES['本科'],
#         'endDegress': DEGREES['及以上'],
#         'startDegreesName': '本科',
#         'endDegreesName': '及以上',
#
#         'startAge': 20,
#         'endAge': 28,
#
#         'hopeAdressStr': '1,6,13',
#         'regionName': '北京市,天津市,张家口市',
#
#         'gender': GENDER['男'],
#
#         'startWorkYear': WORK_YEAR['无经验'],
#         'endWorkYear': WORK_YEAR['2年'],
#     }

def get_degrees_name(degrees):
    for k, v in DEGREES.items():
        if v == degrees:
            return k


def run_by_gender(token, number, gender, query, folder_id, share_url_list):
    query['pageSize'] = 0
    query['gender'] = GENDER[gender]
    while number:
        resume_list, resume_str = get_resume_list(token, query)
        print(resume_list)
        resume_list_is_purchase = get_resume_list_is_purchase(token, resume_str)
        resume_id_list_is_purchase = [get_resume_id_is_purchase(resume) for resume in resume_list_is_purchase]
        for resume in resume_list:
            resume_id = get_resume_id(resume)
            if resume_id in resume_id_list_is_purchase:
                continue
            else:
                print(resume_id)
                is_purchase, share_url = get_share_url(token, resume_id)
                print('is_purchase', is_purchase)
                result, balance, free_count = unlock_resume(token, resume_id, folder_id)
                print(result, balance, free_count)
                if result:
                    share_url_list.append(share_url)
                    number -= 1
                    if number == 0:
                        return
        query['pageSize'] += 1
        print(query['pageSize'])


def run(data):
    work_name = data.pop('work')

    username = data.pop('username')
    password = data.pop('password')
    token = Token(username, password)

    man_number = data.pop('manNumber')
    woman_number = data.pop('womanNumber')

    city = data.pop('city')
    city_query_list = city.split(' ')
    city_list = [get_city_id(token, city_name) for city_name in city_query_list]
    data['hopeAdressStr'] = ','.join([str(each_city[0]) for each_city in city_list])
    data['regionName'] = ','.join([str(each_city[1]) for each_city in city_list])

    # email = data.pop('email')
    data['startDegreesName'] = get_degrees_name(data.get('startDegrees'))
    data['endDegreesName'] = get_degrees_name(data.get('endDegrees'))

    # 原网站拼写错误
    data['endDegress'] = data.pop('endDegrees')
    logger.info(('query:', data))

    share_url_list = []
    output = []

    folder_id, folder_name = get_folder_id(token)

    run_by_gender(token, man_number, '男', data, folder_id, share_url_list)
    run_by_gender(token, woman_number, '女', data, folder_id, share_url_list)

    for share_url in share_url_list:
        info = get_info(token, share_url)
        logger.info(info)
        output.append(info)

    df = pd.DataFrame(output)
    df.to_excel('./xlsx/{}.xlsx'.format(work_name))