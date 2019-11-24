import json

from api import (get_resume_list, get_resume_list_is_purchase, get_resume_id_is_purchase, get_resume_id, unlock_resume,
                 get_city_id, get_folder_id, get_info, read_resume, convert_balance)
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
    return DEGREES.get(degrees)


def run_by_gender(token, number, gender, query, folder_id, ws):
    query['pageSize'] = 0
    query['gender'] = GENDER[gender]
    while number:
        resume_list, resume_str = get_resume_list(token, query)
        resume_list_is_purchase = get_resume_list_is_purchase(token, resume_str)
        resume_id_list_is_purchase = [get_resume_id_is_purchase(resume) for resume in resume_list_is_purchase]
        for resume in resume_list:
            if ws.closed:
                return
            resume_id = get_resume_id(resume)
            if resume_id in resume_id_list_is_purchase:
                continue
            else:
                read_resume(token, resume_id)
                result, balance, free_count = unlock_resume(token, resume_id, folder_id)
                if free_count < 100:
                    convert_balance(token)
                if result:
                    info = get_info(token, resume_id)
                    msg = json.dumps({'info': info})
                    ws.send(msg)
                    number -= 1
                    if number == 0:
                        return
        query['pageSize'] += 1


def run(data, ws):
    username = data.pop('username')
    password = data.pop('password')
    token = Token(username, password)

    man_number = data.pop('manNumber')
    woman_number = data.pop('womanNumber')

    city = data.pop('city')
    # city_query_list = city.split(' ')
    # city_list = [get_city_id(token, city_name) for city_name in city_query_list]
    # data['hopeAdressStr'] = ','.join([str(each_city[0]) for each_city in city_list])
    # data['regionName'] = ','.join([str(each_city[1]) for each_city in city_list])
    data['cityId'], _ = get_city_id(token, city)

    # email = data.pop('email')
    data['startDegreesName'] = get_degrees_name(data.get('startDegrees'))
    data['endDegreesName'] = get_degrees_name(data.get('endDegrees'))

    # 原网站拼写错误
    data['endDegress'] = data.pop('endDegrees')
    logger.info(('query:', data))

    folder_id, folder_name = get_folder_id(token)

    run_by_gender(token, man_number, '男', data, folder_id, ws)
    run_by_gender(token, woman_number, '女', data, folder_id, ws)

    # df = pd.DataFrame(output)
    # df.to_excel('./xlsx/{}'.format(work_name))
