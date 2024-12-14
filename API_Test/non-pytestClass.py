import pytest
import requests
import json


class Notes:

    def __init__(self):
        self.token = None
        self.add_id = None

    def test_refresh_token(self):
        url = "https://practice.expandtesting.com/notes/api/users/login"
        data = {'email': 'abhinay.dixit@hotmail.com', 'password': 'pass@1234'}
        resp = requests.post(url, json=data)
        json_date = resp.json()
        j = json.dumps(json_date, indent=4)
        print(f'Value=', j)
        assert resp.status_code == 200
        assert json_date['message'] == "Login successful"
        self.token = json_date['data']['token']
        print(f'access_token={self.token}')
        # return self.token

    def test_create_notes(self):
        self.test_refresh_token()
        url = "https://practice.expandtesting.com/notes/api/notes"
        # Set up the headers
        headers = {
            'Content-Type': 'application/json',
            'x-auth-token': self.token
        }
        data = {
            "title": "Pyest_API",
            "description": "Done via RestAssured",
            "category": "Home"
        }
        resp = requests.post(url, json=data, headers=headers)
        print(resp)
        json_data = resp.json()
        j = json.dumps(json_data, indent=4)
        print("response body:", j)
        assert resp.status_code == 200
        assert json_data['data']['title'] == "Pyest_API"
        self.add_id = json_data['data']['id']
        print(f'Address_id={self.add_id}')

    def test_update_notes(self):
        self.test_refresh_token()
        self.test_create_notes()
        url = "https://practice.expandtesting.com/notes/api/notes/"+self.add_id
        # Set up the headers
        headers = {
            'Content-Type': 'application/json',
            'x-auth-token': self.token
        }
        data = {
            "title": "Pyest_Update_API",
            "description": "Done via RestAssured",
            "category": "Home",
            "completed": "true"
        }
        resp = requests.put(url, json=data, headers=headers)
        print(resp)
        json_data = resp.json()
        j = json.dumps(json_data, indent=4)
        print("response body:", j)
        assert resp.status_code == 200
        assert json_data['data']['title'] == "Pyest_Update_API"
        # self.add_id = json_data['data']['id']
        # print(f'Address_id={self.add_id}')




    def test_delete_notes(self):
            self.test_refresh_token()
            self.test_update_notes()
            url = "https://practice.expandtesting.com/notes/api/notes/" + self.update_add_id
            # Set up the headers
            headers = {
                # 'Content-Type': 'application/json',
                'x-auth-token': self.token
            }

            resp = requests.delete(url, headers=headers)
            print(resp)
            json_data = resp.json()
            j = json.dumps(json_data, indent=4)
            print("response body:", j)
            assert resp.status_code == 200
            assert json_data['message'] == "Note successfully deleted"


    # Instance of Class
Object = Notes()

# Calling test_get_Verify_details function
Object.test_delete_notes()

# Calling test_get_Verify_details function
Object.test_update_notes()