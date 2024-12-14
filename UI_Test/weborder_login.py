from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Edge()
driver.maximize_window()
# Step 2) Navigate to OrangeHRM
driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")
driver.find_element(By.ID,"ctl00_MainContent_username").send_keys('Tester')
driver.find_element(By.ID,"ctl00_MainContent_password").send_keys('test')
driver.find_element(By.ID,"ctl00_MainContent_login_button").click()
wait = WebDriverWait(driver, 20)
driver.find_element(By.ID,'ctl00_MainContent_btnDelete').is_displayed()
#driver.close()
driver.quit()


