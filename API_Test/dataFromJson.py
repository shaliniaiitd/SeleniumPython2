import pytest
import requests
import json

@pytest.mark.usefixtures("create_notes_token", "supply_notes_url")
class BasicTest:
    pass


class Test_Notes_Fixture(BasicTest):
    def test_create_notes_using_file(self, supply_notes_url, create_notes_token):
        print(create_notes_token)
        url = supply_notes_url + "/notes/api/notes"
        # Set up the headers
        headers = {
            'Content-Type': 'application/json',
            'x-auth-token': create_notes_token
        }
        path = r"C:\Training_Scripts\PycharmProjects\Selenium_Python\TestData\CreateNotes.json"
        with open(path, "r") as read_file:
            data_payload = json.load(read_file)
            json_payload = json.dumps(data_payload, indent=4)
            print(json_payload)
        resp = requests.post(url, data=json_payload, headers=headers)
        print(resp)
        json_data = resp.json()
        j = json.dumps(json_data, indent=4)
        print("response body:", j)
        assert resp.status_code == 200
        assert json_data['data']['title'] == "Data_File"
        add_id = json_data['data']['id']
        print(f'Notes_id={add_id}')

