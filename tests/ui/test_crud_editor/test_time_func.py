import random
import pytest
import allure
from allure_commons.types import Severity
from qa_guru_diploma_project.utils.application import Application


@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_crud_time_functions
@allure.epic("")
@allure.story("")
class TestCrudTimeFunction:

    @pytest.mark.test_crud_range_absolute
    @allure.tag("web")
    @allure.testcase("44373")
    def test_crud_range_absolute(self, browser, refresh_token_admin, create_crud):
        name_tool = create_crud.json()['name']
        time_params_start = {
            "month": "09",
            "day": "03",
            "hour": "0",
            "minute": "0",
            "second": "0"
        }
        time_params_end = {
            "month": "09",
            "day": "05",
            "hour": "7",
            "minute": "6",
            "second": "5"
        }
        preset = "last_5m"
        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)

        app.tools_editor_page.uncover_time_functions_collapse()
        app.tools_editor_page.click_switch_range()
        app.tools_editor_page.click_switch_range_visibility()
        app.tools_editor_page.select_preset(preset)

        app.tools_editor_page.click_btn_absolute()
        app.tools_editor_page.select_time_function_left_date_and_time(**time_params_start)
        app.tools_editor_page.select_time_function_right_date_and_time(**time_params_end)
        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_time_functions_collapse()

        status_switch_range = app.tools_editor_page.get_status_switch_range()
        status_switch_visibility = app.tools_editor_page.get_status_switch_range_visibility()
        list_selected_preset = app.tools_editor_page.get_list_selected_preset()
        text_selected_default_value = app.tools_editor_page.get_text_selected_default_value(browser)
        value_range_start = app.tools_editor_page.get_value_range_start()
        value_range_end = app.tools_editor_page.get_value_range_end()

        assert status_switch_range == "true"
        assert status_switch_visibility == "true"
        assert preset in list_selected_preset
        assert text_selected_default_value == "Абсолютное"
        assert value_range_start == "2026-09-03 00:00:00"
        assert value_range_end == "2026-09-05 07:06:05"

    @pytest.mark.test_crud_range_relative
    @allure.tag("web")
    @allure.testcase("44374")
    def test_crud_range_relative(self, browser, refresh_token_admin, create_crud):
        name_tool = create_crud.json()['name']
        preset = random.choice(["last_5m", "last_1h", "last_1d"])

        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)

        app.tools_editor_page.uncover_time_functions_collapse()
        app.tools_editor_page.click_switch_range()
        app.tools_editor_page.click_switch_range_visibility()
        app.tools_editor_page.click_btn_relative()
        app.tools_editor_page.select_default_preset(preset)

        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_time_functions_collapse()

        status_switch_range = app.tools_editor_page.get_status_switch_range()
        status_switch_visibility = app.tools_editor_page.get_status_switch_range_visibility()
        text_selected_default_value = app.tools_editor_page.get_text_selected_default_value(browser)

        selected_default_preset = app.tools_editor_page.get_selected_default_preset()

        assert status_switch_range == "true"
        assert status_switch_visibility == "true"
        assert text_selected_default_value == "Относительное"
        assert selected_default_preset == preset

    @pytest.mark.test_crud_updater_activation
    @allure.tag("web")
    @allure.testcase("44375")
    def test_crud_updater_activation(self, browser, refresh_token_admin, create_crud):
        name_tool = create_crud.json()['name']
        preset = random.choice(["5сек.", "1мин.", "30мин."])

        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)

        app.tools_editor_page.uncover_time_functions_collapse()
        app.tools_editor_page.click_switch_updater()
        app.tools_editor_page.click_switch_updater_visibility()
        app.tools_editor_page.select_default_preset_updater(preset)
        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_time_functions_collapse()

        assert app.tools_editor_page.get_status_switch_updater() == "true"
        assert app.tools_editor_page.get_status_switch_visibility_updater() == "true"
        assert app.tools_editor_page.get_selected_preset_updater() == preset

    @pytest.mark.test_crud_updater_deactivation
    @allure.tag("web")
    @allure.testcase("44376")
    def test_crud_updater_deactivation(self, browser, refresh_token_admin, create_crud_with_settings_table):
        name_tool = create_crud_with_settings_table.json()['name']
        preset = "Выкл."

        app = Application(browser)

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)
        app.tools_editor_page.uncover_time_functions_collapse()
        app.tools_editor_page.select_default_preset_updater(preset)
        app.tools_editor_page.click_switch_updater_visibility()
        app.tools_editor_page.click_switch_updater()
        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_time_functions_collapse()

        assert app.tools_editor_page.get_status_switch_updater() == "false"
        assert app.tools_editor_page.get_status_switch_visibility_updater() == "false"
        assert app.tools_editor_page.get_selected_preset_updater() == "off" or preset