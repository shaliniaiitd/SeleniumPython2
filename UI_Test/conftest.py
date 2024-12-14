# Import the 'modules' that are required for execution

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#service_obj = Service(r"C:\Browser_Driver\chromedriver.exe")

@pytest.fixture(params=["edge", "firefox", "chrome"])
def driver_init(request):
    if request.param == "edge":
        web_driver = webdriver.Edge()
        web_driver.maximize_window()
    # url ="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
        web_driver.maximize_window()
    # url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    if request.param == "chrome":
        #web_driver = webdriver.Chrome(service=service_obj)
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        web_driver.maximize_window()
    # url ="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture
def app_url():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    return url