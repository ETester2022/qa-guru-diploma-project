import os
import requests
import pytest
import allure
from allure_commons.types import Severity
from jsonschema import validate
from tests.api.application_settings import schemas


@pytest.mark.tests_api
@pytest.mark.tests_app_settings
@allure.epic("43483, Админские настройки")
@allure.feature("43531, Приложение")
class TestGetAppSettings:

    @pytest.mark.test_get_app_settings_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на получение настроек раздел Общие")
    @allure.severity(Severity.CRITICAL)
    def test_get_app_settings_admin(self, get_access_token_admin):
        with allure.step('Запрос настроек приложения'):
            base_url_api = os.getenv('BASE_URL_API')
            response = requests.get(base_url_api + '/application/settings',
                                    headers={"Authorization": f"Bearer {get_access_token_admin}"})
        with allure.step('Соответствие статус-кода 200'):
            assert response.status_code == 200
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_get_app_settings)

    @pytest.mark.test_app_settings_extra_value
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на получение настроек раздел Общие с лишними данными в body")
    @allure.severity(Severity.CRITICAL)
    def test_app_settings_extra_value(self, get_access_token_admin):
        body = {
            "value": "extra value"
        }

        with allure.step('Запрос настроек приложения'):
            base_url_api = os.getenv('BASE_URL_API')
            response = requests.get(base_url_api + '/application/settings',
                                    headers={"Authorization": f"Bearer {get_access_token_admin}"},
                                    json=body)
        with allure.step('Соответствие статус-кода 200'):
            assert response.status_code == 200
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_get_app_settings)

    @pytest.mark.test_app_settings_not_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на отсутствие доступа к настройкам раздел Общие user не admin")
    @allure.severity(Severity.CRITICAL)
    def test_app_settings_not_admin(self, get_access_token_not_admin):
        with allure.step('Выполнение валидного запроса /application/settings'):
            base_url_api = os.getenv('BASE_URL_API')
            response = requests.get(base_url_api + '/application/settings',
                                    headers={"Authorization": f"Bearer {get_access_token_not_admin}"})
        with allure.step('Сравнение статус кода'):
            assert response.status_code == 403
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 31003
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.access_denied'

    @pytest.mark.test_app_settings_invalid_token
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на отсутствие доступа к настройкам раздел Общие не валидный токен")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("invalid_token", [
        'text',
        123,
        ''
    ])
    def test_app_settings_invalid_token(self, invalid_token):
        with allure.step('Выполнение валидного запроса /application/settings'):
            base_url_api = os.getenv('BASE_URL_API')
            response = requests.get(base_url_api + '/application/settings',
                                    headers={"Authorization": f"Bearer {invalid_token}"})

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 401
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 32000
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.invalid_token'
