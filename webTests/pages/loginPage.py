__author__ = 'adnanghaffar'

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.emailTextField_name = '_email'
        self.passwordTextField_name = '_password'
        self.loginButton_css = '.login > form > button'
        self.emailValidationText_css = 'div.field._email > fieldset.fancy-error'
        self.passwordValidationText_css = 'div.field._password > fieldset.fancy-error'
        self.ValidationText_class = '.error-message'

    def enter_user_email(self, email):
            self.driver.find_element_by_name(self.emailTextField_name).clear()
            self.driver.find_element_by_name(self.emailTextField_name).send_keys(email)

    def enter_user_password(self, password):
            self.driver.find_element_by_name(self.passwordTextField_name).clear()
            self.driver.find_element_by_name(self.passwordTextField_name).send_keys(password)

    def click_loign_button(self):
            self.driver.find_element_by_css_selector(self.loginButton_css).click()
