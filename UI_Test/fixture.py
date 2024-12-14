# Import the 'modules' that are required for execution for Selenium test automation
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# Fixture for Firefox
@pytest.fixture(scope="class")
def firefox_driver_init(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


# Fixture for Chrome
@pytest.fixture(scope="class")
def edge_driver_init(request):
    edge_driver = webdriver.Edge()
    request.cls.driver = edge_driver
    yield
    edge_driver.close()


@pytest.mark.usefixtures("firefox_driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        title = "Google"
        assert title == self.driver.title

        search_text = "ISTQB"
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(search_text)

        time.sleep(5)

        # Option 1 - To Submit the search
        # search_box.submit()

        # Option 2 - To Submit the search
        search_box.send_keys(Keys.ARROW_DOWN)
        search_box.send_keys(Keys.ARROW_UP)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)

        # Click on the LambdaTest HomePage Link
        title = "International Software Testing Qualifications Board"
        lt_link = self.driver.find_element(By.XPATH,
                                           "//h3[contains(text(),'International Software Testing Qualifications Board')]")
        lt_link.click()

        time.sleep(5)
        assert title == self.driver.title
        time.sleep(2)


@pytest.mark.usefixtures("edge_driver_init")
class Basic_Chrome_Test:
    pass


class Test_URL_Chrome(Basic_Chrome_Test):
    def test_open_url(self):
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Step 2) Navigate to OrangeHRM
        browser.get(url)

        # Step 3) Search & Enter the Email or Phone field & Enter Password
        # browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Step 3) Enter the Username & Enter Password
        browser.maximize_window()
        browser.implicitly_wait(10)  # seconds
        username = browser.find_element(By.NAME, 'username')
        password = browser.find_element(By.NAME, 'password')
        LoginButton = browser.find_element(By.XPATH, "//button[normalize-space()='Login']")
        username.send_keys("Admin")
        password.send_keys("admin123")
        # Step 4) Click Login
        LoginButton.click()
        browser.implicitly_wait(10)  # seconds
        browser.find_element(By.XPATH, "//span[text()='Dashboard']").is_displayed()
        browser.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        browser.implicitly_wait(2)  # seconds
        browser.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        browser.implicitly_wait(5)  # seconds
        browser.find_element(By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']").is_displayed()