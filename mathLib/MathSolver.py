import requests


class MathSolver:
    def __init__(self, key):
        self.url = "https://math-solver2.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Host": "math-solver2.p.rapidapi.com",
            "X-RapidAPI-Key": key
        }

    def get_result(self, operation, f_num, s_num):
        url = self.url + operation

        res = "Wrong parameters!"
        if operation == "percentage":
            querystring = {"totalpercentage": "100", "number1": f_num, "number2": s_num}
            response = requests.request("GET", url, headers=self.headers, params=querystring)
            res = response.json()["percentage"]
        if operation == "subtraction":
            querystring = {"value": "[{},{}]".format(f_num, s_num)}
            response = requests.request("GET", url, headers=self.headers, params=querystring)
            res = response.json()["answer"]

        return res

    def calculate(self):
        print("Press:")
        print("1 - Calculate percentage")
        print("2 - Subtract two numbers")
        option = input()

        print("Pass first number:")
        f_num = input()

        print("Pass second number:")
        s_num = input()

        if option == '1':
            return self.get_result("percentage", f_num, s_num)
        if option == '2':
            return self.get_result("subtraction", f_num, s_num)
