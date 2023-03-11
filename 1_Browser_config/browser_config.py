from selenium import webdriver

# launch browser
driver = webdriver.Firefox()

# Open Webpage
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.get("https://google.com")

# Browser Close
driver.close()