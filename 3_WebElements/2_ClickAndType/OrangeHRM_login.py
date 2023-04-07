import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def TC_001_login_valid():
    # Step 1: launch browser and Open Webpage
    # launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open Webpage
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    # Step 2: Locating all Elements
    # Locating Username by Name
    username = driver.find_element(By.NAME, "username")
    time.sleep(3)
    # Locating Password by Name
    password = driver.find_element(By.NAME, 'password')
    time.sleep(3)
    # Locating Login Button by CSS
    login_button = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')

    # Step 3: Main Action
    # Enter Username
    username.send_keys("Admin")
    time.sleep(3)
    # Enter Password
    password.send_keys("admin123")
    time.sleep(3)
    # Click Login Button
    login_button.click()
    time.sleep(3)

    # Verify valid Login by URL
    expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    actual_url = driver.current_url

    try:
        assert expected_url == actual_url
        print('Login Successful.Test Passed.')
    except AssertionError:
        print('Login Error.Test Failed.')

    driver.close()


def TC_002_login_invalid():
    # Step 1: launch browser and Open Webpage
    # launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # Open Webpage
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    # Step 2: Locating all Elements
    # Locating Username by Name
    username = driver.find_element(By.NAME, "username")
    time.sleep(3)
    # Locating Password by Name
    password = driver.find_element(By.NAME, 'password')
    time.sleep(3)
    # Locating Login Button by CSS
    login_button = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')

    # Step 3: Main Action
    # Enter Username
    username.send_keys("Admin Invalid")
    time.sleep(3)
    # Enter Password
    password.send_keys("1232f")
    time.sleep(3)
    # Click Login Button
    login_button.click()
    time.sleep(3)

    # Verify invalid login using error message
    expected_error_message = 'Invalid credentials'

    actual_error_message = driver.find_element(By.CSS_SELECTOR, '.oxd-alert-content-text').text

    try:
        assert expected_error_message == actual_error_message
        print("Invalid test case passed.Login Error message display as expected.")
    except AssertionError:
        print('Invalid test case Failed.Unexpected Error message.')

    driver.close()


# TC_001_login_valid()
TC_002_login_invalid()
