from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import time
from config import config

# Function to initialize the browser
def get_driver(browser_name):
    if browser_name.lower() == "edge":
        return webdriver.Edge()
    elif browser_name.lower() == "chrome":
        return webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

# Function to run the test
def run_test(browser_name):
    driver = get_driver(browser_name)
    driver.get(config["url"])  # Load the URL from config

    try:
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
                            return  # Exit the function after finding the match
                    except StaleElementReferenceException:
                        # Re-fetch the row elements if a StaleElementReferenceException occurs
                        rows = driver.find_elements(By.XPATH, '//table[@id="example"]/tbody/tr')

                # Try to locate the "Next" button
                next_button = WebDriverWait(driver, config["timeout"]).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@class="dt-paging-button next" and not(contains(@class, "disabled"))]'))
                )
                next_button.click()  # Click the "Next" button to go to the next page
                time.sleep(1)
            except NoSuchElementException:
                print(f"{browser_name}: Reached the last page or 'Next' button is disabled.")
                break  # Exit the loop if the "Next" button is disabled or not found

    except Exception as e:
        print(f"An error occurred on {browser_name}: {e}")

    finally:
        driver.quit()

# Main execution with ThreadPoolExecutor
if __name__ == "__main__":
    browsers = config["browsers"]

    # Run the test concurrently for all browsers
    with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
        executor.map(run_test, browsers)
