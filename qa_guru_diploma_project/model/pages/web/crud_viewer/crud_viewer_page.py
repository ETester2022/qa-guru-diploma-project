import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from qa_guru_diploma_project.utils.utils import get_picture_path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
import time
import json

class CrudViewerPage:

    def __init__(self, driver):
        self.driver = driver

    def __open_tool_viewer(self, name_tool):
        self.driver.get(f"https://stage.mesone.kz/viewers/tool/{name_tool}")
        self.driver.implicitly_wait(15)

    def set_local_storage(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, json.dumps(value))

    @allure.step("Прямой переход в tools/viewer")
    def open_tools_viewer_admin(self, browser, refresh_token_admin, name_tool):
        self.__open_tool_viewer(name_tool)
        browser.add_cookie({"name": "refreshToken", "value": refresh_token_admin})
        self.__open_tool_viewer(name_tool)

    @allure.step("Проверка отображения pagination")
    def is_enabled_pagination(self):
        try:
            element = self.driver.find_element(By.XPATH, '//ul[contains(@class, "ant-pagination")]')
            return element.is_enabled()
        except NoSuchElementException:
            return False

    @allure.step("Ввод значения в поле Страница")
    def input_value_page_pagination(self, value):
        element = self.driver.find_element(By.XPATH, '//*[@aria-label="Страница"]')
        element.send_keys(value)

    @allure.step("Выбор колличества строк в CRUD Viewer")
    def select_value_count_rows_pagination(self, value):
        element = self.driver.find_element(By.XPATH, '//*[@aria-label="размер страницы"]/div[1]')
        element.click()
        element2 = self.driver.find_element(By.XPATH, f'//*[@id="rc_select_0_list_{value}"]')
        element2.click()

    @allure.step("Получение колличества страниц в pagination")
    def count_btn_pages_in_pagination(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//ul[contains(@class, "ant-pagination")]/li[@title]')))
        elements = self.driver.find_elements(By.XPATH, '//ul[contains(@class, "ant-pagination")]/li[@title]')
        return len(elements) - 2

    @allure.step("Получение порядкового номера первой записи в таблице")
    def get_ordinal_number_of_first_record_in_table(self):
        element = self.driver.find_element(By.XPATH, '(//div[@class="tabulator-table"]//div[@tabulator-field="rownum"])[1]')
        return int(element.text)    

    @allure.step("Получение порядкового номера последней записи в таблице")
    def get_ordinal_number_of_last_record_in_table(self):
        element = self.driver.find_element(By.XPATH, '(//div[@class="tabulator-table"]//div[@tabulator-field="rownum"])[last()]')
        return int(element.text)

    @allure.step("Получение значения из localStorage по ключу")
    def get_value_from_local_storage(self, key):
        value = self.driver.execute_script(f"return JSON.parse(localStorage.getItem('{key}'))")
        return value




    @allure.step("Получение колличества btn import")
    def get_count_btn_import(self):
        element = self.driver.find_elements(By.XPATH, '//*[@aria-label="import"]')
        return len(element)

    @allure.step("Получение колличества btn export")
    def get_count_btn_export(self):
        element = self.driver.find_elements(By.XPATH, '//*[@aria-label="export"]')
        return len(element)

    @allure.step("Получение колличества отображаемых строк в таблице")
    def get_count_fields_in_table(self):
        element = self.driver.find_elements(By.XPATH, '//*[@class="tabulator-table"]/*[@role="row"]')
        number_elements = len(element)
        return number_elements

    @allure.step("Получение высоты строки")
    def get_height_field(self):
        element = self.driver.find_element(
            By.XPATH,
            '(//*[@class="tabulator-table"]//*[@class="tabulator-col-resize-handle"])[11]'
        )
        style = element.get_attribute("style")

        pairs = []
        for p in style.split(";"):
            p = p.strip()
            if p:
                pairs.append(p)

        style_dict = {}
        for pair in pairs:
            if ":" in pair:  # защита от ошибок
                key, value = pair.split(":", 1)
                style_dict[key.strip()] = value.strip()

        # безопасное получение значения
        return style_dict.get("height")

    @allure.step("Получение размера шрифта")
    def get_font_size(self):
        element = self.driver.find_element(By.XPATH,
                                           '//*[@id="tabulatorLink"]')
        style = element.get_attribute("style")
        pairs = []
        for p in style.split(";"):
            p = p.strip()
            if p:  # убираем пустые строки
                pairs.append(p)

        # Формируем словарь
        style_dict = {}
        for pair in pairs:
            key, value = pair.split(":")
            style_dict[key.strip()] = value.strip()

        return style_dict["font-size"]

    @allure.step("Проверка авторастяжения таблицы")
    def is_auto_stretching(self):
        element = self.driver.find_element(By.XPATH, '//*[@id="tabulatorLink"]')
        return element.get_attribute("tabulator-layout") # fitColumns - растянута, fitData - не растянута

    @allure.step("Получение имени столбца fix left")
    def get_name_fix_left(self):
        element = self.driver.find_element(By.XPATH, '//*[@class="tabulator-col tabulator-frozen tabulator-frozen-left"]')
        return element.get_attribute("tabulator-field")

    @allure.step("Получение имени столбца fix right")
    def get_name_fix_right(self):
        element = self.driver.find_element(By.XPATH, '//*[@class="tabulator-col tabulator-frozen tabulator-frozen-right"]')
        return element.get_attribute("tabulator-field")

    @allure.step("Проверка fix row")
    def is_enabled_fix_row(self):
        element = self.driver.find_element(By.XPATH, '//*[@class="tabulator-frozen-rows-holder"]'
                                                     '//*[@tabulator-field="rownum"]')
        return element.is_enabled()

    @allure.step("Вызов table editor по тексту в соотвествии с action")
    def click_pkm_and_action_on_field(self, field_name, action):
        element_field = self.driver.find_element(By.XPATH, f'//*[@role="row"]//*[text()="{field_name}"]/..')
        ActionChains(self.driver).context_click(element_field).perform()
        element_action = self.driver.find_element(By.XPATH, f'//*[@class="tabulator-menu tabulator-popup-container"]//*[text()="{action}"]')
        element_action.click()

    @allure.step("Заполнение текстового поля по имени")
    def filling_text_field_by_name(self, field_name, value):
        element = self.driver.find_element(By.XPATH, f'//*[@class="ant-modal-content"]//label[text()="{field_name}"]/following-sibling::textarea')
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(value)

    @allure.step("Заполнение числового поля по имени")
    def filling_integer_field_by_name(self, field_name, value):
        element = self.driver.find_element(By.XPATH, f'//*[@class="ant-modal-content"]//label[text()="{field_name}"]/following-sibling::div//input')
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(value)

    @allure.step("Клик ОК в table editor")
    def click_ok_table_editor(self):
        element = self.driver.find_element(By.XPATH, '//*[@tabindex="0"]/*[@class="ant-modal-content"]//*[@type="submit"]')
        element.click()

    @allure.step("Клик Отмена в table editor")
    def click_cancel_table_editor(self):
        element = self.driver.find_element(By.XPATH, '//*[@class="ant-modal-footer"]//button[@type="button"]')
        element.click()

    @allure.step("Получение списка записей по названию столбца")
    def get_list_records_by_column_name(self, column_name):
        elements = self.driver.find_elements(By.XPATH, f'//*[@class="tabulator-table"]//*[@tabulator-field="{column_name}"]')
        list_of_text = []
        for element in elements:
            list_of_text.append(element.text)
        return list_of_text

    @allure.step("Получение состояния числового поля")
    def get_status_integer_field_by_label(self, label):
        element = self.driver.find_element(By.XPATH, f'//*[@class="ant-modal-body"]//label[text()="{label}"]/following-sibling::div//input')
        return element.get_attribute("disabled")
        
    @allure.step("Получение состояния текстового поля")
    def get_status_text_field_by_label(self, label):
        element = self.driver.find_element(By.XPATH, f'//*[@class="ant-modal-body"]//label[text()="{label}"]/following-sibling::textarea')
        return element.get_attribute("disabled")

    @allure.step("Клик на кнопку добавления записи")
    def click_btn_add_record(self):
        element = self.driver.find_element(By.XPATH, '//*[@type="button"]//*[@aria-label="plus"]')
        element.click()

    @allure.step("Отображение сообщения об ошибке")
    def get_message_error(self):
        element = self.driver.find_element(By.XPATH, '//*[@class="ant-notification-notice-message"]')
        return element.text