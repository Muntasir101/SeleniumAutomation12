import time

from selenium import webdriver

# launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Webpage
driver.get("https://google.com")
time.sleep(3)

# Verify title
try:
    assert "Google" in driver.title
    print("Title verified. Test Passed")
except AssertionError:
    print("Title incorrect.Test failed")

driver.get("https://apple.com")
time.sleep(4)
# Verify title
try:
    assert "Apple" in driver.title
    print("Title verified. Test Passed")
except AssertionError:
    print("Title incorrect.Test failed")

driver.back()
assert "Google" in driver.title
print("back to Google.")

driver.forward()
assert "Apple" in driver.title
print("forward to Apple.")

# Browser Close
driver.close()
