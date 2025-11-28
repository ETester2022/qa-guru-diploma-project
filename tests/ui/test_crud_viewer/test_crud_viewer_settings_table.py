import random
import time

import pytest
import allure
from allure_commons.types import Severity
from qa_guru_diploma_project.utils.application import Application


@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_crud_viewer_settings_table
@allure.epic("UC0001")
@allure.story("44073")
class TestCrudViewerSettingsTable:

    @pytest.mark.test_enabling_settings_table_without_fix
    @allure.tag("web")
    @allure.testcase("44195, 44196, 44198, 44199")
    def test_enabling_settings_table_without_fix(self, browser, refresh_token_admin, create_crud_with_settings_table):
        tool_name = create_crud_with_settings_table.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)

        assert app.crud_viewer_page.is_enabled_pagination() == True
        assert app.crud_viewer_page.get_count_fields_in_table() == 10
        assert app.crud_viewer_page.get_height_field() == "25px"
        assert app.crud_viewer_page.get_font_size() == "12px"
        assert app.crud_viewer_page.get_count_btn_import() == 2
        assert app.crud_viewer_page.get_count_btn_export() == 4
        assert app.crud_viewer_page.is_auto_stretching() == "fitColumns"

    @pytest.mark.test_settings_table_fix
    @allure.tag("web")
    @allure.testcase("44197")
    def test_settings_table_fix(self, browser, refresh_token_admin, create_crud_with_settings_table_fix):
        tool_name = create_crud_with_settings_table_fix.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)

        assert app.crud_viewer_page.is_enabled_fix_row() == True
        assert app.crud_viewer_page.get_name_fix_left() == 'name'
        assert app.crud_viewer_page.get_name_fix_right() == 'coordinates'
