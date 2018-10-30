__author__ = 'adnanghaffar'

import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
CHROMEDRIVER_PATH = os.path.dirname(PROJECT_PATH)

import unittest
import time

from selenium import webdriver

from webTests.pages.loginPage import LoginPage
from webTests.pages.dashboardPage import DashboardPage
from webTests.common.config import PassTestingURL
from webTests.common.provider.loginData import LoginData

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        CONFIG_PATH = os.path.join(CHROMEDRIVER_PATH, 'chromedriver')
        cls.driver = webdriver.Chrome(executable_path = CONFIG_PATH)
        cls.driver.implicitly_wait(60)
        cls.driver.set_window_size(1300, 1000)
        configuration = PassTestingURL()
        cls.driver.get(configuration.TESTING_URL + '/login')

    def test001_empty_email_and_password_fields(self):
        # Click on login button without giving any input in Email and Password fields
        # *** Expected *** """
        # Validation message should be shown for Email and Password fields
        # User should stay on the login page
        driver = self.driver

        login = LoginPage(driver)
        login.enter_user_email('')
        login.enter_user_password('')
        login.click_loign_button()

        self.assertTrue(login.emailValidationText_css)
        self.assertTrue(login.passwordValidationText_css)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)

    def test002_empty_email_and_fill_password_field(self):
        # Click on login button after giving any input in Password
        # *** Expected ***
        # Validation message should be shown for Email
        # User should stay on the login page

        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_password(login_test_data.VALID_USER_PASSWORD)
        login.click_loign_button()

        self.assertTrue(login.emailValidationText_css)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)
        #self.assertFalse(login.passwordValidationText_css)

    def test003_empty_password_and_fill_email_field(self):
        # Click on login button after giving any input in Email
        # *** Expected ***
        # Validation message should be shown for Password
        # User should stay on the login page
        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_email(login_test_data.VALID_USER_EMAIL_ID)
        login.click_loign_button()

        #self.assertFalse(login.emailValidationText_css)
        self.assertTrue(login.passwordValidationText_css)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)

    def test004_login_with_valid_password_and_invalid_email(self):
        # Verify login with valid password and invalid email id
        # *** Expected ***
        # Validation message should be shown
        # User should stay on the login page
        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_email(login_test_data.INVALID_USER_EMAIL_ID)
        login.enter_user_password(login_test_data.VALID_USER_PASSWORD)

        login.click_loign_button()

        self.assertTrue(login.ValidationText_class)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)

    def test005_login_with_invalid_password_and_valid_email(self):
        # Verify login with invalid password and valid email id
        # *** Expected ***
        # Validation message should be shown
        # User should stay on the login page
        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_email(login_test_data.VALID_USER_EMAIL_ID)
        login.enter_user_password(login_test_data.INVALID_USER_PASSWORD)

        login.click_loign_button()

        self.assertTrue(login.ValidationText_class)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)

    def test006_login_with_invalid_password_and_invalid_email(self):
        # Verify login with invalid password and invalid email id
        # *** Expected ***
        # Validation message should be shown
        # User should stay on the login page
        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_email(login_test_data.INVALID_USER_EMAIL_ID)
        login.enter_user_password(login_test_data.INVALID_USER_PASSWORD)

        login.click_loign_button()

        self.assertTrue(login.ValidationText_class)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)

    def test007_login_with_long_string_in_password_and_email(self):
        # Verify that validation message is displayed in case of entering long string in the Username and password
        # *** Expected ***
        # Validation message should be shown
        # User should stay on the login page
        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_email(login_test_data.LONG_STRING)
        login.enter_user_password(login_test_data.LONG_STRING)

        login.click_loign_button()

        self.assertTrue(login.ValidationText_class)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)

    def test008_login_with_invalid_email_format(self):
        # Verify that validation message is displayed in case of entering invalid format id in the Email field
        # *** Expected ***
        # Validation message should be shown
        # User should stay on the login page
        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_email(login_test_data.INCORRECT_EMAIL_FORMAT)

        login.click_loign_button()

        self.assertTrue(login.ValidationText_class)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)

    def test009_login_with_small_string_in_password_and_email(self):
        # Verify that validation message is displayed in case of entering small string in the Email and Password
        # *** Expected ***
        # Validation message should be shown
        # User should stay on the login page
        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_email(login_test_data.SMALL_STRING)
        login.enter_user_password(login_test_data.SMALL_STRING)

        login.click_loign_button()

        self.assertTrue(login.ValidationText_class)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)

    def test010_entering_special_character_in_the_Username_and_password(self):
        # Verify that validation message is displayed in case of entering special character in the Email and Password
        # *** Expected ***
        # Validation message should be shown
        # User should stay on the login page
        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_email(login_test_data.SPECIAL_CHAR)
        login.enter_user_password(login_test_data.SPECIAL_CHAR)

        login.click_loign_button()

        self.assertTrue(login.ValidationText_class)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/login', driver.current_url)

    def test011_login_valid_credentials(self):
        # Login with valid credentials
        # *** Expected ***
        # it should be re-directed to Dashboard page
        driver = self.driver
        driver.refresh()

        login = LoginPage(driver)
        login_test_data = LoginData()
        login.enter_user_email(login_test_data.VALID_USER_EMAIL_ID)
        login.enter_user_password(login_test_data.VALID_USER_PASSWORD)

        login.click_loign_button()

        dashboard_page = DashboardPage(driver)
        self.assertTrue(dashboard_page.logout_link)
        configuration = PassTestingURL()
        self.assertEquals(configuration.TESTING_URL + '/dashboard', driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)