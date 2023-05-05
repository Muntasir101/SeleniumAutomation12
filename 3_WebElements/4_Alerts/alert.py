from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def alert():
    # Step 1: launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open Webpage
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Step 3: Find Dropdown
    normal_alert_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(1) > button")))
    normal_alert_button.click()

    normal_alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Test 1: Verify alert is open
    try:
        assert normal_alert.text == "I am a JS Alert"
        print("Normal Alert Open.Test 1 Passed.")
    except AssertionError:
        print("Normal Alert is not open.Test 1 Failed.")

    # close the alert
    normal_alert.accept()  # Click OK
    normal_alert.dismiss() # Click Cancel

    # Test 2: Verify alert is closed
    try:
        alert_text = normal_alert.text
        assert False, "Test 2 failed. Alert Still open."
    except NoAlertPresentException:
        print("Test 2 passed. Normal Alert closed.")
        pass


alert()
