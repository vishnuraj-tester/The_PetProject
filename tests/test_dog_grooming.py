import allure
from pages.dog_grooming_page import DogGroomingPage


@allure.feature("Dogs Grooming Module")
@allure.story("Verify Grooming Navigation and Booking")
def test_dog_grooming_navigation(cross_browser_driver, config):

    pet_config = config["environments"]["QA"]
    base_url = pet_config["base_url"]

    grooming_page = DogGroomingPage(cross_browser_driver)

    with allure.step("Navigate to Grooming Page"):
        grooming_page.navigate_to_grooming(base_url)

    with allure.step("Verify Grooming Page Loaded"):
        assert grooming_page.verify_grooming_page_loaded()

    with allure.step("Click Book Now"):
        grooming_page.click_book_now()