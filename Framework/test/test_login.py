import time
import unittest
from selenium import webdriver

from Framework.pages.login_page import LoginPage
from Framework.utils import excel_utils

class LoginTest(unittest.TestCase):

    def test_login_001(self):
        driver = webdriver.Firefox()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(8)

        file = "E:\\Offline_Batch_12\\Project\\SeleniumAutomation12\\Framework\\data\\test_data.xlsx"
        sheet = "Sheet1"

        number_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username = excel_utils.read_data(file, sheet,r,1)
            password = excel_utils.read_data(file, sheet,r,2)

            login_page_obj = LoginPage(driver)
            login_page_obj.login_orange(username, password)

        driver.close()





