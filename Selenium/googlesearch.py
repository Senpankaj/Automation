from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (ensure chromedriver is in your PATH, or provide the path)
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get('https://www.google.com')

    # Find the search box using its name attribute value
    search_box = driver.find_element(By.NAME, 'q')

    # Enter search keyword 'OSNIT' and perform the search
    search_box.send_keys('OSNIT')
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the results (optional)
    time.sleep(5)

finally:
    # Close the WebDriver
    driver.quit()
