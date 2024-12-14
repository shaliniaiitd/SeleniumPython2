import csv
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.chrome.service import Service
# service_obj = Service(r"C:\Browser_Driver\chromedriver.exe")

def test_setUp():
    global driver
    # create a new Chrome session
    # driver = webdriver.Chrome(service=service_obj)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Target URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def test_login_to_application():
    #filename = r"C:\Training_Scripts\PycharmProjects\Selenium_Python\PyTest_UI_Test\TestData.csv"
    #use relative path
    filename = "..TestData\TestData.csv"
    with open(filename, 'rt') as f:
        data = csv.DictReader(f)
        for detail in data:
            username = detail['uname']
            password = detail['upass']

            # Finding Element
            driver.maximize_window()
            driver.implicitly_wait(10)  # seconds
            driver.find_element(By.NAME, 'username').send_keys(username)
            driver.find_element(By.NAME, 'password').send_keys(password)
            driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
            # driver.implicitly_wait(10)  # seconds
            driver.find_element(By.XPATH, "//span[text()='Dashboard']").is_displayed()
            driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
            driver.implicitly_wait(2)  # seconds
            driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            # driver.implicitly_wait(5)  # seconds
            driver.find_element(By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']").is_displayed()


def test_tearDown():
    # close the browser window
    driver.quit()
