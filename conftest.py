import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader
import os
import allure
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope="session")
def config():
    full_config = ConfigReader.read_config()
    return full_config


# Driver fixture for single-browser runs
@pytest.fixture
def driver(config):
    browser = config["browser"]
    # For Docker support here, you'd apply the same logic as below
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


# --- DOCKER & CROSS BROWSER FIXTURE ---
@pytest.fixture(params=ConfigReader.read_config()["environments"]["QA"]["browser"])
def cross_browser_driver(request):
    browser = request.param

    # 1. Determine Execution Mode (Local vs Docker)
    # Set this to 'remote' in your terminal to use Docker
    execution_type = os.environ.get('EXEC_TYPE', 'local')
    remote_url = "http://localhost:4444/wd/hub"

    headless_mode = True
    if os.environ.get('BROWSER'):
        browser = os.environ.get('BROWSER')

    # 2. Configure Chrome
    if browser == "chrome":
        options = ChromeOptions()
        if headless_mode:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        if execution_type == "remote":
            driver = webdriver.Remote(command_executor=remote_url, options=options)
        else:
            driver = webdriver.Chrome(options=options)

    # 3. Configure Firefox
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless_mode:
            options.add_argument("--headless")

        if execution_type == "remote":
            driver = webdriver.Remote(command_executor=remote_url, options=options)
        else:
            driver = webdriver.Firefox(options=options)

    # 4. Configure Edge
    elif browser == "edge":
        options = EdgeOptions()
        if headless_mode:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")

        if execution_type == "remote":
            driver = webdriver.Remote(command_executor=remote_url, options=options)
        else:
            driver = webdriver.Edge(options=options)

    driver.maximize_window()
    yield driver
    driver.quit()


# --- Screenshots on Failure ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Check both potential driver fixture names
        driver = item.funcargs.get("driver") or item.funcargs.get("cross_browser_driver")

        if driver:
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_path = os.path.join(screenshot_dir, f"{item.name}.png")

            driver.save_screenshot(file_path)

            allure.attach.file(
                file_path,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )