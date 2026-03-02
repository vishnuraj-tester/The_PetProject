from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger
class BasePage:
    #---initializer---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)
    #action methods
    def get_url(self,url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def find_element(self,locator):
        self.logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self,locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self,locator,text):
        self.logger.info(f"Typing into element: {text}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.find_element(locator).text

    def hover(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def select_dropdown_by_visible_text(self, locator, text):
        dropdown = self.wait.until(EC.presence_of_element_located(locator))
        Select(dropdown).select_by_visible_text(text)

    def scroll_down(self,locator):
        element=self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)