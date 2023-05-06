from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrolling():
    driver = webdriver.Firefox()
    driver.get("https://www.apple.com/")
    time.sleep(7)

    # Scroll to Specific Position/Element
    ipad = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-unit-id='ipad'] .unit-wrapper > [target]")))

    driver.execute_script("arguments[0].scrollIntoView(true);", ipad)
    time.sleep(3)

    # Scroll to Bottom
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)

    # Scroll to Top
    driver.execute_script("window.scrollTo(0,0)")


scrolling()