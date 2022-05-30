import requests


class Countries:
    def __init__(self, key):
        self.headers = {
            'X-RapidAPI-Host': 'countries-cities.p.rapidapi.com',
            'X-RapidAPI-Key': key
        }

    @staticmethod
    def get_value_from_json(obj):
        array = []
        for key, value in obj.items():
            array.append(value)
        return array

    def get_by_code(self, code, info_name):
        url = "https://countries-cities.p.rapidapi.com/location/country/" + code
        response = requests.request("GET", url, headers=self.headers)
        value = response.json()[info_name]
        return value

    def get_info(self):
        print("Country code:")
        code = input()

        print("Press:")
        print("1 - population")
        print("2 - territories")
        print("3 - area size")
        print("4 - phone code")
        option = input()

        if option == '1':
            return self.get_by_code(code, 'population')
        if option == '2':
            return self.get_value_from_json(self.get_by_code(code, 'territories'))
        if option == '3':
            return self.get_by_code(code, 'area_size')
        if option == '4':
            return self.get_by_code(code, 'phone_code')



    def get_all(self):
        url = "https://countries-cities.p.rapidapi.com/location/country/list"
        querystring = {"format": "json"}

        response = requests.request("GET", url, headers=self.headers, params=querystring)

        obj = response.json()['countries']

        return self.get_value_from_json(obj)
