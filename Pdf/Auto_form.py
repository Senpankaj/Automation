from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Function to fill out the form
def fill_form():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the webpage with the form
        driver.get('https://example.com/form')  # Update with the actual URL

        # Fill out the form fields (update these selectors and data)
        driver.find_element(By.ID, 'first_name').send_keys('John')  # First name
        driver.find_element(By.ID, 'last_name').send_keys('Doe')    # Last name
        driver.find_element(By.ID, 'email').send_keys('john.doe@example.com')  # Email

        # Submit the form (update this selector)
        driver.find_element(By.ID, 'submit_button').click()

    finally:
        # Close the WebDriver
        driver.quit()

# Call the function to fill the form
fill_form()