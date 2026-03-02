import allure
import pytest

from conftest import cross_browser_driver
from pages.dog_page import DogPage
from utilities.config_reader import ConfigReader

@pytest.mark.skip
@allure.feature("The Pet Project -Dog Page")
def test_dog_page(cross_browser_driver):
    config = ConfigReader.read_config()
    pet_config = config["environments"]["QA"]
    base_url = pet_config["base_url"]

    dog_page = DogPage(cross_browser_driver)
    dog_page.open_url(base_url)
    dog_page.dog_link()
    assert "dog" in cross_browser_driver.current_url

@allure.feature("The Pet Project - Dog Page")
def test_dog_product_add_to_cart(cross_browser_driver):
    config = ConfigReader.read_config()
    pet_config = config["environments"]["QA"]
    base_url = pet_config["base_url"]
    dog_page = DogPage(cross_browser_driver)
    dog_page.open_url(base_url)
    dog_page.dog_link()
    dog_page.click_dog_filter()
    dog_page.click_dog_puppy_filter()
    dog_page.click_pedigree_biscrok()
    assert "pedigree-biscrok-milk-n-chicken-biscuit" in cross_browser_driver.current_url







