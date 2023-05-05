from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def hover():
    # Step 1: launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open Webpage
    driver.get("https://demo.opencart.com/")

    # Step 3: Find Desktop
    desktops = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Desktops")))

    all_actions = ActionChains(driver)

    all_actions.move_to_element(desktops).perform()

    mac = driver.find_element(By.LINK_TEXT, "Mac (1)")
    mac.click()


hover()


