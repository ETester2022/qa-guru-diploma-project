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
class TestSettingsAppGeneral:

    @pytest.mark.test_upload_picture
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Загрузка картинки с валидными параметрами")
    @allure.severity(Severity.NORMAL)
    def test_upload_picture(self, browser, refresh_token_admin, default_upload_picture):
        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.click_switch_picture(browser)
        app.application_page.upload_picture("64.png")
        app.application_page.click_save_btn()

        icon_picture = app.application_page.get_attribute_picture()
        status_switch_picture = app.application_page.get_status_switch_picture()
        assert icon_picture == "delete"
        assert status_switch_picture == "true"

    @pytest.mark.test_delete_picture
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Удаление картинки")
    @allure.severity(Severity.NORMAL)
    def test_delete_picture(self, browser, refresh_token_admin, add_picture):
        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.delete_picture()
        app.application_page.click_save_btn()

        icon_picture = app.application_page.get_attribute_picture()
        status_switch_picture = app.application_page.get_status_switch_picture()
        assert icon_picture == "plus"
        assert status_switch_picture == "true"

    @pytest.mark.test_input_main_text_logo
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Ввод Основного текста для лого в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_input_main_text_logo(self, browser, refresh_token_admin, activation_all_locales, default_main_text):

        locale = random.choice(["ru-RU", "en-US", "kk-KZ", "de-DE"])

        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.click_switch_text()
        app.application_page.click_tab_locale(locale)
        app.application_page.input_text_field_main(locale, f"MESone - {locale}")
        app.application_page.click_save_btn()
        app.application_page.click_tab_locale(locale)

        tab_text = app.application_page.get_selected_text_tab()
        text_field_main = app.application_page.get_text_field_main(locale)
        assert tab_text == locale
        assert text_field_main == f"MESone - {locale}"

    @pytest.mark.test_select_style_dark
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Выбор Стиль Темная в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_select_style_dark(self, browser, refresh_token_admin, style_light):
        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.click_btn_dark(browser)
        app.application_page.click_save_btn()

        current_style_app = app.application_page.get_current_style_app()
        assert current_style_app == "dark"

    @pytest.mark.test_select_theme_app
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Выбор Темы в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_select_theme_app(self, browser, refresh_token_admin, theme_default):
        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.click_btn_theme("C")
        app.application_page.click_save_btn()

        current_theme_app = app.application_page.get_current_theme_app()
        assert current_theme_app == "cyan"

    @pytest.mark.test_activation_footer
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Включение футера в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_activation_footer(self, browser, refresh_token_admin, disabling_footer):
        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.click_switch_footer()
        app.application_page.click_save_btn()

        status_footer = app.application_page.get_status_footer()
        assert status_footer is True

    @pytest.mark.test_activation_logo
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Включение логотип в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_activation_logo(self, browser, refresh_token_admin, disabling_logo):
        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.click_switch_logo(browser)
        app.application_page.click_save_btn()

        status_logo = app.application_page.get_status_logo()
        status_switch_logo = app.application_page.get_status_switch_logo()

        assert status_logo is True
        assert status_switch_logo == "true"

    @pytest.mark.test_deactivation_logo
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Выключение логотип в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_deactivation_logo(self, browser, refresh_token_admin, enabling_logo):
        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.click_switch_logo(browser)
        app.application_page.click_save_btn()

        status_logo = app.application_page.get_status_logo()
        status_switch_logo = app.application_page.get_status_switch_logo()

        assert status_logo is False
        assert status_switch_logo == "false"

    @pytest.mark.test_select_lang_app
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("Включение и выбор языков в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_select_lang_app(self, browser, refresh_token_admin, default_localization):

        default_lang = 'Английский'
        app = Application(browser)

        app.application_page.open_settings_app_admin(browser, refresh_token_admin)
        app.application_page.click_switch_lang()
        app.application_page.select_lang('Английский', 'Казахский', 'Немецкий')
        app.application_page.click_save_btn()
        app.application_page.select_default_lang(default_lang)
        app.application_page.click_save_btn()

        status_switch_lang = app.application_page.get_status_switch_lang()
        quantity_langs_in_lang = app.application_page.get_quantity_langs_in_lang()
        quantity_langs_in_instance_editor = app.application_page.get_quantity_langs_in_instance_editor()
        selected_default_lang = app.application_page.get_selected_default_lang()

        assert status_switch_lang == "true"
        assert quantity_langs_in_lang == 4
        assert quantity_langs_in_instance_editor == 4
        assert selected_default_lang == default_lang