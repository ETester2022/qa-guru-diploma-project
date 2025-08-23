import os
import pytest
import requests
import allure
import logging
from allure_commons.types import Severity
from allure_commons.types import AttachmentType
from jsonschema import validate
from tests.api.tools import schemas


@pytest.mark.test_all
@pytest.mark.test_api
@pytest.mark.test_get_tools_name_all
@allure.epic("43590, CRUD")
@allure.feature("43722, Отображение инструмента CRUD")
class TestGetToolsName:

    @pytest.mark.test_get_tools_name_admin
    @allure.tag("api")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на получение данных об инструменте")
    @allure.severity(Severity.CRITICAL)
    def test_get_tools_name_admin(self, get_access_token_admin):
        base_url_api = os.getenv('BASE_URL_API')
        name = "get_tools_name_admin"
        with allure.step('Выполнение валидного запроса /tools/{name}'):
            response = requests.get(base_url_api + f'/tools/{name}',
                                    headers={"Authorization": f"Bearer {get_access_token_admin}"})
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 200
        with allure.step('Проверка наличия "toolSettings"'):
            assert response.json()["toolSettings"]["name"] == name
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_get_tool_name)

    @pytest.mark.test_get_tools_name_not_exist
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/tools/name")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на получение настроек не существующего инструмента авторизован admin")
    def test_get_tools_name_not_exist(self, get_access_token_admin):
        base_url_api = os.getenv('BASE_URL_API')
        with allure.step('Выполнение валидного запроса /tools/{name}'):
            response = requests.get(base_url_api + f'/tools/not_exist',
                                    headers={"Authorization": f'Bearer {get_access_token_admin}'})
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 404
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 31004
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.not_found'

    @pytest.mark.test_get_tools_name_not_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на отсутствие доступа к настройкам инструмента user не admin")
    @allure.severity(Severity.CRITICAL)
    def test_get_tools_name_not_admin(self, get_access_token_not_admin):
        base_url_api = os.getenv('BASE_URL_API')
        name = "get_tools_name_admin"
        with allure.step('Выполнение валидного запроса /tools/{name}'):
            response = requests.get(base_url_api + f'/tools/{name}',
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

    @pytest.mark.test_get_tools_name_invalid_token
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
    def test_get_tools_name_invalid_token(self, invalid_token):
        base_url_api = os.getenv('BASE_URL_API')
        name = "get_tools_name_admin"
        with allure.step('Выполнение валидного запроса /tools/{name}'):
            response = requests.get(base_url_api + f'/tools/{name}',
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
