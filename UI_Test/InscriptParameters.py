# Import the 'modules' that are required for execution for Selenium test automation

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(params=["edge", "firefox"], scope="class")
# def driver_init(request):
#     if request.param == "edge":
#         web_driver = webdriver.Edge()
#     if request.param == "firefox":
#         web_driver = webdriver.Firefox()
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
def get_data():
    return [
        ["Admin","admin123"],
        ["Admin", "admin123"],
        ["Admin", "admin123"]
    ]

@pytest.mark.parametrize("uname, upass", get_data())
class Test_OrangeHRM_Login(BasicTest):
    def test_open_url(self, uname, upass):
        # Step 2) Navigate to OrangeHRM
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Step 3) Enter the Username & Enter Password
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # seconds
        username = self.driver.find_element(By.NAME, 'username')
        password = self.driver.find_element(By.NAME, 'password')
        LoginButton = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        username.send_keys(uname)
        password.send_keys(upass)
        # Step 4) Click Login
        LoginButton.click()
        self.driver.implicitly_wait(10)  # seconds
        self.driver.find_element(By.XPATH, "//span[text()='Dashboard']").is_displayed()
        self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        self.driver.implicitly_wait(2)  # seconds
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        self.driver.implicitly_wait(5)  # seconds
        self.driver.find_element(By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']").is_displayed()
