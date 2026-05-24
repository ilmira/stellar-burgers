from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Класс для страницы регистрации нового пользователя"""

    # Локаторы элементов
    registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    wrong_email = (By.XPATH, "//p[text()='Такой пользователь уже существует']")
    wrong_password = (By.XPATH, "//p[text()='Некорректный пароль']")

    def register(self, name: str, email: str, password: str) -> None:
        """Зарегистрироваться"""
        self.click_element(self.login_page_button)
        self.click_element(self.registration_page_button)
        self.input_text(self.name_field, name)
        self.input_text(self.email_field, email)
        self.input_text(self.password_field, password)
        self.click_element(self.registration_button)

    def is_registration_page_loaded(self) -> bool:
        """Проверка загрузки страницы регистрации"""
        return self.find_element(self.email_field).is_displayed()

    def is_wrong_email(self) -> None:
        assert self.find_element(self.wrong_email).is_displayed()

    def is_wrong_password(self) -> None:
        assert self.find_element(self.wrong_password).is_displayed()
