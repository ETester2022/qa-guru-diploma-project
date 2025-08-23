import os
import pytest
import requests
import logging
import allure
from jsonschema import validate
from tests.api.tools import schemas
from allure_commons.types import Severity
from allure_commons.types import AttachmentType


@pytest.mark.test_all
@pytest.mark.test_api
@pytest.mark.test_post_tools_all
@allure.epic("43590, CRUD")
@allure.feature("43719, Создание инструмента CRUD")
class TestPostTools:

    @pytest.mark.test_post_tools_admin_crud
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/tools")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на создание инструмента CRUD")
    @allure.severity(Severity.BLOCKER)
    def test_post_tools_admin_crud(self, get_access_token_admin, delete_tool_crud_auto):
        base_url_api = os.getenv('BASE_URL_API')
        name = "crud_auto"
        request_body = {
            "name": f"{name}",
            "type": "crud"
        }
        with allure.step('Запрос создания пользователя'):
            response = requests.post(base_url_api + '/tools',
                                     headers={"Authorization": f"Bearer {get_access_token_admin}"},
                                     json=request_body)
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 201
        with allure.step('Сравнение соответствие названия инструмента в body'):
            assert response.json()["name"] == f"{name}"
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_post_tools)

    @pytest.mark.test_post_tools_not_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/tools")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на отстутствие прав на создание инструмента CRUD  для user не admin")
    @allure.severity(Severity.CRITICAL)
    def test_post_tools_not_admin(self, get_access_token_not_admin):
        base_url_api = os.getenv('BASE_URL_API')
        name = "crud_auto"
        request_body = {
            "name": f"{name}",
            "type": "crud"
        }
        with allure.step('Запрос создания инструмента'):
            response = requests.post(base_url_api + '/tools',
                                     headers={"Authorization": f"Bearer {get_access_token_not_admin}"},
                                     json=request_body)
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

    @pytest.mark.test_post_tools_existing_tool_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/tools")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на уникальность имени при создании инструмента CRUD")
    @allure.severity(Severity.CRITICAL)
    def test_post_tools_existing_tool_admin(self, get_access_token_admin):
        base_url_api = os.getenv('BASE_URL_API')
        request_body = {
            "name": "existing_tool",
            "type": "crud"
        }
        with allure.step('Запрос создания пользователя'):
            response = requests.post(base_url_api + '/tools',
                                     headers={"Authorization": f"Bearer {get_access_token_admin}"},
                                     json=request_body)
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 409
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 31009
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.tool_name_conflict_error'
