import os
import logging
import requests
from requests import Response
import pytest
import json
import allure
from allure_commons.types import AttachmentType
from allure_commons.types import Severity
from jsonschema import validate
from tests.api.application_settings import schemas


def reqres_api_get(url, **kwargs):
    args = kwargs
    base_url_api = os.getenv('BASE_URL_API')
    result = requests.get(base_url_api + url, headers=args["headers"])
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")

    logging.info(result.request.url)
    logging.info(result.request.headers)

    logging.info(result.status_code)
    logging.info(result.text)

    return result


@pytest.mark.test_all
@pytest.mark.test_api
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
        url = '/settings/application'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}

        with allure.step('Запрос настроек приложения'):
            result: Response = reqres_api_get(url, headers=token)

        with allure.step('Соответствие статус-кода 200'):
            assert result.status_code == 200
        with allure.step('Валидация json'):
            validate(result.json(), schema=schemas.schema_get_app_settings)

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
            allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                          attachment_type=AttachmentType.JSON, extension="json")

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

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
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

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
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 401
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 32000
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.invalid_token'
