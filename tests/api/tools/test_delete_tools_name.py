import os
import pytest
import requests
import logging
import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType


@pytest.mark.test_all
@pytest.mark.test_api
@pytest.mark.test_del_tools_name_all
@allure.epic("43590, CRUD")
@allure.feature("43721, Удаление инструмента CRUD")
class TestDeleteToolName:

    @pytest.mark.test_delete_tools_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/tools/name")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на удаление инструмента CRUD")
    @allure.severity(Severity.CRITICAL)
    def test_delete_tools_admin(self, get_access_token_admin, create_crud_auto):
        base_url_api = os.getenv('BASE_URL_API')
        name = create_crud_auto
        with allure.step('Запрос удаления инструмента'):
            response = requests.delete(base_url_api + f'/tools/{name}',
                                       headers={"Authorization": f"Bearer {get_access_token_admin}"})
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 204

    @pytest.mark.test_delete_tools_not_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/tools/name")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на отсутствие возможности удаления инструмента user не admin")
    @allure.severity(Severity.CRITICAL)
    def test_delete_tools_not_admin(self, get_access_token_not_admin):
        base_url_api = os.getenv('BASE_URL_API')
        name = "test_delete_tools_not_admin"
        with allure.step('Запрос удаления инструмента'):
            response = requests.delete(base_url_api + f'/tools/{name}',
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

    @pytest.mark.test_delete_tools_not_exist_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/tools/name")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на удаление не существующего инструмента авторизован admin")
    def test_delete_tools_not_exist_admin(self, get_access_token_admin):
        base_url_api = os.getenv('BASE_URL_API')
        with allure.step('Запрос удаления пользователя'):
            response = requests.delete(base_url_api + '/tools/not_exist',
                                       headers={"Authorization": f"Bearer {get_access_token_admin}"})
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
