import token

import pytest
import requests
import json


def get_data():
    return [
        ["Title_1", "User1", "Home"],
        ["Title_2", "User2", "Work"],
        ["Title_3", "User3", "Personal"]
    ]

@pytest.fixture(scope='class')
def create_token(request):
    url = "https://practice.expandtesting.com/notes/api/users/login"
    data = {'email': 'abhinay.dixit@hotmail.com', 'password': 'pass@1234'}
    resp = requests.post(url, json=data)
    json_date = resp.json()
    j = json.dumps(json_date, indent=4)
    print(f'Value=', j)
    assert resp.status_code == 200
    assert json_date['message'] == "Login successful"
    request.cls.token = json_date['data']['token']
    print(f'access_token={request.cls.token}')

@pytest.mark.usefixtures("create_token")
class BasicTest:
    pass

@pytest.mark.parametrize("title, des, category", get_data())
class Test_Notes_Fixture(BasicTest):
    def test_create_notes_fix(self, title, des, category):
        #print(create_token)
        url = "https://practice.expandtesting.com/notes/api/notes"
        # Set up the headers
        headers = {
            'Content-Type': 'application/json',
            'x-auth-token': self.token
        }
        data = {
            "title": title,
            "description": des,
            "category": category
        }
        # json_payload = json.dumps(data)
        resp = requests.post(url, json=data, headers=headers)
        print(resp)
        json_data = resp.json()
        j = json.dumps(json_data, indent=4)
        print("response body:", j)
        assert resp.status_code == 200
        assert json_data['data']['title'] == title
        add_id = json_data['data']['id']
        print(f'add_id={add_id}')