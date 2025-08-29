import pytest
import allure
from allure_commons.types import Severity
from tests.api.application_settings import data_app_settings_api
from jsonschema import validate
from tests.api.application_settings import schemas
from qa_guru_diploma_project.utils.utils import reqres_patch


@pytest.mark.test_all
@pytest.mark.test_api
@pytest.mark.test_patch_app_settings_all
@allure.epic("43483, Админские настройки")
@allure.feature("43531, Приложение")
class TestPatchAppSettings:

    @pytest.mark.test_patch_app_settings_valid_logo
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
    def test_patch_app_settings_valid_logo(self, get_access_token_admin, logo_image):
        url = '/application/settings'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}
        request_body = {
            "commonSettings": {
                "logoImage": f"{logo_image}"
            }
        }

        with allure.step('PATCH-запрос'):
            response = reqres_patch(url, headers=token, json=request_body)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 200
        with allure.step('Проверка наличия переданных настроек в body ответа'):
            assert response.json()["commonSettings"]["logoImage"] == logo_image
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_get_app_settings)

    @pytest.mark.test_patch_app_settings_color_scheme
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
    def test_patch_app_settings_color_scheme(self, get_access_token_admin, color_scheme):
        url = '/application/settings'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}
        request_body = {
            "commonSettings": {
                "colorScheme": f"{color_scheme}"
            }
        }
        with allure.step('PATCH-запрос'):
            response = reqres_patch(url, headers=token, json=request_body)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 200
        with allure.step('Проверка наличия переданных настроек в body ответа'):
            assert response.json()["commonSettings"]["colorScheme"] == color_scheme
        with allure.step('Валидация json'):
            validate(response.json(), schema=schemas.schema_get_app_settings)

    @pytest.mark.test_patch_app_settings_invalid_body
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на отсутствие возможности записать картинки не валидного формата")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("invalid_logo", [
        data_app_settings_api.logo_webp,
        data_app_settings_api.logo_gif
    ])
    def test_patch_app_settings_invalid_body(self, get_access_token_admin, invalid_logo):
        url = '/application/settings'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}
        request_body = {
            "commonSettings": {
                "logoImage": f"{invalid_logo}"
            }
        }
        with allure.step('PATCH-запрос'):
            response = reqres_patch(url, headers=token, json=request_body)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 400
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 31000
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.contract_violation'

    @pytest.mark.test_patch_app_settings_invalid_token
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
    def test_patch_app_settings_invalid_token(self, invalid_token):
        url = '/application/settings'
        token = {"Authorization": f"Bearer {invalid_token}"}
        request_body = {
            "commonSettings": {
                "logoEnabled": True
            }
        }
        with allure.step('PATCH-запрос'):
            response = reqres_patch(url, headers=token, json=request_body)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 401
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 32000
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.invalid_token'
