import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from qa_guru_diploma_project.utils.utils import get_picture_path
from selenium.common.exceptions import NoSuchElementException
import time


class SettingsAppPage:

    def __init__(self, driver):
        self.driver = driver

    def open_settings_app(self):
        self.driver.get("https://stage.mesone.kz/settings/application")
        self.driver.implicitly_wait(15)

    @allure.step("Прямой переход на страницу настроек приложения")
    def open_settings_app_admin(self, browser, refresh_token_admin):

        self.open_settings_app()
        browser.add_cookie({"name": "refreshToken", "value": refresh_token_admin})
        self.open_settings_app()

    @allure.step("Загрузка Picture")
    def upload_picture(self, filename):
        file_path = get_picture_path(filename)
        self.driver.find_element(By.XPATH, '//input[@name="logo"]').send_keys(file_path)

    @allure.step("Удаление Picture")
    def delete_picture(self):
        icon_delete = self.driver.find_element(By.XPATH, '//*[@data-icon="delete"]')
        icon_delete.click()

    @allure.step("Клик Сохранить")
    def click_save_btn(self):
        login_btn = self.driver.find_element(By.XPATH, '//*[@aria-label="save"]')
        login_btn.click()
        time.sleep(1)

    @allure.step("Клик switch Логотип")
    def click_switch_logo(self, browser):
        switch_logo = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[@class="ant-space-item"][1]//*[@role="switch"]')
            )
        )
        switch_logo.click()

    @allure.step("Клик switch Изображение")
    def click_switch_picture(self, browser):
        switch_picture = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[contains(@class, "ant-upload-wrapper")]/../..//button')
            )
        )
        switch_picture.click()

    @allure.step("Клик switch Текст")
    def click_switch_text(self):
        switch_text = self.driver.find_element(By.XPATH, '//*[contains(@role, "tablist")]'
                                                         '/../../..//*[@role="switch"]')
        switch_text.click()

    @allure.step("Клик switch Футер")
    def click_switch_footer(self):
        switch_footer = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-space")]'
                                                           '//*[@class="ant-space-item"][3]//*[@role="switch"]')
        switch_footer.click()

    @allure.step("Клик switch Язык")
    def click_switch_lang(self):
        switch_lang = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-flex")]'
                                                         '/div[2]//*[@role="switch"]')
        switch_lang.click()

    @allure.step("Выбор языка из списка")
    def select_lang(self, l1, l2, l3):

        select_list = self.driver.find_element(By.XPATH, '//*[@class="ant-select-selection-overflow"]')
        select_list.click()
        lang1 = self.driver.find_element(By.XPATH, f'//*[@title="{l1}"]')
        lang1.click()
        lang2 = self.driver.find_element(By.XPATH, f'//*[@title="{l2}"]')
        lang2.click()
        lang3 = self.driver.find_element(By.XPATH, f'//*[@title="{l3}"]')
        lang3.click()

    @allure.step("Выбор языка по умолчанию")
    def select_default_lang(self, lang):

        select_list = self.driver.find_element(By.XPATH, '(//div[contains(@class, "ant-select-selector")])[2]')
        select_list.click()

        lang1 = self.driver.find_element(By.XPATH, f'//div[@class="rc-virtual-list"]//*[@title="{lang}"]')
        lang1.click()

    @allure.step("Клик таб EN")
    def click_tab_en(self):
        tab_en = self.driver.find_element(By.XPATH, '//*[@data-node-key="en-US"]/div')
        tab_en.click()

    @allure.step("Ввод текста в поле Основной EN")
    def input_text_field_main_en(self, text):
        field_main = self.driver.find_element(By.XPATH, '(//*[contains(@id, "panel-en-US")]'
                                                        '//*[@class="ant-space-item"])[1]//input')
        field_main.send_keys(text)

    @allure.step("Ввод текста в поле Дополнительный EN")
    def input_text_field_additional_en(self, text):
        field_additional = self.driver.find_element(By.XPATH, '(//*[contains(@id, "panel-en-US")]'
                                                        '//*[@class="ant-space-item"])[2]//input')
        field_additional.send_keys(text)

    @allure.step("Клик таб RU")
    def click_tab_ru(self):
        tab_en = self.driver.find_element(By.XPATH, '//*[@data-node-key="ru-RU"]/div')
        tab_en.click()

    @allure.step("Клик кнопке Темная")
    def click_btn_dark(self, browser):
        btn_dark = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                locator=(By.XPATH, '//*[contains(@class, "ant-radio-group-outline")]'
                                   '//*[@value="dark"]/../..')
            )
        )
        btn_dark.click()

    @allure.step("Клик кнопке Тема")
    def click_btn_theme(self, theme):
        btn_theme = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-radio-group-solid")]'
                                                       f'//*[text()="{theme}"]/..')
        btn_theme.click()

    @allure.step("Получение иконки поля загрузки лого")
    def get_attribute_picture(self):
        input_picture = self.driver.find_element(By.XPATH,
                                                 '//*[@class="ant-upload ant-upload-select"]//span[@role="img"]')
        return input_picture.get_attribute("aria-label")

    @allure.step("Получение статуса switch Изображение")
    def get_status_switch_picture(self):
        switch_picture = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-upload-wrapper")]/../..//button')
        return switch_picture.get_attribute("aria-checked")

    @allure.step("Получение статуса switch Логотип")
    def get_status_switch_logo(self):
        switch_picture = self.driver.find_element(By.XPATH, '//*[@class="ant-space-item"][1]//*[@role="switch"]')
        return switch_picture.get_attribute("aria-checked")

    @allure.step("Получение статуса switch Логотип")
    def get_status_switch_lang(self):
        switch_picture = self.driver.find_element(By.XPATH, '//*[contains(@class, "ant-flex")]'
                                                            '/div[2]//*[@role="switch"]')
        return switch_picture.get_attribute("aria-checked")

    @allure.step("Получение текста выбранного tab")
    def get_selected_text_tab(self):
        tab = self.driver.find_element(By.XPATH, '//*[@role="tab" and @aria-selected="true"]')
        return tab.text

    @allure.step("Получение текста поле Основной")
    def get_text_field_main_en(self):
        field_main = self.driver.find_element(By.XPATH, '(//*[contains(@id, "panel-en-US")]'
                                                        '//*[@class="ant-space-item"])[1]//input')
        return field_main.get_attribute("value")

    @allure.step("Получение текста поле Дополнительный")
    def get_text_field_additional_en(self):
        field_additional = self.driver.find_element(By.XPATH, '(//*[contains(@id, "panel-en-US")]'
                                                              '//*[@class="ant-space-item"])[2]//input')
        return field_additional.get_attribute("value")

    @allure.step("Получение текущего стиля приложения")
    def get_current_style_app(self):
        style_app = self.driver.find_element(By.XPATH, '//*[@id="footer"]/..')
        return style_app.get_attribute("themestyle")

    @allure.step("Получение текущей темы приложения")
    def get_current_theme_app(self):
        style_app = self.driver.find_element(By.XPATH,
                                             '//*[contains(@class, "ant-radio-group-solid")]//input[@checked]')
        return style_app.get_attribute("value")

    @allure.step("Поиск футера")
    def get_status_footer(self):
        try:
            self.driver.find_element(By.ID, "footer")
            return True
        except NoSuchElementException:
            return False

    @allure.step("Поиск лого в хэдере")
    def get_status_logo(self):
        try:
            self.driver.find_element(By.XPATH, '//header//img[@alt="MESone"]')
            return True
        except NoSuchElementException:
            return False

    @allure.step("Получение количества выбранных языков")
    def get_quantity_langs_in_lang(self):
        quantity_langs = self.driver.find_elements(By.XPATH,
                                                   '//*[@class="ant-select-selection-overflow"]'
                                                   '/div[@class="ant-select-selection-overflow-item"]')
        return len(quantity_langs)

    @allure.step("Получение количества включенных локалей")
    def get_quantity_langs_in_instance_editor(self):
        quantity_langs = self.driver.find_elements(By.XPATH, '//*[@data-node-key]')
        return len(quantity_langs)

    @allure.step("Получение выбранного языка по умолчанию")
    def get_selected_default_lang(self):
        default_lang = self.driver.find_element(By.XPATH, '//span[@class="ant-select-selection-search"]'
                                                          '/following-sibling::span')
        return default_lang.get_attribute("title")
