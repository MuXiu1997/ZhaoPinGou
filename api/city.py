from api.base_api import BaseAPI


class CityAPI(BaseAPI):
    api = '/api/get_city_all_by_key_str'

    def __init__(self, city_name):
        self.payload = {'clientNo': '', 'keyStr': city_name, 'clientType': 2}
        super().__init__()

    def handler(self):
        city_list = self.data.get('listDataCtiy')
        city = city_list[0]
        return city.get('id'), city.get('city_name')


def get_city_id(token, city):
    c = CityAPI(city)
    c.run(token)
    return c.handler()
