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

    @pytest.mark.test_enabling_pagination_settings
    @allure.tag("web")
    @allure.testcase("41175")
    def test_enabling_pagination_settings(self, browser, refresh_token_admin, create_crud):
        tool_name = create_crud.json()["name"]
        number_lines = random.choice([1, 10, 100])
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)
        app.tools_editor_page.uncover_settings_table_collapse()
        app.tools_editor_page.click_switch_pagination()
        app.tools_editor_page.click_rbtn_pagination_top()
        app.tools_editor_page.clear_one_simbol_rows_pagination()
        app.tools_editor_page.clear_one_simbol_rows_pagination()
        app.tools_editor_page.filling_pagination_field(number_lines)

        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_settings_table_collapse()

        assert app.tools_editor_page.get_status_switch_pagination() == "true"
        # assert app.tools_editor_page.get_status_rbtn_pagination() == "Сверху"
        assert int(app.tools_editor_page.get_value_pagination_field()) == number_lines

    @pytest.mark.test_customizing_table_sizes
    @allure.tag("web")
    @allure.testcase("41175")
    def test_customizing_table_sizes(self, browser, refresh_token_admin, create_crud):
        tool_name = create_crud.json()["name"]
        height = random.randint(1, 400)
        size = random.randint(4, 64)
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)
        app.tools_editor_page.uncover_settings_table_collapse()

        app.tools_editor_page.click_switch_stretch_table()
        app.tools_editor_page.clear_one_simbol_line_height()
        app.tools_editor_page.clear_one_simbol_line_height()
        app.tools_editor_page.filling_line_height(height)
        app.tools_editor_page.clear_one_simbol_font_size()
        app.tools_editor_page.clear_one_simbol_font_size()
        app.tools_editor_page.filling_font_size(size)

        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_settings_table_collapse()

        assert app.tools_editor_page.get_status_switch_stretch_table() == "true"
        assert int(app.tools_editor_page.get_value_height_field()) == height
        assert int(app.tools_editor_page.get_value_font_size_field()) == size

    @pytest.mark.test_field_fixation
    @allure.tag("web")
    @allure.testcase("41175")
    def test_field_fixation(self, browser, refresh_token_admin, create_crud):
        tool_name = create_crud.json()["name"]
        top = random.randint(1, 100)
        left = random.randint(1, 100)
        right = random.randint(1, 100)
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)
        app.tools_editor_page.uncover_settings_table_collapse()

        app.tools_editor_page.click_switch_top_fix()
        app.tools_editor_page.click_switch_left_fix()
        app.tools_editor_page.click_switch_right_fix()

        app.tools_editor_page.filling_top_fix(top)
        app.tools_editor_page.filling_left_fix(left)
        app.tools_editor_page.filling_right_fix(right)

        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_settings_table_collapse()

        assert app.tools_editor_page.get_status_switch_top_fix() == 'true'
        assert app.tools_editor_page.get_status_switch_left_fix() == 'true'
        assert app.tools_editor_page.get_status_switch_right_fix() == 'true'

        assert int(app.tools_editor_page.get_value_top_fix_field()) == top
        assert int(app.tools_editor_page.get_value_left_fix_field()) == left
        assert int(app.tools_editor_page.get_value_right_fix_field()) == right

    @pytest.mark.test_enable_export_all_formats
    @allure.tag("web")
    @allure.testcase("41175")
    def test_enable_export_all_formats(self, browser, refresh_token_admin, create_crud):
        tool_name = create_crud.json()["name"]
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)
        app.tools_editor_page.uncover_settings_table_collapse()

        app.tools_editor_page.click_switch_export_csv()
        app.tools_editor_page.click_switch_export_json()
        app.tools_editor_page.click_switch_export_xlsx()
        app.tools_editor_page.click_switch_export_pdf()

        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_settings_table_collapse()

        assert app.tools_editor_page.get_status_switch_export_csv() == 'true'
        assert app.tools_editor_page.get_status_switch_export_json() == 'true'
        assert app.tools_editor_page.get_status_switch_export_xlsx() == 'true'
        assert app.tools_editor_page.get_status_switch_export_pdf() == 'true'

    @pytest.mark.test_enable_import_all_formats
    @allure.tag("web")
    @allure.testcase("41175")
    def test_enable_import_all_formats(self, browser, refresh_token_admin, create_crud):
        tool_name = create_crud.json()["name"]
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)
        app.tools_editor_page.uncover_settings_table_collapse()

        app.tools_editor_page.click_switch_import_csv()
        app.tools_editor_page.click_switch_import_json()

        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_settings_table_collapse()

        assert app.tools_editor_page.get_status_switch_import_csv() == 'true'
        assert app.tools_editor_page.get_status_switch_import_json() == 'true'

    @pytest.mark.test_disable_all_settings
    @allure.tag("web")
    @allure.testcase("41175")
    def test_disabling_pagination_settings(self, browser, refresh_token_admin, create_crud_with_settings_table):
        tool_name = create_crud_with_settings_table.json()["name"]
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)
        app.tools_editor_page.uncover_settings_table_collapse()

        app.tools_editor_page.click_switch_pagination()
        app.tools_editor_page.click_switch_stretch_table()
        app.tools_editor_page.click_switch_top_fix()
        app.tools_editor_page.click_switch_left_fix()
        app.tools_editor_page.click_switch_right_fix()
        app.tools_editor_page.click_switch_export_csv()
        app.tools_editor_page.click_switch_export_json()
        app.tools_editor_page.click_switch_export_xlsx()
        app.tools_editor_page.click_switch_export_pdf()
        app.tools_editor_page.click_switch_import_csv()
        app.tools_editor_page.click_switch_import_json()

        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_settings_table_collapse()

        assert app.tools_editor_page.get_status_switch_pagination() == "false"
        assert app.tools_editor_page.get_status_switch_stretch_table() == "false"
        assert app.tools_editor_page.get_status_switch_top_fix() == 'false'
        assert app.tools_editor_page.get_status_switch_left_fix() == 'false'
        assert app.tools_editor_page.get_status_switch_right_fix() == 'false'
        assert app.tools_editor_page.get_status_switch_export_csv() == 'false'
        assert app.tools_editor_page.get_status_switch_export_json() == 'false'
        assert app.tools_editor_page.get_status_switch_export_xlsx() == 'false'
        assert app.tools_editor_page.get_status_switch_export_pdf() == 'false'
        assert app.tools_editor_page.get_status_switch_import_csv() == 'false'
        assert app.tools_editor_page.get_status_switch_import_json() == 'false'

        assert app.tools_editor_page.is_enabled_pagination_field() is False
        assert app.tools_editor_page.is_enabled_rbtn_pagination_top() is False
        assert app.tools_editor_page.is_enabled_rbtn_pagination_bottom() is False
        assert app.tools_editor_page.is_enabled_top_fix_field() is False
        assert app.tools_editor_page.is_enabled_left_fix_field() is False
        assert app.tools_editor_page.is_enabled_right_fix_field() is False
