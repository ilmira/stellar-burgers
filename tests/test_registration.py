import pytest
import allure

from conftest import login_page


@allure.feature("Тесты для страницы регистрации")
class TestRegistration:
    data_for_test = [(None, None, None, 'Позитивный тест на успешную регистрацию', 'success'),
                     ('', None, None, "Негативный тест на поле 'Имя' (пустое значение)", 'empty_name'),
                     (None, 'testyandex.ru', None, "Негативный тест на поле 'Email'(невалидный формат)", 'wrong_email'),
                     (None, None, '234', "Негативный тест на поле 'Пароль' (менее 6 символов)", 'wrong_password')]

    @pytest.mark.smoke
    @pytest.mark.parametrize('name, email, password, test_name, result', data_for_test)
    def test_registration_burgers(self, registration_page, login_page, user, name, email, password, test_name, result):
        allure.dynamic.title(test_name)
        reg_name = name if name is not None else user.name
        reg_email = email if email is not None else user.email
        reg_pass = password if password is not None else user.password
        with allure.step(f"Регистрация пользователя с данными: имя: {reg_name} пароль: {reg_pass}"):
            registration_page.register(reg_name, reg_email, reg_pass)

        with allure.step("Проверка результата регистрации"):
            if result == 'success':
                login_page.authorise_by_login_page(user.email, user.password)
                login_page.user_profile_available()
            elif result == 'empty_name':
                registration_page.check_url('https://stellarburgers.education-services.ru/register')
            elif result == 'wrong_email':
                registration_page.is_wrong_email()
            elif result == 'wrong_password':
                registration_page.is_wrong_password()
            else:
                pytest.fail(f"Передан некорректный результат: {result}")
