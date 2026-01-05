import random
import time

import pytest
import allure
from allure_commons.types import Severity
from qa_guru_diploma_project.utils.application import Application


@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_crud_viewer_fields
@allure.epic("UC0006")
@allure.story("44077")
class TestCrudViewerFields:

    @pytest.mark.test_changing_record_in_table
    @allure.tag("web")
    @allure.testcase("44254, 44256")
    def test_changing_record_in_table(self, browser, refresh_token_admin, create_crud_with_settings_and_record):
        tool_name = create_crud_with_settings_and_record.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)
        app.crud_viewer_page.click_pkm_and_action_on_field("Исеть", "Изменить")
        time.sleep(1)
        # app.crud_viewer_page.filling_text_field_by_name("name", "КУ Исеть")
        # time.sleep(1)
        app.crud_viewer_page.filling_integer_field_by_name("flow_rate", "30")
        time.sleep(1)
        app.crud_viewer_page.click_ok_table_editor()
        time.sleep(1)

        # assert "КУ Исеть" in app.crud_viewer_page.get_list_records_by_column_name("name")
        assert "30" in app.crud_viewer_page.get_list_records_by_column_name("flow_rate")

    @pytest.mark.test_display_error_field_not_filled
    @allure.tag("web")
    @allure.testcase("44259")
    def test_display_error_field_not_filled(self, browser, refresh_token_admin, create_crud_with_settings_and_record):
        tool_name = create_crud_with_settings_and_record.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)
        app.crud_viewer_page.click_pkm_and_action_on_field("Исеть", "Изменить")
        time.sleep(1)
        app.crud_viewer_page.filling_text_field_by_name("name", "")
        time.sleep(1)
        app.crud_viewer_page.click_ok_table_editor()
        time.sleep(1)

        # assert "Поле name обязательно для заполнения" in app.crud_viewer_page.get_error_message()
        # time.sleep(2)

    @pytest.mark.test_cancel_changing_record_in_table
    @allure.tag("web")
    @allure.testcase("44260")
    def test_cancel_changing_record_in_table(self, browser, refresh_token_admin, create_crud_with_settings_and_record):
        tool_name = create_crud_with_settings_and_record.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)
        app.crud_viewer_page.click_pkm_and_action_on_field("Исеть", "Изменить")
        time.sleep(1)
        # app.crud_viewer_page.filling_text_field_by_name("name", "КУ Исеть")
        # time.sleep(1)
        app.crud_viewer_page.filling_integer_field_by_name("flow_rate", "30")
        time.sleep(1)
        app.crud_viewer_page.click_cancel_table_editor()
        time.sleep(1)

        # assert "КУ Исеть" in app.crud_viewer_page.get_list_records_by_column_name("name")
        assert "30" not in app.crud_viewer_page.get_list_records_by_column_name("flow_rate")

    @pytest.mark.test_delete_record_in_table
    @allure.tag("web")
    @allure.testcase("44266, 44267")
    def test_delete_record_in_table(self, browser, refresh_token_admin, create_crud_with_settings_and_record):
        tool_name = create_crud_with_settings_and_record.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)
        app.crud_viewer_page.click_pkm_and_action_on_field("Исеть", "Удалить")
        time.sleep(1)
        assert app.crud_viewer_page.get_status_text_field_by_label("name") == 'true'
        assert app.crud_viewer_page.get_status_integer_field_by_label("flow_rate") == 'true'
        app.crud_viewer_page.click_ok_table_editor()
        time.sleep(1)

        assert "Исеть" not in app.crud_viewer_page.get_list_records_by_column_name("name")

    @pytest.mark.test_cancel_delete_record_in_table
    @allure.tag("web")
    @allure.testcase("44268")
    def test_cancel_delete_record_in_table(self, browser, refresh_token_admin, create_crud_with_settings_and_record):
        tool_name = create_crud_with_settings_and_record.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)
        app.crud_viewer_page.click_pkm_and_action_on_field("Исеть", "Удалить")
        time.sleep(1)
        app.crud_viewer_page.click_cancel_table_editor()
        time.sleep(1)

        assert "Исеть" in app.crud_viewer_page.get_list_records_by_column_name("name")





    @pytest.mark.test_add_record_in_table
    @allure.tag("web")
    @allure.testcase("44278, 44279")
    def test_add_record_in_table(self, browser, refresh_token_admin, create_crud_for_add_record):
        tool_name = create_crud_for_add_record.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)
        app.crud_viewer_page.click_btn_add_record()
        time.sleep(1)
        app.crud_viewer_page.filling_integer_field_by_name("id", "12321")
        time.sleep(1)
        app.crud_viewer_page.filling_text_field_by_name("name", "Каменка")
        time.sleep(1)
        app.crud_viewer_page.filling_integer_field_by_name("flow_rate", "30")
        time.sleep(1)
        app.crud_viewer_page.click_ok_table_editor()
        time.sleep(1)

        assert "12321" in app.crud_viewer_page.get_list_records_by_column_name("id")
        assert "Каменка" in app.crud_viewer_page.get_list_records_by_column_name("name")
        assert "30" in app.crud_viewer_page.get_list_records_by_column_name("flow_rate")

    @pytest.mark.test_cancel_add_record_in_table
    @allure.tag("web")
    @allure.testcase("44280")
    def test_cancel_add_record_in_table(self, browser, refresh_token_admin, create_crud_for_add_record):
        tool_name = create_crud_for_add_record.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)
        app.crud_viewer_page.click_btn_add_record()
        time.sleep(1)
        app.crud_viewer_page.filling_integer_field_by_name("id", "12321")
        time.sleep(1)
        app.crud_viewer_page.filling_text_field_by_name("name", "Каменка")
        time.sleep(1)
        app.crud_viewer_page.filling_integer_field_by_name("flow_rate", "30")
        time.sleep(1)
        app.crud_viewer_page.click_cancel_table_editor()
        time.sleep(1)

        assert "12321" not in app.crud_viewer_page.get_list_records_by_column_name("id")
        assert "Каменка" not in app.crud_viewer_page.get_list_records_by_column_name("name")
        assert "30" not in app.crud_viewer_page.get_list_records_by_column_name("flow_rate")

    @pytest.mark.test_add_record_in_table_without_required_fields
    @allure.tag("web")
    @allure.testcase("44281")
    def test_add_record_in_table_without_required_fields(self, browser, refresh_token_admin, create_crud_for_add_record):
        tool_name = create_crud_for_add_record.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)
        app.crud_viewer_page.click_btn_add_record()
        time.sleep(1)
        app.crud_viewer_page.filling_integer_field_by_name("id", "12321")
        time.sleep(1)
        app.crud_viewer_page.filling_text_field_by_name("name", "")
        time.sleep(1)
        app.crud_viewer_page.filling_integer_field_by_name("flow_rate", "")
        time.sleep(1)
        app.crud_viewer_page.click_ok_table_editor()
        time.sleep(1)

        assert app.crud_viewer_page.get_message_error() == 'Обязательное поле не заполнено'
