import random

import pytest
import allure

from qa_guru_diploma_project.utils.application import Application   
   
   
@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_settings_table
@allure.epic("UC0004")
@allure.story("44079")
class TestSettingsTable:

    @pytest.mark.test_delete_crud
    @allure.tag("web")
    @allure.testcase("43991")
    def test_delete_crud(self, browser, refresh_token_admin, create_crud_with_fields):
        app = Application(browser)
        name_tool = create_crud_with_fields.json()['name']

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)
        app.tools_editor_page.click_delete_tool()
        app.tools_editor_page.click_yes_delete_tool()

        assert f'{name_tool} [crud]' not in app.tools_editor_page.get_list_names_of_tools()

    @pytest.mark.test_cancel_delete_crud
    @allure.tag("web")
    @allure.testcase("43993")
    def test_cancel_delete_crud(self, browser, refresh_token_admin, create_crud_with_fields):
        app = Application(browser)
        name_tool = create_crud_with_fields.json()['name']

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)
        app.tools_editor_page.click_delete_tool()
        app.tools_editor_page.click_no_delete_tool()

        assert f'{name_tool} [crud]' in app.tools_editor_page.get_list_names_of_tools()

    @pytest.mark.test_filling_common_settings_crud
    @allure.tag("web")
    @allure.testcase("43994")
    def test_filling_common_settings_crud(self, browser, refresh_token_admin, create_crud_with_fields):
        app = Application(browser)
        name_tool = create_crud_with_fields.json()['name']

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)

        app.tools_editor_page.selecting_permission("user0")
        app.tools_editor_page.filling_label_field("new_label")
        app.tools_editor_page.selecting_permission("MAIN-TEST-GROUP")
        app.tools_editor_page.click_save_btn()

        assert app.tools_editor_page.get_label_common_settings() == "new_label"
        assert app.tools_editor_page.get_count_selected_group_permission_common_settings() == 1
        assert app.tools_editor_page.get_count_selected_user_permission_common_settings() == 1
        
    @pytest.mark.test_cancel_filling_common_settings_crud
    @allure.tag("web")
    @allure.testcase("43995")
    def test_cancel_filling_common_settings_crud(self, browser, refresh_token_admin, create_crud_with_fields):
        app = Application(browser)
        name_tool = create_crud_with_fields.json()['name']

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)

        app.tools_editor_page.selecting_permission("user0")
        app.tools_editor_page.filling_label_field("new_label")
        app.tools_editor_page.selecting_permission("MAIN-TEST-GROUP")
        app.tools_editor_page.click_cancel_btn()

        assert app.tools_editor_page.get_label_common_settings() == ""
        assert app.tools_editor_page.get_count_selected_group_permission_common_settings() == 0
        assert app.tools_editor_page.get_count_selected_user_permission_common_settings() == -1