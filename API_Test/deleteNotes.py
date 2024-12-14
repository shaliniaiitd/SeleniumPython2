import time

import pytest
import requests
import json
from selenium.webdriver.common.by import By
from selenium import webdriver


class DeleteUINotes:

    def __init__(self):
        self.update_add_id = None
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
            "title": "Pyest_API_Delete_UI",
            "description": "Done via RestAssured",
            "category": "Home"
        }
        resp = requests.post(url, json=data, headers=headers)
        print(resp)
        json_data = resp.json()
        j = json.dumps(json_data, indent=4)
        print("response body:", j)
        assert resp.status_code == 200
        assert json_data['data']['title'] == "Pyest_API_Delete_UI"
        self.add_id = json_data['data']['id']
        print(f'Address_id={self.add_id}')

    def test_delete_notes(self):
        driver = webdriver.Edge()
        driver.maximize_window()
        # Step 2) Navigate to OrangeHRM
        driver.get("https://practice.expandtesting.com/notes/app/login")
        driver.find_element(By.ID, "email").send_keys('Tester')
        driver.find_element(By.ID, "password").send_keys('test')
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        driver.find_element(By.XPATH, "//button[@class='btn btnx-primary text-black fw-bold rounded w-25 me-3']").is_displayed()
        driver.find_element(By.XPATH, "//div[text()='Pyest_API_Delete_UI']//following-sibling::div/div/button[normalize-space()='Delete']").click()
        driver.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Delete']").click()
        time.sleep(5000)

# Instance of Class
Object = DeleteUINotes()

# Calling test_get_Verify_details function
Object.test_delete_notes()
