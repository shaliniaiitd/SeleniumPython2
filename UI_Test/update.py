import time
import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

pytest.ExpUserName = 0


# Fixture for Edge
@pytest.fixture(scope="class")
def edge_driver_init(request):
    edge_driver = webdriver.Edge()
    request.cls.driver = edge_driver
    yield
    edge_driver.close()


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@pytest.mark.usefixtures("edge_driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_Login(self):
        self.driver.maximize_window()
        # Step 2) Navigate to OrangeHRM
        self.driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")
        self.driver.find_element(By.ID, "ctl00_MainContent_username").send_keys('Tester')
        self.driver.find_element(By.ID, "ctl00_MainContent_password").send_keys('test')
        self.driver.find_element(By.ID, "ctl00_MainContent_login_button").click()
        wait = WebDriverWait(self.driver, 20)
        self.driver.find_element(By.ID, 'ctl00_MainContent_btnDelete').is_displayed()

    def test_Order(self):
        self.driver.find_element(By.LINK_TEXT, "Order").click()
        dropdown = Select(self.driver.find_element(By.ID, 'ctl00_MainContent_fmwOrder_ddlProduct'))
        dropdown.select_by_visible_text('ScreenSaver')

        # Create Unique Name
        randomInt = random.randint(0, 1000)
        pytest.ExpUserName = "abhi" + str(randomInt)
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_txtQuantity").send_keys('10')
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_txtName").send_keys(pytest.ExpUserName)
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_TextBox2").send_keys('ABC')
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_TextBox3").send_keys('Bangalore')
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_TextBox5").send_keys('560076')
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_cardList_1").click()
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_TextBox6").send_keys('123456789')
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_TextBox1").send_keys('12/24')
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_InsertButton").click()
        time.sleep(2)
        textvalue = self.driver.find_element(By.XPATH,"//strong[normalize-space()='New order has been successfully added.']")
        textvalue.is_displayed()

        # Verify the Message by comparing
        exp_res = textvalue.text
        print(textvalue)
        assert exp_res == "New order has been successfully added."

        # Go to View All Order Page and Verify that created user is present
        self.driver.find_element(By.LINK_TEXT, "View all orders").click()
        time.sleep(2)
        cellvalue = self.driver.find_element(By.XPATH, "//td[normalize-space()='" + pytest.ExpUserName + "']")

        textvalue = cellvalue.text
        print(textvalue)
        assert pytest.ExpUserName == textvalue

    def test_Update_Order(self):
        self.driver.find_element(By.XPATH,"//td[text()='" + pytest.ExpUserName + "']//following-sibling::td/input").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//h2[normalize-space()='Edit Order']").is_displayed()
        self.driver.find_element(By.NAME, "ctl00$MainContent$fmwOrder$TextBox4").clear()
        self.driver.find_element(By.NAME, "ctl00$MainContent$fmwOrder$TextBox4").send_keys('CA')
        self.driver.find_element(By.ID, "ctl00_MainContent_fmwOrder_UpdateButton").click()
        time.sleep(2)
        ActState = self.driver.find_element(By.XPATH,"//td[text()='" + pytest.ExpUserName + "']//following-sibling::td[text()='CA']")
        textvalue = ActState.text
        ExpState = "CA"
        assert textvalue == ExpState