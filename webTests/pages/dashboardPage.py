__author__ = 'adnanghaffar'

class DashboardPage():
    def __init__(self, driver):
        self.driver = driver

        self.logout_link = 'div.nav-logout a.btn'

    def click_logout_link(self):
        self.driver.find_element_by_css_selector(self.logout_link).click()
