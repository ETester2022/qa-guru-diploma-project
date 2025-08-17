import os

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from qa_guru_diploma_project.utils.path_utils import get_picture_path
from selenium.common.exceptions import NoSuchElementException
import time


class SettingsAppPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход страницу настроек приложения")
    def open_settings_app(self):
        self.driver.get("https://stage.mesone.kz/settings/application")
        self.driver.implicitly_wait(15)

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

    @allure.step("Клик таб EN")
    def click_tab_en(self):
        tab_en = self.driver.find_element(By.XPATH, '//*[@data-node-key="en-US"]/div')
        tab_en.click()

    @allure.step("Ввод текста в поле Основной EN")
    def input_text_field_main_en(self, text):
        field_main = self.driver.find_element(By.XPATH, '//*[contains(@id, "panel-en-US")]'
                                                        '//*[text()="Основной"]/..//input')
        field_main.send_keys(text)

    @allure.step("Ввод текста в поле Дополнительный EN")
    def input_text_field_additional_en(self, text):
        field_additional = self.driver.find_element(By.XPATH, '//*[contains(@id, "panel-en-US")]'
                                                              '//*[text()="Дополнительный"]/..//input')
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

    @allure.step("Получение текста выбранного tab")
    def get_selected_text_tab(self):
        tab = self.driver.find_element(By.XPATH, '//*[@role="tab" and @aria-selected="true"]')
        return tab.text

    @allure.step("Получение текста поле Основной")
    def get_text_field_main_en(self):
        field_main = self.driver.find_element(By.XPATH, '//*[contains(@id, "panel-en-US")]'
                                                        '//*[text()="Основной"]/..//input')
        return field_main.get_attribute("value")

    @allure.step("Получение текста поле Дополнительный")
    def get_text_field_additional_en(self):
        field_additional = self.driver.find_element(By.XPATH, '//*[contains(@id, "panel-en-US")]'
                                                              '//*[text()="Дополнительный"]/..//input')
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
