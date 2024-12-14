import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from PyTest_UI_Test import XLUtils

browser = webdriver.Edge()
# Step 2) Navigate to OrangeHRM
# browser.get("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
browser.implicitly_wait(30)
path = "../TestData/OrangeHRM_TestData.xlsx"

rows = XLUtils.getRowCount(path, 'SignIn')

for r in range(2, rows + 1):
    username_value = XLUtils.readData(path, 'SignIn', r, 1)
    password_value = XLUtils.readData(path, 'SignIn', r, 2)
    Exp_Result = XLUtils.readData(path, 'SignIn', r, 3)

    # Step 3) Enter UserName and Password
    username = browser.find_element(By.XPATH, "//input[@placeholder='Username']")
    password = browser.find_element(By.XPATH, "//input[@placeholder='Password']")
    submit = browser.find_element(By.XPATH, "//button[normalize-space()='Login']")
    username.send_keys(username_value)
    password.send_keys(password_value)
    # Step 4) Click Login
    submit.click()
    # time.sleep(5)
    if Exp_Result == "Dashboard":
        # if browser.find_element(By.XPATH, "//span[text()='Dashboard']").is_displayed():
        print("test is successful")
        Act_Res = browser.find_element(By.XPATH, "//span[text()='Dashboard']").text
        assert Exp_Result == Act_Res
        XLUtils.writeData(path, 'SignIn', r, 4, "Test Successful")
        XLUtils.writeData(path, 'SignIn', r, 5, Act_Res)
        # time.sleep(4)
        browser.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        # time.sleep(2)
        browser.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        # time.sleep(5)
    # except:
    else:
        print("test is un-successful")
        Act_msg = browser.find_element(By.XPATH, "//p[text()='Invalid credentials']").text
        assert Act_msg == Exp_Result
        XLUtils.writeData(path, 'SignIn', r, 4, "Test Un-Successful")
        XLUtils.writeData(path, 'SignIn', r, 5, Act_msg)
browser.quit()