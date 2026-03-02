import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DogPage(BasePage):

    DOG_LINK=(By.PARTIAL_LINK_TEXT,"Dogs")
    PUPPY_LINK=(By.PARTIAL_LINK_TEXT,"Puppy (0 to 3 Months)")
    BAKED_BISCUITS=(By.PARTIAL_LINK_TEXT,"Baked Biscuits")
    DOG_FILTER=(By.XPATH,"(//span[text()='Dogs'])[4]")
    DOG_PUPPY_FILTER=(By.XPATH,"//span[text()='Adult / Puppy']")
    PEDIGREE_BISCROK_MILK_CHICKEN=(By.PARTIAL_LINK_TEXT,"Pedigree Biscrok Milk & Chicken Biscuit")
    ADD_TO_CART=(By.CSS_SELECTOR,'button[name="add"]')
    VIEW_CART=(By.PARTIAL_LINK_TEXT,"View Cart")

    def open_url(self, base_url):
        self.logger.info(f"Opening login page: {base_url}")
        self.get_url(base_url)

    def dog_link(self):
        self.logger.info(f"Dog link: {self.DOG_LINK}")
        self.click(self.DOG_LINK)


    def puppy_link(self):
        self.logger.info(f"Puppy link: {self.PUPPY_LINK}")
        self.hover(self.DOG_LINK)
        self.click(self.PUPPY_LINK)
        time.sleep(5)

    def baked_biscuits(self):
        self.logger.info(f"Baked Biscuits: {self.BAKED_BISCUITS}")
        self.click(self.BAKED_BISCUITS)
        time.sleep(5)

    def click_dog_filter(self):
        self.logger.info(f"Select dog filter: {self.DOG_FILTER}")
        self.scroll_down(self.DOG_FILTER)
        self.click(self.DOG_FILTER)
        time.sleep(5)

    def click_dog_puppy_filter(self):
        self.logger.info(f"Select dog-puppy filter: {self.DOG_FILTER}")
        self.scroll_down(self.DOG_PUPPY_FILTER)
        self.click(self.DOG_PUPPY_FILTER)
        time.sleep(5)


    def click_pedigree_biscrok(self):
        self.scroll_down(self.PEDIGREE_BISCROK_MILK_CHICKEN)
        self.click(self.PEDIGREE_BISCROK_MILK_CHICKEN)
        time.sleep(5)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART)
        time.sleep(5)

    def click_view_cart(self):
        self.click(self.VIEW_CART)
        time.sleep(5)









