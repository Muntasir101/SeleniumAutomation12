import time

from selenium import webdriver

# launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Webpage
driver.get("https://google.com")

# Fetch website title from browser
title = driver.title

# Verify title
try:
    assert "Google" in title
    print("Title verified. Test Passed")
except AssertionError:
    print("Title incorrect.Test failed")

# Browser Close
driver.close()