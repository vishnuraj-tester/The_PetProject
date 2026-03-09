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



from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager


@pytest.fixture(params=ConfigReader.read_config()["environments"]["QA"]["browser"])
def cross_browser_driver(request):
    browser = request.param

    headless_mode = True

    if browser == "chrome":
        options = ChromeOptions()
        if headless_mode:
            options.add_argument("--headless=new")  # Recommended for newer Chrome versions
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless_mode:
            options.add_argument("--headless")
            options.set_preference("width", 1920)
            options.set_preference("height", 1080)
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if headless_mode:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
        driver = webdriver.Edge(options=options)

    elif browser == "safari":
        options = SafariOptions()
        # Note: Safari does not support headless mode [web:1][web:21]
        driver = webdriver.Safari(options=options)

    elif browser == "opera":
        options = ChromeOptions()
        if headless_mode:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(OperaDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    yield driver
    driver.quit()
