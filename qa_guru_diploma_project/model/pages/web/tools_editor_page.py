import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from qa_guru_diploma_project.utils.utils import get_picture_path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
import time


class SettingsToolsPage:

    def __init__(self, driver):
        self.driver = driver

    def __open_tools_editor(self):
        self.driver.get("https://stage.mesone.kz/settings/tools")
        self.driver.implicitly_wait(15)

    @allure.step("Прямой переход в tools/editor")
    def open_settings_tools_admin(self, browser, refresh_token_admin):
        self.__open_tools_editor()
        browser.add_cookie({"name": "refreshToken", "value": refresh_token_admin})
        self.__open_tools_editor()

    @allure.step("Выбор эдитора инструмента")
    def selecting_editor_tool(self, tool_name):
        element_search = self.driver.find_element(By.XPATH, '//input[@placeholder="Search text"]')
        element_search.send_keys(tool_name)

        element_name = self.driver.find_element(By.XPATH,
                                                f'(//*[@class="ant-tree-list"]//span[contains(., "{tool_name}")])[1]')
        element_name.click()

    @allure.step("Клик Настройки таблицы")
    def uncover_settings_table_collapse(self):
        element = self.driver.find_element(By.XPATH, '//*[@data-test-id="settings_table_collapse"]/*[@role="button"]')
        element.click()

    @allure.step("Клик Конструктор формы ввода/вывода")
    def uncover_form_constructor_collapse(self):
        element = self.driver.find_element(By.XPATH, '//*[@data-test-id="form_builder_collapse"]/*[@role="button"]')
        element.click()

    @allure.step("Клик Switch Пагинация")
    def click_switch_pagination(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[1]')
        element.click()

    @allure.step("Удаление 1 символа в поле Пагинация")
    def clear_one_simbol_rows_pagination(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[1]')
        element.send_keys(Keys.BACKSPACE)

    @allure.step("Заполнение поля Пагинация")
    def filling_pagination_field(self, number_lines):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[1]')
        element.send_keys(number_lines)

    @allure.step("Проверка доступности поля Пагинация")
    def is_enabled_pagination_field(self):
        element = self.driver.find_element(By.XPATH,
                                    '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[1]')
        return element.is_enabled()

    @allure.step("Клик btn сверху")
    def click_rbtn_pagination_top(self):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="settings_table_collapse"]//input[@value="top"]/../..')
        element.click()

    @allure.step("Проверка доступности btn сверху")
    def is_enabled_rbtn_pagination_top(self):
        element = self.driver.find_element(By.XPATH,
                                    '//*[@data-test-id="settings_table_collapse"]//input[@value="top"]')
        return element.is_enabled()

    @allure.step("Клик btn снизу")
    def click_rbtn_pagination_bottom(self):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="settings_table_collapse"]//input[@value="bottom"]/../..')
        element.click()

    @allure.step("Проверка доступности btn снизу")
    def is_enabled_rbtn_pagination_bottom(self):
        element = self.driver.find_element(By.XPATH,
                                    '//*[@data-test-id="settings_table_collapse"]//input[@value="bottom"]')
        return element.is_enabled()

    @allure.step("Клик Сохранить")
    def click_save_btn(self):
        login_btn = self.driver.find_element(By.XPATH, '//*[@aria-label="save"]')
        login_btn.click()

    @allure.step("Получение статуса Switch Пагинация")
    def get_status_switch_pagination(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[1]')
        return element.get_attribute("aria-checked")

    @allure.step("Получение статуса rbtn Пагинация")
    def get_status_rbtn_pagination(self):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="settings_table_collapse"]'
                                           '//label[contains(@class, "checked")]/span[2]')
        return element.text()

    @allure.step("Получение value поля Пагинация")
    def get_value_pagination_field(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[1]')
        return element.get_attribute("aria-valuenow")

    @allure.step("Клик Switch Растянуть столбцы на всю ширину")
    def click_switch_stretch_table(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[2]')
        element.click()

    @allure.step("Удаление 1 символа в поле Высота строки")
    def clear_one_simbol_line_height(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[2]')
        element.send_keys(Keys.BACKSPACE)

    @allure.step("Заполнение поля Высота строки")
    def filling_line_height(self, height):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[2]')
        element.send_keys(height)

    @allure.step("Удаление 1 символа в поле Размер шрифта")
    def clear_one_simbol_font_size(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[3]')
        element.send_keys(Keys.BACKSPACE)

    @allure.step("Заполнение поля Размер шрифта")
    def filling_font_size(self, size):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[3]')
        element.send_keys(size)

    @allure.step("Получение статуса Switch Растянуть столбцы на всю ширину")
    def get_status_switch_stretch_table(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[2]')
        return element.get_attribute("aria-checked")

    @allure.step("Получение value поля Высота строки")
    def get_value_height_field(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[2]')
        return element.get_attribute("value")

    @allure.step("Получение value поля Размер шрифта")
    def get_value_font_size_field(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="spinbutton"])[3]')
        return element.get_attribute("value")

    @allure.step("Клик Switch Сверху")
    def click_switch_top_fix(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[3]')
        element.click()

    @allure.step("Получение статуса Switch Сверху")
    def get_status_switch_top_fix(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[3]')
        return element.get_attribute("aria-checked")

    @allure.step("Клик Switch Слева")
    def click_switch_left_fix(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[4]')
        element.click()

    @allure.step("Получение статуса Switch Слева")
    def get_status_switch_left_fix(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[4]')
        return element.get_attribute("aria-checked")

    @allure.step("Клик Switch Справа")
    def click_switch_right_fix(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[5]')
        element.click()

    @allure.step("Получение статуса Switch Справа")
    def get_status_switch_right_fix(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[5]')
        return element.get_attribute("aria-checked")

    @allure.step("Заполнение поля Сверху")
    def filling_top_fix(self, fix):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="settings_table_collapse"]//*[@name="rowTop"]')
        element.send_keys(fix)

    @allure.step("Проверка доступности поля Сверху")
    def is_enabled_top_fix_field(self):
        element = self.driver.find_element(By.XPATH,
                                    '//*[@data-test-id="settings_table_collapse"]//*[@name="rowTop"]')
        return element.is_enabled()

    @allure.step("Получение value поля Сверху")
    def get_value_top_fix_field(self):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="settings_table_collapse"]//*[@name="rowTop"]')
        return element.get_attribute("value")

    @allure.step("Заполнение поля Слева")
    def filling_left_fix(self, fix):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="settings_table_collapse"]//*[@name="colLeft"]')
        element.send_keys(fix)

    @allure.step("Проверка доступности поля Слева")
    def is_enabled_left_fix_field(self):
        element = self.driver.find_element(By.XPATH,
                                    '//*[@data-test-id="settings_table_collapse"]//*[@name="colLeft"]')
        return element.is_enabled()

    @allure.step("Получение value поля Слева")
    def get_value_left_fix_field(self):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="settings_table_collapse"]//*[@name="colLeft"]')
        return element.get_attribute("value")

    @allure.step("Заполнение поля Справа")
    def filling_right_fix(self, fix):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="settings_table_collapse"]//*[@name="colRight"]')
        element.send_keys(fix)

    @allure.step("Проверка доступности поля Справа")
    def is_enabled_right_fix_field(self):
        element = self.driver.find_element(By.XPATH,
                                    '//*[@data-test-id="settings_table_collapse"]//*[@name="colRight"]')
        return element.is_enabled()

    @allure.step("Получение value поля Справа")
    def get_value_right_fix_field(self):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="settings_table_collapse"]//*[@name="colRight"]')
        return element.get_attribute("value")

    @allure.step("Клик Switch export CSV")
    def click_switch_export_csv(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[6]')
        element.click()

    @allure.step("Получение статуса Switch export CSV")
    def get_status_switch_export_csv(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[6]')
        return element.get_attribute("aria-checked")

    @allure.step("Клик Switch export JSON")
    def click_switch_export_json(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[7]')
        element.click()

    @allure.step("Получение статуса Switch export JSON")
    def get_status_switch_export_json(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[7]')
        return element.get_attribute("aria-checked")

    @allure.step("Клик Switch export XLSX")
    def click_switch_export_xlsx(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[8]')
        element.click()

    @allure.step("Получение статуса Switch export XLSX")
    def get_status_switch_export_xlsx(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[8]')
        return element.get_attribute("aria-checked")

    @allure.step("Клик Switch export PDF")
    def click_switch_export_pdf(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[9]')
        element.click()

    @allure.step("Получение статуса Switch export PDF")
    def get_status_switch_export_pdf(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[9]')
        return element.get_attribute("aria-checked")

    @allure.step("Клик Switch import CSV")
    def click_switch_import_csv(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[10]')
        element.click()

    @allure.step("Получение статуса Switch import CSV")
    def get_status_switch_import_csv(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[10]')
        return element.get_attribute("aria-checked")

    @allure.step("Клик Switch import JSON")
    def click_switch_import_json(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[11]')
        element.click()

    @allure.step("Получение статуса Switch import JSON")
    def get_status_switch_import_json(self):
        element = self.driver.find_element(By.XPATH,
                                           '(//*[@data-test-id="settings_table_collapse"]//*[@role="switch"])[11]')
        return element.get_attribute("aria-checked")

    @allure.step("Удаление 1 символа в поле Размер шрифта")
    def clear_one_simbol_columns(self):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="form_builder_collapse"]//*[@aria-valuemin="1"]')
        element.send_keys(Keys.BACKSPACE)

    @allure.step("Заполнение поля Столбцов")
    def filling_columns(self, columns):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@data-test-id="form_builder_collapse"]//*[@aria-valuemin="1"]')
        element.send_keys(columns)
    @allure.step("Подсчет кол-ва полей в Конструктор формы ввода/вывода")
    def count_fields_in_form_constructor(self):
        elements = self.driver.find_elements(By.XPATH,
                                        '//*[@data-test-id="form_builder_collapse"]//*[@data-grid="[object Object]"]')
        return len(elements)

    @allure.step("Перемещение поля 3 на место поля 1 в Конструктор формы ввода/вывода")
    def moving_field_in_form_constructor(self):
        source = self.driver.find_element(By.XPATH, '(//*[@data-test-id="form_builder_collapse"]'
                                                    '//*[@data-grid="[object Object]"]/label)[3]')

        target = self.driver.find_element(By.XPATH, '(//*[@data-test-id="form_builder_collapse"]'
                                                    '//*[@data-grid="[object Object]"])[1]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)

        actions = ActionChains(self.driver)
        actions.click_and_hold(source).pause(0.5)
        actions.move_to_element(target).move_by_offset(10, 10).pause(0.5)
        actions.release().perform()

    @allure.step("Изменение ширины и высоты поля в Конструктор формы ввода/вывода")
    def changing_width_and_height_field_in_form_constructor(self):
        # Находим ручку ресайза (например, span[7])
        resize_handle = self.driver.find_element(By.XPATH, '(//*[@data-test-id="form_builder_collapse"]'
                                                           '//*[@data-grid="[object Object]"])[1]/span[7]')

        actions = ActionChains(self.driver)
        actions.click_and_hold(resize_handle).pause(0.5)
        actions.move_by_offset(120, 60).pause(0.5)
        actions.release().perform()

    @allure.step("Сравнение размеров полей в Конструктор формы ввода/вывода")
    def comparison_field_sizes(self):
        # Находим элемент
        element1 = self.driver.find_element(By.XPATH,
                                       '(//*[@data-test-id="form_builder_collapse"]//*[@data-grid="[object Object]"])[1]')
        element2 = self.driver.find_element(By.XPATH,
                                       '(//*[@data-test-id="form_builder_collapse"]//*[@data-grid="[object Object]"])[2]')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element1)

        # Получаем размеры
        size1 = element1.size  # {'height': 70, 'width': 153}
        size2 = element2.size  # {'height': 110, 'width': 317}

        # Сравнение
        assert size1['height'] > size2['height'], f"Высота одинаковая: {size1['height']}"
        assert size1['width'] > size2['width'], f"Ширина одинаковая: {size1['width']}"

    @allure.step("Получение списка полей в Конструктор формы ввода/вывода")
    def get_list_of_fields_in_form_constructor(self):
        elements = self.driver.find_elements(By.XPATH,
                                       '//*[@data-test-id="form_builder_collapse"]//*[@data-grid="[object Object]"]//label')
        names = [element.text for element in elements]
        return names

    @allure.step("Получение расположения поля в Конструктор формы ввода/вывода")
    def get_field_location_in_form_constructor(self):
        element = self.driver.find_element(By.XPATH,
                                       '(//*[@data-test-id="form_builder_collapse"]//*[@data-grid="[object Object]"])[3]')
        transform_inline = self.driver.execute_script("return arguments[0].style.transform;", element)
        return transform_inline

"transform: translate(10px, 10px)"
"transform: translate(10px, 170px)"
