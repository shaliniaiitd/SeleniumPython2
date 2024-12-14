import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# //tag(normalize-space()='value') 
# driver = webdriver.Firefox()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
# Step 2) Navigate to OrangeHRM
driver.get(url)

# Step 3) Search & Enter the Email or Phone field & Enter Password
time.sleep(5)
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
submit = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
username.send_keys("Admin")
password.send_keys("admin123")
# Step 4) Click Login
submit.click()
time.sleep(5)
# Logout from application
driver.find_element(By.XPATH, "//span[text()='Dashboard']").is_displayed()
print("test is successful")
Act_Res = driver.find_element(By.XPATH, "//span[text()='Dashboard']").text
assert Act_Res == "Dashboard"
time.sleep(4)
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
time.sleep(5)
driver.quit()