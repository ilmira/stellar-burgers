import pytest
import allure

@allure.feature("Тесты для страницы авторизации")
class TestLogin:

    @pytest.mark.regression
    @allure.title("Тест успешной авторизации: вход через кнопку 'Личный кабинет'")
    def test_login_from_login_button(self, login_page, registered_user):
        with allure.step("Авторизация пользователя"):
            login_page.authorise_by_login_page(registered_user.email, registered_user.password)
        with allure.step("Проверка авторизации через кнопку 'Личный кабинет'"):
            login_page.user_profile_available()

    @pytest.mark.regression
    @allure.title("Тест успешной авторизации: вход через кнопку 'Войти в аккаунт' на главной странице")
    def test_login_from_base_page(self, login_page, registered_user):
        with allure.step("Авторизация пользователя"):
            login_page.authorise_by_login_from_base_page(registered_user.email, registered_user.password)
        with allure.step("Проверка авторизации через кнопку 'Войти в аккаунт'"):
            login_page.user_profile_available()

    @pytest.mark.regression
    @allure.title("Тест успешной авторизации: вход через кнопку в форме регистрации")
    def test_login_from_registration_page(self, login_page, registered_user):
        with allure.step("Авторизация пользователя: проверка авторизации через кнопку в форме регистрации"):
            login_page.authorise_by_login_from_registration_page(registered_user.email, registered_user.password)
        with allure.step("Проверка авторизации через кнопку форме регистрации"):
            login_page.user_profile_available()

    @pytest.mark.regression
    @allure.title("Тест успешной авторизации: вход через кнопку в форме восстановления пароля")
    def test_login_from_forgotten_password_page(self, login_page, registered_user):
        with allure.step("Авторизация пользователя: проверка авторизации через кнопку в форме восстановления пароля"):
            login_page.authorise_by_login_from_forgotten_pass_page(registered_user.email, registered_user.password)
        with allure.step("Проверка авторизации через кнопку в форме восстановления пароля"):
            login_page.user_profile_available()