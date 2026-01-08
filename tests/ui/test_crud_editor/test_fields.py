
import pytest
import allure

from qa_guru_diploma_project.utils.application import Application   
   
   
@pytest.mark.test_all
@pytest.mark.test_web
@pytest.mark.test_fields_crud
@allure.epic("")
@allure.story("")
class TestFieldsCrud:

    @pytest.mark.test_enabling_and_configuring_field
    @allure.tag("web")
    @allure.testcase("44365")
    def test_enabling_and_configuring_field(self, browser, refresh_token_admin, create_crud_with_settings_table):
        app = Application(browser)
        name_tool = create_crud_with_settings_table.json()['name']
        field_name = 'name'
        label = 'label'
        read_only = 'RO'

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)
        app.tools_editor_page.uncover_fields_collapse()

        app.tools_editor_page.click_edit_by_name(field_name)
        app.tools_editor_page.click_switch_enable_field()
        app.tools_editor_page.filling_label_field_in_params(label)
        app.tools_editor_page.uncover_params_collapse_in_field()
        app.tools_editor_page.click_switch_params_read_only()

        app.tools_editor_page.click_ok_mw_fields()
        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_fields_collapse()

        assert app.tools_editor_page.get_text_label_in_fields(field_name) == label
        assert app.tools_editor_page.get_text_attribute_green(field_name) == 'on'
        assert app.tools_editor_page.get_text_attribute_purple_read_only(field_name, read_only) == 'RO'

    @pytest.mark.test_disabling_the_field_and_its_settings
    @allure.tag("web")
    @allure.testcase("44366")
    def test_disabling_the_field_and_its_settings(self, browser, refresh_token_admin, create_crud_with_fields):
        app = Application(browser)
        name_tool = create_crud_with_fields.json()['name']
        field_name = 'name'
        label = ''
        read_only = 'RO'

        app.tools_editor_page.open_settings_tools_admin(browser, refresh_token_admin)
        app.tools_editor_page.selecting_editor_tool(name_tool)
        app.tools_editor_page.uncover_fields_collapse()

        app.tools_editor_page.click_edit_by_name(field_name)
        app.tools_editor_page.click_switch_enable_field()
        app.tools_editor_page.clear_label_field_in_params()
        app.tools_editor_page.uncover_params_collapse_in_field()
        app.tools_editor_page.click_switch_params_read_only()
        app.tools_editor_page.click_ok_mw_fields()
        app.tools_editor_page.click_save_btn()
        browser.refresh()
        app.tools_editor_page.uncover_fields_collapse()

        assert app.tools_editor_page.get_text_label_in_fields(field_name) == label
        assert app.tools_editor_page.get_text_attribute_green(field_name) == None
        assert app.tools_editor_page.get_text_attribute_purple_read_only(field_name, read_only) == None
