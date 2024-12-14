import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
base_url = str("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")
driver.get(base_url)
driver.maximize_window()
driver.find_element(By.ID,"ctl00_MainContent_username").send_keys('Tester')
driver.find_element(By.ID,"ctl00_MainContent_password").send_keys('test')
driver.find_element(By.ID,"ctl00_MainContent_login_button").click()

webtable = driver.find_element(By.XPATH,"//table[@id='ctl00_MainContent_orderGrid']").get_attribute("outerHTML")
df = pd.read_html(webtable)
print(df)
print(f'Total tables: {len(df)}')
df = df[-1]
df.to_csv('table.csv')
df.to_excel('../TestData/pandas_to_excel.xlsx', sheet_name='Order')
# making data frame from csv
data = pd.read_csv("table.csv")

# Converting a specific Dataframe
# column to list using Series.tolist()
Name_list = data["Name"].tolist()
print(Name_list)
driver.close()
