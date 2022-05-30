import requests


class Cities:
    def __init__(self, key):
        self.url = "https://andruxnet-world-cities-v1.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Host": "andruxnet-world-cities-v1.p.rapidapi.com",
            "X-RapidAPI-Key": key
        }

    def get_by_name(self, city, country):
        querystring = {"query": city, "searchby": "city"}
        response = requests.request("GET", self.url, headers=self.headers, params=querystring)
        obj = response.json()
        arr = []
        for city in obj:
            if city["country"] == country:
                arr.append(city)
        return arr

    def get_all(self, country):
        querystring = {"query": country, "searchby": "country"}
        response = requests.request("GET", self.url, headers=self.headers, params=querystring)
        obj = response.json()
        array = []
        for city in obj:
            for k, v in city.items():
                if k == 'city':
                    array.append(v)
        return array

    def get_info(self):

        print("Press:")
        print("1 - Cities in the given country")
        print("2 - City details")
        option = input()

        if option == '1':
            print("Country name:")
            country = input()
            return self.get_all(country)
        if option == '2':
            print("City name:")
            city = input()
            print("Country name:")
            country = input()
            return self.get_by_name(city, country)


