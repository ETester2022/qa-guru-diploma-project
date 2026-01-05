
import pytest
import allure
from qa_guru_diploma_project.utils.application import Application


@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_tool_navigator_crud
@allure.epic("")
@allure.story("")
class TestToolNavigatorCrud:

    @pytest.mark.test_create_crud
    @allure.tag("web")
    @allure.testcase("43988")
    def test_create_crud(self, browser, refresh_token_admin, delete_tool_crud):
        app = Application(browser)
        name_tool = 'selenium_CRUD'
        type_tool = 'crud'

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.click_add_tool()
        app.tools_editor_page.fill_tool_name(name_tool)
        app.tools_editor_page.select_tool_type(type_tool)
        app.tools_editor_page.click_ok_create_tool()

        assert f'{name_tool} [{type_tool}]' in app.tools_editor_page.get_list_names_of_tools()
        assert app.tools_editor_page.get_name_common_settings() == name_tool
        assert app.tools_editor_page.get_type_common_settings() == type_tool
        assert app.tools_editor_page.is_enabled_field_name() == False
        assert app.tools_editor_page.is_enabled_field_type() == False

    @pytest.mark.test_create_crud_exist
    @allure.tag("web")
    @allure.testcase("43990")
    def test_create_crud_exist(self, browser, refresh_token_admin, create_crud_with_fields):
        app = Application(browser)
        name_tool = create_crud_with_fields.json()['name']
        type_tool = 'crud'

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.click_add_tool()
        app.tools_editor_page.fill_tool_name(name_tool)
        app.tools_editor_page.select_tool_type(type_tool)
        app.tools_editor_page.click_ok_create_tool()

        assert app.tools_editor_page.get_error_message() == '409 Conflict'

    @pytest.mark.test_cancel_create_crud
    @allure.tag("web")
    @allure.testcase("43989")
    def test_cancel_create_crud(self, browser, refresh_token_admin):
        app = Application(browser)
        name_tool = 'selenium_CRUD'
        type_tool = 'crud'

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.click_add_tool()
        app.tools_editor_page.fill_tool_name(name_tool)
        app.tools_editor_page.select_tool_type(type_tool)
        app.tools_editor_page.click_cancel_create_tool()

        assert f'{name_tool} [{type_tool}]' not in app.tools_editor_page.get_list_names_of_tools()