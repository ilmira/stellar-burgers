import pytest
import allure

@allure.feature("Тесты для проверки навигации")
class TestNavigation:

    @pytest.mark.regression
    @allure.title("Тест навигации: проверка перехода в 'Личный кабинет'")
    def test_navigation_login_page(self, for_navigation, login_page, registered_user):
        with allure.step("Авторизация пользователя"):
            login_page.authorise_by_login_page(registered_user.email, registered_user.password)
        with allure.step("Проверка перехода в 'Личный кабинет'"):
            for_navigation.login_page()
            login_page.user_profile_available()

    @pytest.mark.regression
    @allure.title("Тест навигации: проверка перехода по клику на 'Конструктор'")
    def test_navigation_constructor(self, for_navigation,login_page, registered_user):
        with allure.step("Авторизация пользователя"):
            login_page.authorise_by_login_page(registered_user.email, registered_user.password)
        with allure.step("Проверка перехода по клику на 'Конструктор'"):
            for_navigation.go_to_construction()
            for_navigation.is_construction_opened()

    @pytest.mark.regression
    @allure.title("Тест навигации: проверка перехода по клику на логотип Stellar Burgers")
    def test_navigation_logo(self, for_navigation,login_page, registered_user):
        with allure.step("Авторизация пользователя"):
            login_page.authorise_by_login_page(registered_user.email, registered_user.password)
        with (allure.step("Проверка перехода по клику на логотип Stellar Burgers")):
            for_navigation.click_to_logo()
            for_navigation.is_construction_opened()

    @pytest.mark.regression
    @allure.title("Тест навигации: проверка выхода через кнопку 'Выйти' в личном кабинете")
    def test_navigation_exit(self, for_navigation,login_page, registered_user):
        with allure.step("Авторизация пользователя"):
            login_page.authorise_by_login_page(registered_user.email, registered_user.password)
        with allure.step("Проверка выхода через кнопку 'Выйти' в личном кабинете"):
            for_navigation.login_page()
            for_navigation.click_to_exit()
            for_navigation.login_page()
            for_navigation.is_user_exit_from_account()
