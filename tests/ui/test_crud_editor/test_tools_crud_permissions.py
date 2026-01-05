import pytest
import allure

from qa_guru_diploma_project.utils.application import Application

@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_crud_permissions_tools_page
@allure.epic("")
@allure.story("")
class TestCrudPermissionsToolsPage:

    @pytest.mark.test_enabling_for_permissions
    @allure.tag("web")
    @allure.testcase("44357")
    def test_enabling_for_permissions(self, browser, refresh_token_admin, create_crud):
        tool_name = create_crud.json()["name"]
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)

        app.tools_editor_page.uncover_permissions_collapse()

        assert app.tools_editor_page.get_status_switch_add() == 'false'
        assert app.tools_editor_page.get_status_switch_edit() == 'false'
        assert app.tools_editor_page.get_status_switch_delete() == 'false'

        app.tools_editor_page.click_switch_add()
        app.tools_editor_page.click_switch_edit()
        app.tools_editor_page.click_switch_delete()
        app.tools_editor_page.click_save_btn()
        browser.refresh()

        app.tools_editor_page.uncover_permissions_collapse()

        assert app.tools_editor_page.get_status_switch_add() == 'true'
        assert app.tools_editor_page.get_status_switch_edit() == 'true'
        assert app.tools_editor_page.get_status_switch_delete() == 'true'

    @pytest.mark.test_disabling_for_permissions
    @allure.tag("web")
    @allure.testcase("44358")
    def test_disabling_for_permissions(self, browser, refresh_token_admin, create_crud_with_settings_table):
        tool_name = create_crud_with_settings_table.json()["name"]
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)

        app.tools_editor_page.uncover_permissions_collapse()

        assert app.tools_editor_page.get_status_switch_add() == 'true'
        assert app.tools_editor_page.get_status_switch_edit() == 'true'
        assert app.tools_editor_page.get_status_switch_delete() == 'true'

        app.tools_editor_page.click_switch_add()
        app.tools_editor_page.click_switch_edit()
        app.tools_editor_page.click_switch_delete()
        app.tools_editor_page.click_save_btn()
        browser.refresh()

        app.tools_editor_page.uncover_permissions_collapse()

        assert app.tools_editor_page.get_status_switch_add() == 'false'
        assert app.tools_editor_page.get_status_switch_edit() == 'false'
        assert app.tools_editor_page.get_status_switch_delete() == 'false'
