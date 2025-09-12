import pytest
import allure
from allure_commons.types import Severity
from qa_guru_diploma_project.utils.utils import reqres_delete


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
    @allure.title("Удаление инструмента CRUD")
    @allure.severity(Severity.CRITICAL)
    def test_delete_tools_admin(self, get_access_token_admin, create_crud_auto):
        url = f'/tools/{create_crud_auto}'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}

        with allure.step('DELETE-запрос'):
            response = reqres_delete(url, headers=token)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 204

    @pytest.mark.test_delete_tools_not_admin
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/tools/name")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Отсутствие возможности удаления инструмента user не admin")
    @allure.severity(Severity.CRITICAL)
    def test_delete_tools_not_admin(self, get_access_token_not_admin):
        name = "test_delete_tools_not_admin"
        url = f'/tools/{name}'
        token = {"Authorization": f"Bearer {get_access_token_not_admin}"}

        with allure.step('DELETE-запрос'):
            response = reqres_delete(url, headers=token)

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
    @allure.title("Удаление не существующего инструмента авторизован admin")
    def test_delete_tools_not_exist_admin(self, get_access_token_admin):
        name = 'not_exist'
        url = f'/tools/{name}'
        token = {"Authorization": f"Bearer {get_access_token_admin}"}

        with allure.step('DELETE-запрос'):
            response = reqres_delete(url, headers=token)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 404
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 31004
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.not_found'

    @pytest.mark.test_delete_tools_invalid_token
    @allure.tag("api")
    @allure.link("https://stage.mesone.kz/tools/name")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Отсутствие доступа к удалению инструмента не валидный токен")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("invalid_token", [
        'text',
        123,
        ''
    ])
    def test_delete_tools_invalid_token(self, invalid_token):
        name = 'tool_name'
        url = f'/tools/{name}'
        token = {"Authorization": f"Bearer {invalid_token}"}

        with allure.step('DELETE-запрос'):
            response = reqres_delete(url, headers=token)

        with allure.step('Сравнение статус кода'):
            assert response.status_code == 401
        with allure.step('Сравнение id ошибки'):
            assert response.json()["id"] == 32000
        with allure.step('Сравнение текста ошибки с backend'):
            assert response.json()["code"] == 'err.invalid_token'
