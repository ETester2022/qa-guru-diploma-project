import pytest
import allure
from allure_commons.types import Severity
from jsonschema import validate
from tests.api.test_application_settings import schemas
from qa_guru_diploma_project.utils.utils import reqres_get


@pytest.mark.test_all
@pytest.mark.test_api
@pytest.mark.test_get_app_settings_all
@allure.epic("43483, Админские настройки")
@allure.feature("43531, Приложение")
class TestGetAppSettings:

    @pytest.mark.test_get_app_settings_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/application/settings")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Получение настроек раздел Общие")
    @allure.severity(Severity.CRITICAL)
    def test_get_app_settings_admin(self, get_access_token_admin):
        url = '/application/settings'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}

        with allure.step('GET-запрос'):
            response = reqres_get(url, headers=token)

        with allure.step('Соответствие статус-кода 200'):
            assert response.status_code == 200
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_get_app_settings)

    @pytest.mark.test_get_app_settings_extra_value
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/application/settings")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Получение настроек раздел Общие с лишними данными в body")
    @allure.severity(Severity.CRITICAL)
    def test_get_app_settings_extra_value(self, get_access_token_admin):
        url = '/application/settings'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}
        body = {
            "value": "extra value"
        }

        with allure.step('GET-запрос'):
            response = reqres_get(url, headers=token, json=body)

        with allure.step('Соответствие статус-кода 200'):
            assert response.status_code == 200
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_get_app_settings)

    @pytest.mark.test_get_app_settings_not_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/application/settings")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Отсутствие доступа к настройкам раздел Общие user не admin")
    @allure.severity(Severity.CRITICAL)
    def test_get_app_settings_not_admin(self, get_access_token_not_admin):
        url = '/application/settings'
        token = {"Authorization": f"Bearer {get_access_token_not_admin}"}

        with allure.step('GET-запрос'):
            response = reqres_get(url, headers=token)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 403
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 31003
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.access_denied'

    @pytest.mark.test_get_app_settings_invalid_token
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/application/settings")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Отсутствие доступа к настройкам раздел Общие не валидный токен")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("invalid_token", [
        'text',
        123,
        ''
    ])
    def test_get_app_settings_invalid_token(self, invalid_token):
        url = '/application/settings'
        token = {"Authorization": f"Bearer {invalid_token}"}

        with allure.step('GET-запрос'):
            response = reqres_get(url, headers=token)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 401
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 32000
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.invalid_token'
