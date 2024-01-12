import pytest
import requests
import json
import pprint

@pytest.fixture()
def main_url():
    return "https://reqres.in/"


def test_valid_login(main_url):

    url = main_url+"api/login/"

    data = {'email': 'eve.holt@reqres.in','password': 'cityslicka'}

    response = requests.get(url, data=data)
    token = json.loads(response.text)


    print(token['page'])
    assert response.status_code == 200
    #    sassert token['token'] == 'QpwL5tke4Pnpja7X4'

    pprint.pp((token))
    print(len(token))
    print("===========")
    pprint.pprint(token['data'][0]['color'])

    pprint.pprint(token["data"][1]['color'])
    pprint.pprint(token["data"][2]['color'])

    for i in range(4):
        print(token["data"][i]['color'])

