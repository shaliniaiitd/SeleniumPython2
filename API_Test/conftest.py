import json
import pytest
import requests


@pytest.fixture
def supply_notes_url():
    return "https://practice.expandtesting.com"

@pytest.fixture
def create_notes_token():
    url = "https://practice.expandtesting.com/notes/api/users/login"
    data = {'email': 'abhinay.dixit@hotmail.com', 'password': 'pass@1234'}
    resp = requests.post(url, data=data)
    json_date = resp.json()
    j = json.dumps(json_date, indent=4)
    print(f'Value=', j)
    assert resp.status_code == 200
    assert json_date['message'] == "Login successful"
    token = json_date['data']['token']
    print(f'access_token={token}')
    return token
