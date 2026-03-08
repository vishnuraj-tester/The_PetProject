import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader
import os
import allure

@pytest.fixture(scope="session")
def config():
    full_config = ConfigReader.read_config()
    return full_config

#driver fixture
@pytest.fixture
def driver(config):
    browser = config["browser"]

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception(f"Unsupported browser {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()

#Screenshots on Failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver",None)

        if driver:
            screenshot_dir = os.path.join("reports","screenshots")
            os.makedirs(screenshot_dir,exist_ok=True)

            file_path = os.path.join(screenshot_dir,f"{item.name}.png")

            driver.save_screenshot(file_path)

            allure.attach.file(
                file_path,
                name = "screenshot",
                attachment_type = allure.attachment_type.PNG,
            )

@pytest.fixture(params=ConfigReader.read_config()["environments"]["QA"]["browser"])
def cross_browser_driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception(f"Unsupported browser {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()