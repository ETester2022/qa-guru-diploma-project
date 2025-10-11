import random
import pytest
import allure
from allure_commons.types import Severity
from qa_guru_diploma_project.utils.application import Application


@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_settings_app
@allure.epic("43483, Админские настройки")
@allure.feature("43531, Приложение")
class TestSettingsAppTimeFunction:

    @pytest.mark.test_range_absolute
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Установка диапазона Абсолютное")
    @allure.severity(Severity.NORMAL)
    def test_range_absolute(self, browser, refresh_token_admin, default_range):
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

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.uncover_time_functions_collapse()
        app.application_page.click_switch_range()
        app.application_page.click_switch_range_visibility()
        app.application_page.select_preset(preset)
        app.application_page.click_btn_absolute()
        app.application_page.select_time_function_left_date_and_time(**time_params_start)
        app.application_page.select_time_function_right_date_and_time(**time_params_end)
        app.application_page.click_save_btn()

        app.application_page.uncover_time_functions_collapse()

        status_switch_range = app.application_page.get_status_switch_range()
        status_switch_visibility = app.application_page.get_status_switch_visibility()
        selected_preset = app.application_page.get_selected_preset(preset)
        text_selected_default_value = app.application_page.get_text_selected_default_value()
        value_range_start = app.application_page.get_value_range_start()
        value_range_end = app.application_page.get_value_range_end()

        assert status_switch_range == "true"
        assert status_switch_visibility == "true"
        assert selected_preset == preset
        assert text_selected_default_value == "Абсолютное"
        assert value_range_start == "2025-09-03 00:00:00"
        assert value_range_end == "2025-09-05 07:06:05"

    @pytest.mark.test_range_relative
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Установка диапазона Относительное")
    @allure.severity(Severity.NORMAL)
    def test_range_relative(self, browser, refresh_token_admin, default_range):
        preset = random.choice(["last_5m", "last_1h", "last_1d"])

        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.uncover_time_functions_collapse()
        app.application_page.click_switch_range()
        app.application_page.click_switch_range_visibility()
        app.application_page.click_btn_relative()
        app.application_page.select_default_preset(preset)
        app.application_page.click_save_btn()

        app.application_page.uncover_time_functions_collapse()

        status_switch_range = app.application_page.get_status_switch_range()
        status_switch_visibility = app.application_page.get_status_switch_visibility()
        text_selected_default_value = app.application_page.get_text_selected_default_value()
        selected_default_preset = app.application_page.get_selected_default_preset()

        assert status_switch_range == "true"
        assert status_switch_visibility == "true"
        assert text_selected_default_value == "Относительное"
        assert selected_default_preset == preset

    @pytest.mark.test_updater_activation
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Включение и настройка Updater")
    @allure.severity(Severity.NORMAL)
    def test_updater_activation(self, browser, refresh_token_admin, default_updater):
        preset = random.choice(["5сек.", "1мин.", "30мин."])

        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.uncover_time_functions_collapse()
        app.application_page.click_switch_updater()
        app.application_page.click_switch_updater_visibility()
        app.application_page.select_default_preset_updater(preset)
        app.application_page.click_save_btn()

        app.application_page.uncover_time_functions_collapse()

        status_switch_updater = app.application_page.get_status_switch_updater()
        status_switch_visibility_updater = app.application_page.get_status_switch_visibility_updater()
        selected_preset_updater = app.application_page.get_selected_preset_updater()

        assert status_switch_updater == "true"
        assert status_switch_visibility_updater == "true"
        assert selected_preset_updater == preset

    @pytest.mark.test_updater_deactivation
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Выключение настроек Updater")
    @allure.severity(Severity.NORMAL)
    def test_updater_deactivation(self, browser, refresh_token_admin, updater_true):
        preset = "Выкл."

        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.uncover_time_functions_collapse()
        app.application_page.select_default_preset_updater(preset)
        app.application_page.click_switch_updater_visibility()
        app.application_page.click_switch_updater()
        app.application_page.click_save_btn()

        app.application_page.uncover_time_functions_collapse()

        status_switch_updater = app.application_page.get_status_switch_updater()
        status_switch_visibility_updater = app.application_page.get_status_switch_visibility_updater()
        selected_preset_updater = app.application_page.get_selected_preset_updater()

        assert status_switch_updater == "false"
        assert status_switch_visibility_updater == "false"
        assert selected_preset_updater == "off" or preset