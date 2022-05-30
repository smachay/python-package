class Calculate:
    @staticmethod
    def pow(number, n):
        result = 1
        for i in range(n):
            result *= number
        return result

    @staticmethod
    def miles_to_kilometers(distance):
        return distance * 1.609

    @staticmethod
    def kilometers_to_miles(distance):
        return distance * 0.621

    @staticmethod
    def celsius_to_kelvin(temp):
        return temp + 273.15

    @staticmethod
    def kelvin_to_celsius(temp):
        return temp - 273.15
