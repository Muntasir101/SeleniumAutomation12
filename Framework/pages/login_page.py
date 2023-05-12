import time
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):
        # Locating Username by Name
        username_field = self.driver.find_element(By.NAME, "username")
        time.sleep(3)
        # Locating Password by Name
        password_filed = self.driver.find_element(By.NAME, 'password')
        time.sleep(3)
        # Locating Login Button by CSS
        login_button = self.driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')

        # Enter Username
        username_field.send_keys(username)
        time.sleep(3)
        # Enter Password
        password_filed.send_keys(password)
        time.sleep(3)
        # Click Login Button
        login_button.click()