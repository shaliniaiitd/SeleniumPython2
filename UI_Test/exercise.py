from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Edge()
driver.get("https://datatables.net/examples/data_sources/server_side")  # Specified URL

while True:
    try:
        # Locate rows in the table
        rows = driver.find_elements(By.XPATH, '//table[@id="example"]/tbody/tr')

        # Loop through each row to find "Sakura"
        for row in rows:
            try:
                # Check if the first <td> contains the text "Sakura"
                first_td = row.find_element(By.XPATH, './td[1]')
                if first_td.text == "Sakura":
                    # Print all <td> text within this row
                    all_tds = row.find_elements(By.XPATH, './td')
                    for td in all_tds:
                        print(td.text)
                    driver.quit()
                    exit()  # Exit the script after finding the match
            except StaleElementReferenceException:
                # Re-fetch the row elements if a StaleElementReferenceException occurs
                rows = driver.find_elements(By.XPATH, '//table[@id="example"]/tbody/tr')

        # Try to locate the "Next" button
        next_button = driver.find_element(By.XPATH, '//button[@class="dt-paging-button next" and not(contains(@class, "disabled"))]')
        #driver.implicitly_wait(3)
        next_button.click()  # Click the "Next" button to go to the next page
        #driver.implicitly_wait(3)
        #time.sleep(1)  # Wait for the page to load
    except NoSuchElementException:
        print("Reached the last page or 'Next' button is disabled.")
        break  # Exit the loop if the "Next" button is disabled or not found

driver.quit()

