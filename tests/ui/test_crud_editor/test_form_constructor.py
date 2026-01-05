import random
import time

import pytest
import allure

from qa_guru_diploma_project.utils.application import Application


@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_form_constructor
@allure.epic("UC0003")
@allure.story("44075")
class TestFormConstructor:

    @pytest.mark.test_form_constructor_fields_disabled
    @allure.tag("web")
    @allure.testcase("44178")
    def test_form_constructor_fields_disabled(self, browser, refresh_token_admin, create_crud):
        tool_name = create_crud.json()["name"]
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)

        app.tools_editor_page.uncover_form_constructor_collapse()

        assert app.tools_editor_page.count_fields_in_form_constructor() == 0

    @pytest.mark.test_moving_and_resizing_fields
    @allure.tag("web")
    @allure.testcase("44179")
    def test_moving_and_resizing_fields(self, browser, refresh_token_admin, create_crud_with_fields):
        tool_name = create_crud_with_fields.json()["name"]
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(tool_name)
        app.tools_editor_page.uncover_info_collapse()

        app.tools_editor_page.uncover_form_constructor_collapse()
        app.tools_editor_page.clear_one_simbol_columns()
        app.tools_editor_page.filling_columns(columns=3)

        location_field_before = app.tools_editor_page.get_field_location_in_form_constructor()
        app.tools_editor_page.moving_field_in_form_constructor()
        app.tools_editor_page.changing_width_and_height_field_in_form_constructor()

        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_form_constructor_collapse()

        location_field_after = app.tools_editor_page.get_field_location_in_form_constructor()

        assert app.tools_editor_page.count_fields_in_form_constructor() == 3
        assert location_field_before != location_field_after
        app.tools_editor_page.comparison_field_sizes()
