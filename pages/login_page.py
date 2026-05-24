from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Класс для страницы авторизации"""

    # Локаторы элементов
    login_button = (By.XPATH, "//button[text()='Войти']")
    profile = (By.XPATH, "//a[text()='Профиль']")
    login_from_base_page = (By.XPATH, "//button[text()='Войти в аккаунт']")
    login_from_another_page = (By.XPATH, "//a[text()='Войти']")
    forgotten_password = (By.XPATH, "//a[text()='Восстановить пароль']")

    def login(self, email: str, password: str) -> None:
        """Авторизация пользователя"""
        self.input_text(self.email_field, email)
        self.input_text(self.password_field, password)
        self.click_element(self.login_button)


    def is_login_page_loaded(self) -> bool:
        """Проверка загрузки страницы авторизации"""
        return self.find_element(self.email_field).is_displayed()

    def user_profile_available(self) -> None:
        assert self.find_element(self.profile).is_displayed()

    def authorise_by_login_page(self, email: str, password: str) -> None:
        """Авторизация пользователя"""
        self.click_element(self.login_page_button)
        self.login(email, password)
        self.click_element(self.login_page_button)


    def authorise_by_login_from_base_page(self, email: str, password: str) -> None:
        """Авторизация пользователя"""
        self.click_element(self.logo)
        self.click_element(self.login_from_base_page)
        self.login(email, password)
        self.click_element(self.login_page_button)

    def authorise_by_login_from_registration_page(self, email: str, password: str) -> None:
        """Авторизация пользователя"""
        self.click_element(self.login_page_button)
        self.click_element(self.registration_page_button)
        self.click_element(self.login_from_another_page)
        self.login(email, password)
        self.click_element(self.login_page_button)

    def authorise_by_login_from_forgotten_pass_page(self, email: str, password: str) -> None:
        """Авторизация пользователя"""
        self.click_element(self.login_page_button)
        self.click_element(self.forgotten_password)
        self.click_element(self.login_from_another_page)
        self.login(email, password)
        self.click_element(self.login_page_button)
