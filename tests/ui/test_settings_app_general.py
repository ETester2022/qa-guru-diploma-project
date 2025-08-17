import pytest
import allure
from allure_commons.types import Severity
from qa_guru_diploma_project.utils.application import Application


# # pytest -m test_upload_picture -vv --clean-alluredir --alluredir=allure_results
# # allure serve allure_results

@pytest.mark.test_front
@pytest.mark.test_settings_app
@allure.epic("43483, Админские настройки")
@allure.feature("43531, Приложение")
class TestSettingsApp:

    # Свитч Изображение + Загрузка картинки
    @pytest.mark.test_upload_picture
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на загрузку картинки с валидными параметрами")
    @allure.severity(Severity.NORMAL)
    def test_upload_picture(self, default_upload_picture, auth_admin):
        app = Application(auth_admin)

        app.application_page.open_settings_app()
        app.application_page.click_switch_picture(auth_admin)
        app.application_page.upload_picture("64.png")
        app.application_page.click_save_btn()

        icon_picture = app.application_page.get_attribute_picture()
        status_switch_picture = app.application_page.get_status_switch_picture()
        assert icon_picture == "delete"
        assert status_switch_picture == "true"

    # Свитч Изображение + Удаление картинки
    @pytest.mark.test_delete_picture
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на удаление картинки")
    @allure.severity(Severity.NORMAL)
    def test_delete_picture(self, add_picture, auth_admin):
        app = Application(auth_admin)

        app.application_page.open_settings_app()
        app.application_page.delete_picture()
        app.application_page.click_save_btn()

        icon_picture = app.application_page.get_attribute_picture()
        status_switch_picture = app.application_page.get_status_switch_picture()
        assert icon_picture == "plus"
        assert status_switch_picture == "true"

    # Свитч Текст + Ввод текста на EN
    @pytest.mark.test_input_main_text_logo
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на ввод Основного текста для лого в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_input_main_text_logo(self, default_main_text_en, auth_admin):
        app = Application(auth_admin)

        app.application_page.open_settings_app()
        app.application_page.click_switch_text()
        app.application_page.click_tab_en()
        app.application_page.input_text_field_main_en("MESone en-US")
        app.application_page.click_save_btn()
        app.application_page.click_tab_en()

        tab_text = app.application_page.get_selected_text_tab()
        text_field_main = app.application_page.get_text_field_main_en()
        assert tab_text == "EN"
        assert text_field_main == "MESone en-US"

    # Выбор стиля
    @pytest.mark.test_select_style_dark
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на выбор Стиль Темная в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_select_style_dark(self, style_light, auth_admin):
        app = Application(auth_admin)

        app.application_page.open_settings_app()
        app.application_page.click_btn_dark(auth_admin)
        app.application_page.click_save_btn()

        current_style_app = app.application_page.get_current_style_app()
        assert current_style_app == "dark"

    # Выбор темы
    @pytest.mark.test_select_theme_app
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на выбор Темы в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_select_theme_app(self, theme_default, auth_admin):
        app = Application(auth_admin)

        app.application_page.open_settings_app()
        app.application_page.click_btn_theme("C")
        app.application_page.click_save_btn()

        current_theme_app = app.application_page.get_current_theme_app()
        assert current_theme_app == "cyan"

    # Отображение футера
    @pytest.mark.test_activation_footer
    @allure.tag("web")
    @allure.link("https://stage.mesone.kz/settings/application")
    @allure.label('owner', 'tster: Evgeniy')
    @allure.title("тест на включение футера в разделе Приложение/Общие")
    @allure.severity(Severity.NORMAL)
    def test_activation_footer(self, disabling_footer, auth_admin):
        app = Application(auth_admin)

        app.application_page.open_settings_app()
        app.application_page.click_switch_footer()
        app.application_page.click_save_btn()

        status_footer = app.application_page.get_status_footer()
        assert status_footer is True
