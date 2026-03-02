from selenium.webdriver.common.by import By
from base_page import BasePage

class DogGroomingPage(BasePage):

    DOG_MENU = (By.XPATH,"//a[contains(text(),'Dogs')]")
    GROOMING_OPTION =(By.XPATH,"//a[contains(text(),'Dog Grooming')]")
    ADD_TO_CART = (By.XPATH,"(//span[contains(text(),'ADD TO CART')])[1]")
    PAGE_HEADING = (By.XPATH, "//h1")

    def navigate_to_grooming(self, base_url):
        self.logger.info("Navigate to grooming page")
        self.get_url(base_url)
        self.hover(self.DOG_MENU)
        self.click(self.GROOMING_OPTION)

    def click_add_to_cart(self):
        self.logger.info("Click add to_cart button")
        self.click(self.ADD_TO_CART)

    def verify_grooming_page_loaded(self):
        heading_text = self.get_text(self.PAGE_HEADING)
        return "groom" in heading_text.lower()

