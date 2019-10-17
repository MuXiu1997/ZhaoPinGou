from api.base_api import BaseApi

API = '/api/get_city_all_by_key_str'


def get_city_id(token, city_name):
    payload = {'clientNo': '', 'keyStr': city_name, 'clientType': 2}

    api = BaseApi(api=API, payload=payload, token=token)

    def handler(data):
        city_list = data.get('listDataCtiy')
        city = city_list[0]
        return city.get('id'), city.get('city_name')

    api.add_handler(handler)
    return api.run()
