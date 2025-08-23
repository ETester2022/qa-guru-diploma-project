import os
import pytest
import requests
import logging
import allure
from allure_commons.types import AttachmentType
from allure_commons.types import Severity
from tests.api.application_settings import data_app_settings_api
from jsonschema import validate
from tests.api.application_settings import schemas


@pytest.mark.test_all
@pytest.mark.test_api
@pytest.mark.test_patch_app_settings_all
@allure.epic("43483, Админские настройки")
@allure.feature("43531, Приложение")
class TestPatchAppSettings:

    # pytest -m test_patch_settings_valid_logo -vv
    @pytest.mark.test_patch_settings_valid_logo
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на добавление картинки с валидным форматом раздел Общие")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("logo_image", [
        data_app_settings_api.logo_jpeg,
        data_app_settings_api.logo_svg,
        data_app_settings_api.logo_png
    ])
    def test_patch_settings_valid_logo(self, get_access_token_admin, logo_image):
        request_body = {
            "commonSettings": {
                "logoImage": f"{logo_image}"
            }
        }

        with allure.step('Запрос изменения настроек приложения'):
            base_url_api = os.getenv('BASE_URL_API')
            response = requests.patch(base_url_api + '/application/settings',
                                      headers={"Authorization": f"Bearer {get_access_token_admin}"},
                                      json=request_body)
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 200
        with allure.step('Проверка наличия переданных настроек в body ответа'):
            assert response.json()["commonSettings"]["logoImage"] == logo_image
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_get_app_settings)

    # pytest -m test_patch_settings_color_scheme -vv
    @pytest.mark.test_patch_settings_color_scheme
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на запись валидных цветов темы раздел Общие")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("color_scheme", [
        'default',
        'dust',
        'volcano',
        'sunset',
        'cyan',
        'green',
        'geekblue',
        'purple'
    ])
    def test_patch_settings_color_scheme(self, get_access_token_admin, color_scheme):
        request_body = {
            "commonSettings": {
                "colorScheme": f"{color_scheme}"
            }
        }
        with allure.step('Запрос изменения настроек приложения'):
            base_url_api = os.getenv('BASE_URL_API')
            response = requests.patch(base_url_api + '/application/settings',
                                      headers={"Authorization": f"Bearer {get_access_token_admin}"},
                                      json=request_body)
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 200
        with allure.step('Проверка наличия переданных настроек в body ответа'):
            assert response.json()["commonSettings"]["colorScheme"] == color_scheme
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_get_app_settings)

    # pytest -m test_admin_invalid_body -vv
    @pytest.mark.test_admin_invalid_body
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на отсутствие возможности записать картинки не валидного формата")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("invalid_logo", [
        data_app_settings_api.logo_webp,
        data_app_settings_api.logo_gif
    ])
    def test_admin_invalid_body(self, get_access_token_admin, invalid_logo):
        request_body = {
            "commonSettings": {
                "logoImage": f"{invalid_logo}"
            }
        }
        with allure.step('Запрос изменения настроек приложения'):
            base_url_api = os.getenv('BASE_URL_API')
            response = requests.patch(base_url_api + '/application/settings',
                                      headers={"Authorization": f"Bearer {get_access_token_admin}"},
                                      json=request_body)
            allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.JSON)

            logging.info(response.request.url)
            logging.info(response.request.headers)

            logging.info(response.status_code)
            logging.info(response.text)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 400
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 31000
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.contract_violation'

    # pytest -m test_patch_settings_invalid_token -v
    @pytest.mark.test_patch_settings_invalid_token
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
    def test_patch_settings_invalid_token(self, invalid_token):
        request_body = {
            "commonSettings": {
                "logoEnabled": True
            }
        }
        with allure.step('Выполнение валидного запроса /application/settings'):
            base_url_api = os.getenv('BASE_URL_API')
            response = requests.patch(base_url_api + '/application/settings',
                                      headers={"Authorization": f"Bearer {invalid_token}"},
                                      json=request_body)
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
