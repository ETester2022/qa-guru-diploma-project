import random
import time
import pytest
import allure

from qa_guru_diploma_project.utils.application import Application   
   
   
@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_source_crud
@allure.epic("")
@allure.story("")
class TestSourceCrud:

    @pytest.mark.test_selecting_source_of_table
    @allure.tag("web")
    @allure.testcase("44363")
    def test_selecting_source_of_table(self, browser, refresh_token_admin, create_crud):
        app = Application(browser)
        name_tool = create_crud.json()['name']

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)
        app.tools_editor_page.uncover_source_collapse()

        app.tools_editor_page.select_source_of_table(name_table="dflt.cities")
        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_source_collapse()
        app.tools_editor_page.uncover_fields_collapse()

        assert app.tools_editor_page.get_source_of_table() == "dflt.cities"
        assert app.tools_editor_page.get_count_fields() == 5

    @pytest.mark.test_clearing_source_of_table
    @allure.tag("web")
    @allure.testcase("44364")
    def test_clearing_source_of_table(self, browser, refresh_token_admin, create_crud_with_settings_table):
        app = Application(browser)
        name_tool = create_crud_with_settings_table.json()['name']

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)
        app.tools_editor_page.uncover_source_collapse()

        app.tools_editor_page.clear_source_of_table()
        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_source_collapse()
        app.tools_editor_page.uncover_fields_collapse()

        assert app.tools_editor_page.get_source_of_table() == None
        assert app.tools_editor_page.get_icon_empty_fields() == True
