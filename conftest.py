import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import allure

from config.environments import Environment, environments, common_users
from pages.login_page import LoginPage
from pages.navigation import Navigation
from pages.navigation_on_constructor import NavigationOnConstructor
from pages.registration_page import RegistrationPage

DEVICE_PRESETS = {
    "mobile": (375, 667),
    "tablet": (768, 1024),
    "laptop": (1024, 768),
    "desktop": (1280, 800)
}


def pytest_addoption(parser):
    parser.addoption("--browser", default=os.getenv("BROWSER", "chrome"), help="chrome/firefox")
    parser.addoption("--headless", action="store_true", default=os.getenv("HEADLESS", "false").lower() == "true")
    parser.addoption("--device", default=None, help="mobile/tablet/laptop/desktop")
    parser.addoption("--env", default=os.getenv("ENV", "dev"), help="dev/stage")
    parser.addoption("--user-type", default=None)


def create_driver(browser: str, headless: bool, width: int, height: int):
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument(f"--window-size={width},{height}")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        return webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser {browser} not supported")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    device = request.config.getoption("--device")
    width, height = DEVICE_PRESETS.get(device, (1280, 800))
    driver = create_driver(browser, headless, width, height)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)


def pytest_configure(config):
    env_name = config.getoption("--env")
    user_type = config.getoption("--user-type")
    from config.environments import print_environment_info
    print_environment_info(env_name, user_type)


@pytest.fixture(scope="session")
def env_config(request):
    env_name = request.config.getoption("--env")
    return environments[Environment(env_name)]


@pytest.fixture(scope="function")
def user(request, env_config):
    user_type = request.config.getoption("--user-type") or env_config.default_user
    return common_users[user_type]


@pytest.fixture
def login_page(driver, env_config):
    driver.get(env_config.url)
    return LoginPage(driver)


@pytest.fixture
def registration_page(driver, env_config):
    driver.get(env_config.url)
    return RegistrationPage(driver)


@pytest.fixture
def for_navigation(driver):
    return Navigation(driver)


@pytest.fixture
def for_navigation_on_constructor(driver, env_config):
    driver.get(env_config.url)
    return NavigationOnConstructor(driver)


@pytest.fixture
def authorized_user(login_page, user):
    login_page.login(user.email, user.password)
    return user


@pytest.fixture
def registered_user(registration_page, login_page, user):
    registration_page.register(user.name, user.email, user.password)
    return user
