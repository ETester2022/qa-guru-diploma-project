import pytest
import allure
from allure_commons.types import Severity
from qa_guru_diploma_project.utils.application import Application


# # pytest -m test_upload_picture -vv --clean-alluredir --alluredir=allure_results
# # allure serve allure_results

@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_settings_app
@allure.epic("43554, Системные функции")
@allure.feature("43555, Авторизация")
class TestUserLogin:

    @pytest.mark.test_auth_invalid_data
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/user/login")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на отсутствие доступа с не валидным паролем")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("login, password", [
        ('invalid_login', 'invalid_password'),
        (True, True)
    ])
    def test_auth_invalid_data(self, browser, login, password):
        app = Application(browser)

        app.login_page.open_user_login_page()
        app.login_page.filling_login(login)
        app.login_page.filling_password(password)
        app.login_page.click_login_btn()

        text_error = app.login_page.get_text_allert()
        assert text_error == '401 Unauthorized'
