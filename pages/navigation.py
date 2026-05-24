from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Navigation(BasePage):
    """Класс для навигации по разделам"""

    # Локаторы элементов
    construction = (By.XPATH, "//a[contains(., 'Конструктор')]")
    exit = (By.XPATH, "//button[text()='Выход']")
    text_constructor = (By.XPATH, "//h1[text()='Соберите бургер']")
    after_exit = (By.XPATH, "//h2[text()='Вход']")

    def login_page(self) -> None:
        """Переход на страницу пользователя"""
        self.click_element(self.login_page_button)

    def go_to_construction(self) -> None:
        """Переход в раздел построения бургера"""
        self.click_element(self.construction)

    def click_to_logo(self) -> None:
        """Переход в раздел построения бургера"""
        self.click_element(self.logo)

    def click_to_exit(self) -> None:
        """Выход из аккаунта"""
        self.click_element(self.exit)

    def is_construction_opened(self) -> None:
        """Проверка перехода на страницу конструктора"""
        assert self.find_element(self.text_constructor).is_displayed()

    def is_user_exit_from_account(self) -> None:
        """Проверка выхода из аккаунта"""
        assert self.find_element(self.after_exit).is_displayed()
