from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.myntra.com/")
def getElement(category,choice):

    locator = "//a[@class ='desktop-main' and text()='" + category+"']"
    el = driver.find_element(By.XPATH, locator)
    el.click()
    ch = driver.find_element(By.XPATH,"//li/a[text()='"+choice+"']")

    ch.click()
    time.sleep(5)
getElement('Kids','Flipflops')
driver.quit()