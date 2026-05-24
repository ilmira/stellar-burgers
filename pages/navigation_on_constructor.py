from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NavigationOnConstructor(BasePage):
    """Класс для навигации по разделам"""

    # Локаторы элементов
    bread = (By.XPATH, "//span[text()='Булки']")
    sauce = (By.XPATH, "//span[text()='Соусы']")
    filing = (By.XPATH, "//span[text()='Начинки']")

    cosmo_bread = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    cosmo_sauce = (By.XPATH, "//p[text()='Соус Spicy-X']")
    cosmo_filing = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']")

    def go_to_breads(self) -> None:
        """Переход на раздел Булок"""
        self.click_element(self.bread)

    def go_to_sauces(self) -> None:
        """Переход на раздел Соусов"""
        self.click_element(self.sauce)

    def go_to_filing(self) -> None:
        """Переход на раздел Начинок"""
        self.click_element(self.filing)

    def is_breads_opened(self) -> None:
        """Проверка перехода на страницу Булок"""
        assert self.find_element(self.cosmo_bread).is_displayed()

    def is_sauces_opened(self) -> None:
        """Проверка перехода на страницу Соусов"""
        assert self.find_element(self.cosmo_sauce).is_displayed()

    def is_filings_opened(self) -> None:
        """Проверка перехода на страницу Начинок"""
        assert self.find_element(self.cosmo_filing).is_displayed()
