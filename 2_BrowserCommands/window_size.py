import time

from selenium import webdriver

# launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Webpage
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# set window size
driver.set_window_size(800, 600)

time.sleep(10)

# Browser Close
driver.close()