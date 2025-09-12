import pytest
import allure
from allure_commons.types import Severity
from jsonschema import validate
from tests.api.test_tools import schemas
from qa_guru_diploma_project.utils.utils import reqres_get


@pytest.mark.test_all
@pytest.mark.test_api
@pytest.mark.test_get_tools_name_all
@allure.epic("43590, CRUD")
@allure.feature("43722, Отображение инструмента CRUD")
class TestGetToolsName:

    @pytest.mark.test_get_tools_name_admin
    @allure.tag("api")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Получение данных об инструменте")
    @allure.severity(Severity.CRITICAL)
    def test_get_tools_name_admin(self, get_access_token_admin):
        name = "get_tools_name_admin"
        url = f'/tools/{name}'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}

        with allure.step('GET-запрос'):
            response = reqres_get(url, headers=token)

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
    @allure.title("Получение настроек не существующего инструмента авторизован admin")
    def test_get_tools_name_not_exist(self, get_access_token_admin):
        name = "not_exist"
        url = f'/tools/{name}'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}

        with allure.step('GET-запрос'):
            response = reqres_get(url, headers=token)

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
    @allure.title("Отсутствие доступа к настройкам инструмента user не admin")
    @allure.severity(Severity.CRITICAL)
    def test_get_tools_name_not_admin(self, get_access_token_not_admin):
        name = "get_tools_name_admin"
        url = f'/tools/{name}'
        token = {"Authorization": f"Bearer {get_access_token_not_admin}"}

        with allure.step('GET-запрос'):
            response = reqres_get(url, headers=token)

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
    @allure.title("Отсутствие доступа к настройкам раздел Общие не валидный токен")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("invalid_token", [
        'text',
        123,
        ''
    ])
    def test_get_tools_name_invalid_token(self, invalid_token):
        name = "get_tools_name_admin"
        url = f'/tools/{name}'
        token = {"Authorization": f"Bearer {invalid_token}"}

        with allure.step('GET-запрос'):
            response = reqres_get(url, headers=token)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 401
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 32000
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.invalid_token'
