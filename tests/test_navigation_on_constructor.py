import pytest
import allure

from conftest import for_navigation


@allure.feature("Тесты для проверки навигации")
class TestNavigationOnConstructor:

    @pytest.mark.smoke
    @allure.title("Тест навигации по разделам: проверка перехода в раздел 'Булки'")
    def test_navigation_on_constructor_bread(self, for_navigation_on_constructor):
        with allure.step("Переход в раздел 'Булки'"):
            for_navigation_on_constructor.go_to_filing()
            for_navigation_on_constructor.go_to_breads()
        with allure.step("Проверка перехода в раздел 'Булки'"):
            for_navigation_on_constructor.is_breads_opened()

    @pytest.mark.smoke
    @allure.title("Тест навигации по разделам: проверка перехода в раздел 'Соусы'")
    def test_navigation_on_constructor_sauce(self, for_navigation_on_constructor):
        with allure.step("Переход в раздел 'Соусы'"):
            for_navigation_on_constructor.go_to_sauces()
        with allure.step("Проверка перехода в раздел 'Соусы'"):
            for_navigation_on_constructor.is_breads_opened()

    @pytest.mark.smoke
    @allure.title("Тест навигации по разделам: проверка перехода в раздел 'Начинок'")
    def test_navigation_on_constructor_filing(self, for_navigation_on_constructor):
        with allure.step("Переход в раздел 'Начинок'"):
            for_navigation_on_constructor.go_to_filing()
        with allure.step("Проверка перехода в раздел 'Начинок'"):
            for_navigation_on_constructor.is_filings_opened()
