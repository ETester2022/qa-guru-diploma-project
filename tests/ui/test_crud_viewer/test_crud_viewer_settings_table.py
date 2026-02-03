import pytest
import allure
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

    @pytest.mark.test_disable_all_settings_false
    @allure.tag("web")
    @allure.testcase("44200")
    def test_disable_all_settings_false(self, browser, refresh_token_admin, create_crud_all_settings_table_false):
        tool_name = create_crud_all_settings_table_false.json()["name"]
        app = Application(browser)

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)

        assert app.crud_viewer_page.is_enabled_pagination() == False
        assert app.crud_viewer_page.get_height_field() == "25px"
        assert app.crud_viewer_page.get_font_size() == "12px"
        assert app.crud_viewer_page.get_count_btn_import() == 0
        assert app.crud_viewer_page.get_count_btn_export() == 0
        assert app.crud_viewer_page.is_auto_stretching() == "fitData"


@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_crud_viewer_pagination
@allure.epic("UC0008")
@allure.story("44372")
class TestCrudViewerPagination:

    @pytest.mark.test_applaying_pagination_settings
    @allure.tag("web")
    @allure.testcase("44415")
    def test_applaying_pagination_settings(self, browser, refresh_token_admin, create_crud_with_settings_table):
        tool_name = create_crud_with_settings_table.json()["name"]
        app = Application(browser)
        value = 1 #второе значение в выпадающем меню - 20
        number_page = 2
        count_rows = 20

        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)

        count_pages_before = app.crud_viewer_page.count_btn_pages_in_pagination()
        ordinal_number_of_first_record_before = app.crud_viewer_page.get_ordinal_number_of_first_record_in_table()
        ordinal_number_of_last_record_before = app.crud_viewer_page.get_ordinal_number_of_last_record_in_table()
        app.crud_viewer_page.input_value_page_pagination(number_page)
        app.crud_viewer_page.select_value_count_rows_pagination(value)
        count_pages_after = app.crud_viewer_page.count_btn_pages_in_pagination()
        ordinal_number_of_first_record_after = app.crud_viewer_page.get_ordinal_number_of_first_record_in_table()
        ordinal_number_of_last_record_after = app.crud_viewer_page.get_ordinal_number_of_last_record_in_table()
        pagination_value = app.crud_viewer_page.get_value_from_local_storage(f'tool-viewer-{tool_name}/pagination')

        assert app.crud_viewer_page.is_enabled_pagination() == True
        assert app.crud_viewer_page.get_count_fields_in_table() == count_rows
        assert count_pages_before == 7
        assert count_pages_after == 7
        assert ordinal_number_of_first_record_before == 1
        assert ordinal_number_of_last_record_before == 10
        assert ordinal_number_of_first_record_after == 21
        assert ordinal_number_of_last_record_after == 40
        assert pagination_value == {'current': number_page, 'pageSize': count_rows}

    @pytest.mark.test_applaying_pagination_settings_last_page
    @allure.tag("web")
    @allure.testcase("44416")
    def test_applaying_pagination_settings_last_page(self, browser, refresh_token_admin, create_crud_with_settings_table):
        tool_name = create_crud_with_settings_table.json()["name"]
        app = Application(browser)
        value = 3 #последнее значение в выпадающем меню - 100
        current_page = 42
        size_page = 10
        count_rows = 11
        
        app.crud_viewer_page.open_tools_viewer_admin(browser, refresh_token_admin, tool_name)
        app.crud_viewer_page.set_local_storage(key=f"tool-viewer-{tool_name}/pagination", 
                                               value={"current": current_page, "pageSize": size_page})
        browser.refresh()

        count_pages_before = app.crud_viewer_page.count_btn_pages_in_pagination()
        ordinal_number_of_first_record_before = app.crud_viewer_page.get_ordinal_number_of_first_record_in_table()
        ordinal_number_of_last_record_before = app.crud_viewer_page.get_ordinal_number_of_last_record_in_table()
        app.crud_viewer_page.select_value_count_rows_pagination(value)

        count_pages_after = app.crud_viewer_page.count_btn_pages_in_pagination()
        ordinal_number_of_first_record_after = app.crud_viewer_page.get_ordinal_number_of_first_record_in_table()
        ordinal_number_of_last_record_after = app.crud_viewer_page.get_ordinal_number_of_last_record_in_table()
        pagination_value = app.crud_viewer_page.get_value_from_local_storage(f'tool-viewer-{tool_name}/pagination')

        assert app.crud_viewer_page.is_enabled_pagination() == True
        assert app.crud_viewer_page.get_count_fields_in_table() == count_rows
        assert count_pages_before == 7
        assert count_pages_after == 5
        assert ordinal_number_of_first_record_before == 411
        assert ordinal_number_of_last_record_before == 411
        assert ordinal_number_of_first_record_after == 401
        assert ordinal_number_of_last_record_after == 411
        assert pagination_value == {'current': 5, 'pageSize': 100}