import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Webpage
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

username = driver.find_element(By.NAME, "username")

# Verify Username Display or not
username_display_state = username.is_displayed()
print(username_display_state)

# Verify Username Enable or not
username_enable_state = username.is_enabled()
print(username_enable_state)


driver.close()