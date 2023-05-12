import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)


driver.get("https://facebook.com")
time.sleep(3)


username = driver.find_element(By.ID, "email")
time.sleep(3)


password = driver.find_element(By.NAME, 'pass')
time.sleep(3)


login_button = driver.find_element(By.NAME, "login")



username.send_keys("shahinsiraj20@gmail.com")
time.sleep(3)


password.send_keys("asrafull")
time.sleep(3)


login_button.click()
time.sleep(3)
#verify url
expected_url='https://facebook.com'
actual_url=driver.current_url
try:
   assert expected_url==actual_url
   print('login succefully.test pass')
except AssertionError:
   print('Login Error.test fail')


driver.close()
