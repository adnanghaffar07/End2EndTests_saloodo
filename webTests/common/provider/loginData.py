__author__ = 'adnanghaffar'

class LoginData():
    def __init__(self):
        self.VALID_USER_EMAIL_ID = 'test+carrier@saloodo.com'
        self.VALID_USER_PASSWORD = '123456'

        self.INVALID_USER_EMAIL_ID = 'test+test.com'
        self.INVALID_USER_PASSWORD = 'test1234589'
        self.INCORRECT_EMAIL_FORMAT = 'TEST.COM'
        self.LONG_STRING = '23OUOI30877-1984#7260-0'
        self.SMALL_STRING = '_8'
        self.SPECIAL_CHAR = '@#$%^&*()'