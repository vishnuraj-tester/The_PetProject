from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_TEXTFIELD = (By.XPATH, "(//input[@placeholder='Email' and @type='email'])[2]")
    PASSWORD_TEXTFIELD = (By.XPATH, "//input[@type='password' and @name='customer[password]']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign In')]")
    # ACCOUNT_LINK = (By.XPATH, "(//span[contains(text(), 'Account')])[2]")
    ACCOUNT_LINK = (By.XPATH, "(//a[contains(@href,'/account')])[3]")


    def open_login_page(self, base_url):
        self.logger.info(f"Opening login page: {base_url}")
        self.get_url(base_url)
        sleep(5)
        self.click(self.ACCOUNT_LINK)

    def enter_email(self, email):
        self.logger.info(f"Entering email: {email}")
        self.send_keys(self.EMAIL_TEXTFIELD, email)

    def enter_password(self, password):
        self.logger.info(f"Entering password: {password}")
        self.send_keys(self.PASSWORD_TEXTFIELD, password)

    def click_sign_in_button(self):
        self.logger.info(f"Clicking sign in button: {self.SIGN_IN_BUTTON}")
        self.click(self.SIGN_IN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in_button()


