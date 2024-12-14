import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
# Step 2) Navigate to OrangeHRM
driver.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")
driver.find_element(By.ID,"ctl00_MainContent_username").send_keys('Tester')
driver.find_element(By.ID,"ctl00_MainContent_password").send_keys('test')
driver.find_element(By.ID,"ctl00_MainContent_login_button").click()
wait = WebDriverWait(driver, 20)
driver.find_element(By.ID,'ctl00_MainContent_btnDelete').is_displayed()

driver.find_element(By.LINK_TEXT,"Order").click()
dropdown = Select(driver.find_element(By.ID, 'ctl00_MainContent_fmwOrder_ddlProduct'))
dropdown.select_by_visible_text('ScreenSaver')

# Create Unique Name
randomInt = random.randint(0,10000)
ExpUserName = "abhi" + str(randomInt)
driver.find_element(By.ID,"ctl00_MainContent_fmwOrder_txtQuantity").send_keys('10')
driver.find_element(By.ID,"ctl00_MainContent_fmwOrder_txtName").send_keys(ExpUserName)
driver.find_element(By.ID,"ctl00_MainContent_fmwOrder_TextBox2").send_keys('ABC')
driver.find_element(By.ID,"ctl00_MainContent_fmwOrder_TextBox3").send_keys('Bangalore')
driver.find_element(By.ID,"ctl00_MainContent_fmwOrder_TextBox5").send_keys('560076')
driver.find_element(By.ID,"ctl00_MainContent_fmwOrder_cardList_1").click()
driver.find_element(By.ID,"ctl00_MainContent_fmwOrder_TextBox6").send_keys('123456789')
driver.find_element(By.ID,"ctl00_MainContent_fmwOrder_TextBox1").send_keys('12/24')
driver.find_element(By.ID,"ctl00_MainContent_fmwOrder_InsertButton").click()
time.sleep(2)
textvalue = driver.find_element(By.XPATH,"//strong[normalize-space()='New order has been successfully added.']")
textvalue.is_displayed()

#Verify the Message by comparing
exp_res = textvalue.text
print(textvalue)
assert exp_res == "New order has been successfully added."

# Go to View All Order Page and Verify that created user is present
driver.find_element(By.LINK_TEXT,"View all orders").click()
time.sleep(2)
cellvalue = driver.find_element(By.XPATH,"//td[normalize-space()='"+ExpUserName+"']")
#concatenation

textvalue = cellvalue.text
print(textvalue)
assert ExpUserName == textvalue

#driver.close()
driver.quit()