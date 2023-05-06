from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def capture_screenshot():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://google.com")

    driver.get_screenshot_as_file("..\Screenshot_images\Goggle.png")

    driver.close()

capture_screenshot()