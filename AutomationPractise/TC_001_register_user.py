from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1. Launch browser
driver = webdriver.Firefox()
driver.maximize_window()
driver.get_screenshot_as_file("..\Screenshot_images\Step1.png")

#Step 2 Navigate to url 'http://automationexercise.com'
driver.get("http://automationexercise.com")

# Capture Full page screenshot
driver.save_full_page_screenshot("..\Screenshot_images\FullPage.png")

#Step 3 Verify that home page is visible successfully
home_expected_url =  "https://automationexercise.com/"
home_actual_url = driver.current_url

try:
    assert home_expected_url == home_actual_url
    print("home page is visible successfully.Test Passed")
    driver.get_screenshot_as_file("..\Screenshot_images\Step3.png")
except AssertionError:
    print("home page is not visible successfully.Test failed.")

#Step 4 Click on 'Signup / Login' button
signup_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Signup / Login")))

# Capture Specific WebElement screenshot
signup_button.screenshot("..\\Screenshot_images\\Signup_button.png")

signup_button.click()

# Step 5 Verify 'New User Signup!' is visible
new_user_signup_expected_text= "New User Signup!"

new_user_signup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".signup-form h2")))
new_user_signup_actual_text= new_user_signup.text

try:
    assert new_user_signup_expected_text == new_user_signup_actual_text
    print("Verify 'New User Signup!' is visible.Test Passed.")
    driver.get_screenshot_as_file("..\Screenshot_images\Step5_passed.png")
except AssertionError:
    print("Verify 'New User Signup!' is not visible.Test Failed.")
    driver.get_screenshot_as_file("..\Screenshot_images\Step5_failed.png")

# Step 6 Enter name and email address
name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name")))

email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] [type='email']")))

name_field.clear()
name_field.send_keys("Test Name")

email_field.clear()
email_field.send_keys("test@mail.com")

# Step 7 Click 'Signup' button
signup_button  = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] .btn-default")))

signup_button.click()

# Step 8 Verify that 'ENTER ACCOUNT INFORMATION' is visible
# STep 9 Fill details: Title, Name, Email, Password, Date of birth
#Setp 10 Select checkbox 'Sign up for our newsletter!'
#Step 11 Select checkbox 'Receive special offers from our partners!'
# Step 12 Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
#Step 13 Click 'Create Account button'
#Step 14 Verify that 'ACCOUNT CREATED!' is visible
#Step 15 Click 'Continue' button
#Step 16 Verify that 'Logged in as username' is visible
#Step 17 Click 'Delete Account' button
#Setp 18 Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button