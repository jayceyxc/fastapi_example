import requests
import json


class TestClass(object):
    def __init__(self):
        super().__init__()
        self.server_address = 'http://127.0.0.1:8000/'
        self.insert_url = 'insert'

    def test_insert_case_right(self, test_url):
        people = {
            'name': '俞学城',
            'age': '56',
            'address': '杭州',
            'salary': 999999
        }
        response = requests.post(test_url, json=people)
        print(response.status_code)
        print(response.text)

    def test_insert_case_no_name(self, test_url):
        people = {
            'age': 27,
            'address': '杭州',
            'salary': 999999
        }
        response = requests.post(test_url, json=people)
        print(response.status_code)
        print(response.text)

    def test_insert_case_age_format_error(self, test_url):
        people = {
            'name': '俞学城',
            'age': '二十七',
            'address': '杭州',
            'salary': 999999
        }
        response = requests.post(test_url, json=people)
        print(response.status_code)
        print(response.text)


if __name__ == '__main__':
    testClass = TestClass()
    test_url = testClass.server_address + testClass.insert_url
    testClass.test_insert_case_right(
        test_url=test_url)
    testClass.test_insert_case_no_name(
        test_url=test_url)
    testClass.test_insert_case_age_format_error(
        test_url=test_url
    )
