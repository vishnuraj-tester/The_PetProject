from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):

    ADDRESS_LINK = (By.XPATH, "(//a[contains(text(), 'Addresses')])[1]")
    ADD_A_ADDRESS_BUTTON = (By.XPATH, "(//button[contains(text(), 'Add a New Address')])[1]")
    FIRST_NAME_TEXT_FIELD = (By.ID, "AddressFirstName_new")
    LAST_NAME_TEXT_FIELD = (By.ID, "AddressLastName_new")
    ADDRESS_TEXT_FIELD = (By.ID, "AddressAddress1_new")
    APARTMENT_TEXT_FIELD = (By.ID, "AddressAddress2_new")
    CITY_TEXT_FIELD = (By.ID, "AddressCity_new")
    ADD_A_NEW_ADDRESS_BUTTON = (By.XPATH, "(//button[contains(text(), 'Add a New Address')])[2]")
    COUNTRY_DROPDOWN = (By.ID, "AddressCountry_new")

    def open_account_page(self, base_url):
        self.logger.info(f"Opening account page: {base_url}")
        








