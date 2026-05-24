from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    """Базовый класс для всех страниц"""

    # Локаторы элементов
    logo = (By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2 a")
    login_page_button = (By.XPATH, "//a[./p[normalize-space()='Личный Кабинет']]")
    registration_page_button = (By.XPATH, "//a[text()='Зарегистрироваться']")
    name_field = (By.CSS_SELECTOR, "input[name='name']")
    email_field = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_field = (By.CSS_SELECTOR, "input[name='Пароль']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        """Найти элемент с явным ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple[str, str]) -> None:
        """Нажать на элемент с явным ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator: tuple[str, str], text: str) -> None:
        """Ввести текст в элемент"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def check_url(self, url: str) -> None:
        """Проверка URL после авторизации"""
        assert self.driver.current_url == url, f"URL {self.driver.current_url} не соответствует ожидаемому: {url}"

    def attach_screenshot(self, name="screenshot") -> None:
        """Сделать скриншот и прикрепить к отчету Allure."""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
