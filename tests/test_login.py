from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader
import allure

@allure.feature("The Pet Project Login")
def test_login(cross_browser_driver):
    config = ConfigReader.read_config()
    pet_config = config["environments"]["QA"]
    base_url = pet_config["base_url"]
    email = pet_config["email"]
    password = pet_config["password"]

    login_page = LoginPage(cross_browser_driver)
    with allure.step("Open the login page"):
        login_page.open_login_page(base_url)
        login_page.login(email, password)
        assert login_page.is_login_successful()

