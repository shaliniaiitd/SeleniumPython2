import json
# Importing necessary modules
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


driver = webdriver.Edge()
# Reading data from JSON file
jsonfile = open('../TestData/TestData_Multiple.json', 'r')
jsondata = jsonfile.read()

# Parse - convert json data into python dict
data = json.loads(jsondata)
print(data)
# Here will store data in list(array), which will hold all value from Login_details section
list = data['Login_details']
print(list)
print(len(list))

# Iterating through the json
# list
for i in range(len(list)):
    # Target URL
    url = list[i].get('url')
    uname = list[i].get('uname')
    upass = list[i].get('upass')
    print(url)
    print(uname)
    print(upass)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)  # seconds
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    LoginButton = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")

    username.send_keys(uname)
    password.send_keys(upass)
    LoginButton.click()
    driver.implicitly_wait(10)  # seconds
    driver.find_element(By.XPATH, "//span[text()='Dashboard']").is_displayed()
    driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
    driver.implicitly_wait(2)  # seconds
    driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    driver.implicitly_wait(5)  # seconds
    driver.find_element(By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']").is_displayed()
driver.close()
